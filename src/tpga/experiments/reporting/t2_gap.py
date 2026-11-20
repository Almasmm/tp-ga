"""T2: gap and normalised gap by set, size and method (phases ``reference`` and ``main``, budget-only stop)."""

from __future__ import annotations

import pandas as pd

from tpga.experiments.reporting.common import sort_frame

PHASES = ("reference", "main")


def table(runs: pd.DataFrame) -> pd.DataFrame:
    synthetic = ~runs["set"].isin(["lp_scaling", "wheat", "astana"])
    df = runs[runs["phase"].isin(PHASES) & synthetic & (runs["method"] != "LP-ortools")]
    rows = []
    for (set_, size, method), g in df.groupby(["set", "size", "method"]):
        rows.append(
            {
                "set": set_,
                "size": size,
                "method": method,
                "instances": g["instance"].nunique(),
                "runs": len(g),
                "gap_mean": g["gap"].mean(),
                "gap_median": g["gap"].median(),
                "gap_std": g["gap"].std(ddof=1) if len(g) > 1 else float("nan"),
                "gap_min": g["gap"].min(),
                "gap_q1": g["gap"].quantile(0.25),
                "gap_q3": g["gap"].quantile(0.75),
                "gap_max": g["gap"].max(),
                "instance_median_median": g.groupby("instance")["gap"].median().median(),
                "gap_norm_median": g["gap_norm"].median(),
                "share_optimal": g["optimal"].mean(),
                "time_median_s": g["time_s"].median(),
                # convergence: the decoder call at which the best plan of a run was found (stochastic methods)
                "best_eval_median": _median(g, "best_eval"),
                "best_eval_share_median": _median(g.assign(_s=_share(g)), "_s"),
            }
        )
    return sort_frame(pd.DataFrame(rows), ["set", "size", "method"])


def _median(g: pd.DataFrame, col: str) -> float:
    return float(g[col].median()) if col in g and g[col].notna().any() else float("nan")


def _share(g: pd.DataFrame) -> pd.Series:
    """best_eval / budget of every run (NaN for the deterministic methods)."""
    if "best_eval" not in g or "budget" not in g:
        return pd.Series(float("nan"), index=g.index)
    return pd.to_numeric(g["best_eval"], errors="coerce") / pd.to_numeric(g["budget"], errors="coerce")
