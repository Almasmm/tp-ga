"""Extension of the additional experiment v3 on the fixed-charge problem (amendment 9.2-9.4).

A configuration with ``extension: true`` names a base configuration (the 40 instances, the MIP reference and
the runs of amendment 8.4) and adds three parts in the same output area:

* ``tune``: a grid over the population, the number of pivots and the period of the local search of the
  cost-aware variant on training instances (9.2);
* ``run``: the two chosen variants on the instances of the base configuration (9.2), the instances above
  30x30 with their MIP reference (9.4) and the MIP solver with the time of the GA (9.3);
* ``report``: the tables ``E1`` to ``E7`` and one figure.
"""

from __future__ import annotations

import itertools
import json
import statistics
from typing import Any

from tpga.experiments.v2.storage import write_atomic
from tpga.experiments.v2.tasks import ga_config_id
from tpga.experiments.v3 import core
from tpga.experiments.v3 import report as rep
from tpga.experiments.v3.core import STOCHASTIC, ConfigV3, key_of, records, run_tasks

Row = dict[str, Any]
MIP: Row = {"method": "MIP", "kind": "mip", "config": "-", "params": {}, "initialization": None}
MIP_60 = "MIP-60s"
SHARED = ("base_seed", "runs", "budget_factor", "mip")


def base(cfg: ConfigV3) -> ConfigV3:
    """The configuration of amendment 8.4 that this one extends; seeds, budget and MIP options must agree."""
    b = ConfigV3.load(cfg.resolve(cfg.raw["base"]))
    differ = [k for k in SHARED if cfg.raw.get(k) != b.raw.get(k)]
    if differ or b.area != cfg.area:
        raise ValueError(f"the extension and its base configuration differ in {differ or ['output']}")
    return b


# --- methods and tasks ---------------------------------------------------------------------


def grid(cfg: ConfigV3) -> list[Row]:
    """Configurations of the grid in the order of the tie rule (the first is the configuration of 8.4)."""
    g = cfg.raw["tune"]["grid"]
    return [
        {"population": int(p), "pivots": int(k), "local_search_every": int(every)}
        for p, k, every in itertools.product(g["population"], g["pivots"], g["local_search_every"])
    ]


def selected(cfg: ConfigV3) -> dict[str, Row]:
    path = cfg.area / "tune" / "selected.json"
    if not path.exists():
        raise RuntimeError(f"{path} is missing: run the command tune first")
    return dict(json.loads(path.read_text(encoding="utf-8"))["selected"])


def method(cfg: ConfigV3, name: str, choice: Row | None = None) -> Row:
    """Fields of a configured method. ``choice`` (or the entry of ``tune/selected.json`` for a method with
    ``grid_selected``) replaces the population, the number of pivots and the period of the local search."""
    spec = cfg.raw["methods"][name]
    if choice is None and spec.get("grid_selected"):
        choice = selected(cfg)[name]
    if choice is None:
        return core.method_fields(cfg, name)
    fields = core.method_fields(cfg, name, mutation={"mode": "cycle", "strength": int(choice["pivots"])})
    params = {**fields["params"], "population": int(choice["population"])}
    every = int(choice["local_search_every"])
    config = ga_config_id(params, str(fields["initialization"]), "budget") + (f"-ls{every}" if every else "")
    return {**fields, "params": params, "local_search_every": every, "config": config}


def plan(cfg: ConfigV3, phase: str, items: list[Row], names: list[str], seeds: list[int]) -> list[Row]:
    tasks = []
    for inst in items:
        for name in names:
            fields = method(cfg, name)
            for seed in seeds if fields["kind"] in STOCHASTIC else [None]:
                tasks.append(core.make_task(cfg, phase, inst, fields, seed))
    return tasks


def mip_tasks(
    cfg: ConfigV3, phase: str, items: list[Row], limits: dict[str, float] | None = None, label: str = "-"
) -> list[Row]:
    """MIP runs with the options of the configuration; ``limits`` gives a time limit per instance."""
    tasks = []
    for inst in items:
        task = core.make_task(cfg, phase, inst, {**MIP, "config": label}, None)
        if limits is not None:
            task["mip"] = {**(task["mip"] or {}), "time_limit_s": float(limits[inst["id"]])}
        tasks.append(task)
    return tasks


def tune_items(cfg: ConfigV3) -> list[Row]:
    spec = cfg.raw["tune"]["instances"]
    return core.fctp_instances(spec, cfg.area / "tune" / "instances", prefix=str(spec.get("prefix", "t")))


def large_items(cfg: ConfigV3) -> list[Row]:
    spec = cfg.raw["large"]["instances"]
    return core.fctp_instances(
        spec, cfg.area / "large" / "instances", first_size_index=int(spec.get("first_size_index", 0))
    )


def tune_tasks(cfg: ConfigV3, items: list[Row]) -> list[Row]:
    spec = cfg.raw["tune"]
    seeds = cfg.seeds(int(spec["runs"]))
    return [
        core.make_task(cfg, "tune", inst, method(cfg, spec["template"], choice), seed)
        for inst in items
        for choice in grid(cfg)
        for seed in seeds
    ]


def median_times(rows: list[Row], name: str, items: list[Row]) -> dict[str, float]:
    """Instance -> median run time of the method ``name`` over its seeds."""
    out = {}
    for inst in items:
        times = [r["time_s"] for r in rows if r["instance"] == inst["id"] and r["method"] == name]
        if not times:
            raise RuntimeError(f"no run of {name} on {inst['id']}: its time gives the limit of the MIP")
        out[inst["id"]] = statistics.median(times)
    return out


def time_tasks(cfg: ConfigV3, b: ConfigV3, items: list[Row], large: list[Row]) -> list[Row]:
    """MIP with the limit T_i (and multiples of it), T_i the median run time of the reference GA (9.3)."""
    spec = cfg.raw["mip_time"]
    name = spec["reference_method"]
    tasks: list[Row] = []
    for group, raw, phase, factors in (
        (items, b.area / "raw" / "runs.jsonl", "main", spec["factors"]),
        (large, cfg.area / "raw" / "large.jsonl", "large", spec["factors_large"]),
    ):
        times = median_times(records(raw, phase), name, group)
        for factor in factors:
            limits = {iid: float(factor) * t for iid, t in times.items()}
            tasks += mip_tasks(cfg, "mip-time", group, limits, label=f"x{factor:g}")
    return tasks


# --- commands ------------------------------------------------------------------------------


def grid_table(cfg: ConfigV3) -> tuple[list[Row], dict[str, Row]]:
    """Mean training gap of every configuration of the grid and the configurations chosen by the rule."""
    items = tune_items(cfg)
    out = cfg.area / "tune"
    tasks = tune_tasks(cfg, items)
    keys = {key_of(t) for t in tasks}
    rows = [r for r in records(out / "records.jsonl", "tune") if key_of(r) in keys]
    mip = {r["instance"]: r for r in records(out / "mip.jsonl", "tune-mip")}
    if len(rows) != len(tasks) or len(mip) != len(items):
        raise RuntimeError(f"the grid is not complete: {len(rows)} of {len(tasks)} records, {len(mip)} MIP")
    ref = {}
    for inst in items:
        low = min(r["cost"] for r in rows if r["instance"] == inst["id"])
        cost = mip[inst["id"]]["cost"]
        ref[inst["id"]] = low if cost is None else min(low, float(cost))
    sizes = sorted({i["size"] for i in items}, key=rep._size_key)
    template = cfg.raw["tune"]["template"]
    table: list[Row] = []
    for rank, choice in enumerate(grid(cfg)):
        label = method(cfg, template, choice)["config"]
        mine = [r for r in rows if r["config"] == label]
        gaps = {key_of(r): 100.0 * (r["cost"] - ref[r["instance"]]) / ref[r["instance"]] for r in mine}
        row: Row = {"rank": rank, **choice, "config": label, "runs": len(mine)}
        row["mean_gap"] = statistics.fmean(gaps.values())
        for size in sizes:
            row[f"mean_gap_{size}"] = statistics.fmean(gaps[key_of(r)] for r in mine if r["size"] == size)
        row["generations_median"] = statistics.median(r["generations"] for r in mine)
        row["local_search_calls_mean"] = statistics.fmean(r["local_search_calls"] for r in mine)
        row["local_search_improvements_mean"] = statistics.fmean(r["local_search_improvements"] for r in mine)
        row["time_median_s"] = statistics.median(r["time_s"] for r in mine)
        row["selected_as"] = ""
        table.append(row)
    chosen: dict[str, Row] = {}
    for name, rule in cfg.raw["tune"]["select"].items():
        pool = [r for r in table if (r["local_search_every"] > 0) == bool(rule["local_search"])]
        best = min(pool, key=lambda r: (r["mean_gap"], r["rank"]))
        best["selected_as"] = name
        chosen[name] = {k: best[k] for k in ("population", "pivots", "local_search_every", "config", "mean_gap")}
        chosen[name]["rank"] = best["rank"]
    return table, chosen


def tune(cfg: ConfigV3) -> dict[str, Any]:
    """Grid of amendment 9.2. Writes ``tune/mip.jsonl``, ``tune/records.jsonl``, ``grid.csv``, ``selected.json``."""
    base(cfg)
    items = tune_items(cfg)
    out = cfg.area / "tune"
    first = run_tasks(cfg, mip_tasks(cfg, "tune-mip", items), out / "mip.jsonl", "tune mip")
    second = run_tasks(cfg, tune_tasks(cfg, items), out / "records.jsonl", "tune grid")
    table, chosen = grid_table(cfg)
    core.write_csv(out / "grid.csv", table)
    result = {
        "selected": chosen,
        "instances": [i["id"] for i in items],
        "seeds": cfg.seeds(int(cfg.raw["tune"]["runs"])),
        "configurations": len(table),
        "wall_s": first["wall_s"] + second["wall_s"],
        "rule": "smallest mean training gap over instances and seeds, separately without and with the local "
        "search; ties: the earlier configuration of the grid",
    }
    write_atomic(out / "selected.json", result)
    return result


def run(cfg: ConfigV3) -> dict[str, Any]:
    """Runs of amendment 9.2 (chosen variants on the base instances), 9.4 (larger sizes) and 9.3 (MIP with
    the time of the GA), in this order."""
    b = base(cfg)
    items = core.build_fctp(b)
    large = large_items(cfg)
    raw = cfg.area / "raw"
    seeds = cfg.seeds()
    out: dict[str, Any] = {}
    tuned = plan(cfg, "main", items, list(cfg.raw["test_methods"]), seeds)
    out["tuned"] = run_tasks(cfg, tuned, raw / "runs_ft.jsonl", "fctp tuned")
    out["large_mip"] = run_tasks(cfg, mip_tasks(cfg, "large-mip", large), raw / "large_mip.jsonl", "large mip")
    methods = list(cfg.raw["large"]["methods"])
    out["large"] = run_tasks(cfg, plan(cfg, "large", large, methods, seeds), raw / "large.jsonl", "large")
    timed = time_tasks(cfg, b, items, large)
    out["mip_time"] = run_tasks(cfg, timed, raw / "mip_time.jsonl", "mip with the time of the GA")
    out["wall_s"] = sum(part["wall_s"] for part in out.values())
    return out


# --- report --------------------------------------------------------------------------------


def _complete(rows: list[Row], tasks: list[Row], what: str) -> list[Row]:
    keys = {key_of(t) for t in tasks}
    mine = [r for r in rows if key_of(r) in keys]
    if len(mine) != len(tasks):
        raise RuntimeError(f"{what} is not complete: {len(mine)} of {len(tasks)} records")
    return mine


def best_known(items: list[Row], mip: dict[str, Row], *groups: list[Row]) -> dict[str, tuple[float, str]]:
    """Instance -> (Z_best, its source) by the rule of 8.4: the proved optimum, otherwise the smallest cost
    among the MIP plan and every record of ``groups`` (runs of the methods, MIP runs with other limits)."""
    out = {}
    for inst in items:
        iid = inst["id"]
        m = mip[iid]
        mine = [r for g in groups for r in g if r["instance"] == iid and r.get("cost") is not None]
        low = min(mine, key=lambda r: r["cost"])
        if m["proved"]:
            if low["cost"] < m["cost"] - 1e-6:
                raise RuntimeError(f"{low['method']} on {iid}: {low['cost']} is below the proved optimum {m['cost']}")
            out[iid] = (float(m["cost"]), "MIP (proved optimum)")
        elif m["cost"] is not None and m["cost"] <= low["cost"]:
            out[iid] = (float(m["cost"]), "MIP (best solution at the time limit)")
        else:
            source = f"MIP with the limit {low['config']}" if low["kind"] == "mip" else str(low["method"])
            out[iid] = (float(low["cost"]), source)
    return out


def _gap(cost: float, z: float) -> float:
    return 100.0 * (cost - z) / z


def _cells(items: list[Row]) -> list[tuple[str, float]]:
    return sorted({(i["size"], i["rho"]) for i in items}, key=lambda c: (rep._size_key(c[0]), c[1]))


def gap_rows(
    rows: list[Row], items: list[Row], methods: list[str], z: dict[str, tuple[float, str]]
) -> tuple[list[Row], dict[tuple[str, str], float]]:
    """Gap of every method by (size, rho) and the per-instance medians of the gap."""
    for r in rows:
        r["gap"] = _gap(r["cost"], z[r["instance"]][0])
    med = rep.instance_medians(rows, "gap")
    table: list[Row] = []
    for size, rho in _cells(items):
        ids = [i["id"] for i in items if i["size"] == size and i["rho"] == rho]
        for name in methods:
            mine = [r for r in rows if r["instance"] in ids and r["method"] == name]
            row: Row = {
                "size": size,
                "rho": rho,
                "method": name,
                "config": mine[0]["config"],
                "instances": len(ids),
                "runs": len(mine),
                "gap_median": statistics.median(r["gap"] for r in mine),
                "gap_instance_median": statistics.median(med[(name, i)] for i in ids),
                "gap_mean": statistics.fmean(r["gap"] for r in mine),
                "gap_min": min(r["gap"] for r in mine),
                "gap_max": max(r["gap"] for r in mine),
                "share_at_z_best": statistics.fmean(1.0 if r["gap"] <= 1e-9 else 0.0 for r in mine),
                "time_median_s": statistics.median(r["time_s"] for r in mine),
            }
            if mine[0].get("local_search_calls") is not None:
                row["generations_median"] = statistics.median(r["generations"] for r in mine)
                row["local_search_calls_mean"] = statistics.fmean(r["local_search_calls"] for r in mine)
                row["local_search_evaluations_mean"] = statistics.fmean(r["local_search_evaluations"] for r in mine)
                row["local_search_improvements_mean"] = statistics.fmean(r["local_search_improvements"] for r in mine)
            table.append(row)
    return table, med


def time_rows(
    items: list[Row],
    limited: dict[str, list[Row]],
    reference: dict[str, float],
    z: dict[str, tuple[float, str]],
    scope: str,
) -> list[Row]:
    """MIP plans at each time limit against the median cost of the reference GA, by (size, rho). ``limited``
    maps the label of a limit to its MIP records; ``reference`` is instance -> median cost of the GA."""
    table: list[Row] = []
    for size, rho in _cells(items):
        ids = [i["id"] for i in items if i["size"] == size and i["rho"] == rho]
        for label, recs in limited.items():
            mine = {r["instance"]: r for r in recs if r["instance"] in ids}
            if len(mine) != len(ids):
                continue
            with_plan = [r for r in mine.values() if r["cost"] is not None]
            limits = [r["time_limit_s"] for r in mine.values() if r.get("time_limit_s") is not None]
            row: Row = {
                "instances_of": scope,
                "size": size,
                "rho": rho,
                "limit": label,
                "instances": len(ids),
                "limit_median_s": statistics.median(limits) if limits else None,
                "time_used_median_s": statistics.median(r["time_s"] for r in mine.values()),
                "mip_no_plan": len(ids) - len(with_plan),
                "mip_proved": sum(bool(r["proved"]) for r in mine.values()),
                "mip_better": sum(r["cost"] < reference[r["instance"]] for r in with_plan),
                "equal": sum(r["cost"] == reference[r["instance"]] for r in with_plan),
                "ga_better_or_no_plan": len(ids) - sum(r["cost"] <= reference[r["instance"]] for r in with_plan),
                "mip_gap_to_z_best_median": statistics.median(_gap(r["cost"], z[r["instance"]][0]) for r in with_plan)
                if with_plan
                else None,
                "ga_gap_to_z_best_median": statistics.median(_gap(reference[i], z[i][0]) for i in ids),
            }
            table.append(row)
    return table


def report(cfg: ConfigV3) -> dict[str, Any]:
    b = base(cfg)
    tables = cfg.area / "tables"
    raw = cfg.area / "raw"
    seeds = cfg.seeds()
    reference = cfg.raw["mip_time"]["reference_method"]

    table, chosen = grid_table(cfg)
    rep._both(
        tables,
        "E1_tuning",
        "FCTP: grid on the training instances (amendment 9.2)",
        "Mean training gap (%) over 8 training instances and 3 seeds; the reference of an instance is the "
        "smaller of its MIP solution (60 s) and the best run of the grid. `rank` is the order of the tie rule. "
        "`selected_as` marks the configuration with the smallest mean gap without the local search "
        "(GA-cost-cycle-ft) and with it (GA-hybrid-ft).",
        table,
    )

    # 9.2: the chosen variants on the instances of 8.4
    base_rows, base_mip, items = rep.fctp_rows(b)
    large = large_items(cfg)
    tuned = _complete(
        records(raw / "runs_ft.jsonl", "main"), plan(cfg, "main", items, cfg.raw["test_methods"], seeds), "9.2"
    )
    timed = _complete(records(raw / "mip_time.jsonl", "mip-time"), time_tasks(cfg, b, items, large), "9.3")
    mip_by = {r["instance"]: r for r in base_mip}
    ids40 = {i["id"] for i in items}
    timed40 = [r for r in timed if r["instance"] in ids40]
    z_old = best_known(items, mip_by, base_rows)
    z = best_known(items, mip_by, base_rows, tuned, timed40)
    changed = sorted(i for i in ids40 if z[i][0] < z_old[i][0])
    compared: list[str] = []
    for pair in cfg.raw["pairs"]:
        compared += [name for name in pair if name not in compared]
    order = [m for m in list(b.raw["methods"]) + list(cfg.raw["test_methods"]) if m in compared]
    rows40 = [r for r in base_rows + tuned if r["method"] in order]
    e2, med40 = gap_rows(rows40, items, order, z)
    for row in e2:
        row["z_best_lowered_on"] = sum(
            1 for i in items if i["id"] in changed and (i["size"], i["rho"]) == (row["size"], row["rho"])
        )
    rep._both(
        tables,
        "E2_gap_tuned",
        "FCTP: the variants chosen on FCTP training instances against the variants of 8.4",
        "gap = 100 (Z - Z_best) / Z_best on the 40 instances of 8.4. Z_best follows the rule of 8.4 and includes "
        "the runs of this table and the MIP runs of E4; `z_best_lowered_on` counts the instances of the cell "
        "where that lowered Z_best. GA-cost-cycle and GA-hybrid have the parameters of 8.4; the `-ft` variants "
        "have the population, pivots and local-search period of E1.",
        e2,
    )
    e3: list[Row] = []
    all_ids = [i["id"] for i in items]
    e3 += rep.paired_rows(med40, all_ids, cfg.raw["pairs"], {"scope": "all instances"})
    for rho in sorted({i["rho"] for i in items}):
        ids = [i["id"] for i in items if i["rho"] == rho]
        e3 += rep.paired_rows(med40, ids, cfg.raw["pairs"], {"scope": f"rho = {rho:g}"})
    rep._both(
        tables,
        "E3_tests_tuned",
        "FCTP: paired comparisons of the variants chosen on FCTP (amendment 9.2)",
        "Unit: the instance (median gap over its seeds). Two-sided Wilcoxon signed-rank test, Holm correction "
        "over the three pairs of each scope, rank-biserial r (negative: method_a has the smaller gap). Only one "
        "variant was given a grid on FCTP, so the `-ft` variants are not tested against the other heuristics.",
        e3,
    )

    # 9.4: sizes above 30x30
    large_mip = _complete(records(raw / "large_mip.jsonl", "large-mip"), mip_tasks(cfg, "large-mip", large), "9.4 MIP")
    methods = list(cfg.raw["large"]["methods"])
    large_rows = _complete(records(raw / "large.jsonl", "large"), plan(cfg, "large", large, methods, seeds), "9.4")
    large_by = {r["instance"]: r for r in large_mip}
    ids_large = {i["id"] for i in large}
    timed_large = [r for r in timed if r["instance"] in ids_large]
    zl = best_known(large, large_by, large_rows, timed_large)
    e5: list[Row] = []
    for size, rho in _cells(large):
        mine = [large_by[i["id"]] for i in large if (i["size"], i["rho"]) == (size, rho)]
        with_plan = [r for r in mine if r["cost"] is not None]
        e5.append(
            {
                "size": size,
                "rho": rho,
                "instances": len(mine),
                "proved_optimal": sum(bool(r["proved"]) for r in mine),
                "with_plan": len(with_plan),
                "statuses": "; ".join(sorted({r["status"] for r in mine})),
                "mip_time_median_s": statistics.median(r["time_s"] for r in mine),
                "mip_gap_median_percent": statistics.median(100.0 * r["mip_gap"] for r in with_plan)
                if with_plan
                else None,
                "mip_gap_max_percent": max(100.0 * r["mip_gap"] for r in with_plan) if with_plan else None,
                "z_best_from_heuristic": sum(not zl[r["instance"]][1].startswith("MIP") for r in mine),
                "z_best_gap_to_bound_median_percent": statistics.median(
                    100.0 * max(0.0, zl[r["instance"]][0] - r["bound"]) / zl[r["instance"]][0] for r in mine
                )
                if all(r["bound"] is not None for r in mine)
                else None,
            }
        )
    rep._both(
        tables,
        "E5_large_mip",
        "FCTP above 30x30: MIP reference with 60 s (amendment 9.4)",
        "HiGHS, one thread, 60 s. `z_best_from_heuristic` counts the instances where the best known value is a "
        "run of a heuristic and not a MIP plan.",
        e5,
    )
    e6, med_large = gap_rows(large_rows, large, methods, zl)
    for size, rho in _cells(large):
        ids = [i["id"] for i in large if (i["size"], i["rho"]) == (size, rho)]
        gaps = [_gap(large_by[i]["cost"], zl[i][0]) for i in ids if large_by[i]["cost"] is not None]
        e6.append(
            {
                "size": size,
                "rho": rho,
                "method": MIP_60,
                "config": "-",
                "instances": len(ids),
                "runs": len(gaps),
                "gap_median": statistics.median(gaps) if gaps else None,
                "gap_instance_median": statistics.median(gaps) if gaps else None,
                "gap_mean": statistics.fmean(gaps) if gaps else None,
                "gap_min": min(gaps) if gaps else None,
                "gap_max": max(gaps) if gaps else None,
                "share_at_z_best": statistics.fmean(1.0 if g <= 1e-9 else 0.0 for g in gaps) if gaps else None,
                "time_median_s": statistics.median(large_by[i]["time_s"] for i in ids),
            }
        )
    e6.sort(key=lambda r: (rep._size_key(r["size"]), r["rho"]))
    rep._both(
        tables,
        "E6_large_gap",
        "FCTP above 30x30: gap of every method",
        "gap = 100 (Z - Z_best) / Z_best; Z_best is the best known value (no optimum is proved at these sizes "
        "unless E5 says so). The row MIP-60s is the plan of the MIP solver at 60 s (`runs` = instances with a "
        "plan). Run times were measured with 20 runs at once.",
        e6,
    )
    for i in ids_large:
        if large_by[i]["cost"] is not None:
            med_large[(MIP_60, i)] = _gap(large_by[i]["cost"], zl[i][0])
    e7: list[Row] = []
    scopes = [("all instances", [i["id"] for i in large])]
    scopes += [
        (f"size {s}", [i["id"] for i in large if i["size"] == s]) for s in dict.fromkeys(i["size"] for i in large)
    ]
    for label, ids in scopes:
        part = rep.paired_rows(med_large, ids, cfg.raw["large"]["pairs"], {"scope": label})
        for row in part:
            row["mip_without_plan_counted_as_wins_a"] = sum(large_by[i]["cost"] is None for i in ids)
        e7 += part
    rep._both(
        tables,
        "E7_large_tests",
        "FCTP above 30x30: the GA variants against the MIP solver with 60 s",
        "Unit: the instance; the median gap of the GA over its seeds against the gap of the one MIP plan (both "
        "to the same Z_best, so wins and losses are those of the cost). Two-sided Wilcoxon signed-rank test, "
        "Holm correction over the three pairs of each scope, rank-biserial r (negative: the GA has the smaller "
        "gap). Instances where the MIP has no plan at 60 s are left out of the test and counted in the last column.",
        e7,
    )

    # 9.3: the MIP solver with the time of the GA
    ref40 = {
        i: statistics.median(r["cost"] for r in base_rows if r["instance"] == i and r["method"] == reference)
        for i in ids40
    }
    ref_large = {
        i: statistics.median(r["cost"] for r in large_rows if r["instance"] == i and r["method"] == reference)
        for i in ids_large
    }

    full_limit = float((cfg.raw.get("mip") or {}).get("time_limit_s", 60))

    def by_limit(recs: list[Row], full: list[Row]) -> dict[str, list[Row]]:
        out: dict[str, list[Row]] = {}
        for factor in sorted({float(r["config"][1:]) for r in recs}):
            name = "T (time of the GA)" if factor == 1 else f"{factor:g} T"
            out[name] = [r for r in recs if float(r["config"][1:]) == factor]
        out[f"{full_limit:g} s"] = [{**r, "time_limit_s": r.get("time_limit_s", full_limit)} for r in full]
        return out

    e4 = time_rows(items, by_limit(timed40, base_mip), ref40, z, "8.4")
    e4 += time_rows(large, by_limit(timed_large, large_mip), ref_large, zl, "9.4")
    rep._both(
        tables,
        "E4_mip_equal_time",
        "FCTP: the MIP solver with the time of the GA (amendment 9.3)",
        f"T of an instance is the median run time of {reference} over its 10 runs (20 runs at once). The MIP "
        f"(HiGHS, one thread) is run with the limit T, with a multiple of T and with 60 s; its plan is compared "
        f"with the median cost of {reference} over the seeds. `ga_better_or_no_plan` includes the instances "
        "where the MIP has no plan at the limit. Descriptive: the times depend on the machine and on the load; "
        "no test is made.",
        e4,
    )
    figure(cfg, items, large, base_rows + tuned, large_rows, base_mip, large_mip, timed, z, zl)
    return {
        "selected": {k: v["config"] for k, v in chosen.items()},
        "records_tuned": len(tuned),
        "records_large": len(large_rows),
        "mip_time_records": len(timed),
        "z_best_lowered_on": changed,
        "tests": len(e3) + len(e7),
    }


def figure(
    cfg: ConfigV3,
    items: list[Row],
    large: list[Row],
    rows: list[Row],
    large_rows: list[Row],
    mip: list[Row],
    large_mip: list[Row],
    timed: list[Row],
    z: dict[str, tuple[float, str]],
    zl: dict[str, tuple[float, str]],
) -> None:
    """Median over instances of the gap to Z_best by size, for each rho: the GA variants, Balinski and the
    MIP plans with 60 s and with the time of the GA."""
    plt = rep._pyplot()
    everything = items + large
    best = {**z, **zl}
    series: dict[str, dict[str, float]] = {}
    med = rep.instance_medians(
        [{**r, "gap": _gap(r["cost"], best[r["instance"]][0])} for r in rows + large_rows], "gap"
    )
    for (name, iid), value in med.items():
        series.setdefault(name, {})[iid] = value
    for label, recs in (
        (MIP_60, mip + large_mip),
        ("MIP, time of the GA", [r for r in timed if r["config"] == "x1"]),
    ):
        series[label] = {r["instance"]: _gap(r["cost"], best[r["instance"]][0]) for r in recs if r["cost"] is not None}
    shown = [n for n in cfg.raw.get("figure_methods", []) if n in series] or sorted(series)
    rhos = sorted({i["rho"] for i in everything})
    sizes = sorted({i["size"] for i in everything}, key=rep._size_key)
    fig, axes = plt.subplots(1, len(rhos), figsize=(4.4 * len(rhos), 4.2), sharey=True, squeeze=False)
    top = 0.0
    for ax, rho in zip(axes[0], rhos, strict=True):
        for name in shown:
            xs, ys = [], []
            for pos, size in enumerate(sizes):
                ids = [i["id"] for i in everything if i["size"] == size and i["rho"] == rho]
                values = [series[name][i] for i in ids if i in series[name]]
                if ids and len(values) == len(ids):  # a point only where the method has a plan on every instance
                    xs.append(pos)
                    ys.append(statistics.median(values))
            ax.plot(xs, ys, marker="o", linewidth=1.4, markersize=4, label=name)
            top = max([top, *ys])
        ax.set_xticks(range(len(sizes)))
        ax.set_xticklabels(sizes)
        ax.set_yscale("symlog", linthresh=0.1)
        ax.set_title(f"rho = {rho:g}", fontsize=9)
        ax.set_xlabel("size")
        ax.grid(True, which="both", linewidth=0.3, alpha=0.6)
    axes[0][0].set_ylim(0, 1.3 * top if top > 0 else 1.0)  # shared axis: the largest value of both panels
    axes[0][0].set_ylabel("gap to the best known value, %")
    axes[0][-1].legend(fontsize=7)
    fig.tight_layout()
    rep._save(fig, cfg.area / "figures", "fctp_gap_sizes")
    plt.close(fig)
