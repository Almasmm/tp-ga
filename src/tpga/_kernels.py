"""Inner loops of the decoder and the GA operators.

Every kernel is written once as plain Python and compiled with numba. The plain functions
(``*_py``) are kept as the reference implementation: the tests run both and require identical
results, and the coverage report measures the plain versions. All randomness enters through
arrays of uniform numbers drawn from :class:`numpy.random.Generator`, so a seed gives the same
run whichever implementation executes it.

Layout of the uniform numbers for one offspring (``tournament`` = t):

====================  ============================================================
columns ``0 .. t-1``  draws of the first tournament (partial Fisher-Yates)
columns ``t .. 2t-1`` draws of the second tournament
column ``2t``         crossover happens if the value is below the crossover rate
columns ``2t+1, +2``  the two OX1 cut points
column ``2t+3``       mutation happens if the value is below the mutation rate
columns ``2t+4, +5``  the two swapped positions
====================  ============================================================
"""

from __future__ import annotations

import numpy as np
from numba import njit

UNIFORMS_PER_CHILD_EXTRA = 6  # crossover flag, two cuts, mutation flag, two positions


def uniforms_per_child(tournament: int) -> int:
    """Number of uniform numbers consumed by one offspring."""
    return 2 * tournament + UNIFORMS_PER_CHILD_EXTRA


def _decode_cost_py(perm, supply, demand, cost, n):
    """Cost of the plan the greedy decoder builds from ``perm`` (arc ``k`` is ``(k // n, k % n)``)."""
    a = supply.copy()
    b = demand.copy()
    active = 0
    for i in range(a.size):
        if a[i] > 0:
            active += 1
    total = 0.0
    for t in range(perm.size):
        if active == 0:
            break
        k = perm[t]
        i = k // n
        j = k - i * n
        q = min(a[i], b[j])
        if q > 0:
            total += cost[k] * q
            a[i] -= q
            b[j] -= q
            if a[i] == 0:
                active -= 1
    return total


def _decode_plan_py(perm, supply, demand, n):
    """Flat plan (length ``m * n``) built by the greedy decoder from ``perm``."""
    a = supply.copy()
    b = demand.copy()
    plan = np.zeros(a.size * n)
    active = 0
    for i in range(a.size):
        if a[i] > 0:
            active += 1
    for t in range(perm.size):
        if active == 0:
            break
        k = perm[t]
        i = k // n
        j = k - i * n
        q = min(a[i], b[j])
        if q > 0:
            plan[k] = q
            a[i] -= q
            b[j] -= q
            if a[i] == 0:
                active -= 1
    return plan


def _two_positions_py(u1, u2, length):
    """Two distinct positions in ``range(length)`` from two uniforms, returned in increasing order."""
    a = min(int(u1 * length), length - 1)
    b = min(int(u2 * (length - 1)), length - 2)
    if b >= a:
        b += 1
    if a < b:
        return a, b
    return b, a


def _order_crossover_py(p1, p2, i, j, child, kept):
    """OX1 variant: copy ``p1[i..j]``, fill the other positions left to right in ``p2`` order.

    ``kept`` is a boolean scratch array of length ``len(p1)`` that is all False on entry and on exit.
    """
    length = p1.size
    for t in range(i, j + 1):
        child[t] = p1[t]
        kept[p1[t]] = True
    pos = 0
    for t in range(length):
        g = p2[t]
        if not kept[g]:
            if pos == i:
                pos = j + 1
            child[pos] = g
            pos += 1
    for t in range(i, j + 1):
        kept[p1[t]] = False


def _tournament_py(fit, draws, scratch):
    """Index of the best of ``len(draws)`` distinct individuals chosen by partial Fisher-Yates.

    ``scratch`` holds ``0 .. P-1`` on entry and on exit.
    """
    size = scratch.size
    t = draws.size
    best = -1
    for s in range(t):
        r = s + min(int(draws[s] * (size - s)), size - s - 1)
        tmp = scratch[s]
        scratch[s] = scratch[r]
        scratch[r] = tmp
        c = scratch[s]
        if best < 0 or fit[c] < fit[best]:
            best = c
    # undo the swaps in reverse order so scratch is the identity again
    for s in range(t - 1, -1, -1):
        r = s + min(int(draws[s] * (size - s)), size - s - 1)
        tmp = scratch[s]
        scratch[s] = scratch[r]
        scratch[r] = tmp
    return best


def _next_generation_py(
    pop,
    fit,
    order,
    elite,
    uniforms,
    tournament,
    crossover_rate,
    mutation_rate,
    supply,
    demand,
    cost,
    n,
    new_pop,
    new_fit,
    scratch,
    kept,
):
    """Fill ``new_pop``/``new_fit``: ``elite`` best individuals keep their fitness, the rest are offspring.

    Returns the number of decoder calls (the offspring count).
    """
    size, length = pop.shape
    for e in range(elite):
        src = order[e]
        new_pop[e, :] = pop[src, :]
        new_fit[e] = fit[src]
    for c in range(size - elite):
        u = uniforms[c]
        a = _tournament(fit, u[0:tournament], scratch)
        b = _tournament(fit, u[tournament : 2 * tournament], scratch)
        child = new_pop[elite + c]
        base = 2 * tournament
        if u[base] < crossover_rate and length >= 2:
            i, j = _two_positions(u[base + 1], u[base + 2], length)
            _order_crossover(pop[a], pop[b], i, j, child, kept)
        else:
            child[:] = pop[a, :]
        if u[base + 3] < mutation_rate and length >= 2:
            i, j = _two_positions(u[base + 4], u[base + 5], length)
            tmp = child[i]
            child[i] = child[j]
            child[j] = tmp
        new_fit[elite + c] = _decode_cost(child, supply, demand, cost, n)
    return size - elite


def _shuffle_py(perm, uniforms):
    """Fisher-Yates shuffle of ``perm`` in place driven by ``len(perm) - 1`` uniforms."""
    length = perm.size
    for t in range(length - 1, 0, -1):
        r = min(int(uniforms[length - 1 - t] * (t + 1)), t)
        tmp = perm[t]
        perm[t] = perm[r]
        perm[r] = tmp


def _random_batch_cost_py(uniforms, supply, demand, cost, n, out):
    """Decode ``len(out)`` random permutations; return the row index of the cheapest one.

    Row ``r`` of ``uniforms`` drives a Fisher-Yates shuffle of the identity; ``out[r]`` gets its cost.
    """
    length = cost.size
    perm = np.empty(length, dtype=np.int64)
    best = -1
    for r in range(out.size):
        for t in range(length):
            perm[t] = t
        _shuffle(perm, uniforms[r])
        out[r] = _decode_cost(perm, supply, demand, cost, n)
        if best < 0 or out[r] < out[best]:
            best = r
    return best


# --- compiled versions ---------------------------------------------------------------------
# The plain functions above refer to the module-level names below. Under numba those names are
# the compiled kernels; when ``_PURE`` is switched on (tests only) they are the Python originals.

_decode_cost = njit(cache=True)(_decode_cost_py)
_decode_plan = njit(cache=True)(_decode_plan_py)
_two_positions = njit(cache=True)(_two_positions_py)
_order_crossover = njit(cache=True)(_order_crossover_py)
_tournament = njit(cache=True)(_tournament_py)
_shuffle = njit(cache=True)(_shuffle_py)
_next_generation = njit(cache=True)(_next_generation_py)
_random_batch_cost = njit(cache=True)(_random_batch_cost_py)

_COMPILED = {
    "_decode_cost": _decode_cost,
    "_decode_plan": _decode_plan,
    "_two_positions": _two_positions,
    "_order_crossover": _order_crossover,
    "_tournament": _tournament,
    "_shuffle": _shuffle,
    "_next_generation": _next_generation,
    "_random_batch_cost": _random_batch_cost,
}
_PLAIN = {
    "_decode_cost": _decode_cost_py,
    "_decode_plan": _decode_plan_py,
    "_two_positions": _two_positions_py,
    "_order_crossover": _order_crossover_py,
    "_tournament": _tournament_py,
    "_shuffle": _shuffle_py,
    "_next_generation": _next_generation_py,
    "_random_batch_cost": _random_batch_cost_py,
}


class Kernels:
    """Access to one implementation of the kernels: ``Kernels("numba")`` or ``Kernels("python")``.

    The plain Python implementation is slow and exists for verification; selecting it rebinds the
    module-level names that the plain functions call, so it must not be used concurrently with the
    numba engine in one process.
    """

    def __init__(self, engine: str = "numba") -> None:
        if engine not in ("numba", "python"):
            raise ValueError("engine must be numba or python")
        self.engine = engine

    def _table(self) -> dict:
        table = _COMPILED if self.engine == "numba" else _PLAIN
        globals().update(table)
        return table

    def decode_cost(self, perm, supply, demand, cost, n):
        return self._table()["_decode_cost"](perm, supply, demand, cost, n)

    def decode_plan(self, perm, supply, demand, n):
        return self._table()["_decode_plan"](perm, supply, demand, n)

    def order_crossover(self, p1, p2, i, j):
        child = np.empty_like(p1)
        kept = np.zeros(p1.size, dtype=np.bool_)
        self._table()["_order_crossover"](p1, p2, i, j, child, kept)
        return child

    def two_positions(self, u1, u2, length):
        return self._table()["_two_positions"](u1, u2, length)

    def next_generation(self, *args):
        return self._table()["_next_generation"](*args)

    def random_batch_cost(self, uniforms, supply, demand, cost, n, out):
        return self._table()["_random_batch_cost"](uniforms, supply, demand, cost, n, out)

    def shuffle(self, perm, uniforms):
        self._table()["_shuffle"](perm, uniforms)
