"""Tables and figures of amendment 10, rebuilt from the raw records (``review/tables``, ``review/figures``).

R0 rules and times, R1 grids of the rivals, R2 gap of every method on the 60 FCTP instances, R3 tests of the
GA against the rivals, R4 MIP in two settings, R5 new instance classes, R6 public instances, R7 times with one
run at a time, R8 share of pivots with theta > 0, R9 second rule for the entering arc, S1 every paired
comparison of experiment v3 in one table, S2 bootstrap intervals for the linear problem, S3 the two
normalisations. Every gap of this module uses the Z_best of amendment 10 (see :func:`fctp_data`).
"""

from __future__ import annotations

import csv
import json
import math
import statistics
from pathlib import Path
from typing import Any

import numpy as np

from tpga.classical import northwest_corner
from tpga.experiments.v2 import methods as v2_methods
from tpga.experiments.v3 import core, ext, rev
from tpga.experiments.v3 import report as rep
from tpga.experiments.v3.core import ConfigV3, records

Row = dict[str, Any]
Series = dict[str, dict[str, list[float]]]
MIP_T = "MIP, time of the GA"
MIP_300 = "MIP, all threads, 300 s"
NOTE = "Exploratory (amendment 10, written after the results of amendments 8 and 9 were seen). "


def _gap(cost: float, z: float) -> float:
    return 100.0 * (cost - z) / z


class Boot:
    """Percentile bootstrap of the median over instances (10.6); one generator for the whole report."""

    def __init__(self, cfg: ConfigV3) -> None:
        spec = cfg.raw["bootstrap"]
        self.resamples = int(spec["resamples"])
        self.rng = np.random.default_rng(int(spec["seed"]))

    def interval(self, values: list[float]) -> tuple[float, float]:
        v = np.asarray(values, dtype=float)
        if v.size == 0:
            return math.nan, math.nan
        pick = self.rng.integers(0, v.size, size=(self.resamples, v.size))
        low, high = np.percentile(np.median(v[pick], axis=1), [2.5, 97.5])
        return float(low), float(high)


def add(series: Series, name: str, iid: str, value: float) -> None:
    series.setdefault(name, {}).setdefault(iid, []).append(value)


def medians(series: Series) -> dict[tuple[str, str], float]:
    return {(name, iid): statistics.median(v) for name, by in series.items() for iid, v in by.items()}


def cell_table(
    groups: list[tuple[Row, list[str]]], names: list[str], gaps: Series, times: Series, boot: Boot
) -> list[Row]:
    """One row per cell and method: median over the instances of the per-instance median gap, its bootstrap
    interval, the range over the runs and the median time."""
    table: list[Row] = []
    for label, ids in groups:
        for name in names:
            by = gaps.get(name, {})
            mine = [i for i in ids if i in by]
            if not mine:
                continue
            per_instance = [statistics.median(by[i]) for i in mine]
            runs = [g for i in mine for g in by[i]]
            low, high = boot.interval(per_instance)
            secs = [t for i in mine for t in times.get(name, {}).get(i, [])]
            table.append(
                {
                    **label,
                    "method": name,
                    "instances": len(mine),
                    "runs": len(runs),
                    "gap_instance_median": statistics.median(per_instance),
                    "ci95_low": low,
                    "ci95_high": high,
                    "gap_min": min(runs),
                    "gap_max": max(runs),
                    "time_median_s": statistics.median(secs) if secs else None,
                }
            )
    return table


def tests(med: dict[tuple[str, str], float], scopes: list[tuple[str, list[str]]], pairs: list[list[str]]) -> list[Row]:
    out: list[Row] = []
    for label, ids in scopes:
        out += rep.paired_rows(med, ids, pairs, {"scope": label})
    return out


# --- data of the fixed-charge problem ------------------------------------------------------


def fctp_data(cfg: ConfigV3) -> Row:
    """Records of the 60 FCTP instances and the Z_best of amendment 10: the optimum if a MIP run proved one,
    otherwise the smallest cost over every MIP run and every heuristic run on disk."""
    e = rev.ext_cfg(cfg)
    b = ext.base(e)
    base_rows, base_mip, items40 = rep.fctp_rows(b)
    large = ext.large_items(e)
    raw, mine = e.area / "raw", rev.area(cfg) / "raw"
    tuned = records(raw / "runs_ft.jsonl", "main")
    large_rows = records(raw / "large.jsonl", "large")
    large_mip = records(raw / "large_mip.jsonl", "large-mip")
    timed = records(raw / "mip_time.jsonl", "mip-time")
    rivals = records(mine / "rivals.jsonl", "rivals")
    timing = records(mine / "timing.jsonl", "timing")
    timing_mip = records(mine / "timing_mip.jsonl", "timing-mip")
    default = records(mine / "mip_default.jsonl", "mip-default")
    items = items40 + large
    labelled = (
        [(r, "MIP, 1 thread, 60 s") for r in base_mip + large_mip]
        + [(r, f"MIP, limit {r['config']} the time of the GA") for r in timed]
        + [(r, "MIP, limit = time of the GA on one processor") for r in timing_mip]
        + [(r, MIP_300) for r in default]
    )
    heuristic = base_rows + tuned + large_rows + rivals + timing
    z: dict[str, tuple[float, str, bool]] = {}
    for inst in items:
        iid = inst["id"]
        mips = [(r, label) for r, label in labelled if r["instance"] == iid and r["cost"] is not None]
        low_h = min((r for r in heuristic if r["instance"] == iid), key=lambda r: r["cost"])
        low_m, low_label = min(mips, key=lambda pair: pair[0]["cost"])
        proved = [r for r, _ in mips if r["proved"]]
        if proved:
            value = min(float(r["cost"]) for r in proved)
            if max(float(r["cost"]) for r in proved) - value > 1e-6 or low_h["cost"] < value - 1e-6:
                raise RuntimeError(f"{iid}: runs disagree with a proved optimum")
            z[iid] = (value, "MIP (proved optimum)", True)
        elif low_m["cost"] <= low_h["cost"]:
            z[iid] = (float(low_m["cost"]), low_label, False)
        else:
            z[iid] = (float(low_h["cost"]), str(low_h["method"]), False)
    ids40 = {i["id"] for i in items40}
    old = ext.best_known(
        items40, {r["instance"]: r for r in base_mip}, base_rows, tuned, [r for r in timed if r["instance"] in ids40]
    )
    old.update(
        ext.best_known(
            large,
            {r["instance"]: r for r in large_mip},
            large_rows,
            [r for r in timed if r["instance"] not in ids40],
        )
    )
    gaps: Series = {}
    times: Series = {}
    for r in base_rows + tuned + large_rows + rivals:  # runs made with 20 at once
        add(gaps, r["method"], r["instance"], _gap(r["cost"], z[r["instance"]][0]))
        add(times, r["method"], r["instance"], r["time_s"])
    for name, recs in (
        (ext.MIP_60, base_mip + large_mip),
        (MIP_T, [r for r in timed if r["config"] == "x1"]),
        (MIP_300, default),
    ):
        for r in recs:
            if r["cost"] is not None:
                add(gaps, name, r["instance"], _gap(r["cost"], z[r["instance"]][0]))
                add(times, name, r["instance"], r["time_s"])
    return {
        "items": items,
        "z": z,
        "z_before": old,
        "gaps": gaps,
        "times": times,
        "reference": {r["instance"]: r for r in base_mip + large_mip},
        "default": {r["instance"]: r for r in default},
        "timing": timing,
        "timing_mip": {r["instance"]: r for r in timing_mip},
        "base_methods": list(b.raw["methods"]),
    }


def _groups(items: list[Row]) -> list[tuple[Row, list[str]]]:
    return [
        ({"size": size, "rho": rho}, [i["id"] for i in items if (i["size"], i["rho"]) == (size, rho)])
        for size, rho in rev.cells(items)
    ]


def _scopes(items: list[Row]) -> list[tuple[str, list[str]]]:
    scopes = [("all instances", [i["id"] for i in items])]
    scopes += [
        (f"rho = {rho:g}", [i["id"] for i in items if i["rho"] == rho]) for rho in sorted({i["rho"] for i in items})
    ]
    scopes += [
        (f"size {s}", [i["id"] for i in items if i["size"] == s]) for s in dict.fromkeys(i["size"] for i in items)
    ]
    return scopes


# --- parts of the report -------------------------------------------------------------------


def report_rivals(cfg: ConfigV3, data: Row, boot: Boot, tables: Path) -> Row:
    table, _ = rev.grid_table(cfg)
    rep._both(
        tables,
        "R1_tuning",
        "FCTP: grids of Tabu and ILS on the training instances (amendment 10.1)",
        NOTE + "Mean training gap (%) over the 8 training instances of 9.2 and 3 seeds; the reference of an "
        "instance is its MIP value of 9.2 or a smaller value of a run of the grid of 9.2 or of these grids. "
        "`rank` is the order of the tie rule; `selected` marks the configuration with the smallest mean gap.",
        table,
    )
    items = data["items"]
    order = [*data["base_methods"], "GA-cost-cycle-ft", "GA-hybrid-ft", *cfg.raw["rivals"], MIP_T, ext.MIP_60, MIP_300]
    r2 = cell_table(_groups(items), order, data["gaps"], data["times"], boot)
    rep._both(
        tables,
        "R2_gap",
        "FCTP: gap of every method by size and rho (instances of 8.4 and 9.4)",
        NOTE + "gap = 100 (Z - Z_best) / Z_best with the Z_best of amendment 10 (proved optimum, otherwise the "
        "smallest cost over every MIP run and every heuristic run on disk). `gap_instance_median`: median over "
        "the instances of the median over the seeds; `ci95_*`: percentile bootstrap over the instances "
        "(10 000 resamples). Tabu and ILS start from the plan of Balinski and have the budget B = 200 m n of "
        "the GA (one evaluation of the start plan plus neighbour evaluations). A MIP row has one plan per "
        "instance; `MIP, time of the GA` has the limit of 9.3. Run times were measured with 20 runs at once.",
        r2,
    )
    changed = [
        {
            "instance": i["id"],
            "size": i["size"],
            "rho": i["rho"],
            "z_best_before": data["z_before"][i["id"]][0],
            "source_before": data["z_before"][i["id"]][1],
            "z_best": data["z"][i["id"]][0],
            "source": data["z"][i["id"]][1],
            "change_percent": _gap(data["z"][i["id"]][0], data["z_before"][i["id"]][0]),
        }
        for i in items
        if data["z"][i["id"]][0] < data["z_before"][i["id"]][0] - 1e-9
    ]
    rep._both(
        tables,
        "R2_z_best_lowered",
        "FCTP: instances where Z_best became smaller in amendment 10",
        NOTE + "`z_best_before` is the value used by the tables of amendments 8 and 9, which keep it.",
        changed,
    )
    med = medians(data["gaps"])
    r3 = tests(med, _scopes(items), cfg.raw["pairs"])
    rep._both(
        tables,
        "R3_tests",
        "FCTP: GA-cost-cycle against Tabu and ILS",
        NOTE + "Unit: the instance (median gap over its seeds). Two-sided Wilcoxon signed-rank test, Holm "
        "correction over the two pairs of each scope; `rank_biserial_r` and `hl_shift` (Hodges-Lehmann, with "
        "its 95 % interval) are for gap(method_a) - gap(method_b): positive means method_a (the GA) is worse.",
        r3,
    )
    return {"R2": len(r2), "R3": len(r3), "z_best_lowered": len(changed)}


def report_mip(cfg: ConfigV3, data: Row, tables: Path) -> Row:
    plan = json.loads((rev.area(cfg) / "mip_default.json").read_text(encoding="utf-8"))
    order = {iid: k for k, iid in enumerate(plan["order"])}
    rows: list[Row] = []
    for inst in sorted(data["items"], key=lambda i: order[i["id"]]):
        a, d = data["reference"][inst["id"]], data["default"].get(inst["id"])
        row: Row = {
            "order": order[inst["id"]],
            "instance": inst["id"],
            "size": inst["size"],
            "rho": inst["rho"],
            "status_1thread_60s": a["status"],
            "proved_1thread_60s": bool(a["proved"]),
            "cost_1thread_60s": a["cost"],
            "gap_percent_1thread_60s": None if a["mip_gap"] is None else 100.0 * a["mip_gap"],
            "time_s_1thread_60s": a["time_s"],
            "status_all_threads_300s": "not run (time rule)" if d is None else d["status"],
        }
        if d is not None:
            row.update(
                proved_all_threads_300s=bool(d["proved"]),
                cost_all_threads_300s=d["cost"],
                gap_percent_all_threads_300s=None if d["mip_gap"] is None else 100.0 * d["mip_gap"],
                time_s_all_threads_300s=d["time_s"],
                cpu_s_all_threads_300s=d["cpu_s"],
                cpu_over_wall=d["cpu_s"] / d["time_s"] if d["time_s"] > 0 else None,
                nodes_all_threads_300s=d["nodes"],
                cost_change_percent=None if d["cost"] is None or a["cost"] is None else _gap(d["cost"], a["cost"]),
            )
        rows.append(row)
    rep._both(
        tables,
        "R4_mip_instances",
        "FCTP: the MIP solver in two settings, by instance",
        NOTE + "Model of 8.4 (x <= min(a, b) y) in HiGHS, relative gap 0, absolute gap 0.99. Setting 1: one "
        "thread, 60 s, made with 20 runs at once (records of 8.4 and 9.4). Setting 2: `threads = 0` (the "
        "solver's own choice among all processors), 300 s, one run at a time in a fresh process; `cpu_s` is "
        "the processor time of that process, `cpu_over_wall` shows how much of the run was parallel. "
        "`order` is the order of the time rule (10.0); `not run (time rule)`: not started within the limit of "
        "90 minutes. `cost_change_percent` = 100 (cost of setting 2 - cost of setting 1) / cost of setting 1.",
        rows,
    )
    summary: list[Row] = []
    for label, ids in _groups(data["items"]):
        mine = [r for r in rows if r["instance"] in ids]
        ran = [r for r in mine if "cost_all_threads_300s" in r]
        gaps_a = [r["gap_percent_1thread_60s"] for r in mine if r["gap_percent_1thread_60s"] is not None]
        gaps_b = [r["gap_percent_all_threads_300s"] for r in ran if r["gap_percent_all_threads_300s"] is not None]
        summary.append(
            {
                **label,
                "instances": len(mine),
                "proved_1thread_60s": sum(r["proved_1thread_60s"] for r in mine),
                "gap_median_percent_1thread_60s": statistics.median(gaps_a) if gaps_a else None,
                "time_median_s_1thread_60s": statistics.median(r["time_s_1thread_60s"] for r in mine),
                "run_all_threads_300s": len(ran),
                "proved_all_threads_300s": sum(r["proved_all_threads_300s"] for r in ran),
                "gap_median_percent_all_threads_300s": statistics.median(gaps_b) if gaps_b else None,
                "time_median_s_all_threads_300s": statistics.median(r["time_s_all_threads_300s"] for r in ran)
                if ran
                else None,
                "cpu_over_wall_median": statistics.median(r["cpu_over_wall"] for r in ran) if ran else None,
                "gap_median_percent_1thread_60s_same_instances": statistics.median(
                    r["gap_percent_1thread_60s"] for r in ran
                )
                if ran
                else None,
                "plan_better_with_300s": sum(r["cost_change_percent"] < 0 for r in ran),
                "plan_equal": sum(r["cost_change_percent"] == 0 for r in ran),
                "plan_worse_with_300s": sum(r["cost_change_percent"] > 0 for r in ran),
            }
        )
    rep._both(
        tables,
        "R4_mip_summary",
        "FCTP: the MIP solver in two settings, by size and rho",
        NOTE + "Counts and medians of R4_mip_instances. `gap_*` is the gap of the solver, 100 (cost - bound) / "
        "cost. The columns of setting 2 cover the instances that were run (`run_all_threads_300s`); "
        "`gap_median_percent_1thread_60s_same_instances` gives setting 1 on these same instances.",
        summary,
    )
    return {"R4_run": sum("cost_all_threads_300s" in r for r in rows), "R4_not_run": len(plan["not_run_time_rule"])}


def report_generator(cfg: ConfigV3, data: Row, boot: Boot, tables: Path) -> Row:
    plan = rev.generator_plan(cfg)
    k = int(plan["instances_per_new_cell"])
    items = [i for i in rev.generator_items(cfg) if not i["new"] or rev.index_of(i) < k]
    raw = rev.area(cfg) / "raw"
    mip = {r["instance"]: r for r in records(raw / "gen_mip.jsonl", "gen-mip")}
    runs = records(raw / "gen.jsonl", "gen")
    names = list(cfg.raw["generator"]["methods"])
    gaps: Series = {}
    times: Series = {}
    reference: list[Row] = []
    for inst in items:
        iid = inst["id"]
        if not inst["new"]:
            for name in [*names, ext.MIP_60]:
                gaps.setdefault(name, {})[iid] = data["gaps"][name][iid]
                times.setdefault(name, {})[iid] = data["times"][name][iid]
            continue
        mine = [r for r in runs if r["instance"] == iid]
        m = mip[iid]
        low = min(r["cost"] for r in mine)
        if m["proved"] and low < m["cost"] - 1e-6:
            raise RuntimeError(f"a run on {iid} is below the proved optimum")
        z = float(m["cost"]) if m["proved"] or (m["cost"] is not None and m["cost"] <= low) else float(low)
        for r in mine:
            add(gaps, r["method"], iid, _gap(r["cost"], z))
            add(times, r["method"], iid, r["time_s"])
        if m["cost"] is not None:
            add(gaps, ext.MIP_60, iid, _gap(m["cost"], z))
            add(times, ext.MIP_60, iid, m["time_s"])
        reference.append({**inst, "proved": bool(m["proved"]), "mip_gap": m["mip_gap"], "from_mip": z == m["cost"]})
    groups = []
    keys = sorted({(i["class"], i["rho"], i["m"]) for i in items}, key=lambda c: (c[0] != "uniform", c[1], c[2]))
    for cls, rho, m in keys:
        mine_i = [i for i in items if (i["class"], i["rho"], i["m"]) == (cls, rho, m)]
        new = [r for r in reference if r["id"] in {i["id"] for i in mine_i}]
        label = {
            "class": cls,
            "rho": rho,
            "size": mine_i[0]["size"],
            "instances_from": "amendment 10" if mine_i[0]["new"] else "amendments 8 and 9",
            "mip_proved": sum(r["proved"] for r in new) if new else None,
        }
        groups.append((label, [i["id"] for i in mine_i]))
    r5 = cell_table(groups, [*names, ext.MIP_60], gaps, times, boot)
    rep._both(
        tables,
        "R5_generator_gap",
        "FCTP: new instance classes (amendment 10.3 b)",
        NOTE + "Class `uniform`: generator of 8.4 with rho = 0.05 and 5 (new) and rho = 0.2 and 1 (instances of "
        "8.4 and 9.4). Class `concentrated`: a tenth of the suppliers hold 80 % of the supply. Gap to Z_best "
        "(proved optimum of the MIP with 1 thread and 60 s, otherwise the best known value); `mip_proved` "
        "counts the new instances of the cell with a proved optimum. Columns as in R2_gap. Nothing was tuned "
        "on these instances.",
        r5,
    )
    med = medians(gaps)
    scopes = []
    for cls, rho in dict.fromkeys((c[0], c[1]) for c in keys):
        scopes.append((f"{cls}, rho = {rho:g}", [i["id"] for i in items if (i["class"], i["rho"]) == (cls, rho)]))
    r5t = tests(med, scopes, cfg.raw["pairs"])
    rep._both(
        tables,
        "R5_generator_tests",
        "FCTP: GA-cost-cycle against Tabu and ILS on the instance classes",
        NOTE + "As R3_tests; one scope per class and rho (the three sizes together), Holm over the two pairs.",
        r5t,
    )
    return {"R5": len(r5), "R5_tests": len(r5t), "generator_instances_per_new_cell": k}


def report_public(cfg: ConfigV3, tables: Path) -> Row:
    spec = cfg.raw["public"]
    plan = json.loads((rev.area(cfg) / "public.json").read_text(encoding="utf-8"))
    raw = rev.area(cfg) / "raw"
    mip = {r["instance"]: r for r in records(raw / "public_mip.jsonl", "public-mip")}
    runs = records(raw / "public.jsonl", "public")
    rows: list[Row] = []
    for b in spec["instances"]:
        iid = b["id"]
        if iid not in plan["instances"]:
            continue
        mine = [r for r in runs if r["instance"] == iid]
        m = mip[iid]
        published = {k: float(v) for k, v in b["published"].items()}
        ours = [r["cost"] for r in mine] + ([m["cost"]] if m["cost"] is not None else [])
        z = float(m["cost"]) if m["proved"] else min([*published.values(), *ours])
        row: Row = {
            "instance": iid,
            "size": mine[0]["size"],
            **{f"published_{k}": v for k, v in published.items()},
            "barr2021": b.get("barr2021"),
            "mip_cost": m["cost"],
            "mip_status": m["status"],
            "mip_proved": bool(m["proved"]),
            "mip_time_s": m["time_s"],
            "z_ref": z,
            "z_ref_minus_smallest_published": z - min(published.values()),
        }
        for name in spec["methods"]:
            costs = [r["cost"] for r in mine if r["method"] == name]
            row[f"{name}_median"] = statistics.median(costs)
            row[f"{name}_best"] = min(costs)
            row[f"{name}_gap_median_percent"] = _gap(statistics.median(costs), z)
        rows.append(row)
    rep._both(
        tables,
        "R6_public",
        "FCTP: public instances (subset of the test problems of Sun et al. used by Glover et al. 2005)",
        NOTE + str(spec["source"]) + " `published_*`: CPLEX 9.0, tabu search of Sun et al. and the parametric "
        "ghost image process, as printed there; `barr2021`: the value of Barr et al. (Networks, 2021, Table 2), "
        "which differs for a reason we do not know. `mip_*`: our HiGHS run (1 thread, 60 s). z_ref: the optimum "
        "proved by our MIP, otherwise the smallest of the published and of our values. Methods: 10 seeds, "
        "B = 200 m n; gap of the median cost to z_ref.",
        rows,
    )
    return {"R6": len(rows), "public_left_out": plan["left_out"]}


def report_timing(cfg: ConfigV3, data: Row, tables: Path) -> Row:
    plan = json.loads((rev.area(cfg) / "timing.json").read_text(encoding="utf-8"))
    used = [iid for r in plan["rounds"] if r["started"] for iid in r["instances"]]
    items = [i for i in data["items"] if i["id"] in used]
    rows: list[Row] = []
    names = list(cfg.raw["timing"]["methods"])
    for label, ids in _groups(items):
        mips = [data["timing_mip"][i] for i in ids]
        with_plan = [r for r in mips if r["cost"] is not None]
        for name in names:
            mine = [r for r in data["timing"] if r["instance"] in ids and r["method"] == name]
            cost = {i: statistics.median(r["cost"] for r in mine if r["instance"] == i) for i in ids}
            loaded = [t for i in ids for t in data["times"][name][i]]
            rows.append(
                {
                    **label,
                    "method": name,
                    "instances": len(ids),
                    "runs": len(mine),
                    "time_one_processor_median_s": statistics.median(r["time_s"] for r in mine),
                    "time_20_at_once_median_s": statistics.median(loaded),
                    "decoder_or_start_evaluations": statistics.median(
                        r.get("full_evaluations", r["evals"]) for r in mine
                    ),
                    "neighbour_evaluations": statistics.median(r.get("neighbour_evaluations", 0) for r in mine),
                    "gap_median": statistics.median(_gap(r["cost"], data["z"][r["instance"]][0]) for r in mine),
                    "better_than_mip": sum(cost[r["instance"]] < r["cost"] for r in with_plan),
                    "equal_to_mip": sum(cost[r["instance"]] == r["cost"] for r in with_plan),
                    "worse_than_mip": sum(cost[r["instance"]] > r["cost"] for r in with_plan),
                    "mip_no_plan": len(mips) - len(with_plan),
                }
            )
        rows.append(
            {
                **label,
                "method": "MIP, limit = time of GA-cost-cycle",
                "instances": len(ids),
                "runs": len(mips),
                "time_one_processor_median_s": statistics.median(r["time_s"] for r in mips),
                "time_limit_median_s": statistics.median(r["time_limit_s"] for r in mips),
                "gap_median": statistics.median(_gap(r["cost"], data["z"][r["instance"]][0]) for r in with_plan)
                if with_plan
                else None,
                "mip_no_plan": len(mips) - len(with_plan),
                "mip_proved": sum(bool(r["proved"]) for r in mips),
            }
        )
    rep._both(
        tables,
        "R7_timing",
        "FCTP: time with one run at a time on one logical processor (amendment 10.4)",
        NOTE + f"Processor {plan['cpu']} (process bound to it: {plan['pinned']}), no other run of the experiment "
        "active; 5 seeds per instance. The MIP run of an instance (1 thread) has the median time of its five "
        "GA-cost-cycle runs of this block as its limit. `decoder_or_start_evaluations`: decoder calls of the GA, "
        "or the one evaluation of the start plan of Tabu and ILS; `neighbour_evaluations`: the separate counter "
        "of the local searches; their sum is B = 200 m n. `better/equal/worse_than_mip`: the median cost of the "
        "method on an instance against the cost of that MIP plan. `time_20_at_once_median_s`: the same method "
        "on the same instances in the runs made with 20 at once.",
        rows,
    )
    return {"R7": len(rows), "timing_instances": len(items), "timing_sizes_left_out": plan["sizes_left_out"]}


def report_degenerate(cfg: ConfigV3, boot: Boot, tables: Path) -> tuple[Row, list[Row]]:
    lin = rev.lin_cfg(cfg)
    spec = cfg.raw["degenerate"]
    raw = rev.area(cfg) / "raw" / "linear.jsonl"
    plan = rev.degenerate_plan(cfg)
    trace_tasks, nd_tasks = rev.degenerate_tasks(
        cfg, int(plan["instances_at_reduce_size"]), int(plan["traced_instances_at_reduce_size"])
    )
    trace = ext._complete(records(raw, "trace"), trace_tasks, "10.5 a")
    nd = ext._complete(records(raw, "nd"), nd_tasks, "10.5 b")
    r8: list[Row] = []
    parts = 10
    for name in spec["variants"].values():
        params = core.method_fields(lin, name)["params"]
        for size in spec["trace"]["sizes"]:
            mine = [r for r in trace if r["method"] == name and r["size"] == size]
            shares: list[list[float]] = [[] for _ in range(parts)]
            for r in mine:
                done = [[0, 0] for _ in range(parts)]
                before = (0, 0)
                for g, (pivots, zero) in enumerate(r["pivot_trace"], start=1):
                    evals = int(params["population"]) + g * int(r["offspring"])
                    d = min(parts - 1, math.ceil(parts * evals / r["budget"]) - 1)
                    done[d][0] += pivots - before[0]
                    done[d][1] += zero - before[1]
                    before = (pivots, zero)
                for d in range(parts):
                    if done[d][0]:
                        shares[d].append(1.0 - done[d][1] / done[d][0])
            for d in range(parts):
                if shares[d]:
                    r8.append(
                        {
                            "method": name,
                            "size": size,
                            "budget_from_percent": 10 * d,
                            "budget_to_percent": 10 * (d + 1),
                            "instances": len({r["instance"] for r in mine}),
                            "runs": len(shares[d]),
                            "share_theta_positive_median": statistics.median(shares[d]),
                            "share_theta_positive_min": min(shares[d]),
                            "share_theta_positive_max": max(shares[d]),
                        }
                    )
    rep._both(
        tables,
        "R8_theta_share",
        "Linear problem: share of pivots with theta > 0 along the budget (amendment 10.5 a)",
        NOTE + "Runs of GA-rand-cycle and GA-cost-cycle of 8.3 repeated with a record of the pivots of every "
        "generation (same seeds; their costs equal the recorded ones). A generation belongs to the tenth of "
        "the budget in which its last evaluation falls (the first tenth includes the start population, which "
        "makes no pivot). Median, smallest and largest share over the runs of a size.",
        r8,
    )
    old, items = rep.linear_rows(lin)
    gaps: Series = {}
    times: Series = {}
    for r in old + nd:
        add(gaps, r["method"], r["instance"], r["gap"])
        add(times, r["method"], r["instance"], r["time_s"])
    cells = sorted({(i["set"], i["size"]) for i in items}, key=lambda c: (c[0] != "uniform", rep._size_key(c[1])))
    with_nd = {r["instance"] for r in nd}
    groups = [
        ({"set": s, "size": z}, [i["id"] for i in items if (i["set"], i["size"]) == (s, z) and i["id"] in with_nd])
        for s, z in cells
    ]
    order = [x for pair in spec["variants"].items() for x in (pair[1], pair[0])]
    r9 = cell_table(groups, order, gaps, times, boot)
    for row in r9:
        ids = next(g for label, g in groups if (label["set"], label["size"]) == (row["set"], row["size"]))
        mine = [r for r in old + nd if r["method"] == row["method"] and r["instance"] in ids]
        row["pivots_theta_zero_share"] = sum(r["zero_pivots"] for r in mine) / sum(r["pivots"] for r in mine)
        row["pivots_left_to_uniform_rule_share"] = (
            sum(r["fallback_pivots"] for r in mine) / sum(r["pivots"] for r in mine)
            if row["method"] in spec["variants"]
            else None
        )
        row["unchanged_offspring_share"] = sum(r["unchanged_offspring"] for r in mine) / sum(
            r["evals"]
            - int(core.method_fields(lin, spec["variants"].get(row["method"], row["method"]))["params"]["population"])
            for r in mine
        )
    rep._both(
        tables,
        "R9_entering_rule",
        "Linear problem: two rules for the entering arc of the cycle mutation (amendment 10.5 b)",
        NOTE + "`-nd`: the entering arc is drawn among the non-basic arcs whose cycle has no arc with zero "
        "amount on a minus position (theta > 0); otherwise the same GA, parameters, k, seeds and budget. Gap "
        "to Z* in percent, columns as in R2_gap. The runs without `-nd` are the records of amendments 8 and 9. "
        "`pivots_left_to_uniform_rule_share`: pivots for which no such arc existed. `unchanged_offspring_share`"
        ": offspring whose pivots all had theta = 0. Times with 20 runs at once.",
        r9,
    )
    med = medians(gaps)
    pairs = [[name, base] for name, base in spec["variants"].items()]
    scopes = [(f"{label['set']} {label['size']}", ids) for label, ids in groups]
    scopes.append(("all instances", [i for _, ids in groups for i in ids]))
    r9t = tests(med, scopes, pairs)
    rep._both(
        tables,
        "R9_entering_tests",
        "Linear problem: the second rule for the entering arc against the present rule",
        NOTE + "Unit: the instance (median gap over 10 seeds). Two-sided Wilcoxon signed-rank test, Holm over "
        "the two pairs of each scope; `hl_shift` and `rank_biserial_r` are for gap(method_a) - gap(method_b): "
        "negative means the second rule gives the smaller gap.",
        r9t,
    )
    return {"R8": len(r8), "R9": len(r9), "R9_tests": len(r9t)}, r8


def report_statistics(cfg: ConfigV3, boot: Boot, tables: Path) -> tuple[Row, list[Row]]:
    lin = rev.lin_cfg(cfg)
    e = rev.ext_cfg(cfg)
    sources = [
        ("8.6 linear (T2_tests)", lin.area / "tables" / "T2_tests.csv"),
        ("9.1 linear 100x100 (T2_tests_extension)", lin.area / "tables" / "T2_tests_extension.csv"),
        ("8.4 FCTP (F3_tests)", e.area / "tables" / "F3_tests.csv"),
        ("9.2 FCTP tuned (E3_tests_tuned)", e.area / "tables" / "E3_tests_tuned.csv"),
        ("9.4 FCTP large (E7_large_tests)", e.area / "tables" / "E7_large_tests.csv"),
        ("10.1 FCTP rivals (R3_tests)", tables / "R3_tests.csv"),
        ("10.3 FCTP classes (R5_generator_tests)", tables / "R5_generator_tests.csv"),
        ("10.5 entering rule (R9_entering_tests)", tables / "R9_entering_tests.csv"),
    ]
    keep = (
        "method_a", "method_b", "n", "wins_a", "ties", "losses_a", "median_a", "median_b", "p", "p_holm",
        "rank_biserial_r", "hl_shift", "hl_ci_low", "hl_ci_high", "hl_ci_method",
    )  # fmt: skip
    s1: list[Row] = []
    for title, path in sources:
        if not path.exists():  # a table that its report did not have to write (no rows)
            continue
        with path.open(encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                if "hl_ci_low" not in r:
                    raise RuntimeError(f"{path.name} has no interval of the shift: rebuild the report it belongs to")
                scope = r.get("scope") or " ".join(x for x in (r.get("set"), r.get("size")) if x)
                s1.append({"comparison": title, "scope": scope, **{k: r[k] for k in keep}})
    rep._both(
        tables,
        "S1_pairs",
        "Every paired comparison of experiment v3 with effect sizes (amendment 10.6)",
        NOTE + "Rows of the test tables named in `comparison`, unchanged. Unit: the instance (median over its "
        "seeds); the measure is the gap in percent (to Z* for the linear problem, to the Z_best of the table "
        "it comes from for FCTP). `hl_shift`: Hodges-Lehmann estimate of gap(method_a) - gap(method_b) with "
        "its 95 % interval from the Walsh averages; `rank_biserial_r`: matched-pairs rank-biserial "
        "correlation (negative: method_a has the smaller gap). `p_holm`: Holm within the family of its table.",
        s1,
    )
    old, items = rep.linear_rows(lin)
    nwc = {i["id"]: northwest_corner(v2_methods.load(i["path"])).cost for i in items}
    star = {i["id"]: float(i["z_star"]) for i in items}
    gap: Series = {}
    rand: Series = {}
    corner: Series = {}
    for r in old:
        add(gap, r["method"], r["instance"], r["gap"])
        if r.get("gap_norm") is not None:
            add(rand, r["method"], r["instance"], r["gap_norm"])
        if nwc[r["instance"]] > star[r["instance"]]:
            add(
                corner,
                r["method"],
                r["instance"],
                (r["cost"] - star[r["instance"]]) / (nwc[r["instance"]] - star[r["instance"]]),
            )
    names = list(lin.raw["methods"])
    cells = sorted({(i["set"], i["size"]) for i in items}, key=lambda c: (c[0] != "uniform", rep._size_key(c[1])))
    groups = [({"set": s, "size": z}, [i["id"] for i in items if (i["set"], i["size"]) == (s, z)]) for s, z in cells]
    s2 = cell_table(groups, names, gap, {}, boot)
    for row in s2:
        del row["time_median_s"]
    rep._both(
        tables,
        "S2_bootstrap_linear",
        "Linear problem: median gap of every method by cell with a bootstrap interval (amendment 10.6)",
        NOTE + "Gap to Z* in percent. `gap_instance_median`: median over the instances of the median over the "
        "seeds; `ci95_*`: percentile bootstrap over the instances of the cell (10 000 resamples).",
        s2,
    )
    s3: list[Row] = []
    same = 0
    for label, ids in groups:
        part = []
        both = [i for i in ids if all(i in rand.get(n, {}) and i in corner.get(n, {}) for n in names)]
        for name in names:
            a = [statistics.median(rand[name][i]) for i in both]
            c = [statistics.median(corner[name][i]) for i in both]
            part.append(
                {
                    **label,
                    "method": name,
                    "instances": len(ids),
                    "instances_with_both": len(both),
                    "norm_rand_median": statistics.median(a),
                    "norm_nwc_median": statistics.median(c),
                }
            )
        for key, rank in (("norm_rand_median", "rank_rand"), ("norm_nwc_median", "rank_nwc")):
            for row in part:
                row[rank] = 1 + sum(other[key] < row[key] for other in part)
        equal = all(row["rank_rand"] == row["rank_nwc"] for row in part)
        same += equal
        for row in part:
            row["same_order_in_cell"] = equal
        s3 += part
    rep._both(
        tables,
        "S3_normalisation",
        "Linear problem: two normalisations of the gap (amendment 10.6)",
        NOTE + "`norm_rand` = (Z - Z*) / (Z_rand - Z*) as in 8.3 (Z_rand: mean cost of random basic plans); "
        "`norm_nwc` = (Z - Z*) / (Z_NWC - Z*) with the north-west corner plan. Median over the instances of "
        "the median over the seeds, on the instances where both denominators are positive "
        "(`instances_with_both`). `rank_*`: 1 = smallest median in the cell (equal medians share a rank); "
        "`same_order_in_cell`: the two rankings of the cell are identical.",
        s3,
    )
    return {"S1": len(s1), "S2": len(s2), "S3_cells": len(groups), "S3_cells_with_same_order": same}, s2


def report_rules(cfg: ConfigV3, tables: Path) -> Row:
    out = rev.area(cfg)
    spent = json.loads((out / "budget.json").read_text(encoding="utf-8"))["commands"]

    def load(name: str) -> Row:
        path = out / name
        return dict(json.loads(path.read_text(encoding="utf-8"))) if path.exists() else {}

    riv, gen, deg, pub, tim, mip = (
        load(n)
        for n in ("rivals.json", "generator.json", "degenerate.json", "public.json", "timing.json", "mip_default.json")
    )
    gave = {
        "pilot": f"{load('pilot.json').get('runs')} single runs",
        "tune": "grids complete",
        "rivals": f"{riv.get('instances_70x70')} instances per cell at 70x70, {riv.get('instances_50x50')} at 50x50",
        "generator": f"{gen.get('instances_per_new_cell')} instances per new cell",
        "degenerate": f"{deg.get('instances_at_reduce_size')} instances at 100x100 for 10.5 b, "
        f"{deg.get('traced_instances_at_reduce_size')} for 10.5 a",
        "public": f"{len(pub.get('instances', []))} instances, {len(pub.get('left_out', []))} left out",
        "timing": f"{sum(r['started'] for r in tim.get('rounds', []))} round(s) of one instance per cell; "
        f"sizes left out: {tim.get('sizes_left_out')}",
    }
    rows: list[Row] = []
    ran_total: list[str] = []
    for c in spent:
        text = gave.get(c["command"], "")
        if c["command"] == "mipdefault":
            state_ran = c.get("ran")
            text = "see R4_mip_instances" if state_ran is None else f"{state_ran} instances run"
        rows.append(
            {
                "command": c["command"],
                "started": c["started"],
                "allowance_s": c["allowance_s"],
                "wall_s": c["wall_s"],
                "beyond_limit": c["beyond_limit"],
                "rule_gave": text,
            }
        )
        ran_total.append(c["command"])
    total = sum(c["wall_s"] for c in spent if not c["beyond_limit"])
    rows.append(
        {
            "command": "all commands within the limit",
            "allowance_s": 60.0 * float(cfg.raw["limit_min"]),
            "wall_s": total,
            "rule_gave": f"MIP in its usual setting: {len(mip.get('ran', []))} run in the last start, "
            f"{len(mip.get('not_run_time_rule', []))} not run (time rule)",
        }
    )
    rep._both(
        tables,
        "R0_rules",
        "Amendment 10: time used by every run command and what the reduction rules gave",
        "Times in seconds, measured inside the commands (`review/budget.json`). Limit of all run commands: "
        f"{cfg.raw['limit_min']} minutes. `allowance_s`: what the command could use when it started (10.0, 10.9).",
        rows,
    )
    return {"time_used_s": total, "commands": ran_total}


# --- figures -------------------------------------------------------------------------------


def _style() -> Any:
    plt = rep._pyplot()
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Times New Roman", "DejaVu Serif"],
            "mathtext.fontset": "dejavuserif",
            "font.size": 9,
        }
    )
    return plt


def _save(fig: Any, directory: Path, name: str) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    fig.savefig(directory / f"{name}.pdf", metadata={"CreationDate": None})
    fig.savefig(directory / f"{name}.jpg", dpi=600, pil_kwargs={"quality": 92})


def _lines(ax: Any, table: list[Row], names: list[str], sizes: list[str], where: Row) -> None:
    markers = ["o", "s", "^", "D", "v", "P"]
    for k, name in enumerate(names):
        rows = {r["size"]: r for r in table if r["method"] == name and all(r[c] == v for c, v in where.items())}
        xs = [x + 0.06 * (k - (len(names) - 1) / 2) for x, s in enumerate(sizes) if s in rows]
        got = [rows[s] for s in sizes if s in rows]
        if not got:
            continue
        y = [r["gap_instance_median"] for r in got]
        err = [
            [r["gap_instance_median"] - r["ci95_low"] for r in got],
            [r["ci95_high"] - r["gap_instance_median"] for r in got],
        ]
        ax.errorbar(xs, y, yerr=err, marker=markers[k % 6], markersize=3.5, linewidth=1.1, capsize=2, label=name)
    ax.set_xticks(range(len(sizes)))
    ax.set_xticklabels(sizes)
    ax.set_yscale("symlog", linthresh=1.0)
    ax.set_ylim(bottom=0)
    ax.grid(True, which="both", linewidth=0.3, alpha=0.6)


def figures(cfg: ConfigV3, s2: list[Row], r2: list[Row], r8: list[Row]) -> list[str]:
    plt = _style()
    directory = rev.area(cfg) / "figures"
    names = list(cfg.raw["figure_linear"])
    sizes = sorted({r["size"] for r in s2 if r["set"] == "uniform"}, key=rep._size_key)
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    _lines(ax, s2, names, sizes, {"set": "uniform"})
    ax.set_xlabel("Problem size (uniform instances)")
    ax.set_ylabel("Gap to the optimum, % (median over instances)")
    ax.legend(fontsize=8)
    fig.tight_layout()
    _save(fig, directory, "linear_gap_sizes")
    plt.close(fig)

    names = list(cfg.raw["figure_fctp"])
    rhos = sorted({r["rho"] for r in r2})
    sizes = sorted({r["size"] for r in r2}, key=rep._size_key)
    fig, axes = plt.subplots(1, len(rhos), figsize=(3.6 * len(rhos), 3.8), sharey=True, squeeze=False)
    top = max(r["ci95_high"] for r in r2 if r["method"] in names)
    for ax, rho in zip(axes[0], rhos, strict=True):
        _lines(ax, r2, names, sizes, {"rho": rho})
        ax.set_ylim(0, 1.3 * top)
        ax.set_title(f"$\\rho$ = {rho:g}", fontsize=9)
        ax.set_xlabel("Problem size")
    axes[0][0].set_ylabel("Gap to the best known value, %")
    axes[0][-1].legend(fontsize=7)
    fig.tight_layout()
    _save(fig, directory, "fctp_gap_rivals")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    styles = {name: style for name, style in zip(dict.fromkeys(r["method"] for r in r8), ("-", "--"), strict=False)}
    for name, style in styles.items():
        for k, size in enumerate(dict.fromkeys(r["size"] for r in r8)):
            rows = [r for r in r8 if r["method"] == name and r["size"] == size]
            x = [r["budget_to_percent"] - 5 for r in rows]
            y = [100 * r["share_theta_positive_median"] for r in rows]
            low = [100 * r["share_theta_positive_min"] for r in rows]
            high = [100 * r["share_theta_positive_max"] for r in rows]
            ax.plot(x, y, style, color=f"C{k}", marker="o", markersize=3, linewidth=1.1, label=f"{name}, {size}")
            ax.fill_between(x, low, high, color=f"C{k}", alpha=0.12, linewidth=0)
    ax.set_xlabel("Part of the evaluation budget, %")
    ax.set_ylabel("Pivots with $\\theta$ > 0, %")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.grid(True, linewidth=0.3, alpha=0.6)
    ax.legend(fontsize=7, ncol=2)
    fig.tight_layout()
    _save(fig, directory, "theta_share")
    plt.close(fig)
    return ["linear_gap_sizes", "fctp_gap_rivals", "theta_share"]


def report(cfg: ConfigV3) -> dict[str, Any]:
    tables = rev.area(cfg) / "tables"
    boot = Boot(cfg)
    data = fctp_data(cfg)
    out: Row = {}
    out.update(report_rivals(cfg, data, boot, tables))
    out.update(report_mip(cfg, data, tables))
    out.update(report_generator(cfg, data, boot, tables))
    out.update(report_public(cfg, tables))
    out.update(report_timing(cfg, data, tables))
    part, r8 = report_degenerate(cfg, boot, tables)
    out.update(part)
    part, s2 = report_statistics(cfg, boot, tables)
    out.update(part)
    out.update(report_rules(cfg, tables))
    with (tables / "R2_gap.csv").open(encoding="utf-8", newline="") as fh:
        r2 = [
            {**r, "rho": float(r["rho"]), **{k: float(r[k]) for k in ("gap_instance_median", "ci95_low", "ci95_high")}}
            for r in csv.DictReader(fh)
        ]
    out["figures"] = figures(cfg, s2, r2, r8)
    return out
