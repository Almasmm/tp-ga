"""T3: run time (phase ``timing``, performance cores) and power-law fits over two ranges.

Fits ``t = a (m n)^b`` on per-instance medians: once over the whole range and once over instances with
``m n >= 2500`` (50 x 50 and larger). Small instances are dominated by fixed costs (process-level set-up of
the solver call, the GA's per-generation overhead), which flattens the curve; the large-instance fit is the
better description of the asymptotic growth inside the tested range. No extrapolation.
"""

from __future__ import annotations

import pandas as pd

from tpga.experiments.reporting import stats
from tpga.experiments.reporting.common import sort_frame

PHASE = "timing"
LARGE = 2500


def _time(g: pd.DataFrame) -> pd.Series:
    """Solver time for LP rows (HiGHS run time or OR-Tools solve time), wall time per run otherwise."""
    return g["time_s"]


def table(runs: pd.DataFrame) -> pd.DataFrame:
    t = runs[runs["phase"] == PHASE]
    rows = []
    for (set_, size, method), g in t.groupby(["set", "size", "method"]):
        row = {
            "set": set_,
            "size": size,
            "arcs": int(g["arcs"].iloc[0]),
            "method": method,
            "runs": len(g),
            "time_median_s": _time(g).median(),
            "time_q1_s": _time(g).quantile(0.25),
            "time_q3_s": _time(g).quantile(0.75),
            "cpu_classes": ",".join(sorted({str(int(c)) for c in g["cpu_class"].dropna()})),
        }
        if "evals" in g and g["evals"].notna().any():
            row["us_per_eval_median"] = float((1e6 * g["time_s"] / g["evals"]).median())
        if "presolve_s" in g and g["presolve_s"].notna().any():
            row["presolve_median_s"] = g["presolve_s"].median()
            row["build_median_s"] = g["build_s"].median()
            row["wrapper_median_s"] = g["wrapper_s"].median()
        rows.append(row)
    return sort_frame(pd.DataFrame(rows), ["set", "size", "method"])


def fits(runs: pd.DataFrame) -> pd.DataFrame:
    t = runs[runs["phase"] == PHASE]
    rows = []
    for method, g in t.groupby("method"):
        per = g.groupby("instance").agg(arcs=("arcs", "first"), t=("time_s", "median"))
        for label, sub in (("all sizes", per), (f"m n >= {LARGE}", per[per["arcs"] >= LARGE])):
            if sub["arcs"].nunique() >= 2 and len(sub) >= 3:
                rows.append({"method": method, "range": label, **stats.loglog_fit(sub["arcs"], sub["t"])})
    return pd.DataFrame(rows)
