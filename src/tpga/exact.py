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


@dataclass
class HighsTiming:
    """Optimum from ``highspy`` with the time split reported by HiGHS itself.

    * ``solver_s``: HiGHS run time of ``Highs.run()`` (``getRunTime``; presolve, simplex and postsolve);
    * ``presolve_s``: HiGHS run time of ``Highs.presolve()`` alone, on a separate solver object;
    * ``build_s``: wall time to assemble the sparse model and pass it to HiGHS;
    * ``wrapper_s``: wall time of the ``run()`` call and the extraction of the solution minus ``solver_s``.
    """

    x: FloatArray
    cost: float
    model_status: str
    solver_s: float
    presolve_s: float
    build_s: float
    wrapper_s: float
    version: str


def _highs_model(p: TransportProblem):
    import highspy

    m, n = p.shape
    lp = highspy.HighsLp()
    lp.num_col_ = m * n
    lp.num_row_ = m + n
    lp.col_cost_ = p.cost.ravel().astype(np.float64)
    lp.col_lower_ = np.zeros(m * n)
    lp.col_upper_ = np.full(m * n, highspy.kHighsInf)
    b = np.concatenate([p.supply, p.demand]).astype(np.float64)
    lp.row_lower_ = b
    lp.row_upper_ = b
    lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
    lp.a_matrix_.num_col_ = m * n
    lp.a_matrix_.num_row_ = m + n
    lp.a_matrix_.start_ = np.arange(0, 2 * m * n + 1, 2, dtype=np.int32)
    rows = np.empty(2 * m * n, dtype=np.int32)
    rows[0::2] = np.repeat(np.arange(m, dtype=np.int32), n)
    rows[1::2] = m + np.tile(np.arange(n, dtype=np.int32), m)
    lp.a_matrix_.index_ = rows
    lp.a_matrix_.value_ = np.ones(2 * m * n)
    return lp


def _highs(threads: int):
    import highspy

    h = highspy.Highs()
    h.setOptionValue("output_flag", False)
    h.setOptionValue("threads", threads)
    h.setOptionValue("primal_feasibility_tolerance", 1e-9)
    h.setOptionValue("dual_feasibility_tolerance", 1e-9)
    return h


def solve_lp_highspy(problem: TransportProblem, threads: int = 1) -> HighsTiming:
    """Solve the balanced classical model with ``highspy``; status ``Optimal`` is required."""
    import highspy

    p = problem.balanced()
    m, n = p.shape
    t0 = time.perf_counter()
    lp = _highs_model(p)
    h = _highs(threads)
    h.passModel(lp)
    build = time.perf_counter() - t0
    t1 = time.perf_counter()
    h.run()
    solver = h.getRunTime()
    status = h.getModelStatus()
    if status != highspy.HighsModelStatus.kOptimal:  # pragma: no cover - balanced problems are feasible
        raise RuntimeError(f"HiGHS model status {h.modelStatusToString(status)}")
    x = np.asarray(h.getSolution().col_value).reshape(m, n)
    cost = float(h.getInfo().objective_function_value)
    wrapper = time.perf_counter() - t1 - solver
    pre = _highs(threads)
    pre.passModel(lp)
    pre.presolve()
    return HighsTiming(
        x=x,
        cost=cost,
        model_status=h.modelStatusToString(status),
        solver_s=solver,
        presolve_s=pre.getRunTime(),
        build_s=build,
        wrapper_s=max(0.0, wrapper),
        version=h.version(),
    )
