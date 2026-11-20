"""Cycle mutation (a random simplex pivot on the decoded plan) and the GA that uses it.

The swap mutation of the permutation encoding often leaves the decoded plan unchanged (Proposition 3 of the
article). The cycle mutation works on the plan instead: the offspring is decoded into a basic plan, the
basis is completed to a spanning tree, ``k`` times a non-basic arc chosen uniformly at random enters the
basis (the amount ``theta`` is moved along the cycle it closes and an arc that drops to zero leaves), and the
new plan is encoded back into a permutation by the construction in the proof of Proposition 2: the basic
arcs in the order of leaf elimination, then the other arcs in the order they had. No cost, dual value or
other LP information is used to choose the entering arc. The plan changes unless ``theta = 0`` (a degenerate
pivot).

:func:`run_ga_x` is a GA with the selection and crossover of :func:`tpga.ga.run_ga`, the mutation modes
``swap_count``, ``swap_scaled``, ``cycle`` and ``cycle_scaled``, an optional fixed charge per used arc and an
optional pivot local search. With a swap mode and no fixed charge it reproduces :func:`tpga.ga.run_ga`
exactly (same random numbers, same result); the existing GA is not changed.
"""

from __future__ import annotations

import time
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Literal

import numpy as np
from numpy.typing import ArrayLike

from tpga import _xkernels
from tpga._kernels import uniforms_per_child
from tpga.decoder import DECODER_TOL, decoder_eps
from tpga.ga import GAResult, ProgressCallback, _arrays
from tpga.initialization import cost_aware_population
from tpga.model import FloatArray, TransportProblem

XMutationMode = Literal["swap_count", "swap_scaled", "cycle", "cycle_scaled"]
X_MODES = ("swap_count", "swap_scaled", "cycle", "cycle_scaled")


def _work(m: int, n: int, length: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    return (
        np.empty(m),
        np.empty(n),
        np.empty(m + n),
        np.empty((_xkernels.IW_ROWS, _xkernels.iw_columns(m, n)), dtype=np.int64),
        np.zeros(length, dtype=np.bool_),
    )


def _fixed_array(fixed: ArrayLike | None, m: int, n: int) -> FloatArray:
    if fixed is None:
        return np.zeros(m * n)
    f = np.ascontiguousarray(np.asarray(fixed, dtype=np.float64).reshape(-1))
    if f.size != m * n:
        raise ValueError("fixed charges must have the shape of the cost matrix")
    if (f < 0).any():
        raise ValueError("fixed charges must be nonnegative")
    return f


def _balanced(problem: TransportProblem) -> TransportProblem:
    if not problem.is_balanced:
        raise ValueError("a balanced problem is required; call problem.balanced() first")
    return problem


def encode_plan(
    problem: TransportProblem, x: ArrayLike, parent: ArrayLike | None = None, engine: str = "numba"
) -> np.ndarray:
    """Permutation whose greedy decoding is the basic plan ``x``.

    The positive cells of ``x`` (they must form a forest) are completed to a spanning tree with zero arcs in
    index order, the tree arcs are written in the order of leaf elimination and the other arcs follow in the
    relative order they have in ``parent`` (index order when ``parent`` is None). Exact for integer data.
    """
    p = _balanced(problem)
    m, n = p.shape
    plan = np.asarray(x, dtype=np.float64)
    if plan.shape != (m, n):
        raise ValueError("plan shape does not match the problem")
    eps = decoder_eps(p)
    cells = np.flatnonzero(plan.ravel() > eps)
    if cells.size > m + n - 1:
        raise ValueError("the plan is not basic: more than m + n - 1 positive cells")
    k = _xkernels.table(engine)
    _, _, flows, iw, in_basis = _work(m, n, m * n)
    iw[0, : cells.size] = cells
    flows[: cells.size] = plan.ravel()[cells]
    parent_uf = iw[1]
    parent_uf[: m + n] = np.arange(m + n)
    for arc in cells.tolist():
        ra, rb = k["_find"](parent_uf, arc // n), k["_find"](parent_uf, m + arc % n)
        if ra == rb:
            raise ValueError("the plan is not basic: its positive cells contain a cycle")
        parent_uf[ra] = rb
    k["_complete_basis"](iw[0], flows, int(cells.size), m, n, iw[1])
    perm = (
        np.arange(m * n, dtype=np.int64)
        if parent is None
        else np.ascontiguousarray(np.asarray(parent, dtype=np.int64).ravel()).copy()
    )
    if perm.size != m * n or not np.array_equal(np.sort(perm), np.arange(m * n)):
        raise ValueError(f"parent must be a permutation of range({m * n})")
    k["_encode"](perm, iw[0], m + n - 1, m, n, iw[9], iw[1], iw[8], in_basis)
    return perm


@dataclass
class CycleMove:
    """Result of :func:`cycle_mutation`: the new permutation, the cost of its plan (with fixed charges when
    given), the number of pivots done and the number of them with ``theta = 0``."""

    permutation: np.ndarray
    cost: float
    pivots: int
    zero_pivots: int


def cycle_mutation(
    problem: TransportProblem,
    perm: ArrayLike,
    pivots: int,
    rng: np.random.Generator | None = None,
    uniforms: ArrayLike | None = None,
    fixed: ArrayLike | None = None,
    engine: str = "numba",
    tol: float = DECODER_TOL,
) -> CycleMove:
    """Apply the cycle mutation with ``pivots`` pivots to a permutation (the input is not modified).

    The entering arc of pivot ``p`` is the ``floor(u_p N')``-th non-basic arc in index order, ``N'`` the
    number of non-basic arcs; ``u_p`` comes from ``uniforms`` or is drawn from ``rng``.
    """
    p = _balanced(problem)
    m, n = p.shape
    child = np.ascontiguousarray(np.asarray(perm, dtype=np.int64).ravel()).copy()
    if child.size != m * n or not np.array_equal(np.sort(child), np.arange(m * n)):
        raise ValueError(f"perm must be a permutation of range({m * n})")
    if pivots < 0:
        raise ValueError("pivots must be nonnegative")
    if uniforms is None:
        u = (rng or np.random.default_rng()).random(pivots)
    else:
        u = np.ascontiguousarray(np.asarray(uniforms, dtype=np.float64).ravel())
        if u.size < pivots:
            raise ValueError("one uniform number per pivot is needed")
    supply, demand, cost, n_cols = _arrays(p)
    a, b, flows, iw, in_basis = _work(m, n, m * n)
    total, done, zero = _xkernels.table(engine)["_cycle_mutation"](
        child,
        supply,
        demand,
        cost,
        _fixed_array(fixed, m, n),
        n_cols,
        decoder_eps(p, tol),
        int(pivots),
        u,
        0,
        a,
        b,
        flows,
        iw,
        in_basis,
    )
    return CycleMove(child, float(total), int(done), int(zero))


@dataclass(frozen=True)
class GAXConfig:
    """Parameters of :func:`run_ga_x` (budget-only stop).

    Mutation, applied to every offspring:

    * ``swap_count``: ``round(mutation_strength)`` swaps of two positions;
    * ``swap_scaled``: ``max(1, round(mutation_strength (m + n)))`` swaps;
    * ``cycle``: cycle mutation with ``round(mutation_strength)`` pivots;
    * ``cycle_scaled``: cycle mutation with ``max(1, round(mutation_strength (m + n)))`` pivots.

    ``entering`` is the rule for the entering arc of a pivot of the cycle mutation: ``uniform`` among all
    non-basic arcs, or ``nondegenerate`` (amendment 10.5): uniform among the non-basic arcs whose cycle has
    no arc with zero flow on a minus position, so that ``theta > 0``; when there is no such arc the uniform
    rule is used for that pivot. The same uniform number chooses the arc under both rules.

    ``local_search_every = g > 0``: after every ``g``-th generation one step of the pivot local search on the
    best individual of the population (its decoding and every neighbour count as evaluations).
    """

    population: int
    crossover_rate: float
    tournament: int
    elite: int
    max_evaluations: int
    mutation_mode: XMutationMode = "cycle"
    mutation_strength: float = 1.0
    initialization: Literal["random", "cost-aware"] = "random"
    seed: int | None = None
    local_search_every: int = 0
    decoder_tol: float = DECODER_TOL
    entering: Literal["uniform", "nondegenerate"] = "uniform"

    def __post_init__(self) -> None:
        if self.mutation_mode not in X_MODES:
            raise ValueError(f"mutation_mode must be one of {list(X_MODES)}")
        if self.entering not in ("uniform", "nondegenerate"):
            raise ValueError("entering must be uniform or nondegenerate")
        if self.entering == "nondegenerate" and self.mutation_mode not in ("cycle", "cycle_scaled"):
            raise ValueError("the rule nondegenerate belongs to the cycle mutation")
        if self.mutation_mode in ("swap_count", "cycle") and round(self.mutation_strength) < 1:
            raise ValueError("mutation_strength must be at least 1 (moves per offspring)")
        if self.mutation_strength <= 0:
            raise ValueError("mutation_strength must be positive")
        if self.initialization not in ("random", "cost-aware"):
            raise ValueError("initialization must be random or cost-aware")
        if self.population < 2:
            raise ValueError("population must be at least 2")
        if not 0.0 <= self.crossover_rate <= 1.0:
            raise ValueError("crossover_rate must lie in [0, 1]")
        if not 1 <= self.tournament <= self.population:
            raise ValueError("tournament size must lie in [1, population]")
        if not 0 <= self.elite < self.population:
            raise ValueError("elite must lie in [0, population)")
        if self.max_evaluations < self.population:
            raise ValueError("max_evaluations must be at least the population size")
        if self.local_search_every < 0:
            raise ValueError("local_search_every must be nonnegative")
        if not 0.0 <= self.decoder_tol < 1e-3:
            raise ValueError("decoder_tol must lie in [0, 1e-3)")

    def moves(self, m: int, n: int) -> int:
        """Swaps or pivots per offspring on an ``m x n`` problem."""
        if self.mutation_mode in ("swap_scaled", "cycle_scaled"):
            return max(1, int(round(self.mutation_strength * (m + n))))
        return int(round(self.mutation_strength))


@dataclass
class GAXResult(GAResult):
    """:class:`tpga.ga.GAResult` plus the counters of the cycle mutation and of the local search.
    ``fallback_pivots``: pivots of the rule ``nondegenerate`` that the uniform rule chose; ``pivot_trace``:
    (pivots, pivots with theta = 0) summed up to the end of every generation."""

    pivots: int = 0
    zero_pivots: int = 0
    unchanged_offspring: int = 0
    local_search_calls: int = 0
    local_search_evaluations: int = 0
    local_search_improvements: int = 0
    fallback_pivots: int = 0
    pivot_trace: list[tuple[int, int]] = field(default_factory=list)


def run_ga_x(
    problem: TransportProblem,
    config: GAXConfig,
    fixed: ArrayLike | None = None,
    start_problem: TransportProblem | None = None,
    callback: ProgressCallback | None = None,
    engine: str = "numba",
    *,
    fill_budget: bool = False,
    reencode: Literal["after_swap", "only"] | None = None,
    generation_hook: Callable[[int, np.ndarray, np.ndarray, np.ndarray], None] | None = None,
    population_hook: Callable[[int, np.ndarray, bool], None] | None = None,
) -> GAXResult:
    """GA with the cycle mutation (or swaps), minimising ``sum c x + sum fixed [x > 0]``.

    ``fixed`` is the matrix of fixed charges (None: the classical linear cost). ``start_problem`` is the
    problem whose costs build the cost-aware start (default: ``problem``); for the fixed-charge problem it is
    the linearised problem. ``evaluations`` counts decoder calls and local-search neighbours.

    Read-only hooks receive the input to selection or a completed population, without consuming GA
    random draws. The population hook's final flag is true on the last notification.
    """
    cfg = config
    t0 = time.perf_counter()
    k = _xkernels.table(engine)
    p = problem.balanced()
    if fixed is not None and p is not problem:
        raise ValueError("fixed charges need a balanced problem")
    m, n = p.shape
    length = m * n
    supply, demand, cost, n_cols = _arrays(p)
    fx = _fixed_array(fixed, m, n)
    eps = decoder_eps(p, cfg.decoder_tol)
    rng = np.random.default_rng(cfg.seed)
    size = cfg.population

    starts = (
        cost_aware_population((start_problem or p).balanced(), size, rng)
        if cfg.initialization == "cost-aware"
        else [rng.permutation(length) for _ in range(size)]
    )
    pop = np.ascontiguousarray(np.vstack(starts), dtype=np.int64)
    fit = np.array([k["_decode_cost_fc"](pop[r], supply, demand, cost, fx, n_cols, eps) for r in range(size)])
    evaluations = size
    winner = int(np.argmin(fit))
    best = pop[winner].copy()
    best_cost = float(fit[winner])
    best_evaluation, best_generation = winner + 1, 0
    history = [best_cost]
    improvements = [(best_evaluation, best_cost)]
    if population_hook is not None:
        population_hook(evaluations, pop, False)

    new_pop = np.empty_like(pop)
    new_fit = np.empty_like(fit)
    scratch = np.arange(size, dtype=np.int64)
    kept = np.zeros(length, dtype=np.bool_)
    offspring = size - cfg.elite
    width = uniforms_per_child(cfg.tournament)
    cycle = 1 if cfg.mutation_mode in ("cycle", "cycle_scaled") else 0
    mode = 2 if cycle and cfg.entering == "nondegenerate" else cycle
    if reencode is not None:
        if cycle:
            raise ValueError("re-encoding controls require a swap configuration")
        mode = 3
    trace: list[tuple[int, int]] = []
    moves = cfg.moves(m, n)
    per_move = 1 if cycle else 2
    counts = np.full(max(offspring, 1), 0 if reencode == "only" else moves, dtype=np.int64)
    offsets = (per_move * moves * np.arange(max(offspring, 1))).astype(np.int64)
    stats = np.zeros(4, dtype=np.int64)
    ls_calls = ls_evals = ls_improved = 0
    work = _work(m, n, length)
    generation, stop_reason = 0, "budget"
    if callback is not None and callback(0, evaluations, best_cost):
        stop_reason = "cancelled"
    else:
        while evaluations < cfg.max_evaluations and offspring > 0:
            count = min(offspring, cfg.max_evaluations - evaluations)
            if count < offspring and not fill_budget:
                break
            order = np.argsort(fit, kind="stable").astype(np.int64)
            uniforms = rng.random((count, width))
            extra_u = rng.random(per_move * moves * count)
            if generation_hook is not None:
                generation_hook(evaluations, pop, fit, uniforms)
            k["_next_generation_x"](
                pop,
                fit,
                order,
                cfg.elite,
                uniforms,
                cfg.tournament,
                cfg.crossover_rate,
                supply,
                demand,
                cost,
                fx,
                n_cols,
                eps,
                new_pop,
                new_fit,
                scratch,
                kept,
                mode,
                counts,
                offsets,
                extra_u,
                stats,
            )
            pop, new_pop = new_pop, pop
            fit, new_fit = new_fit, fit
            generation += 1
            if cycle:
                trace.append((int(stats[0]), int(stats[1])))
            child = cfg.elite + int(np.argmin(fit[cfg.elite : cfg.elite + count]))
            if fit[child] < best_cost:
                best_cost = float(fit[child])
                best = pop[child].copy()
                best_evaluation = evaluations + (child - cfg.elite) + 1
                best_generation = generation
                improvements.append((best_evaluation, best_cost))
            evaluations += count
            if cfg.local_search_every and generation % cfg.local_search_every == 0:
                room = cfg.max_evaluations - evaluations
                if room >= 2:
                    target = int(np.argmin(fit))
                    used, improved, value = k["_first_improvement"](
                        pop[target], supply, demand, cost, fx, n_cols, eps, float(rng.random()), room, *work
                    )
                    ls_calls += 1
                    ls_evals += int(used)
                    evaluations += int(used)
                    if improved:
                        ls_improved += 1
                        fit[target] = value
                        if value < best_cost:
                            best_cost = float(value)
                            best = pop[target].copy()
                            best_evaluation = evaluations
                            best_generation = generation
                            improvements.append((best_evaluation, best_cost))
            history.append(best_cost)
            if population_hook is not None:
                population_hook(evaluations, pop[: cfg.elite + count], False)
            if callback is not None and callback(generation, evaluations, best_cost):
                stop_reason = "cancelled"
                break

    if population_hook is not None:
        population_hook(evaluations, pop[: cfg.elite + count] if generation else pop, True)
    flat = np.zeros(length)
    a, b, flows, iw, _ = work
    count = k["_decode_arcs"](best, supply, demand, n_cols, eps, a, b, iw[0], flows)
    flat[iw[0, :count]] = flows[:count]
    x = flat.reshape(m, n)
    true_cost = p.total_cost(x) + float(fx.reshape(m, n)[x > eps].sum())
    return GAXResult(
        x=x,
        cost=true_cost,
        history=history,
        evaluations=evaluations,
        runtime_s=time.perf_counter() - t0,
        best_evaluation=best_evaluation,
        best_generation=best_generation,
        generations=generation,
        stop_reason=stop_reason,
        improvements=improvements,
        permutation=best,
        generations_since_improvement=generation - best_generation,
        evaluations_since_improvement=evaluations - best_evaluation,
        pivots=int(stats[0]),
        zero_pivots=int(stats[1]),
        unchanged_offspring=int(stats[2]),
        local_search_calls=ls_calls,
        local_search_evaluations=ls_evals,
        local_search_improvements=ls_improved,
        fallback_pivots=int(stats[3]),
        pivot_trace=trace,
    )
