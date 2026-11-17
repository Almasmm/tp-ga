"""Representation phase (non-confirmatory): medians over instances and seeds of every measure.

Rows come from ``raw/representation`` (long format: one value per instance, seed, source, snapshot,
measure, operator, k and metric). ``source`` is ``random`` (random permutations) or the tuned GA whose
population was sampled; ``snapshot`` is the fraction of the budget at which it was sampled.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from tpga.experiments.reporting.common import sort_frame
from tpga.experiments.v2.storage import read_parts

KEYS = ["set", "size", "mn", "source", "snapshot", "measure", "operator", "k", "metric"]


def load(output: Path) -> pd.DataFrame:
    return pd.DataFrame(list(read_parts(output / "raw" / "representation", "representation")))


def table(rows: pd.DataFrame) -> pd.DataFrame:
    if not len(rows):
        return pd.DataFrame()
    df = rows.copy()
    for col in ("snapshot", "operator", "k"):
        df[col] = df[col].astype(object).where(df[col].notna(), "-")
    g = df.groupby(KEYS, dropna=False)["value"]
    out = g.agg(
        median="median",
        q1=lambda v: float(np.nanquantile(v, 0.25)) if v.notna().any() else np.nan,
        q3=lambda v: float(np.nanquantile(v, 0.75)) if v.notna().any() else np.nan,
        values="count",
    ).reset_index()
    out["instances"] = df.groupby(KEYS, dropna=False)["instance"].nunique().to_numpy()
    return sort_frame(out, ["set", "size", "source", "measure", "operator", "k", "metric"])
