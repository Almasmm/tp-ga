"""T10: illustrative cases (phase ``applied`` and the reference rows of the sets ``wheat`` and ``astana``).

No test: the cases illustrate the data pipeline. Per instance the stochastic methods are averaged over their
runs; the summary gives the median and range over the instances of a set and how many instances a method
solved better than VAM.
"""

from __future__ import annotations

import pandas as pd

from tpga.experiments.reporting.common import sort_frame

SETS = ("wheat", "astana")


def per_instance(runs: pd.DataFrame) -> pd.DataFrame:
    df = runs[runs["set"].isin(SETS) & runs["phase"].isin(["reference", "applied"]) & (runs["method"] != "LP-ortools")]
    if not len(df):
        return pd.DataFrame()
    out = (
        df.groupby(["set", "size", "instance", "method"])
        .agg(
            runs=("gap", "size"),
            gap_mean=("gap", "mean"),
            gap_min=("gap", "min"),
            gap_max=("gap", "max"),
            time_median_s=("time_s", "median"),
        )
        .reset_index()
    )
    return sort_frame(out, ["set", "instance", "method"])


def summary(runs: pd.DataFrame) -> pd.DataFrame:
    inst = per_instance(runs)
    if not len(inst):
        return pd.DataFrame()
    vam = inst[inst["method"] == "VAM"].set_index("instance")["gap_mean"]
    rows = []
    for (set_, size, method), g in inst.groupby(["set", "size", "method"]):
        better = (g.set_index("instance")["gap_mean"] < vam.reindex(g["instance"]).to_numpy()).sum()
        rows.append(
            {
                "set": set_,
                "size": size,
                "method": method,
                "instances": len(g),
                "gap_median": g["gap_mean"].median(),
                "gap_min": g["gap_mean"].min(),
                "gap_max": g["gap_mean"].max(),
                "better_than_vam": int(better),
                "time_median_s": g["time_median_s"].median(),
            }
        )
    return sort_frame(pd.DataFrame(rows), ["set", "method"])
