"""Statistics of the v0.4 report (all functions are pure and tested on inputs with known answers).

* Paired comparison: exact two-sided Wilcoxon signed-rank test (normal approximation above 50 non-zero
  pairs or with ties), Holm correction within a stated family, matched-pairs rank-biserial r, and the
  Hodges-Lehmann estimate of the location shift with its confidence interval from Walsh averages
  (Hollander, Wolfe & Chicken, *Nonparametric Statistical Methods*, 3rd ed., section 3.2): exact critical
  value of the signed-rank statistic up to 50 pairs, normal approximation above.
* Friedman test with Kendall's W = chi2 / (n (k - 1)).
* p-values below 0.001 are printed as "< 0.001".
"""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Any

import numpy as np
from scipy import stats

EXACT_LIMIT = 50


def format_p(p: float | None) -> str:
    if p is None or (isinstance(p, float) and math.isnan(p)):
        return "–"
    return "< 0.001" if p < 0.001 else f"{p:.3f}"


def holm(p: list[float]) -> list[float]:
    order = np.argsort(p)
    adj = np.empty(len(p))
    running = 0.0
    for rank, idx in enumerate(order):
        running = max(running, (len(p) - rank) * p[idx])
        adj[idx] = min(1.0, running)
    return adj.tolist()


@lru_cache(maxsize=128)
def _signed_rank_counts(n: int) -> np.ndarray:
    """Number of subsets of {1..n} with each sum: the exact null distribution of W+ (times 2**n)."""
    counts = np.zeros(n * (n + 1) // 2 + 1, dtype=object)
    counts[0] = 1
    for k in range(1, n + 1):
        counts[k:] = counts[k:] + counts[:-k].copy()
    return counts


def _critical_index(n: int, alpha: float) -> int:
    """Largest c with P(W+ <= c - 1) <= alpha / 2 (exact up to EXACT_LIMIT, normal approximation above)."""
    if n <= EXACT_LIMIT:
        counts = _signed_rank_counts(n)
        cdf = np.cumsum(counts.astype(float)) / 2.0**n
        c = int(np.searchsorted(cdf, alpha / 2, side="right"))  # number of sums with cdf <= alpha/2
        return max(c, 0)
    mean = n * (n + 1) / 4
    sd = math.sqrt(n * (n + 1) * (2 * n + 1) / 24)
    return max(0, int(math.floor(mean - stats.norm.ppf(1 - alpha / 2) * sd)))


def hodges_lehmann(d: np.ndarray, alpha: float = 0.05) -> tuple[float, float, float, str]:
    """Estimate and CI of the median of paired differences ``d`` from the Walsh averages."""
    d = np.asarray(d, dtype=float)
    n = len(d)
    if n == 0:
        return math.nan, math.nan, math.nan, "none"
    i, j = np.triu_indices(n)
    walsh = np.sort((d[i] + d[j]) / 2.0)
    est = float(np.median(walsh))
    c = _critical_index(n, alpha)
    method = "exact Walsh-average CI" if n <= EXACT_LIMIT else "normal-approximation Walsh-average CI"
    if c < 1 or c > len(walsh):
        return est, math.nan, math.nan, method + " (too few pairs for this level)"
    return est, float(walsh[c - 1]), float(walsh[len(walsh) - c]), method


def paired(x: np.ndarray, y: np.ndarray, alpha: float = 0.05) -> dict[str, Any]:
    """Wilcoxon signed-rank test of x - y with effect sizes and the Hodges-Lehmann shift."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    d = x - y
    nz = d[d != 0]
    if len(nz) == 0:
        p, w, r = 1.0, 0.0, 0.0
    else:
        method = "exact" if len(nz) <= EXACT_LIMIT and len(np.unique(np.abs(nz))) == len(nz) else "approx"
        res = stats.wilcoxon(x, y, zero_method="wilcox", method=method)
        p, w = float(res.pvalue), float(res.statistic)
        ranks = stats.rankdata(np.abs(nz))
        r = float((ranks[nz > 0].sum() - ranks[nz < 0].sum()) / ranks.sum())
    est, lo, hi, ci_method = hodges_lehmann(d, alpha)
    return {
        "n": len(d),
        "nonzero": len(nz),
        "W": w,
        "p": p,
        "rank_biserial_r": r,
        "hl_shift": est,
        "hl_ci_low": lo,
        "hl_ci_high": hi,
        "hl_method": ci_method,
        "wins_x": int((d < 0).sum()),
        "wins_y": int((d > 0).sum()),
        "ties": int((d == 0).sum()),
    }


def friedman(matrix: np.ndarray) -> dict[str, float]:
    """Friedman test on blocks x treatments with Kendall's W."""
    m = np.asarray(matrix, dtype=float)
    n, k = m.shape
    if n and np.all(m == m[:, :1]):
        return {"blocks": n, "treatments": k, "chi2": 0.0, "p": 1.0, "kendall_w": 0.0}  # all blocks tied
    stat, p = stats.friedmanchisquare(*[m[:, c] for c in range(k)])
    w = float(stat) / (n * (k - 1)) if n and k > 1 else math.nan
    return {"blocks": n, "treatments": k, "chi2": float(stat), "p": float(p), "kendall_w": w}


def loglog_fit(x: np.ndarray, y: np.ndarray) -> dict[str, float]:
    """Least squares on log10 t = log10 a + b log10 x; 95 % CI of b from the t distribution."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    keep = (x > 0) & (y > 0)
    x, y = x[keep], y[keep]
    if len(x) < 3 or len(np.unique(x)) < 2:
        return {
            "a": math.nan,
            "b": math.nan,
            "b_ci_low": math.nan,
            "b_ci_high": math.nan,
            "r2": math.nan,
            "points": float(len(x)),
        }
    fit = stats.linregress(np.log10(x), np.log10(y))
    tcrit = stats.t.ppf(0.975, len(x) - 2)
    return {
        "a": 10**fit.intercept,
        "b": fit.slope,
        "b_ci_low": fit.slope - tcrit * fit.stderr,
        "b_ci_high": fit.slope + tcrit * fit.stderr,
        "r2": fit.rvalue**2,
        "points": float(len(x)),
        "x_min": float(x.min()),
        "x_max": float(x.max()),
    }
