"""Cost-aware starting chromosomes for the transportation GA."""

import numpy as np

from tpga.model import TransportProblem


def vogel_order(problem: TransportProblem) -> np.ndarray:
    """Arcs in the allocation order of Vogel's method, followed by the other arcs in index order.

    The order comes from :func:`tpga.classical.vogel` (one implementation of the method and its tie rules),
    so decoding it gives exactly Vogel's plan.
    """
    from tpga.classical import vogel

    m, n = problem.shape
    first = np.asarray(vogel(problem).order, dtype=np.int64)
    remaining = np.ones(m * n, dtype=bool)
    remaining[first] = False
    return np.concatenate((first, np.flatnonzero(remaining)))


def cost_aware_population(problem: TransportProblem, population: int, rng: np.random.Generator) -> list[np.ndarray]:
    """Mix constructive, perturbed least-cost, and random starts without an LP solution."""
    cost = problem.cost.ravel()
    spread = float(np.std(cost))
    chromosomes = [vogel_order(problem), np.argsort(cost, kind="stable")]
    for i in range(population - 2):
        if i % 4 == 3:
            chromosomes.append(rng.permutation(cost.size))
        else:
            scale = (0.05, 0.15, 0.35)[i % 4] * spread
            chromosomes.append(np.argsort(cost + rng.normal(0, scale, cost.size), kind="stable"))
    return chromosomes
