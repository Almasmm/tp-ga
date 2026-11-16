"""Generation-by-generation record of a small GA run, for teaching and visualisation.

The run is the same as :func:`tpga.ga.run_ga` with the same configuration and seed: the same
uniform numbers drive the same kernels. In addition, every generation records the population
costs, the best plan, the diversity of the population and, for the first offspring, the two
tournaments, the OX1 cut points and the mutation. The recorded first offspring is checked against
the one the kernel produced.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from tpga._kernels import Kernels, uniforms_per_child
from tpga.ga import GAConfig, _arrays
from tpga.initialization import cost_aware_population
from tpga.model import TransportProblem

MAX_ARCS = 100
MAX_POPULATION = 60
MAX_GENERATIONS = 300


def _tournament_detail(fit: np.ndarray, draws: np.ndarray) -> tuple[list[int], int]:
    """Candidates and winner of one tournament, replaying the kernel's partial Fisher-Yates."""
    idx = list(range(fit.size))
    candidates = []
    best = -1
    for s, u in enumerate(draws):
        r = s + min(int(u * (fit.size - s)), fit.size - s - 1)
        idx[s], idx[r] = idx[r], idx[s]
        c = idx[s]
        candidates.append(c)
        if best < 0 or fit[c] < fit[best]:
            best = c
    return candidates, best


def diversity(pop: np.ndarray) -> float:
    """Mean share of positions at which two individuals differ, over all pairs (0: identical, 1: all differ)."""
    size = pop.shape[0]
    if size < 2:
        return 0.0
    total = 0.0
    for i in range(size - 1):
        total += float((pop[i + 1 :] != pop[i]).mean(axis=1).sum())
    return total / (size * (size - 1) / 2)


def _plan_cells(x: np.ndarray) -> list[dict[str, float]]:
    return [{"row": int(i), "col": int(j), "quantity": float(x[i, j])} for i, j in zip(*np.nonzero(x > 0), strict=True)]


def trace_ga(problem: TransportProblem, config: GAConfig) -> dict[str, Any]:
    """Run the GA on a small problem and return the record of every generation."""
    p = problem.balanced()
    m, n = p.shape
    length = m * n
    if length > MAX_ARCS:
        raise ValueError(f"trace is limited to {MAX_ARCS} arcs")
    if config.population > MAX_POPULATION:
        raise ValueError(f"trace is limited to a population of {MAX_POPULATION}")
    gens = config.generations if config.generations is not None else MAX_GENERATIONS
    if gens > MAX_GENERATIONS:
        raise ValueError(f"trace is limited to {MAX_GENERATIONS} generations")
    k = Kernels("numba")
    supply, demand, cost, cols = _arrays(p)
    rng = np.random.default_rng(config.seed)
    size, elite, t = config.population, config.elite, config.tournament
    starts = (
        cost_aware_population(p, size, rng)
        if config.initialization == "cost-aware"
        else [rng.permutation(length) for _ in range(size)]
    )
    pop = np.ascontiguousarray(np.vstack(starts), dtype=np.int64)
    fit = np.array([k.decode_cost(pop[r], supply, demand, cost, cols) for r in range(size)])
    evaluations = size
    best_cost = float(fit.min())
    best = pop[int(np.argmin(fit))].copy()

    def snapshot(gen: int, detail: dict[str, Any] | None) -> dict[str, Any]:
        x = k.decode_plan(best, supply, demand, cols).reshape(m, n)
        return {
            "generation": gen,
            "evaluations": evaluations,
            "best_cost": best_cost,
            "population_costs": fit.tolist(),
            "diversity": diversity(pop),
            "best_permutation": best.tolist(),
            "best_plan": _plan_cells(x),
            "offspring": detail,
        }

    record = [snapshot(0, None)]
    new_pop, new_fit = np.empty_like(pop), np.empty_like(fit)
    scratch, kept = np.arange(size, dtype=np.int64), np.zeros(length, dtype=np.bool_)
    width = uniforms_per_child(t)
    since = 0
    for gen in range(1, gens + 1):
        if config.stagnation is not None and since >= config.stagnation:
            break
        if config.max_evaluations is not None and evaluations + size - elite > config.max_evaluations:
            break
        order = np.argsort(fit, kind="stable").astype(np.int64)
        u = rng.random((size - elite, width))
        cand_a, a = _tournament_detail(fit, u[0, :t])
        cand_b, b = _tournament_detail(fit, u[0, t : 2 * t])
        base = 2 * t
        crossed = bool(u[0, base] < config.crossover_rate and length >= 2)
        cut = k.two_positions(u[0, base + 1], u[0, base + 2], length) if crossed else None
        child = k.order_crossover(pop[a], pop[b], *cut) if cut else pop[a].copy()
        after_cx = child.copy()
        mutated = bool(u[0, base + 3] < config.mutation_rate and length >= 2)
        swap = k.two_positions(u[0, base + 4], u[0, base + 5], length) if mutated else None
        if swap:
            child[swap[0]], child[swap[1]] = child[swap[1]], child[swap[0]]
        detail = {
            "elite": [int(v) for v in order[:elite]],
            "tournament_a": {"candidates": cand_a, "winner": a},
            "tournament_b": {"candidates": cand_b, "winner": b},
            "parent_a": pop[a].tolist(),
            "parent_b": pop[b].tolist(),
            "crossover": {"applied": crossed, "cut": list(cut) if cut else None},
            "after_crossover": after_cx.tolist(),
            "mutation": {"applied": mutated, "positions": list(swap) if swap else None},
            "child": child.tolist(),
        }
        k.next_generation(
            pop,
            fit,
            order,
            elite,
            u,
            t,
            config.crossover_rate,
            config.mutation_rate,
            supply,
            demand,
            cost,
            cols,
            new_pop,
            new_fit,
            scratch,
            kept,
        )
        if size > elite and not np.array_equal(new_pop[elite], child):  # pragma: no cover - same rule twice
            raise AssertionError("trace disagrees with the kernel")
        detail["child_cost"] = float(new_fit[elite]) if size > elite else None
        pop, new_pop = new_pop, pop
        fit, new_fit = new_fit, fit
        evaluations += size - elite
        if fit.min() < best_cost:
            best_cost = float(fit.min())
            best = pop[int(np.argmin(fit))].copy()
            since = 0
        else:
            since += 1
        record.append(snapshot(gen, detail))
    return {"m": m, "n": n, "generations": record, "final_cost": best_cost}
