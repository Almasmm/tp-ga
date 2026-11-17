"""``tpga-exp report``: every table and figure of v0.4 from ``<output>/raw`` (nothing is computed elsewhere).

Each table is written as CSV and Markdown under ``<output>/tables``; figures go to ``<output>/figures/{en,ru}``.
A table whose phase has not been run yet is written with a note instead of rows, so a partial run still
produces a consistent report. ``report.json`` lists the files and the row counts.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

from tpga.experiments.reporting import (
    figures,
    t1_instances,
    t2_gap,
    t3_time,
    t4_factorial,
    t5_methods,
    t6_initialisation,
    t7_stopping,
    t8_lp_scaling,
    t9_representation,
)
from tpga.experiments.reporting.common import load_curves, load_runs, write_table
from tpga.experiments.v2.config import ConfigV2
from tpga.experiments.v2.storage import write_atomic

NOTE_T5 = (
    "Unit: per-instance median over seeds (10 instances per set and size). Wilcoxon signed-rank test "
    "(exact for n <= 50 without ties, normal approximation otherwise), Holm correction within each (set, size). "
    "hl_shift = Hodges-Lehmann estimate of method_a minus method_b in percentage points of gap, with a 95 % CI. "
    'p < 0.001 is printed as "< 0.001".'
)


def tables(output: Path, runs: pd.DataFrame) -> dict[str, pd.DataFrame]:
    empty = pd.DataFrame()
    have = len(runs) > 0
    return {
        "T1_instances": t1_instances.table(output, runs),
        "T2_gap": t2_gap.table(runs) if have else empty,
        "T3_time": t3_time.table(runs) if have else empty,
        "T3_fits": t3_time.fits(runs) if have else empty,
        "T4_factorial": t4_factorial.table(runs) if have else empty,
        "T4_tests": t4_factorial.tests(runs) if have else empty,
        "T5_methods_gap": t5_methods.table(runs, "gap") if have else empty,
        "T5_methods_gap_norm": t5_methods.table(runs, "gap_norm") if have else empty,
        "T6_initialisation": t6_initialisation.table(runs) if have else empty,
        "T7_stopping": t7_stopping.table(runs) if have else empty,
        "T8_lp_scaling": t8_lp_scaling.table(runs) if have else empty,
        "T8_lp_disagreement": t8_lp_scaling.agreement(runs) if have else empty,
        "A1_methods_pooled": t5_methods.appendix_pooled(runs, "gap") if have else empty,
    }


TITLES = {
    "T1_instances": ("Instance sets", "Median LP optimum and Z_rand (mean cost of 1000 decoded random permutations)."),
    "T2_gap": ("Gap by set, size and method", "Phases reference and main; budget-only stop."),
    "T3_time": ("Run time", "Phase timing on performance cores; LP time is solver run time (median of repeats)."),
    "T3_fits": ("Power-law fits t = a (m n)^b", "Per-instance medians; two ranges; no extrapolation."),
    "T4_factorial": ("Factorial plan (RQ4)", "Phase factorial only; budget-only stop."),
    "T4_tests": ("Factorial plan: Friedman tests, Kendall's W and post-hoc Wilcoxon-Holm", "Blocks are instances."),
    "T5_methods_gap": ("Paired method comparisons, gap", NOTE_T5),
    "T5_methods_gap_norm": ("Paired method comparisons, normalised gap", NOTE_T5),
    "T6_initialisation": ("Random vs cost-aware start", "One pair per instance (median over cells and seeds)."),
    "T7_stopping": ("Stopping rules", "Budget only vs stagnation (0.1 B calls) vs 200 generations (v0.3.0)."),
    "T8_lp_scaling": ("Exact solvers on large instances", "HiGHS (highspy) and OR-Tools min-cost flow."),
    "T8_lp_disagreement": ("Instances where the two exact solvers disagree", "Expected to be empty."),
    "A1_methods_pooled": ("Appendix: comparisons pooled over sizes", "Not used for conclusions; see T5."),
    "representation": (
        "Representation: decoder prefix, neutrality, locality, heritability (non-confirmatory)",
        "Medians over instances and seeds; source random = random permutations, otherwise the tuned GA "
        "population at the given fraction of the budget.",
    ),
}


def generate(cfg: ConfigV2) -> dict[str, Any]:
    output = cfg.output
    runs = load_runs(output)
    curves = load_curves(output)
    out_tables = output / "tables"
    result: dict[str, Any] = {"runs": int(len(runs)), "curve_rows": int(len(curves)), "tables": {}, "figures": []}
    built = tables(output, runs)
    rep = t9_representation.load(output)
    built["representation"] = t9_representation.table(rep)
    for name, df in built.items():
        title, note = TITLES[name]
        write_table(df, out_tables / name, title, note)
        result["tables"][name] = int(len(df))
    figures.setup_fonts()
    fig_dir = output / "figures"
    if len(runs):
        result["figures"] += figures.boxplot(runs, fig_dir, "gap")
        result["figures"] += figures.boxplot(runs, fig_dir, "gap_norm")
        result["figures"] += figures.convergence(curves, runs, fig_dir)
        result["figures"] += figures.time_scaling(runs, built["T3_fits"], fig_dir)
        result["figures"] += figures.factorial_heatmap(built["T4_factorial"], fig_dir)
        result["figures"] += figures.representation_neutrality(rep, fig_dir)
    if len(runs):
        result["phases"] = {str(k): int(v) for k, v in runs["phase"].value_counts().sort_index().items()}
    write_atomic(output / "report.json", result)
    return result


def summary_text(result: dict[str, Any]) -> str:
    return json.dumps(result, indent=1, ensure_ascii=False)
