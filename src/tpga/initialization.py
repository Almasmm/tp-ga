"""Cost-aware starting chromosomes for the transportation GA."""

import numpy as np

from tpga.model import TransportProblem


def vogel_order(problem: TransportProblem) -> np.ndarray:
    """Prioritize an allocation with the largest penalty for losing its cheapest arc."""
    m, n = problem.shape
    supply = problem.supply.copy()
    demand = problem.demand.copy()
    first = []
    while (supply > 0).any() and (demand > 0).any():
        rows, cols = np.flatnonzero(supply > 0), np.flatnonzero(demand > 0)
        cost = problem.cost[np.ix_(rows, cols)]
        if min(cost.shape) == 1:
            i, j = map(int, np.unravel_index(np.argmin(cost), cost.shape))
        else:
            cheapest_rows = np.partition(cost, 1, axis=1)[:, :2]
            cheapest_cols = np.partition(cost, 1, axis=0)[:2, :]
            row_penalty = cheapest_rows[:, 1] - cheapest_rows[:, 0]
            col_penalty = cheapest_cols[1] - cheapest_cols[0]
            i, j = int(np.argmax(row_penalty)), int(np.argmax(col_penalty))
            if row_penalty[i] >= col_penalty[j]:
                j = int(np.argmin(cost[i]))
            else:
                i = int(np.argmin(cost[:, j]))
        i, j = int(rows[i]), int(cols[j])
        quantity = min(supply[i], demand[j])
        supply[i] -= quantity
        demand[j] -= quantity
        first.append(i * n + j)

    remaining = np.ones(m * n, dtype=bool)
    remaining[first] = False
    return np.concatenate((np.asarray(first, dtype=np.int64), np.flatnonzero(remaining)))


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
