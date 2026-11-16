"""Second exact solver for LP-scaling measurements: OR-Tools min-cost flow (network simplex).

OR-Tools (Apache-2.0) works with integer supplies, demands and costs; the balanced transportation problem
is a min-cost flow on the complete bipartite graph. Used only to measure how exact solution time scales.
"""

from __future__ import annotations

import time
from dataclasses import dataclass

import numpy as np

from tpga.model import FloatArray, TransportProblem


@dataclass
class FlowResult:
    x: FloatArray
    cost: float
    solve_s: float
    build_s: float


def solve_min_cost_flow(problem: TransportProblem) -> FlowResult:
    """Optimal plan of an integer balanced problem; ``solve_s`` is the wall time of ``solve()`` only."""
    from ortools.graph.python import min_cost_flow

    p = problem.balanced()
    m, n = p.shape
    data = (p.supply, p.demand, p.cost)
    if any(not np.array_equal(d, np.round(d)) for d in data):
        raise ValueError("the min-cost flow solver needs integer supplies, demands and costs")
    t0 = time.perf_counter()
    flow = min_cost_flow.SimpleMinCostFlow()
    tails = np.repeat(np.arange(m, dtype=np.int32), n)
    heads = m + np.tile(np.arange(n, dtype=np.int32), m)
    cap = int(max(np.max(p.supply), np.max(p.demand)))
    flow.add_arcs_with_capacity_and_unit_cost(
        tails, heads, np.full(m * n, cap, dtype=np.int64), p.cost.ravel().astype(np.int64)
    )
    flow.set_nodes_supplies(np.arange(m + n, dtype=np.int32), np.concatenate([p.supply, -p.demand]).astype(np.int64))
    build = time.perf_counter() - t0
    t1 = time.perf_counter()
    status = flow.solve()
    solve = time.perf_counter() - t1
    if status != flow.OPTIMAL:  # pragma: no cover - balanced integer problems are feasible
        raise RuntimeError(f"min-cost flow status {status}")
    x = np.asarray(flow.flows(np.arange(m * n, dtype=np.int32)), dtype=float).reshape(m, n)
    return FlowResult(x=x, cost=float(flow.optimal_cost()), solve_s=solve, build_s=build)
