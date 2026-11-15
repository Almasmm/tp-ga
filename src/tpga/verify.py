"""Independent check of a shipment plan, written without the model's own helpers."""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike

from tpga.model import TransportProblem


@dataclass(frozen=True)
class PlanCheck:
    """Residuals of a plan against the balanced problem; ``feasible`` uses a relative tolerance."""

    feasible: bool
    max_row_residual: float
    max_col_residual: float
    min_value: float
    cost: float
    tolerance: float


def check_plan(problem: TransportProblem, x: ArrayLike, rtol: float = 1e-9) -> PlanCheck:
    """Recompute row sums, column sums, the minimum entry and the cost with plain loops.

    The tolerance is ``rtol * max(1, largest supply or demand)``.
    """
    p = problem.balanced()
    a = [float(v) for v in p.supply]
    b = [float(v) for v in p.demand]
    c = p.cost.tolist()
    plan = np.asarray(x, dtype=float).tolist()
    m, n = len(a), len(b)
    if len(plan) != m or any(len(row) != n for row in plan):
        return PlanCheck(False, math.inf, math.inf, -math.inf, math.nan, 0.0)
    tol = rtol * max(1.0, max(a), max(b))
    row_res = max(abs(math.fsum(plan[i]) - a[i]) for i in range(m))
    col_res = max(abs(math.fsum(plan[i][j] for i in range(m)) - b[j]) for j in range(n))
    low = min(min(row) for row in plan)
    cost = math.fsum(c[i][j] * plan[i][j] for i in range(m) for j in range(n))
    ok = row_res <= tol and col_res <= tol and low >= -tol
    return PlanCheck(ok, row_res, col_res, low, cost, tol)
