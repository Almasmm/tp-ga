"""Exact baseline: linear programming with the HiGHS solver."""

from __future__ import annotations

import time
from dataclasses import dataclass

import numpy as np
from scipy import sparse
from scipy.optimize import linprog

from tpga.model import FloatArray, TransportProblem


@dataclass
class LPResult:
    """Solution of the LP with the solver status and the wall-clock time of the solver call."""

    x: FloatArray
    cost: float
    status: int
    message: str
    time_s: float
    method: str


def _constraints(p: TransportProblem) -> tuple[sparse.csr_matrix, np.ndarray]:
    m, n = p.shape
    rows = np.concatenate([np.repeat(np.arange(m), n), m + np.tile(np.arange(n), m)])
    cols = np.concatenate([np.arange(m * n), np.arange(m * n)])
    a_eq = sparse.csr_matrix((np.ones(2 * m * n), (rows, cols)), shape=(m + n, m * n))
    return a_eq, np.concatenate([p.supply, p.demand])


def solve_lp_detailed(problem: TransportProblem, method: str = "highs") -> LPResult:
    """Solve the balanced classical model and report status, objective and solver time.

    ``method="highs-ds"`` forces the dual simplex, whose solution is a vertex (a basic solution).
    The time covers the ``linprog`` call only, not the construction of the constraint matrix.
    """
    p = problem.balanced()
    m, n = p.shape
    a_eq, b_eq = _constraints(p)
    c = p.cost.ravel()
    t0 = time.perf_counter()
    res = linprog(
        c,
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=(0, None),
        method=method,
        options={"primal_feasibility_tolerance": 1e-9, "dual_feasibility_tolerance": 1e-9},
    )
    elapsed = time.perf_counter() - t0
    if res.status != 0:  # pragma: no cover - a balanced classical problem is always feasible and bounded
        raise RuntimeError(f"LP solver failed with status {res.status}: {res.message}")
    return LPResult(res.x.reshape(m, n), float(res.fun), int(res.status), str(res.message), elapsed, method)


def solve_lp(problem: TransportProblem) -> tuple[FloatArray, float]:
    """Return the optimal plan and cost of the (balanced) classical model.

    Exact methods apply directly to the classical model, so this optimum is the reference
    against which any heuristic result on it should be reported.
    """
    r = solve_lp_detailed(problem)
    return r.x, r.cost
