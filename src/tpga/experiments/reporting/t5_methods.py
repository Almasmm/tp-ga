"""T5: paired method comparisons per (set, size); appendix A1: the same comparisons pooled over instances.

Unit: per-instance median gap over the seeds (10 pairs per set and size). Family for the Holm correction:
the comparisons of one (set, size). Every row gives the Wilcoxon p-value, rank-biserial r, wins/losses/ties
and the Hodges-Lehmann shift (method_a minus method_b, percentage points) with its 95 % CI.
"""

from __future__ import annotations

import pandas as pd

from tpga.experiments.reporting import stats
from tpga.experiments.reporting.common import per_instance, sort_frame

#: pre-registered comparisons (PREREGISTRATION.md, section 5)
PAIRS = [
    ("GA-rand-base", "NWC"),
    ("GA-rand-base", "LCM"),
    ("GA-rand-base", "VAM"),
    ("GA-rand-base", "RS"),
    ("GA-rand-tuned", "VAM"),
    ("GA-rand-tuned", "GA-rand-base"),
    ("GA-cost-tuned", "VAM"),
    ("SA-rand-tuned", "VAM"),
    ("SA-rand-tuned", "GA-rand-tuned"),
    ("SA-cost-tuned", "GA-cost-tuned"),
]
PHASES = ("reference", "main")


def _rows(med: pd.DataFrame, groups: list[tuple[str, str, pd.DataFrame]], value: str) -> list[dict]:
    rows = []
    for set_, size, g in groups:
        wide = g.pivot_table(index="instance", columns="method", values=value)
        family = []
        for a, b in PAIRS:
            if a in wide and b in wide:
                sub = wide[[a, b]].dropna()
                if len(sub) >= 2:
                    res = stats.paired(sub[a].to_numpy(), sub[b].to_numpy())
                    family.append({"set": set_, "size": size, "method_a": a, "method_b": b, "value": value, **res})
        if family:
            adj = stats.holm([r["p"] for r in family])
            for r, p in zip(family, adj, strict=True):
                r["p_holm"] = p
                r["p_holm_text"] = stats.format_p(p)
            rows += family
    return rows


def table(runs: pd.DataFrame, value: str = "gap") -> pd.DataFrame:
    df = runs[runs["phase"].isin(PHASES) & ~runs["set"].isin(["lp_scaling", "wheat", "astana"])]
    med = per_instance(df, value)
    groups = [(s, z, g) for (s, z), g in med.groupby(["set", "size"])]
    return sort_frame(pd.DataFrame(_rows(med, groups, value)), ["set", "size"])


def appendix_pooled(runs: pd.DataFrame, value: str = "gap") -> pd.DataFrame:
    """Appendix A1: pooled over all instances of a set (not used in the main tables)."""
    df = runs[runs["phase"].isin(PHASES) & ~runs["set"].isin(["lp_scaling", "wheat", "astana"])]
    med = per_instance(df, value)
    groups = [(s, "all sizes", g) for s, g in med.groupby("set")]
    return pd.DataFrame(_rows(med, groups, value))
