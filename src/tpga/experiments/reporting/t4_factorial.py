"""T4: factorial plan of RQ4 (phase ``factorial`` only), Friedman tests with Kendall's W and post-hoc tests.

Only rows of the ``factorial`` phase enter (the phase filter is what was missing in the v0.3.0 T4).
Blocks of the Friedman tests are instances (per-instance median over seeds); post-hoc tests compare the
levels of one factor after taking the median over the other factor's levels per instance.
"""

from __future__ import annotations

import re
from itertools import combinations

import pandas as pd

from tpga.experiments.reporting import stats
from tpga.experiments.reporting.common import sort_frame

PHASE = "factorial"
_CONFIG = re.compile(
    r"^P(?P<pop>\d+)-pc[^-]+-t\d+-e\d+-(?P<mode>[a-z_]+):(?P<level>[0-9.eE+-]+?)-(?P<init>random|cost-aware)-"
)


def parse_config(config: str) -> dict[str, object]:
    """``P20-pc0.9-t3-e2-swap_count:3-random-budget`` -> population, mutation mode and level, start."""
    m = _CONFIG.match(config)
    if m is None:
        raise ValueError(f"not a GA configuration id: {config!r}")
    return {
        "population": int(m["pop"]),
        "mutation_mode": m["mode"],
        "mutation_level": float(m["level"]),
        "initialization": m["init"],
    }


def cells(runs: pd.DataFrame) -> pd.DataFrame:
    f = runs[runs["phase"] == PHASE].copy()
    if not len(f):
        return f
    parsed = f["config"].map(parse_config).apply(pd.Series)
    f = pd.concat([f, parsed], axis=1)
    f["mutation"] = f["mutation_mode"] + ":" + f["mutation_level"].map(lambda v: f"{v:g}")
    return f


def table(runs: pd.DataFrame) -> pd.DataFrame:
    f = cells(runs)
    if not len(f):
        return pd.DataFrame()
    rows = []
    for (size, init, pop, mut), g in f.groupby(["size", "initialization", "population", "mutation"]):
        rows.append(
            {
                "size": size,
                "initialization": init,
                "population": int(pop),
                "mutation": mut,
                "runs": len(g),
                "instances": g["instance"].nunique(),
                "gap_mean": g["gap"].mean(),
                "gap_median": g["gap"].median(),
                "gap_norm_median": g["gap_norm"].median(),
                "time_median_s": g["time_s"].median(),
            }
        )
    return sort_frame(pd.DataFrame(rows), ["size", "initialization", "population", "mutation"])


def tests(runs: pd.DataFrame) -> pd.DataFrame:
    f = cells(runs)
    if not len(f):
        return pd.DataFrame()
    rows = []
    for (size, init), g in f.groupby(["size", "initialization"]):
        med = g.groupby(["instance", "population", "mutation"])["gap"].median()
        wide = med.unstack(["population", "mutation"]).dropna(axis=1)
        if wide.shape[0] >= 2 and wide.shape[1] >= 3:
            fr = stats.friedman(wide.to_numpy())
            rows.append(
                {
                    "size": size,
                    "initialization": init,
                    "test": "Friedman, all cells",
                    **fr,
                    "p_text": stats.format_p(fr["p"]),
                }
            )
        for factor in ("population", "mutation"):
            agg = g.groupby(["instance", factor])["gap"].median().unstack(factor).dropna(axis=1)
            if agg.shape[1] < 2 or agg.shape[0] < 2:
                continue
            if agg.shape[1] >= 3:
                fr = stats.friedman(agg.to_numpy())
                rows.append(
                    {
                        "size": size,
                        "initialization": init,
                        "test": f"Friedman, {factor}",
                        **fr,
                        "p_text": stats.format_p(fr["p"]),
                    }
                )
            post = []
            for x, y in combinations(agg.columns, 2):
                res = stats.paired(agg[x].to_numpy(), agg[y].to_numpy())
                post.append({"size": size, "initialization": init, "test": f"Wilcoxon {factor}: {x} vs {y}", **res})
            for r, p in zip(post, stats.holm([r["p"] for r in post]), strict=True):
                r["p_holm"] = p
                r["p_text"] = stats.format_p(p)
            rows += post
    return pd.DataFrame(rows)
