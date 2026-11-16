"""Permutation-encoded genetic algorithm with the greedy decoder, and the random-search control."""

from __future__ import annotations

import time
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Literal

import numpy as np

from tpga._kernels import Kernels, uniforms_per_child
from tpga.decoder import DECODER_TOL, decoder_eps
from tpga.initialization import cost_aware_population
from tpga.model import FloatArray, TransportProblem

IntArray = np.ndarray

#: ``callback(generation, evaluations, best_cost) -> stop``; returning True stops the run.
ProgressCallback = Callable[[int, int, float], bool | None]

MutationMode = Literal["swap_fixed", "swap_count", "swap_per_position", "swap_scaled"]
MUTATION_MODES: dict[str, int] = {"swap_fixed": 0, "swap_count": 1, "swap_per_position": 2, "swap_scaled": 3}


@dataclass(frozen=True)
class GAConfig:
    """Parameters of the genetic algorithm.

    Mutation (``mutation_mode``):

    * ``swap_fixed`` (default, v0.3.0): with probability ``mutation_rate`` one swap of two positions;
    * ``swap_count``: every offspring gets ``k = round(mutation_strength)`` swaps;
    * ``swap_per_position``: every position takes part with probability ``q = mutation_strength``; the
      number of participating positions is Binomial(m n, q) and they form ``floor(s / 2)`` swaps of
      uniformly drawn position pairs (expected about ``q m n / 2`` swaps);
    * ``swap_scaled``: ``k = max(1, round(mutation_strength * (m + n)))`` swaps per offspring.

    The run stops at the first of: ``generations`` generations (``None`` for no limit),
    ``max_evaluations`` decoder calls (``None`` for no limit; a generation is only started if all
    its offspring fit in the budget), ``stagnation`` generations without improvement of the best
    cost, ``stagnation_evaluations`` decoder calls without improvement (``None`` to disable either).
    At least one limit must be set. ``decoder_tol`` is the relative tolerance of the decoder's zero test.
    """

    population: int = 60
    generations: int | None = 200
    crossover_rate: float = 0.9
    mutation_rate: float = 0.2
    tournament: int = 3
    elite: int = 2
    seed: int | None = None
    initialization: Literal["random", "cost-aware"] = "random"
    max_evaluations: int | None = None
    stagnation: int | None = None
    mutation_mode: MutationMode = "swap_fixed"
    mutation_strength: float = 1.0
    stagnation_evaluations: int | None = None
    decoder_tol: float = DECODER_TOL

    def __post_init__(self) -> None:
        if self.mutation_mode not in MUTATION_MODES:
            raise ValueError(f"mutation_mode must be one of {sorted(MUTATION_MODES)}")
        if self.mutation_mode == "swap_count" and round(self.mutation_strength) < 1:
            raise ValueError("swap_count needs mutation_strength >= 1 (swaps per offspring)")
        if self.mutation_mode == "swap_per_position" and not (0.0 < self.mutation_strength <= 1.0):
            raise ValueError("swap_per_position needs mutation_strength in (0, 1]")
        if self.mutation_mode == "swap_scaled" and self.mutation_strength <= 0:
            raise ValueError("swap_scaled needs a positive mutation_strength")
        if self.stagnation_evaluations is not None and self.stagnation_evaluations < 1:
            raise ValueError("stagnation_evaluations must be positive")
        if not (0.0 <= self.decoder_tol < 1e-3):
            raise ValueError("decoder_tol must lie in [0, 1e-3)")
        if self.initialization not in ("random", "cost-aware"):
            raise ValueError("initialization must be random or cost-aware")
        if self.population < 2:
            raise ValueError("population must be at least 2")
        if self.generations is not None and self.generations < 0:
            raise ValueError("generations must be nonnegative")
        if not (0.0 <= self.crossover_rate <= 1.0 and 0.0 <= self.mutation_rate <= 1.0):
            raise ValueError("rates must lie in [0, 1]")
        if not (1 <= self.tournament <= self.population):
            raise ValueError("tournament size must lie in [1, population]")
        if not (0 <= self.elite < self.population):
            raise ValueError("elite must lie in [0, population)")
        if self.max_evaluations is not None and self.max_evaluations < self.population:
            raise ValueError("max_evaluations must be at least the population size")
        if self.stagnation is not None and self.stagnation < 1:
            raise ValueError("stagnation must be positive")
        if (
            self.generations is None
            and self.max_evaluations is None
            and self.stagnation is None
            and self.stagnation_evaluations is None
        ):
            raise ValueError("set at least one of generations, max_evaluations, stagnation, stagnation_evaluations")


@dataclass
class GAResult:
    """Best plan found and the run record.

    ``evaluations`` counts decoder calls. ``improvements`` lists ``(evaluation, cost)`` each time the
    best cost decreased, starting with the best of the initial population; it is an exact step
    curve of the best cost against decoder calls.
    """

    x: FloatArray
    cost: float
    history: list[float] = field(default_factory=list)  # best cost after each generation
    evaluations: int = 0
    runtime_s: float = 0.0
    best_evaluation: int = 0
    best_generation: int = 0
    generations: int = 0
    stop_reason: str = ""
    improvements: list[tuple[int, float]] = field(default_factory=list)
    permutation: IntArray | None = None
    generations_since_improvement: int = 0
    evaluations_since_improvement: int = 0


def order_crossover(p1: IntArray, p2: IntArray, rng: np.random.Generator) -> IntArray:
    """Order crossover (OX1 variant): keep a slice of ``p1``, fill the rest left to right in ``p2`` order."""
    n = p1.size
    if n < 2:
        return p1.copy()
    k = Kernels()
    i, j = k.two_positions(float(rng.random()), float(rng.random()), n)
    return k.order_crossover(np.asarray(p1, dtype=np.int64), np.asarray(p2, dtype=np.int64), i, j)


def swap_mutation(p: IntArray, rng: np.random.Generator) -> IntArray:
    """Swap two random distinct positions."""
    q = p.copy()
    if q.size >= 2:
        i, j = Kernels().two_positions(float(rng.random()), float(rng.random()), q.size)
        q[i], q[j] = q[j], q[i]
    return q


def _arrays(problem: TransportProblem) -> tuple[FloatArray, FloatArray, FloatArray, int]:
    m, n = problem.shape
    return (
        np.ascontiguousarray(problem.supply, dtype=np.float64),
        np.ascontiguousarray(problem.demand, dtype=np.float64),
        np.ascontiguousarray(problem.cost.ravel(), dtype=np.float64),
        n,
    )


def run_ga(
    problem: TransportProblem,
    config: GAConfig | None = None,
    callback: ProgressCallback | None = None,
    engine: str = "numba",
) -> GAResult:
    """Run the GA. Every individual decodes to a feasible plan of the balanced classical model,
    so no penalty or repair is used. This is a reference implementation, not a tuned solver.

    ``engine="python"`` runs the plain-Python kernels; it gives the same result and is meant for tests.
    """
    cfg = config or GAConfig()
    t0 = time.perf_counter()
    kernels = Kernels(engine)
    p = problem.balanced()
    m, n = p.shape
    length = m * n
    supply, demand, cost, n_cols = _arrays(p)
    eps = decoder_eps(p, cfg.decoder_tol)
    rng = np.random.default_rng(cfg.seed)
    size = cfg.population

    starts = (
        cost_aware_population(p, size, rng)
        if cfg.initialization == "cost-aware"
        else [rng.permutation(length) for _ in range(size)]
    )
    pop = np.ascontiguousarray(np.vstack(starts), dtype=np.int64)
    fit = np.array([kernels.decode_cost(pop[r], supply, demand, cost, n_cols, eps) for r in range(size)])
    evaluations = size
    winner = int(np.argmin(fit))
    best = pop[winner].copy()
    best_cost = float(fit[winner])
    best_evaluation, best_generation = winner + 1, 0
    history = [best_cost]
    improvements = [(best_evaluation, best_cost)]

    new_pop = np.empty_like(pop)
    new_fit = np.empty_like(fit)
    scratch = np.arange(size, dtype=np.int64)
    kept = np.zeros(length, dtype=np.bool_)
    offspring = size - cfg.elite
    width = uniforms_per_child(cfg.tournament)
    mode = MUTATION_MODES[cfg.mutation_mode]
    if mode == 1:
        fixed_swaps = int(round(cfg.mutation_strength))
    elif mode == 3:
        fixed_swaps = max(1, int(round(cfg.mutation_strength * (m + n))))
    else:
        fixed_swaps = 0
    no_counts = np.zeros(max(offspring, 1), dtype=np.int64)
    no_uniforms = np.empty(0)
    generation, since_improvement, stop_reason = 0, 0, "generations"
    if callback is not None and callback(0, evaluations, best_cost):
        stop_reason = "cancelled"
    else:
        while True:
            if cfg.generations is not None and generation >= cfg.generations:
                stop_reason = "generations"
                break
            if cfg.max_evaluations is not None and evaluations + offspring > cfg.max_evaluations:
                stop_reason = "budget"
                break
            if cfg.stagnation is not None and since_improvement >= cfg.stagnation:
                stop_reason = "stagnation"
                break
            if cfg.stagnation_evaluations is not None and evaluations - best_evaluation >= cfg.stagnation_evaluations:
                stop_reason = "stagnation_evaluations"
                break
            order = np.argsort(fit, kind="stable").astype(np.int64)
            uniforms = rng.random((offspring, width))
            # extra random numbers only for the new mutation modes, drawn after the generation's block,
            # so that swap_fixed consumes the generator exactly as v0.3.0 did
            if mode == 0:
                counts, offsets, swap_u = no_counts, no_counts, no_uniforms
            else:
                if mode == 2:
                    counts = rng.binomial(length, cfg.mutation_strength, size=offspring).astype(np.int64) // 2
                else:
                    counts = np.full(offspring, fixed_swaps, dtype=np.int64)
                offsets = np.concatenate(([0], np.cumsum(2 * counts)[:-1])).astype(np.int64)
                swap_u = rng.random(int(2 * counts.sum()))
            kernels.next_generation(
                pop,
                fit,
                order,
                cfg.elite,
                uniforms,
                cfg.tournament,
                cfg.crossover_rate,
                cfg.mutation_rate,
                supply,
                demand,
                cost,
                n_cols,
                eps,
                new_pop,
                new_fit,
                scratch,
                kept,
                mode,
                counts,
                offsets,
                swap_u,
            )
            pop, new_pop = new_pop, pop
            fit, new_fit = new_fit, fit
            generation += 1
            child = cfg.elite + int(np.argmin(fit[cfg.elite :])) if offspring else 0
            if offspring and fit[child] < best_cost:
                best_cost = float(fit[child])
                best = pop[child].copy()
                best_evaluation = evaluations + (child - cfg.elite) + 1
                best_generation = generation
                improvements.append((best_evaluation, best_cost))
                since_improvement = 0
            else:
                since_improvement += 1
            evaluations += offspring
            history.append(best_cost)
            if callback is not None and callback(generation, evaluations, best_cost):
                stop_reason = "cancelled"
                break

    x = kernels.decode_plan(best, supply, demand, n_cols, eps).reshape(m, n)
    return GAResult(
        x=x,
        cost=p.total_cost(x),
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
    )


def run_random_search(
    problem: TransportProblem,
    evaluations: int,
    seed: int | None = None,
    engine: str = "numba",
    batch_floats: int = 1 << 20,
    callback: ProgressCallback | None = None,
    decoder_tol: float = DECODER_TOL,
) -> GAResult:
    """Random search control: decode ``evaluations`` uniformly random permutations, keep the cheapest.

    It uses the same decoder as the GA and no selection, crossover or mutation, so the difference
    to the GA at an equal number of decoder calls measures what the operators contribute.
    """
    if evaluations < 1:
        raise ValueError("evaluations must be positive")
    t0 = time.perf_counter()
    kernels = Kernels(engine)
    p = problem.balanced()
    m, n = p.shape
    length = m * n
    supply, demand, cost, n_cols = _arrays(p)
    eps = decoder_eps(p, decoder_tol)
    rng = np.random.default_rng(seed)
    rows = max(1, batch_floats // max(1, length - 1))
    done, best_cost, best_evaluation = 0, np.inf, 0
    best_uniforms = np.empty(max(0, length - 1))
    improvements: list[tuple[int, float]] = []
    batches, stop_reason = 0, "budget"
    while done < evaluations:
        k = min(rows, evaluations - done)
        uniforms = rng.random((k, max(0, length - 1)))
        out = np.empty(k)
        kernels.random_batch_cost(uniforms, supply, demand, cost, n_cols, out, eps)
        running = np.minimum.accumulate(out)
        better = np.flatnonzero(running < np.concatenate(([best_cost], running[:-1])))
        for r in better:
            if out[r] < best_cost:
                best_cost = float(out[r])
                best_evaluation = done + int(r) + 1
                best_uniforms = uniforms[r].copy()
                improvements.append((best_evaluation, best_cost))
        done += k
        batches += 1
        if callback is not None and callback(batches, done, best_cost) and done < evaluations:
            stop_reason = "cancelled"
            break
    perm = np.arange(length, dtype=np.int64)
    kernels.shuffle(perm, best_uniforms)
    x = kernels.decode_plan(perm, supply, demand, n_cols, eps).reshape(m, n)
    return GAResult(
        x=x,
        cost=p.total_cost(x),
        history=[best_cost],
        evaluations=done,
        runtime_s=time.perf_counter() - t0,
        best_evaluation=best_evaluation,
        best_generation=0,
        generations=0,
        stop_reason=stop_reason,
        improvements=improvements,
        permutation=perm,
        evaluations_since_improvement=done - best_evaluation,
    )
