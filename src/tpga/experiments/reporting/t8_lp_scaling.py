"""T8: exact solvers on the ``lp_scaling`` set (100 x 100 to 1000 x 1000), phase ``timing``.

HiGHS (highspy) reports solver run time, presolve, model build and wrapper time separately; OR-Tools
reports the min-cost-flow solve time and the graph build time. Both optima must agree on every instance.
"""

from __future__ import annotations

import pandas as pd

from tpga.experiments.reporting.common import sort_frame

PHASE = "timing"
SET = "lp_scaling"


def table(runs: pd.DataFrame) -> pd.DataFrame:
    t = runs[(runs["phase"] == PHASE) & (runs["set"] == SET) & runs["method"].isin(["LP", "LP-ortools"])]
    rows = []
    for (size, method), g in t.groupby(["size", "method"]):
        row = {
            "size": size,
            "arcs": int(g["arcs"].iloc[0]),
            "method": method,
            "instances": g["instance"].nunique(),
            "solver_median_s": g["time_s"].median(),
            "solver_max_s": g["time_s"].max(),
            "build_median_s": g["build_s"].median() if "build_s" in g else float("nan"),
        }
        if "presolve_s" in g and g["presolve_s"].notna().any():
            row["presolve_median_s"] = g["presolve_s"].median()
            row["wrapper_median_s"] = g["wrapper_s"].median()
        rows.append(row)
    return sort_frame(pd.DataFrame(rows), ["size", "method"])


def agreement(runs: pd.DataFrame) -> pd.DataFrame:
    """Instances where HiGHS and OR-Tools optima differ by more than the tolerance (should be empty)."""
    t = runs[(runs["phase"] == PHASE) & runs["method"].isin(["LP", "LP-ortools"])]
    wide = t.groupby(["instance", "method"])["cost"].first().unstack("method")
    if not {"LP", "LP-ortools"} <= set(wide.columns):
        return pd.DataFrame(columns=["instance", "LP", "LP-ortools", "difference"])
    wide = wide.dropna()
    wide["difference"] = wide["LP"] - wide["LP-ortools"]
    bad = wide[wide["difference"].abs() > 1e-6 * wide["LP"].abs().clip(lower=1.0)]
    return bad.reset_index()
