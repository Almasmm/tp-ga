"""T6: random vs cost-aware start, aggregated to the instance level first (10 pairs per size).

For every instance the gap is reduced to one number per start: the median over all factorial cells and
seeds. The test then has one pair per instance, not one per (instance, cell) as in v0.3.0.
"""

from __future__ import annotations

import pandas as pd

from tpga.experiments.reporting import stats
from tpga.experiments.reporting.t4_factorial import cells


def table(runs: pd.DataFrame) -> pd.DataFrame:
    f = cells(runs)
    if not len(f):
        return pd.DataFrame()
    rows = []
    for size, g in f.groupby("size"):
        per = g.groupby(["instance", "initialization"])["gap"].median().unstack("initialization").dropna()
        if {"random", "cost-aware"} <= set(per.columns) and len(per) >= 2:
            res = stats.paired(per["cost-aware"].to_numpy(), per["random"].to_numpy())
            rows.append(
                {
                    "size": size,
                    "pairs": len(per),
                    "median_random": per["random"].median(),
                    "median_cost_aware": per["cost-aware"].median(),
                    **res,
                    "p_text": stats.format_p(res["p"]),
                }
            )
    return pd.DataFrame(rows)
