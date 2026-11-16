"""Basic solutions of the transportation problem and permutations that reproduce them.

A plan is basic when its positive cells form a forest in the bipartite graph of sources and
destinations; then it has at most ``m + n - 1`` positive cells.
"""

from __future__ import annotations

from collections import deque

import numpy as np
from numpy.typing import ArrayLike

from tpga.model import TransportProblem


def support(x: ArrayLike, tol: float = 0.0) -> list[tuple[int, int]]:
    """Cells with ``x_ij > tol`` in row-major order."""
    arr = np.asarray(x, dtype=float)
    return [(int(i), int(j)) for i, j in zip(*np.nonzero(arr > tol), strict=True)]


def is_acyclic(cells: list[tuple[int, int]], m: int, n: int) -> bool:
    """True if the cells, read as edges between row ``i`` and column ``m + j``, contain no cycle."""
    parent = list(range(m + n))

    def find(v: int) -> int:
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for i, j in cells:
        a, b = find(i), find(m + j)
        if a == b:
            return False
        parent[a] = b
    return True


def is_basic(x: ArrayLike, tol: float = 0.0) -> bool:
    """True if the positive cells of ``x`` number at most ``m + n - 1`` and contain no cycle."""
    arr = np.asarray(x, dtype=float)
    m, n = arr.shape
    cells = support(arr, tol)
    return len(cells) <= m + n - 1 and is_acyclic(cells, m, n)


def permutation_from_basis(problem: TransportProblem, x: ArrayLike, tol: float = 0.0) -> np.ndarray | None:
    """Permutation of all arcs whose greedy decoding is the basic plan ``x``, or None if ``x`` is not basic.

    The positive cells are ordered by repeatedly removing a leaf of the support forest (a row or
    column with exactly one remaining positive cell); the remaining arcs follow in index order.
    When the leaf is row ``i`` with cell ``(i, j)``, the row's remaining supply equals ``x_ij`` and
    the column's remaining demand is at least ``x_ij``, so the decoder allocates exactly ``x_ij``.
    The same holds for a column leaf. This is an argument for exact arithmetic; with floating-point
    data the reproduction is checked empirically.
    """
    p = problem.balanced()
    m, n = p.shape
    arr = np.asarray(x, dtype=float)
    if arr.shape != (m, n):
        raise ValueError("plan shape does not match the balanced problem")
    cells = support(arr, tol)
    if not is_acyclic(cells, m, n):
        return None
    incident: list[set[int]] = [set() for _ in range(m + n)]
    for e, (i, j) in enumerate(cells):
        incident[i].add(e)
        incident[m + j].add(e)
    queue = deque(v for v in range(m + n) if len(incident[v]) == 1)
    order: list[int] = []
    removed = [False] * len(cells)
    while queue:
        v = queue.popleft()
        if len(incident[v]) != 1:
            continue
        e = next(iter(incident[v]))
        removed[e] = True
        i, j = cells[e]
        order.append(i * n + j)
        for node in (i, m + j):
            incident[node].discard(e)
            if len(incident[node]) == 1:
                queue.append(node)
    if not all(removed):  # pragma: no cover - a forest is always emptied by leaf removal
        return None
    rest = np.setdiff1d(np.arange(m * n), np.asarray(order, dtype=np.int64), assume_unique=False)
    return np.concatenate((np.asarray(order, dtype=np.int64), rest.astype(np.int64)))
