"""``PROGRESS.md``: which phases are finished and the main numbers of the finished ones.

Written by every ``tpga-exp report``. The numbers are copied from the tables built in the same call (the cells
named in ``MANUSCRIPT_MAP.md``); nothing is computed here except the counts of planned and recorded runs.
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any

import pandas as pd

from tpga.experiments.reporting.common import fmt, size_key
from tpga.experiments.v2.config import ConfigV2

PHASES = ("reference", "representation", "main", "applied", "factorial", "stagnation", "legacy", "timing")
SOURCES = {
    "reference": "T0_checks, T0_example1, T1_instances, T2_gap (LP, NWC, LCM, VAM)",
    "representation": "representation; figure representation_neutrality",
    "main": "T2_gap, T5_methods_gap, T5_methods_gap_norm, A1_methods_pooled; figures boxplot_gap, "
    "boxplot_gap_norm, convergence",
    "applied": "T10_applied_instances, T10_applied_summary",
    "factorial": "T4_factorial, T4_tests, T6_initialisation; figure factorial_heatmap",
    "stagnation": "T7_stopping (0.1 B calls without improvement)",
    "legacy": "T7_stopping (200 generations)",
    "timing": "T3_time, T3_fits, T8_lp_scaling, T8_lp_disagreement; figure time_scaling",
}
STOCHASTIC = ["RS", "GA-rand-base", "GA-cost-base", "GA-rand-tuned", "GA-cost-tuned", "SA-rand-tuned", "SA-cost-tuned"]


def planned(cfg: ConfigV2) -> dict[str, int | None]:
    """Runs of every phase in the task plan (None when the plan cannot be built, e.g. no tuned parameters)."""
    try:
        from tpga.experiments.v2.instances import build
        from tpga.experiments.v2.tasks import phase_tasks

        items = build(cfg)
        return {ph: len(phase_tasks(cfg, ph, items)) for ph in PHASES if ph in cfg.raw["phases"]}
    except Exception:  # noqa: BLE001 - the report must not fail because the plan is not available
        return dict.fromkeys(PHASES)


def status(done: int, plan: int | None) -> str:
    if plan is None:
        return f"{done:,} runs recorded (plan not available)" if done else "not started"
    if done >= plan > 0:
        return f"ready ({done:,} of {plan:,} runs)"
    return f"in progress ({done:,} of {plan:,} runs)" if done else f"not started (0 of {plan:,} runs)"


def md(df: pd.DataFrame, cols: list[str], limit: int = 40) -> list[str]:
    cols = [c for c in cols if c in df.columns]
    if not len(df) or not cols:
        return ["_No rows yet._"]
    lines = ["| " + " | ".join(cols) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    for _, r in df.head(limit).iterrows():
        lines.append("| " + " | ".join(fmt(r[c]) for c in cols) + " |")
    if len(df) > limit:
        lines.append(f"_{len(df) - limit} more rows in the table file._")
    return lines


def gap_by_size(t2: pd.DataFrame, methods: list[str], set_: str = "uniform") -> pd.DataFrame:
    """Median gap (%) of the methods on one set, one row per size."""
    if not len(t2):
        return t2
    sub = t2[(t2["set"] == set_) & t2["method"].isin(methods)]
    if not len(sub):
        return sub
    wide = sub.pivot_table(index="size", columns="method", values="gap_median")
    wide = wide[[m for m in methods if m in wide.columns]]
    return wide.loc[sorted(wide.index, key=size_key)].reset_index()


def wins(t5: pd.DataFrame) -> pd.DataFrame:
    """Wins / ties / losses of every pre-registered pair summed over the (set, size) families."""
    if not len(t5):
        return t5
    out = t5.groupby(["method_a", "method_b"], sort=False).agg(
        families=("n", "size"),
        instances=("n", "sum"),
        a_better=("wins_x", "sum"),
        ties=("ties", "sum"),
        b_better=("wins_y", "sum"),
        families_p_holm_below_0_05=("p_holm", lambda p: int((p < 0.05).sum())),
    )
    return out.reset_index()


def sections(built: dict[str, pd.DataFrame], ready: dict[str, bool]) -> list[str]:
    lines: list[str] = []

    def get(name: str) -> pd.DataFrame:
        return built.get(name, pd.DataFrame())

    def head(phase: str, title: str) -> bool:
        if not ready.get(phase):
            return False
        lines.extend(["", f"### {phase}: {title}", "", f"Tables: {SOURCES[phase]}.", ""])
        return True

    t2 = get("T2_gap")
    if head("reference", "optimum and classical rules"):
        cols = ["phase", "records", "failed_runs", "plans_checked", "plans_infeasible", "plans_feasible_share"]
        lines.extend(md(get("T0_checks"), [*cols, "max_residual"]))
        lines.extend(["", "Median gap, %, uniform set (`T2_gap.gap_median`):", ""])
        lines.extend(md(gap_by_size(t2, ["NWC", "LCM", "VAM"]), ["size", "NWC", "LCM", "VAM"]))
    if head("representation", "why the gap grows with the size (non-confirmatory)"):
        rep = get("representation")
        if len(rep):
            sub = rep[(rep["set"] == "uniform") & rep["metric"].isin(["prefix_share", "neutral_share"])]
            sub = sub[sub["source"] == "random"]
            lines.extend(md(sub, ["size", "measure", "operator", "k", "metric", "median", "q1", "q3"], 40))
    if head("main", "gap of the stochastic methods (RQ1, RQ2)"):
        for set_ in ("uniform", "structured", "skewed", "ties"):
            lines.extend(["", f"Median gap, %, {set_} set (`T2_gap.gap_median`):", ""])
            lines.extend(md(gap_by_size(t2, STOCHASTIC, set_), ["size", *STOCHASTIC]))
        note = "Paired comparisons summed over the (set, size) families (`T5_methods_gap`; the lower gap wins; "
        lines.extend(["", note + "unit: per-instance median over seeds):", ""])
        cols = ["method_a", "method_b", "families", "instances", "a_better", "ties", "b_better"]
        lines.extend(md(wins(get("T5_methods_gap")), [*cols, "families_p_holm_below_0_05"]))
    if head("applied", "illustrative cases"):
        cols = ["set", "size", "method", "instances", "gap_median", "gap_min", "gap_max", "better_than_vam"]
        lines.extend(md(get("T10_applied_summary"), [*cols, "time_median_s"]))
    if head("factorial", "population, mutation, start (RQ4)"):
        cols = ["size", "pairs", "median_random", "median_cost_aware", "ratio_median", "reduction_pp_median"]
        lines.extend(md(get("T6_initialisation"), [*cols, "wins_x", "wins_y", "p_text"]))
        t4 = get("T4_tests")
        if len(t4):
            cols = ["size", "initialization", "test", "blocks", "treatments", "chi2", "p_text", "kendall_w"]
            lines.append("")
            lines.extend(md(t4[t4["test"].str.startswith("Friedman")], cols))
    t7 = get("T7_stopping")
    for phase, label in (("stagnation", "0.1 B calls without improvement"), ("legacy", "200 generations")):
        if head(phase, f"stopping rule: {label}") and len(t7):
            sub = t7[t7["stop"].isin(["budget only", label])]
            cols = ["size", "method", "stop", "runs", "gap_mean", "gap_median", "stopped_early_share"]
            lines.extend(md(sub, [*cols, "budget_used_median", "best_found_median", "p_text"], 60))
    if head("timing", "run time (RQ3)"):
        t3 = get("T3_time")
        if len(t3):
            cols = ["size", "method", "runs", "time_median_s", "us_per_eval_median"]
            lines.extend(md(t3[t3["set"] == "uniform"], cols, 60))
        lines.append("")
        lines.extend(md(get("T3_fits"), ["method", "measure", "range", "b", "b_ci_low", "b_ci_high", "r2"]))
        lines.append("")
        lines.extend(md(get("T8_lp_scaling"), list(get("T8_lp_scaling").columns)[:8]))
    return lines


def write(cfg: ConfigV2, runs: pd.DataFrame, built: dict[str, pd.DataFrame], result: dict[str, Any]) -> Path:
    plan = planned(cfg)
    done = {str(k): int(v) for k, v in runs["phase"].value_counts().items()} if len(runs) else {}
    ready = {ph: plan.get(ph) is not None and done.get(ph, 0) >= (plan.get(ph) or 0) > 0 for ph in PHASES}
    out = cfg.output
    lines = [
        "# Progress of the v0.4 main run",
        "",
        f"Written by `tpga-exp report` on {time.strftime('%Y-%m-%d %H:%M')} from {result['runs']:,} run records. "
        "A phase is ready when every run of its task plan is recorded.",
        "",
        "| Phase | Status |",
        "|---|---|",
        *[f"| {ph} | {status(done.get(ph, 0), plan.get(ph))} |" for ph in PHASES],
        "",
        "## Where the results are",
        "",
        f"* Tables (CSV and Markdown): `{out.name}/tables/`",
        f"* Figures for the article (600 dpi JPG and PDF, serif font): `{out.name}/figures/final_en/`",
        f"* Figures with English and Russian labels (PNG, PDF): `{out.name}/figures/en/`, `{out.name}/figures/ru/`",
        f"* Raw records: `{out.name}/raw/`; run log and errors: `{out.name}/logs/`",
        f"* Source of every number of the article: `{out.name}/MANUSCRIPT_MAP.md`",
        "",
        "Numbers of a phase that is not ready are left out below; its tables exist but cover only the runs "
        "recorded so far.",
        "",
        "## Main numbers of the finished phases",
    ]
    body = sections(built, ready)
    lines += body if body else ["", "_No phase is finished yet._"]
    path = out / "PROGRESS.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path
