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
                "gap_q1": g["gap"].quantile(0.25),
                "gap_q3": g["gap"].quantile(0.75),
                "gap_max": g["gap"].max(),
                "instance_median_median": g.groupby("instance")["gap"].median().median(),
                "gap_norm_median": g["gap_norm"].median(),
                "share_optimal": g["optimal"].mean(),
                "time_median_s": g["time_s"].median(),
            }
        )
    return sort_frame(pd.DataFrame(rows), ["set", "size", "method"])
