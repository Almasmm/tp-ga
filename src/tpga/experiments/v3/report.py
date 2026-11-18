"""Tables and figures of the additional experiment v3, rebuilt from the raw records (amendment 8.6)."""

from __future__ import annotations

import csv
import json
import statistics
from pathlib import Path
from typing import Any

import numpy as np

from tpga.experiments.reporting import stats
from tpga.experiments.v3.core import (
    STOCHASTIC,
    ConfigV3,
    build_benchmark,
    build_fctp,
    build_linear,
    key_of,
    linear_groups,
    plan_tasks,
    records,
    write_csv,
)

Row = dict[str, Any]


def _size_key(size: str) -> int:
    return int(size.split("x")[0])


def write_md(path: Path, title: str, note: str, rows: list[Row]) -> None:
    lines = [f"# {title}", "", note, ""]
    if rows:
        fields: list[str] = []
        for row in rows:
            fields += [k for k in row if k not in fields]
        lines += ["| " + " | ".join(fields) + " |", "|" + "---|" * len(fields)]
        for row in rows:
            lines.append("| " + " | ".join(_cell(row.get(f)) for f in fields) + " |")
    else:
        lines.append("_No rows._")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def _cell(value: Any) -> str:
    if value is None:
        return "–"
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, float):
        if value != value:
            return "–"
        return f"{value:.4g}"
    return str(value)


def _both(directory: Path, name: str, title: str, note: str, rows: list[Row]) -> None:
    write_csv(directory / f"{name}.csv", rows)
    write_md(directory / f"{name}.md", title, note, rows)


def instance_medians(rows: list[Row], field: str) -> dict[tuple[str, str], float]:
    """(method, instance) -> median of ``field`` over the seeds of the instance."""
    groups: dict[tuple[str, str], list[float]] = {}
    for r in rows:
        if r.get(field) is not None:
            groups.setdefault((r["method"], r["instance"]), []).append(float(r[field]))
    return {k: statistics.median(v) for k, v in groups.items()}


def paired_rows(
    medians: dict[tuple[str, str], float],
    instances: list[str],
    pairs: list[list[str]],
    scope: dict[str, Any],
    test: bool = True,
) -> list[Row]:
    """One row per pair: wins/ties/losses of the first method and, with ``test``, the Wilcoxon test with the
    Holm correction over the pairs of this scope."""
    out: list[Row] = []
    for a, b in pairs:
        ids = [i for i in instances if (a, i) in medians and (b, i) in medians]
        if not ids:
            continue
        x = np.array([medians[(a, i)] for i in ids])
        y = np.array([medians[(b, i)] for i in ids])
        res = stats.paired(x, y)
        row: Row = {
            **scope,
            "method_a": a,
            "method_b": b,
            "n": res["n"],
            "wins_a": res["wins_x"],
            "ties": res["ties"],
            "losses_a": res["wins_y"],
            "median_a": float(np.median(x)),
            "median_b": float(np.median(y)),
        }
        if test:
            row.update(
                W=res["W"],
                p=res["p"],
                rank_biserial_r=res["rank_biserial_r"],
                hl_shift=res["hl_shift"],
                smallest_possible_p=2.0 / 2 ** res["n"],
            )
        out.append(row)
    if test and out:
        for row, adj in zip(out, stats.holm([r["p"] for r in out]), strict=True):
            row["p_holm"] = adj
            row["p_holm_text"] = stats.format_p(adj)
    return out


# --- linear problem ------------------------------------------------------------------------


def linear_rows(cfg: ConfigV3) -> tuple[list[Row], list[Row]]:
    """Records of the plan in force (after the reduction rule) and the instances of that plan."""
    pilot = json.loads((cfg.area / "pilot.json").read_text(encoding="utf-8"))
    items = build_linear(cfg, linear_groups(cfg, bool(pilot["reduced"])), cfg.area / "instances")
    plan = {key_of(t) for t in plan_tasks(cfg, "main", items, list(cfg.raw["methods"]), cfg.seeds())}
    rows = [r for r in records(cfg.area / "raw" / "runs.jsonl", "main") if key_of(r) in plan]
    if len(rows) != len(plan):
        raise RuntimeError(f"the linear run is not complete: {len(rows)} of {len(plan)} records")
    return rows, items


def report_linear(cfg: ConfigV3) -> dict[str, Any]:
    rows, items = linear_rows(cfg)
    tables = cfg.area / "tables"
    methods = list(cfg.raw["methods"])
    cells = sorted({(r["set"], r["size"]) for r in rows}, key=lambda c: (c[0] != "uniform", _size_key(c[1])))
    gap_med = instance_medians(rows, "gap")
    norm_med = instance_medians(rows, "gap_norm")
    t1: list[Row] = []
    t4: list[Row] = []
    tests: list[Row] = []
    for set_name, size in cells:
        ids = [i["id"] for i in items if i["set"] == set_name and i["size"] == size]
        for method in methods:
            mine = [r for r in rows if r["set"] == set_name and r["size"] == size and r["method"] == method]
            gaps = [r["gap"] for r in mine]
            norms = [r["gap_norm"] for r in mine]
            t1.append(
                {
                    "set": set_name,
                    "size": size,
                    "method": method,
                    "instances": len(ids),
                    "runs": len(mine),
                    "gap_median": statistics.median(gaps),
                    "gap_instance_median": statistics.median(gap_med[(method, i)] for i in ids),
                    "gap_mean": statistics.fmean(gaps),
                    "gap_min": min(gaps),
                    "gap_max": max(gaps),
                    "gap_norm_median": statistics.median(norms),
                    "gap_norm_instance_median": statistics.median(norm_med[(method, i)] for i in ids),
                    "share_optimal": statistics.fmean(1.0 if r["optimal"] else 0.0 for r in mine),
                    "time_median_s": statistics.median(r["time_s"] for r in mine),
                }
            )
            if mine and mine[0].get("pivots"):
                offspring = sum(r["evals"] - int(r["config"].split("-")[0][1:]) for r in mine)
                t4.append(
                    {
                        "set": set_name,
                        "size": size,
                        "method": method,
                        "config": mine[0]["config"],
                        "runs": len(mine),
                        "offspring": offspring,
                        "pivots": sum(r["pivots"] for r in mine),
                        "pivots_theta_zero": sum(r["zero_pivots"] for r in mine),
                        "share_pivots_theta_zero": sum(r["zero_pivots"] for r in mine) / sum(r["pivots"] for r in mine),
                        "offspring_all_pivots_theta_zero": sum(r["unchanged_offspring"] for r in mine),
                        "share_offspring_all_pivots_theta_zero": sum(r["unchanged_offspring"] for r in mine)
                        / offspring,
                    }
                )
        tests += paired_rows(gap_med, ids, cfg.raw["pairs"], {"set": set_name, "size": size})
    _both(
        tables,
        "T1_gap",
        "Linear problem: gap, normalised gap and run time",
        "gap = 100 (Z - Z*) / Z*; gap_norm = (Z - Z*) / (Z_rand - Z*). `*_median` is over all runs, "
        "`*_instance_median` is the median over instances of the per-instance median over seeds. Run times were "
        "measured with many runs at once and are not a timing result.",
        t1,
    )
    _both(
        tables,
        "T2_tests",
        "Linear problem: paired comparisons on gap",
        "Unit: the instance (median over its seeds). Two-sided Wilcoxon signed-rank test, Holm correction over "
        "the five pairs of each (set, size), matched-pairs rank-biserial r (negative: method_a has the smaller "
        "gap), Hodges-Lehmann shift of gap(a) - gap(b) in percentage points. wins_a counts the instances where "
        "method_a has the smaller median gap. `smallest_possible_p` is 2 / 2^n.",
        tests,
    )
    wide: list[Row] = []
    for field, name in (("gap_median", "gap"), ("gap_norm_median", "gap_norm"), ("time_median_s", "time_s")):
        for method in methods:
            row: Row = {"value": name, "method": method}
            for set_name, size in cells:
                hit = [r for r in t1 if (r["set"], r["size"], r["method"]) == (set_name, size, method)]
                row[f"{set_name} {size}"] = hit[0][field]
            wide.append(row)
    _both(
        tables,
        "T3_by_size",
        "Linear problem: medians by method and size",
        "Median over all runs of the gap (%), the normalised gap and the run time (s).",
        wide,
    )
    _both(
        tables,
        "T4_cycle_counters",
        "Cycle mutation inside the GA runs",
        "Pivots made by the cycle mutation in the main runs, the pivots with theta = 0 and the offspring whose "
        "pivots all had theta = 0 (their plan is the plan decoded before the mutation).",
        t4,
    )
    figure_linear(cfg, t1, cells, methods)
    return {"records": len(rows), "cells": len(cells), "tests": len(tests)}


# --- fixed-charge problem ------------------------------------------------------------------


def fctp_rows(cfg: ConfigV3) -> tuple[list[Row], list[Row], list[Row]]:
    items = build_fctp(cfg)
    plan = {key_of(t) for t in plan_tasks(cfg, "main", items, list(cfg.raw["methods"]), cfg.seeds())}
    rows = [r for r in records(cfg.area / "raw" / "runs.jsonl", "main") if key_of(r) in plan]
    mip = records(cfg.area / "raw" / "mip.jsonl", "mip")
    if len(rows) != len(plan) or len(mip) != len(items):
        raise RuntimeError(f"the FCTP run is not complete: {len(rows)} of {len(plan)} records, {len(mip)} MIP")
    return rows, mip, items


def report_fctp(cfg: ConfigV3) -> dict[str, Any]:
    rows, mip, items = fctp_rows(cfg)
    tables = cfg.area / "tables"
    methods = list(cfg.raw["methods"])
    mip_by = {r["instance"]: r for r in mip}
    best: dict[str, float] = {}
    f1: list[Row] = []
    for inst in items:
        iid = inst["id"]
        m = mip_by[iid]
        mine = [r for r in rows if r["instance"] == iid]
        low = min(mine, key=lambda r: r["cost"])
        if m["proved"]:
            if low["cost"] < m["cost"] - 1e-6:
                raise RuntimeError(f"{low['method']} on {iid}: {low['cost']} is below the proved optimum {m['cost']}")
            z_best, source = float(m["cost"]), "MIP (proved optimum)"
        elif m["cost"] is not None and m["cost"] <= low["cost"]:
            z_best, source = float(m["cost"]), "MIP (best solution at the time limit)"
        else:
            z_best, source = float(low["cost"]), low["method"]
        best[iid] = z_best
        f1.append(
            {
                "instance": iid,
                "size": inst["size"],
                "rho": inst["rho"],
                "mip_status": m["status"],
                "proved": bool(m["proved"]),
                "mip_cost": m["cost"],
                "mip_bound": m["bound"],
                "mip_gap_percent": None if m["mip_gap"] is None else 100.0 * m["mip_gap"],
                "mip_time_s": m["time_s"],
                "mip_nodes": m["nodes"],
                "z_best": z_best,
                "z_best_source": source,
                "z_best_gap_to_bound_percent": 100.0 * max(0.0, z_best - m["bound"]) / z_best,
            }
        )
    for r in rows:
        r["gap"] = 100.0 * (r["cost"] - best[r["instance"]]) / best[r["instance"]]
    cells = sorted({(r["size"], r["rho"]) for r in rows}, key=lambda c: (_size_key(c[0]), c[1]))
    f1_summary: list[Row] = []
    for size, rho in cells:
        mine_i = [r for r in f1 if r["size"] == size and r["rho"] == rho]
        f1_summary.append(
            {
                "size": size,
                "rho": rho,
                "instances": len(mine_i),
                "proved_optimal": sum(r["proved"] for r in mine_i),
                "statuses": "; ".join(sorted({r["mip_status"] for r in mine_i})),
                "mip_time_median_s": statistics.median(r["mip_time_s"] for r in mine_i),
                "mip_time_max_s": max(r["mip_time_s"] for r in mine_i),
                "mip_gap_median_percent": statistics.median(r["mip_gap_percent"] or 0.0 for r in mine_i),
                "mip_gap_max_percent": max(r["mip_gap_percent"] or 0.0 for r in mine_i),
                "z_best_from_heuristic": sum(not r["z_best_source"].startswith("MIP") for r in mine_i),
                "z_best_gap_to_bound_median_percent": statistics.median(
                    r["z_best_gap_to_bound_percent"] for r in mine_i
                ),
            }
        )
    gap_med = instance_medians(rows, "gap")
    f2: list[Row] = []
    cell_wtl: list[Row] = []
    for size, rho in cells:
        ids = [i["id"] for i in items if i["size"] == size and i["rho"] == rho]
        for method in methods:
            mine = [r for r in rows if r["size"] == size and r["rho"] == rho and r["method"] == method]
            row: Row = {
                "size": size,
                "rho": rho,
                "method": method,
                "instances": len(ids),
                "runs": len(mine),
                "gap_median": statistics.median(r["gap"] for r in mine),
                "gap_instance_median": statistics.median(gap_med[(method, i)] for i in ids),
                "gap_mean": statistics.fmean(r["gap"] for r in mine),
                "gap_min": min(r["gap"] for r in mine),
                "gap_max": max(r["gap"] for r in mine),
                "share_at_z_best": statistics.fmean(1.0 if r["gap"] <= 1e-9 else 0.0 for r in mine),
                "time_median_s": statistics.median(r["time_s"] for r in mine),
            }
            if mine[0]["kind"] in STOCHASTIC and mine[0].get("local_search_calls") is not None:
                row["generations_median"] = statistics.median(r["generations"] for r in mine)
                row["local_search_calls_mean"] = statistics.fmean(r["local_search_calls"] for r in mine)
                row["local_search_evaluations_mean"] = statistics.fmean(r["local_search_evaluations"] for r in mine)
                row["local_search_improvements_mean"] = statistics.fmean(r["local_search_improvements"] for r in mine)
            f2.append(row)
        cell_wtl += paired_rows(gap_med, ids, cfg.raw["pairs"], {"size": size, "rho": rho}, test=False)
    f3: list[Row] = []
    all_ids = [i["id"] for i in items]
    f3 += paired_rows(gap_med, all_ids, cfg.raw["pairs"], {"scope": "all instances"})
    for rho in sorted({i["rho"] for i in items}):
        ids = [i["id"] for i in items if i["rho"] == rho]
        f3 += paired_rows(gap_med, ids, cfg.raw["pairs"], {"scope": f"rho = {rho:g}"})
    _both(
        tables,
        "F1_mip_instances",
        "FCTP: reference by instance",
        "MIP in HiGHS, one thread, time limit as configured. z_best is the proved optimum, otherwise the best "
        "known value (minimum of the MIP solution and of every run of every method). "
        "`z_best_gap_to_bound_percent` = 100 (z_best - bound) / z_best.",
        f1,
    )
    _both(
        tables,
        "F1_mip_summary",
        "FCTP: MIP status and time by size and rho",
        "`proved_optimal` counts the instances where HiGHS proved the optimum within the limit.",
        f1_summary,
    )
    _both(
        tables,
        "F2_gap",
        "FCTP: gap of every method by size and rho",
        "gap = 100 (Z - z_best) / z_best. `gap_median` over all runs; `gap_instance_median` is the median over "
        "instances of the per-instance median. Parameters come from the linear tuning without tuning on FCTP.",
        f2,
    )
    _both(
        tables,
        "F3_tests",
        "FCTP: paired comparisons on gap",
        "Unit: the instance (median over its seeds). Two-sided Wilcoxon signed-rank test, Holm correction over "
        "the four pairs of each scope, rank-biserial r (negative: method_a has the smaller gap). The tests are "
        "made on all 40 instances and for each rho (20 instances), as fixed in amendment 8.6.",
        f3,
    )
    _both(
        tables,
        "F3_cells",
        "FCTP: wins, ties and losses by size and rho",
        "Five instances per cell: only the counts and the medians of the per-instance median gap are given.",
        cell_wtl,
    )
    figure_fctp(cfg, f2, cells, methods)
    return {"records": len(rows), "mip": len(mip), "proved": sum(r["proved"] for r in f1), "tests": len(f3)}


def report_benchmark(cfg: ConfigV3) -> dict[str, Any]:
    """Table of the external benchmark: gap of every method to the objective value listed by the source."""
    items = build_benchmark(cfg)
    methods = list(cfg.raw["methods"])
    plan = {key_of(t) for t in plan_tasks(cfg, "benchmark", items, methods, cfg.seeds())}
    rows = [r for r in records(cfg.area / "raw" / "benchmark.jsonl", "benchmark") if key_of(r) in plan]
    mip = {r["instance"]: r for r in records(cfg.area / "raw" / "benchmark_mip.jsonl", "benchmark-mip")}
    if len(rows) != len(plan) or len(mip) != len(items):
        raise RuntimeError(f"the benchmark run is not complete: {len(rows)} of {len(plan)} records")
    table: list[Row] = []
    reference: list[Row] = []
    for inst in items:
        listed = float(inst["listed_objective"])
        m = mip[inst["id"]]
        reference.append(
            {
                "instance": inst["id"],
                "size": inst["size"],
                "listed_objective": listed,
                "url": inst["url"],
                "highs_status": m["status"],
                "highs_proved": bool(m["proved"]),
                "highs_cost": m["cost"],
                "highs_bound": m["bound"],
                "highs_time_s": m["time_s"],
                "highs_minus_listed": None if m["cost"] is None else m["cost"] - listed,
            }
        )
        for method in methods:
            mine = [r for r in rows if r["instance"] == inst["id"] and r["method"] == method]
            gaps = [100.0 * (r["cost"] - listed) / listed for r in mine]
            table.append(
                {
                    "instance": inst["id"],
                    "size": inst["size"],
                    "method": method,
                    "runs": len(mine),
                    "listed_objective": listed,
                    "cost_median": statistics.median(r["cost"] for r in mine),
                    "cost_min": min(r["cost"] for r in mine),
                    "gap_median": statistics.median(gaps),
                    "gap_min": min(gaps),
                    "gap_max": max(gaps),
                    "runs_at_listed_objective": sum(abs(r["cost"] - listed) <= 1e-6 * listed for r in mine),
                    "time_median_s": statistics.median(r["time_s"] for r in mine),
                }
            )
    source = str(cfg.raw["benchmark"].get("source", ""))
    _both(
        cfg.area / "tables",
        "B1_benchmark_reference",
        "External FCTP benchmark: reference values",
        f"Source: {source} `listed_objective` is the value given by the source; the HiGHS columns are our MIP run.",
        reference,
    )
    _both(
        cfg.area / "tables",
        "B2_benchmark_gap",
        "External FCTP benchmark: gap of every method",
        f"Source: {source} gap = 100 (Z - listed objective) / listed objective. Same methods, parameters, "
        "budget (200 m n) and seeds as in the generated FCTP set; three instances, so no test is made.",
        table,
    )
    return {"benchmark_records": len(rows), "benchmark_instances": len(items)}


# --- figures -------------------------------------------------------------------------------


def _save(fig: Any, directory: Path, name: str) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    fig.savefig(directory / f"{name}.pdf", metadata={"CreationDate": None})
    fig.savefig(directory / f"{name}.jpg", dpi=300, pil_kwargs={"quality": 92})


def _pyplot() -> Any:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    return plt


def figure_linear(cfg: ConfigV3, t1: list[Row], cells: list[tuple[str, str]], methods: list[str]) -> None:
    plt = _pyplot()
    sizes = [c for c in cells if c[0] == "uniform"]
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    for method in methods:
        y = [
            r["gap_norm_instance_median"]
            for c in sizes
            for r in t1
            if (r["set"], r["size"], r["method"]) == (*c, method)
        ]
        ax.plot(range(len(sizes)), y, marker="o", linewidth=1.4, markersize=4, label=method)
    ax.set_xticks(range(len(sizes)))
    ax.set_xticklabels([c[1] for c in sizes])
    ax.set_yscale("symlog", linthresh=1e-3)
    ax.set_ylim(bottom=0)
    ax.set_xlabel("size (uniform instances)")
    ax.set_ylabel("normalised gap (median of instance medians)")
    ax.grid(True, which="both", linewidth=0.3, alpha=0.6)
    ax.legend(fontsize=7, ncol=2)
    fig.tight_layout()
    _save(fig, cfg.area / "figures", "linear_gap_norm")
    plt.close(fig)


def figure_fctp(cfg: ConfigV3, f2: list[Row], cells: list[tuple[str, float]], methods: list[str]) -> None:
    plt = _pyplot()
    rhos = sorted({c[1] for c in cells})
    fig, axes = plt.subplots(1, len(rhos), figsize=(4.2 * len(rhos), 4.2), sharey=True, squeeze=False)
    for ax, rho in zip(axes[0], rhos, strict=True):
        sizes = [c[0] for c in cells if c[1] == rho]
        for method in methods:
            y = [
                r["gap_instance_median"]
                for s in sizes
                for r in f2
                if (r["size"], r["rho"], r["method"]) == (s, rho, method)
            ]
            ax.plot(range(len(sizes)), y, marker="o", linewidth=1.4, markersize=4, label=method)
        ax.set_xticks(range(len(sizes)))
        ax.set_xticklabels(sizes)
        ax.set_yscale("symlog", linthresh=0.1)
        ax.set_ylim(bottom=0)
        ax.set_title(f"rho = {rho:g}", fontsize=9)
        ax.set_xlabel("size")
        ax.grid(True, which="both", linewidth=0.3, alpha=0.6)
    axes[0][0].set_ylabel("gap to the best known value, %")
    axes[0][-1].legend(fontsize=7)
    fig.tight_layout()
    _save(fig, cfg.area / "figures", "fctp_gap")
    plt.close(fig)


def figure_neutrality(summary_csv: Path, directory: Path) -> bool:
    """Share of offspring with an unchanged plan by size, from the summary of ``scripts/neutrality_check.py``."""
    if not summary_csv.exists():
        return False
    with summary_csv.open(encoding="utf-8", newline="") as fh:
        rows = [r for r in csv.DictReader(fh) if r["set"] == "uniform"]
    if not rows:
        return False
    plt = _pyplot()
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    for operator in sorted({r["operator"] for r in rows}):
        mine = sorted((r for r in rows if r["operator"] == operator), key=lambda r: _size_key(r["size"]))
        ax.plot(
            [r["size"] for r in mine],
            [float(r["unchanged_share_median"]) for r in mine],
            marker="o",
            linewidth=1.4,
            markersize=4,
            label=operator,
        )
    ax.set_ylim(-0.02, 1.02)
    ax.set_xlabel("size (uniform instances)")
    ax.set_ylabel("share of offspring with the plan of the parent")
    ax.grid(True, linewidth=0.3, alpha=0.6)
    ax.legend(fontsize=7)
    fig.tight_layout()
    _save(fig, directory, "neutrality_operators")
    plt.close(fig)
    return True


def report(cfg: ConfigV3) -> dict[str, Any]:
    if cfg.raw["problem"] == "linear":
        out = report_linear(cfg)
        out["neutrality_figure"] = figure_neutrality(
            cfg.output / "neutrality" / "operators_summary.csv", cfg.output / "neutrality"
        )
        return out
    out = report_fctp(cfg)
    if "benchmark" in cfg.raw and (cfg.area / "raw" / "benchmark.jsonl").exists():
        out.update(report_benchmark(cfg))
    return out
