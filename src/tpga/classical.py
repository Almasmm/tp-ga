"""Classical starting-plan methods: north-west corner (NWC), least cost (LCM), Vogel (VAM).

Each method returns a :class:`ClassicalResult` with the plan, its cost and a step trace. The
rules for ties and for degenerate steps are fixed and documented, because the comparison with the
decoder depends on them:

* An allocation is ``q = min(remaining supply, remaining demand)``. When both reach zero at once
  (a degenerate step) the row and the column are both removed; no zero basic cell is recorded.
  This matches the greedy decoder and leaves the plan unchanged compared with the textbook rule
  of crossing out only one line.
* NWC moves right when the row still has supply, otherwise down.
* LCM visits cells by increasing cost; equal costs are taken in row-major index order
  (``i * n + j``).
* VAM: the penalty of an active row (column) is the difference between its two smallest costs
  over active columns (rows). The largest penalty wins; on equal penalties rows come before
  columns and lower indices before higher. Inside the chosen line the cheapest active cell is
  taken, lowest index first. When only one row or one column is still active, the remaining
  cells are filled cheapest first (no penalty is defined there).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from tpga.model import FloatArray, TransportProblem


@dataclass
class ClassicalResult:
    """Plan of a classical method with its cost and step trace."""

    method: str
    x: FloatArray
    cost: float
    steps: list[dict] = field(default_factory=list)
    order: list[int] = field(default_factory=list)  # arcs i*n+j in allocation order


def _allocate(x: np.ndarray, supply: np.ndarray, demand: np.ndarray, i: int, j: int) -> float:
    q = float(min(supply[i], demand[j]))
    x[i, j] += q
    supply[i] -= q
    demand[j] -= q
    return q


def _step(i: int, j: int, q: float, supply: np.ndarray, demand: np.ndarray, **extra: object) -> dict:
    return {
        "row": i,
        "col": j,
        "quantity": float(q),
        "supply_left": supply.tolist(),
        "demand_left": demand.tolist(),
        **extra,
    }


def _prepare(problem: TransportProblem) -> tuple[TransportProblem, np.ndarray, np.ndarray, np.ndarray]:
    p = problem.balanced()
    return p, p.supply.copy(), p.demand.copy(), np.zeros(p.shape)


def northwest_corner(problem: TransportProblem) -> ClassicalResult:
    """North-west corner rule on the balanced problem."""
    p, supply, demand, x = _prepare(problem)
    m, n = p.shape
    i = j = 0
    steps: list[dict] = []
    order: list[int] = []
    while i < m and j < n:
        q = _allocate(x, supply, demand, i, j)
        if q > 0:
            steps.append(_step(i, j, q, supply, demand))
            order.append(i * n + j)
        if supply[i] == 0 and demand[j] == 0:
            i, j = i + 1, j + 1
        elif supply[i] == 0:
            i += 1
        else:
            j += 1
    return ClassicalResult("NWC", x, p.total_cost(x), steps, order)


def least_cost(problem: TransportProblem) -> ClassicalResult:
    """Least-cost (minimum element) method on the balanced problem."""
    p, supply, demand, x = _prepare(problem)
    _, n = p.shape
    steps: list[dict] = []
    order: list[int] = []
    for k in np.argsort(p.cost.ravel(), kind="stable"):
        i, j = divmod(int(k), n)
        if supply[i] > 0 and demand[j] > 0:
            q = _allocate(x, supply, demand, i, j)
            steps.append(_step(i, j, q, supply, demand, unit_cost=float(p.cost[i, j])))
            order.append(int(k))
    return ClassicalResult("LCM", x, p.total_cost(x), steps, order)


def vogel(problem: TransportProblem) -> ClassicalResult:
    """Vogel's approximation method on the balanced problem, with the penalties of every step."""
    p, supply, demand, x = _prepare(problem)
    _, n = p.shape
    c = p.cost
    steps: list[dict] = []
    order: list[int] = []
    while (supply > 0).any() and (demand > 0).any():
        rows, cols = np.flatnonzero(supply > 0), np.flatnonzero(demand > 0)
        sub = c[np.ix_(rows, cols)]
        row_pen: list[float | None] = [None] * supply.size
        col_pen: list[float | None] = [None] * demand.size
        if rows.size == 1 or cols.size == 1:
            r, s = map(int, np.unravel_index(np.argmin(sub), sub.shape))
            line = "single"
        else:
            two_r = np.partition(sub, 1, axis=1)[:, :2]
            two_c = np.partition(sub, 1, axis=0)[:2, :]
            rp = two_r[:, 1] - two_r[:, 0]
            cp = two_c[1] - two_c[0]
            for k, row in enumerate(rows):
                row_pen[int(row)] = float(rp[k])
            for k, col in enumerate(cols):
                col_pen[int(col)] = float(cp[k])
            r, s = int(np.argmax(rp)), int(np.argmax(cp))
            if rp[r] >= cp[s]:
                s = int(np.argmin(sub[r]))
                line = "row"
            else:
                r = int(np.argmin(sub[:, s]))
                line = "col"
        i, j = int(rows[r]), int(cols[s])
        q = _allocate(x, supply, demand, i, j)
        steps.append(
            _step(
                i, j, q, supply, demand, unit_cost=float(c[i, j]), row_penalty=row_pen, col_penalty=col_pen, line=line
            )
        )
        order.append(i * n + j)
    return ClassicalResult("VAM", x, p.total_cost(x), steps, order)


METHODS = {"NWC": northwest_corner, "LCM": least_cost, "VAM": vogel}
