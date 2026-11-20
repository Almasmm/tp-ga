"""Properties of the permutation representation under the greedy decoder (non-confirmatory, v0.4).

Why does the gap grow with the size of the instance? A plan of an m x n instance has at most m + n - 1
positive cells, and the decoder stops as soon as all supply is used, so most of the m n positions of a
permutation never influence the plan. This module measures, with the project's decoder and operators:

* the decoder prefix: positive cells of the plan and the number of positions read before the decoder stops;
* neutrality: the share of mutation offspring whose decoded cost equals the parent's;
* locality: |dZ| / Z* after k random swaps, and the Spearman correlation between k and |dZ|;
* heritability of the order crossover: the share of the child's positive cells that are positive in a parent.

Mutation offspring follow the rules of :func:`tpga.ga.run_ga`: ``swap_fixed`` swaps two positions with
probability ``rate``; ``swap_count`` makes ``round(s)`` swaps, ``swap_scaled`` ``max(1, round(s (m + n)))``,
``swap_per_position`` ``Binomial(m n, q) // 2``. A swap exchanges two distinct positions chosen uniformly.
"""

from __future__ import annotations

import numpy as np
from numba import njit
from scipy import stats

from tpga._kernels import Kernels, _decode_cost
from tpga.decoder import DECODER_TOL, decoder_eps
from tpga.ga import _arrays
from tpga.model import TransportProblem

LOCALITY_K = (1, 2, 5, 10, 20)


@njit(cache=True)
def _prefix(perm, supply, demand, n, eps):  # pragma: no cover - compiled; checked against decode_plan in tests
    """(positive cells, positions read) of the greedy decoder on ``perm``."""
    a = supply.copy()
    b = demand.copy()
    active = 0
    for i in range(a.size):
        if a[i] > eps:
            active += 1
    positive = 0
    for t in range(perm.size):
        if active == 0:
            return positive, t
        k = perm[t]
        i = k // n
        j = k - i * n
        q = min(a[i], b[j])
        if q > eps:
            positive += 1
            a[i] -= q
            b[j] -= q
            if a[i] <= eps:
                active -= 1
    return positive, perm.size


@njit(cache=True)
def _costs(perms, supply, demand, cost, n, eps, out):  # pragma: no cover - compiled
    for r in range(perms.shape[0]):
        out[r] = _decode_cost(perms[r], supply, demand, cost, n, eps)


class Decoder:
    """The project's decoder bound to one (balanced) problem."""

    def __init__(self, problem: TransportProblem, tol: float = DECODER_TOL) -> None:
        self.problem = problem
        p = problem.balanced()
        supply, demand, cost, cols = _arrays(p)
        self._args = (supply, demand, cost, cols, decoder_eps(p, tol))
        self.shape: tuple[int, int] = (int(p.shape[0]), int(p.shape[1]))
        self.length = self.shape[0] * self.shape[1]

    def costs(self, perms: np.ndarray) -> np.ndarray:
        supply, demand, cost, cols, eps = self._args
        perms = np.ascontiguousarray(np.atleast_2d(perms), dtype=np.int64)
        out = np.empty(perms.shape[0])
        _costs(perms, supply, demand, cost, cols, eps, out)
        return out

    def prefix(self, perm: np.ndarray) -> tuple[int, int]:
        supply, demand, _, cols, eps = self._args
        pos, read = _prefix(np.ascontiguousarray(perm, dtype=np.int64), supply, demand, cols, eps)
        return int(pos), int(read)

    def positive_cells(self, perm: np.ndarray) -> np.ndarray:
        supply, demand, _, cols, eps = self._args
        plan = Kernels("numba").decode_plan(np.ascontiguousarray(perm, dtype=np.int64), supply, demand, cols, eps)
        return np.flatnonzero(plan > eps)


def swap_count(mode: str, strength: float, m: int, n: int, rng: np.random.Generator) -> int:
    """Number of swaps one offspring receives under ``mode`` (as in :func:`tpga.ga.run_ga`)."""
    if mode == "swap_fixed":
        return int(rng.random() < strength)
    if mode == "swap_count":
        return int(round(strength))
    if mode == "swap_scaled":
        return max(1, int(round(strength * (m + n))))
    if mode == "swap_per_position":
        return int(rng.binomial(m * n, strength)) // 2
    raise ValueError(f"unknown mutation mode {mode!r}")


def apply_swaps(parent: np.ndarray, k: int, rng: np.random.Generator) -> np.ndarray:
    """``k`` swaps of two distinct uniformly chosen positions each."""
    child = parent.copy()
    length = child.size
    first = rng.integers(length, size=k)
    second = rng.integers(length - 1, size=k)
    second += second >= first  # distinct from the first position, uniform over the others
    for a, b in zip(first.tolist(), second.tolist(), strict=True):
        child[a], child[b] = child[b], child[a]
    return child


def prefix_rows(dec: Decoder, perms: np.ndarray) -> dict[str, float]:
    """Medians over ``perms`` of positive cells and prefix length (absolute and as a share of m n)."""
    pos, read = np.array([dec.prefix(p) for p in perms]).T
    return {
        "positive_cells": float(np.median(pos)),
        "prefix_length": float(np.median(read)),
        "prefix_share": float(np.median(read) / dec.length),
        "basis_size": float(sum(dec.shape) - 1),
    }


def neutrality(
    dec: Decoder, parents: np.ndarray, parent_costs: np.ndarray, mode: str, strength: float, rng: np.random.Generator
) -> dict[str, float]:
    """Share of offspring with the parent's cost; also among offspring with at least one swap."""
    m, n = dec.shape
    swaps = np.array([swap_count(mode, strength, m, n, rng) for _ in range(len(parents))])
    children = np.vstack([apply_swaps(p, int(k), rng) for p, k in zip(parents, swaps, strict=True)])
    neutral = dec.costs(children) == parent_costs
    mutated = swaps > 0
    return {
        "offspring": float(len(parents)),
        "neutral_share": float(neutral.mean()),
        "neutral_share_mutated": float(neutral[mutated].mean()) if mutated.any() else float("nan"),
        "mean_swaps": float(swaps.mean()),
    }


def locality(
    dec: Decoder,
    parents: np.ndarray,
    parent_costs: np.ndarray,
    z_star: float,
    rng: np.random.Generator,
    ks: tuple[int, ...] = LOCALITY_K,
) -> list[dict[str, float]]:
    """Per k: median |dZ| / Z* and the neutral share; last row: Spearman correlation of k and |dZ|."""
    rows, all_k, all_d = [], [], []
    for k in ks:
        children = np.vstack([apply_swaps(p, k, rng) for p in parents])
        d = np.abs(dec.costs(children) - parent_costs)
        rows.append(
            {"k": float(k), "median_rel_change": float(np.median(d) / z_star), "neutral_share": float((d == 0).mean())}
        )
        all_k += [k] * len(d)
        all_d += list(d)
    rho = stats.spearmanr(all_k, all_d).statistic if np.ptp(all_d) > 0 else float("nan")
    rows.append({"k": float("nan"), "spearman_k_vs_abs_change": float(rho)})
    return rows


def heritability(dec: Decoder, population: np.ndarray, pairs: int, rng: np.random.Generator) -> dict[str, float]:
    """Order crossover of random parent pairs: share of the child's positive cells positive in a parent."""
    kernels = Kernels("numba")
    length = population.shape[1]
    shares = []
    for _ in range(pairs):
        a, b = rng.choice(len(population), size=2, replace=False)
        i, j = sorted(rng.choice(length, size=2, replace=False))
        child = kernels.order_crossover(population[a], population[b], int(i), int(j))
        cells = dec.positive_cells(child)
        inherited = np.union1d(dec.positive_cells(population[a]), dec.positive_cells(population[b]))
        shares.append(np.isin(cells, inherited).mean())
    return {"pairs": float(pairs), "inherited_share": float(np.mean(shares)), "inherited_share_min": float(min(shares))}


def random_parents(dec: Decoder, count: int, rng: np.random.Generator) -> np.ndarray:
    return np.vstack([rng.permutation(dec.length) for _ in range(count)]).astype(np.int64)


class Snapshots:
    """A ``population_hook`` for :func:`tpga.ga.run_ga`: copies the first population at or after each fraction
    of the budget below 1 and keeps a reference to the latest one (the final population once the run ends;
    ``run_ga`` does not write to it after its last generation)."""

    def __init__(self, budget: int, fractions: tuple[float, ...]) -> None:
        self.budget = budget
        self.fractions = tuple(f for f in fractions if f < 1.0)
        self.kept: dict[float, np.ndarray] = {}
        self._last: np.ndarray | None = None
        self.last_evaluations = 0

    def __call__(self, evaluations: int, pop: np.ndarray, fit: np.ndarray) -> None:
        for f in self.fractions:
            if f not in self.kept and evaluations >= f * self.budget:
                self.kept[f] = pop.copy()
        self._last = pop
        self.last_evaluations = evaluations

    def final(self) -> np.ndarray:
        assert self._last is not None
        return self._last.copy()
