"""Kernels of the cycle mutation and of the fixed-charge objective (amendment 8 of the v0.4 plan).

They are separate from :mod:`tpga._kernels`: nothing here is called by the operators of v0.3.0 and v0.4, so
those give the same results as before. Every kernel is written once as plain Python (``*_py``) and compiled
with numba on first use; the tests run both and require identical results. Randomness enters only through
arrays of uniform numbers.

Notation: arc ``k`` is ``(k // n, k % n)``; the graph has the sources as nodes ``0 .. m-1`` and the
destinations as nodes ``m .. m+n-1``; a basis is a spanning tree with ``m + n - 1`` arcs held in the slots
``0 .. m+n-2`` of ``arcs`` (arc index) and ``flows`` (amount, zero on degenerate arcs).

The integer work matrix ``iw`` has at least 10 rows and ``2 (m + n) + 2`` columns; its rows are used as
``arcs, parent, sorted, off, adj_node, adj_slot, par_node, par_slot, queue, deg`` (``xr`` shares the row of
``parent``, which is free when the leaves are eliminated).
"""

from __future__ import annotations

import math
from typing import Any

import numpy as np
from numba import njit

IW_ROWS = 10


def iw_columns(m: int, n: int) -> int:
    return 2 * (m + n) + 2


def _decode_cost_fc_py(perm, supply, demand, cost, fixed, n, eps):
    """Cost of the decoded plan with a fixed charge ``fixed[k]`` on every arc that carries flow.

    The same loop as ``tpga._kernels._decode_cost``; with ``fixed = 0`` the value is bit for bit the same.
    """
    a = supply.copy()
    b = demand.copy()
    active = 0
    for i in range(a.size):
        if a[i] > eps:
            active += 1
    total = 0.0
    for t in range(perm.size):
        if active == 0:
            break
        k = perm[t]
        i = k // n
        j = k - i * n
        q = min(a[i], b[j])
        if q > eps:
            total += cost[k] * q
            total += fixed[k]
            a[i] -= q
            b[j] -= q
            if a[i] <= eps:
                active -= 1
    return total


def _decode_arcs_py(perm, supply, demand, n, eps, a, b, arcs, flows):
    """Greedy decoder that lists the positive arcs and their amounts in decoding order; returns their number.

    ``a`` and ``b`` are scratch arrays of the sizes of ``supply`` and ``demand``.
    """
    active = 0
    for i in range(supply.size):
        a[i] = supply[i]
        if a[i] > eps:
            active += 1
    for j in range(demand.size):
        b[j] = demand[j]
    count = 0
    for t in range(perm.size):
        if active == 0:
            break
        k = perm[t]
        i = k // n
        j = k - i * n
        q = min(a[i], b[j])
        if q > eps:
            arcs[count] = k
            flows[count] = q
            count += 1
            a[i] -= q
            b[j] -= q
            if a[i] <= eps:
                active -= 1
    return count


def _find_py(parent, v):
    while parent[v] != v:
        parent[v] = parent[parent[v]]
        v = parent[v]
    return v


def _complete_basis_py(arcs, flows, count, m, n, parent):
    """Complete a forest of ``count`` arcs to a spanning tree: zero arcs in index order that join components."""
    size = m + n - 1
    if count >= size:
        return count
    for v in range(m + n):
        parent[v] = v
    for e in range(count):
        k = arcs[e]
        i = k // n
        j = k - i * n
        ra = _find(parent, i)
        rb = _find(parent, m + j)
        parent[ra] = rb
    for k in range(m * n):
        if count >= size:
            break
        i = k // n
        j = k - i * n
        ra = _find(parent, i)
        rb = _find(parent, m + j)
        if ra != rb:
            parent[ra] = rb
            arcs[count] = k
            flows[count] = 0.0
            count += 1
    return count


def _nonbasic_py(sorted_basis, size, r):
    """The ``r``-th arc (from 0) that is not in the sorted list of basic arcs."""
    arc = r
    for t in range(size):
        if sorted_basis[t] <= arc:
            arc += 1
        else:
            break
    return arc


def _replace_sorted_py(sorted_basis, size, old, new):
    """Replace ``old`` by ``new`` in the sorted list of basic arcs, keeping it sorted."""
    t = 0
    while sorted_basis[t] != old:
        t += 1
    if new > old:
        while t + 1 < size and sorted_basis[t + 1] < new:
            sorted_basis[t] = sorted_basis[t + 1]
            t += 1
    else:
        while t > 0 and sorted_basis[t - 1] > new:
            sorted_basis[t] = sorted_basis[t - 1]
            t -= 1
    sorted_basis[t] = new


def _adjacency_py(arcs, size, m, n, off, adj_node, adj_slot, cursor):
    """Adjacency lists of the tree (compressed rows): neighbours of ``v`` are ``adj_node[off[v]:off[v+1]]``."""
    nodes = m + n
    for v in range(nodes + 1):
        off[v] = 0
    for s in range(size):
        k = arcs[s]
        i = k // n
        j = k - i * n
        off[i + 1] += 1
        off[m + j + 1] += 1
    for v in range(nodes):
        off[v + 1] += off[v]
    for v in range(nodes):
        cursor[v] = off[v]
    for s in range(size):
        k = arcs[s]
        i = k // n
        j = k - i * n
        c = cursor[i]
        adj_node[c] = m + j
        adj_slot[c] = s
        cursor[i] = c + 1
        c = cursor[m + j]
        adj_node[c] = i
        adj_slot[c] = s
        cursor[m + j] = c + 1


def _tree_path_py(entering, m, n, off, adj_node, adj_slot, par_node, par_slot, queue):
    """Breadth-first search from the source of ``entering`` to its destination; fills the parent arrays."""
    nodes = m + n
    i0 = entering // n
    target = m + entering - i0 * n
    for v in range(nodes):
        par_node[v] = -1
        par_slot[v] = -1
    par_node[i0] = i0
    head = 0
    tail = 1
    queue[0] = i0
    while head < tail:
        v = queue[head]
        head += 1
        if v == target:
            break
        for c in range(off[v], off[v + 1]):
            w = adj_node[c]
            if par_node[w] < 0:
                par_node[w] = v
                par_slot[w] = adj_slot[c]
                queue[tail] = w
                tail += 1


def _path_theta_py(entering, m, n, flows, par_node, par_slot):
    """(theta, leaving slot): the smallest flow on the minus arcs of the cycle and the first arc that has it.

    The path is walked from the destination of the entering arc; its arcs at even positions are the minus
    arcs (the first one shares the destination with the entering arc, the last one its source).
    """
    i0 = entering // n
    v = m + entering - i0 * n
    theta = np.inf
    leaving = -1
    pos = 0
    while v != i0:
        s = par_slot[v]
        if pos % 2 == 0 and flows[s] < theta:
            theta = flows[s]
            leaving = s
        v = par_node[v]
        pos += 1
    return theta, leaving


def _path_delta_py(entering, m, n, arcs, flows, cost, fixed, par_node, par_slot, theta, eps):
    """Change of the cost (with fixed charges) if ``theta`` is moved along the cycle of ``entering``."""
    if theta <= eps:
        return 0.0
    delta = cost[entering] * theta + fixed[entering]
    i0 = entering // n
    v = m + entering - i0 * n
    pos = 0
    while v != i0:
        s = par_slot[v]
        k = arcs[s]
        if pos % 2 == 0:
            delta -= cost[k] * theta
            if flows[s] > eps and flows[s] - theta <= eps:
                delta -= fixed[k]
        else:
            delta += cost[k] * theta
            if flows[s] <= eps:
                delta += fixed[k]
        v = par_node[v]
        pos += 1
    return delta


def _path_apply_py(entering, m, n, arcs, flows, par_node, par_slot, theta, leaving):
    """Move ``theta`` along the cycle; the entering arc takes the slot of the leaving arc. Returns the old arc."""
    i0 = entering // n
    v = m + entering - i0 * n
    pos = 0
    while v != i0:
        s = par_slot[v]
        if pos % 2 == 0:
            flows[s] -= theta
        else:
            flows[s] += theta
        v = par_node[v]
        pos += 1
    old = arcs[leaving]
    arcs[leaving] = entering
    flows[leaving] = theta
    return old


def _encode_py(perm, arcs, size, m, n, deg, xr, queue, in_basis):
    """Rewrite ``perm`` in place: the tree arcs in the order of leaf elimination, then the other arcs in the
    relative order they had. ``in_basis`` is all False on entry and on exit. Returns the number of tree arcs
    written (``size`` for a spanning tree).
    """
    nodes = m + n
    length = perm.size
    for s in range(size):
        in_basis[arcs[s]] = True
    w = length - 1
    for t in range(length - 1, -1, -1):
        g = perm[t]
        if not in_basis[g]:
            perm[w] = g
            w -= 1
    for v in range(nodes):
        deg[v] = 0
        xr[v] = 0
    for s in range(size):
        k = arcs[s]
        i = k // n
        j = k - i * n
        deg[i] += 1
        xr[i] ^= s
        deg[m + j] += 1
        xr[m + j] ^= s
    head = 0
    tail = 0
    for v in range(nodes):
        if deg[v] == 1:
            queue[tail] = v
            tail += 1
    pos = 0
    while head < tail:
        v = queue[head]
        head += 1
        if deg[v] != 1:
            continue
        s = xr[v]
        k = arcs[s]
        i = k // n
        j = k - i * n
        perm[pos] = k
        pos += 1
        other = m + j if v == i else i
        deg[v] = 0
        deg[other] -= 1
        xr[other] ^= s
        if deg[other] == 1:
            queue[tail] = other
            tail += 1
    for s in range(size):
        in_basis[arcs[s]] = False
    return pos


def _plan_cost_py(arcs, flows, size, cost, fixed, eps):
    total = 0.0
    for s in range(size):
        if flows[s] > eps:
            total += cost[arcs[s]] * flows[s]
            total += fixed[arcs[s]]
    return total


def _cycle_mutation_py(child, supply, demand, cost, fixed, n, eps, pivots, pivot_u, u_off, a, b, flows, iw, in_basis):
    """Cycle mutation of ``child`` in place. Returns (cost of the new plan, pivots done, pivots with theta = 0).

    ``pivot_u[u_off + p]`` chooses the entering arc of pivot ``p`` uniformly among the non-basic arcs.
    """
    m = supply.size
    size = m + n - 1
    arcs = iw[0]
    count = _decode_arcs(child, supply, demand, n, eps, a, b, arcs, flows)
    _complete_basis(arcs, flows, count, m, n, iw[1])
    nonbasic = m * n - size
    done = 0
    zero = 0
    if nonbasic > 0 and pivots > 0:
        sorted_basis = iw[2]
        for s in range(size):
            sorted_basis[s] = arcs[s]
        sorted_basis[:size].sort()
        for p in range(pivots):
            r = min(int(pivot_u[u_off + p] * nonbasic), nonbasic - 1)
            entering = _nonbasic(sorted_basis, size, r)
            _adjacency(arcs, size, m, n, iw[3], iw[4], iw[5], iw[6])
            _tree_path(entering, m, n, iw[3], iw[4], iw[5], iw[6], iw[7], iw[8])
            theta, leaving = _path_theta(entering, m, n, flows, iw[6], iw[7])
            old = _path_apply(entering, m, n, arcs, flows, iw[6], iw[7], theta, leaving)
            _replace_sorted(sorted_basis, size, old, entering)
            done += 1
            if theta <= eps:
                zero += 1
    _encode(child, arcs, size, m, n, iw[9], iw[1], iw[8], in_basis)
    return _plan_cost(arcs, flows, size, cost, fixed, eps), done, zero


def _first_improvement_py(perm, supply, demand, cost, fixed, n, eps, start_u, max_evals, a, b, flows, iw, in_basis):
    """One step of the pivot local search on ``perm`` (in place).

    The permutation is decoded (one evaluation). Its non-basic arcs are scanned in index order from a random
    start; every neighbour (one pivot) is one evaluation; the first neighbour with a strictly smaller cost is
    applied and encoded. Returns (evaluations used, 1 if improved else 0, cost of the plan afterwards).
    """
    m = supply.size
    size = m + n - 1
    arcs = iw[0]
    count = _decode_arcs(perm, supply, demand, n, eps, a, b, arcs, flows)
    _complete_basis(arcs, flows, count, m, n, iw[1])
    current = _plan_cost(arcs, flows, size, cost, fixed, eps)
    evals = 1
    nonbasic = m * n - size
    if nonbasic <= 0:
        return evals, 0, current
    sorted_basis = iw[2]
    for s in range(size):
        sorted_basis[s] = arcs[s]
    sorted_basis[:size].sort()
    _adjacency(arcs, size, m, n, iw[3], iw[4], iw[5], iw[6])
    start = min(int(start_u * nonbasic), nonbasic - 1)
    tol = 1e-9 * max(1.0, abs(current))
    for q in range(nonbasic):
        if evals >= max_evals:
            break
        r = start + q
        if r >= nonbasic:
            r -= nonbasic
        entering = _nonbasic(sorted_basis, size, r)
        _tree_path(entering, m, n, iw[3], iw[4], iw[5], iw[6], iw[7], iw[8])
        theta, leaving = _path_theta(entering, m, n, flows, iw[6], iw[7])
        delta = _path_delta(entering, m, n, arcs, flows, cost, fixed, iw[6], iw[7], theta, eps)
        evals += 1
        if delta < -tol:
            _path_apply(entering, m, n, arcs, flows, iw[6], iw[7], theta, leaving)
            _encode(perm, arcs, size, m, n, iw[9], iw[1], iw[8], in_basis)
            return evals, 1, _plan_cost(arcs, flows, size, cost, fixed, eps)
    return evals, 0, current


def _next_generation_x_py(
    pop,
    fit,
    order,
    elite,
    uniforms,
    tournament,
    crossover_rate,
    supply,
    demand,
    cost,
    fixed,
    n,
    eps,
    new_pop,
    new_fit,
    scratch,
    kept,
    cycle,
    counts,
    offsets,
    extra_u,
    stats,
):
    """One generation with the fixed-charge cost. Selection and crossover are those of ``_next_generation``
    (same columns of ``uniforms``). ``cycle = 0``: offspring ``c`` gets ``counts[c]`` swaps of two positions,
    swap ``s`` from ``extra_u[offsets[c] + 2 s]`` and the next number, and one decoding. ``cycle = 1``: cycle
    mutation with ``counts[c]`` pivots from ``extra_u[offsets[c] + p]`` (``cycle = 2``: with the rule
    ``nondegenerate``, and ``stats[3]`` counts the pivots left to the uniform rule). ``stats`` accumulates the
    pivots, the pivots with theta = 0 and the offspring whose pivots all had theta = 0. Returns the decoder
    calls.
    """
    size, length = pop.shape
    m = supply.size
    a = np.empty(m)
    b = np.empty(demand.size)
    flows = np.empty(m + n)
    iw = np.empty((10, 2 * (m + n) + 2), dtype=np.int64)
    in_basis = np.zeros(length, dtype=np.bool_)
    for e in range(elite):
        src = order[e]
        new_pop[e, :] = pop[src, :]
        new_fit[e] = fit[src]
    for c in range(size - elite):
        u = uniforms[c]
        pa = _tournament(fit, u[0:tournament], scratch)
        pb = _tournament(fit, u[tournament : 2 * tournament], scratch)
        child = new_pop[elite + c]
        base = 2 * tournament
        if u[base] < crossover_rate and length >= 2:
            i, j = _two_positions(u[base + 1], u[base + 2], length)
            _order_crossover(pop[pa], pop[pb], i, j, child, kept)
        else:
            child[:] = pop[pa, :]
        if cycle == 1:
            total, done, zero = _cycle_mutation(
                child, supply, demand, cost, fixed, n, eps, counts[c], extra_u, offsets[c], a, b, flows, iw, in_basis
            )
            new_fit[elite + c] = total
            stats[0] += done
            stats[1] += zero
            if done > 0 and zero == done:
                stats[2] += 1
        elif cycle == 2:  # the rule ``nondegenerate`` for the entering arc (amendment 10.5)
            total, done, zero, fallback = _cycle_mutation_nd(
                child, supply, demand, cost, fixed, n, eps, counts[c], extra_u, offsets[c], a, b, flows, iw, in_basis
            )
            new_fit[elite + c] = total
            stats[0] += done
            stats[1] += zero
            if done > 0 and zero == done:
                stats[2] += 1
            stats[3] += fallback
        else:
            if length >= 2:
                off = offsets[c]
                for s in range(counts[c]):
                    i, j = _two_positions(extra_u[off + 2 * s], extra_u[off + 2 * s + 1], length)
                    tmp = child[i]
                    child[i] = child[j]
                    child[j] = tmp
            new_fit[elite + c] = _decode_cost_fc(child, supply, demand, cost, fixed, n, eps)
    return size - elite


def _random_batch_cost_fc_py(uniforms, supply, demand, cost, fixed, n, eps, out):
    """``tpga._kernels._random_batch_cost`` with the fixed-charge cost."""
    length = cost.size
    perm = np.empty(length, dtype=np.int64)
    best = -1
    for r in range(out.size):
        for t in range(length):
            perm[t] = t
        _shuffle(perm, uniforms[r])
        out[r] = _decode_cost_fc(perm, supply, demand, cost, fixed, n, eps)
        if best < 0 or out[r] < out[best]:
            best = r
    return best


def _anneal_fc_py(
    perm,
    current,
    best_perm,
    best,
    uniforms,
    temperature,
    alpha,
    insertion_probability,
    supply,
    demand,
    cost,
    fixed,
    n,
    eps,
    evaluations,
    best_evaluation,
    imp_evals,
    imp_costs,
):
    """``tpga.sa._anneal`` with the fixed-charge cost (budget-only stop)."""
    length = perm.size
    n_imp = 0
    for s in range(uniforms.shape[0]):
        u = uniforms[s]
        kind, i, j = _move_from_uniforms(u[0], u[1], u[2], length, insertion_probability)
        _apply_move(perm, kind, i, j)
        value = _decode_cost_fc(perm, supply, demand, cost, fixed, n, eps)
        evaluations += 1
        delta = value - current
        if delta <= 0 or u[3] < math.exp(-delta / temperature):
            current = value
            if value < best:
                best = value
                best_evaluation = evaluations
                best_perm[:] = perm
                imp_evals[n_imp] = evaluations
                imp_costs[n_imp] = value
                n_imp += 1
        else:
            _undo_move(perm, kind, i, j)
        temperature *= alpha
    return current, best, temperature, evaluations, best_evaluation, n_imp


# --- amendment 10: second rule for the entering arc, tabu search and iterated local search ------


def _nd_search_py(i0, m, nodes, flows, eps, off, adj_node, adj_slot, depth, queue):
    """Search of the tree from source ``i0`` that never crosses an arc with zero flow from its source to its
    destination (the minus positions of the cycles that start at ``i0``). Fills ``depth`` (-1: not reached)
    and returns the number of destinations reached at depth 3 or more: each closes a cycle with theta > 0."""
    for v in range(nodes):
        depth[v] = -1
    depth[i0] = 0
    queue[0] = i0
    head = 0
    tail = 1
    count = 0
    while head < tail:
        v = queue[head]
        head += 1
        for c in range(off[v], off[v + 1]):
            w = adj_node[c]
            if depth[w] >= 0:
                continue
            if v < m and flows[adj_slot[c]] <= eps:
                continue
            depth[w] = depth[v] + 1
            queue[tail] = w
            tail += 1
            if w >= m and depth[w] >= 3:
                count += 1
    return count


def _nd_entering_py(u, m, n, flows, eps, off, adj_node, adj_slot, depth, queue, cnt):
    """Entering arc of the rule ``nondegenerate``: the ``floor(u A)``-th, in index order, of the ``A``
    non-basic arcs whose cycle has no arc with zero flow on a minus position; -1 when there is none."""
    nodes = m + n
    total = 0
    for i0 in range(m):
        cnt[i0] = _nd_search(i0, m, nodes, flows, eps, off, adj_node, adj_slot, depth, queue)
        total += cnt[i0]
    if total == 0:
        return -1
    r = min(int(u * total), total - 1)
    i0 = 0
    while r >= cnt[i0]:
        r -= cnt[i0]
        i0 += 1
    _nd_search(i0, m, nodes, flows, eps, off, adj_node, adj_slot, depth, queue)
    for j in range(n):
        if depth[m + j] >= 3:
            if r == 0:
                return i0 * n + j
            r -= 1
    return -1


def _cycle_mutation_nd_py(
    child, supply, demand, cost, fixed, n, eps, pivots, pivot_u, u_off, a, b, flows, iw, in_basis
):
    """``_cycle_mutation`` with the rule ``nondegenerate`` for the entering arc; the same uniform number is
    used when the rule finds no arc and the uniform choice among all non-basic arcs takes over. Returns
    (cost, pivots done, pivots with theta = 0, pivots chosen by the uniform rule)."""
    m = supply.size
    size = m + n - 1
    arcs = iw[0]
    count = _decode_arcs(child, supply, demand, n, eps, a, b, arcs, flows)
    _complete_basis(arcs, flows, count, m, n, iw[1])
    nonbasic = m * n - size
    done = 0
    zero = 0
    fallback = 0
    if nonbasic > 0 and pivots > 0:
        sorted_basis = iw[2]
        for s in range(size):
            sorted_basis[s] = arcs[s]
        sorted_basis[:size].sort()
        for p in range(pivots):
            _adjacency(arcs, size, m, n, iw[3], iw[4], iw[5], iw[6])
            entering = _nd_entering(pivot_u[u_off + p], m, n, flows, eps, iw[3], iw[4], iw[5], iw[6], iw[8], iw[9])
            if entering < 0:
                r = min(int(pivot_u[u_off + p] * nonbasic), nonbasic - 1)
                entering = _nonbasic(sorted_basis, size, r)
                fallback += 1
            _tree_path(entering, m, n, iw[3], iw[4], iw[5], iw[6], iw[7], iw[8])
            theta, leaving = _path_theta(entering, m, n, flows, iw[6], iw[7])
            old = _path_apply(entering, m, n, arcs, flows, iw[6], iw[7], theta, leaving)
            _replace_sorted(sorted_basis, size, old, entering)
            done += 1
            if theta <= eps:
                zero += 1
    _encode(child, arcs, size, m, n, iw[9], iw[1], iw[8], in_basis)
    return _plan_cost(arcs, flows, size, cost, fixed, eps), done, zero, fallback


def _tabu_iteration_py(
    arcs,
    flows,
    m,
    n,
    cost,
    fixed,
    eps,
    current,
    best,
    sample_u,
    n_sample,
    start_u,
    expiry,
    iteration,
    tenure,
    max_evals,
    iw,
):
    """One iteration of the tabu search over pivots on the basis ``arcs``/``flows`` (``iw[2]`` holds the
    sorted basic arcs). ``n_sample = 0``: every non-basic arc is a candidate, in index order from a random
    start; otherwise ``n_sample`` candidates are drawn by ``sample_u``. A candidate is tabu while
    ``expiry`` of its entering or leaving arc is above ``iteration``, unless it gives a cost below ``best``.
    The admitted candidate with the smallest change is applied. Returns (neighbour evaluations, cost after
    the iteration, 1 if a move was made)."""
    size = m + n - 1
    nonbasic = m * n - size
    sorted_basis = iw[2]
    _adjacency(arcs, size, m, n, iw[3], iw[4], iw[5], iw[6])
    count = nonbasic if n_sample == 0 else n_sample
    start = min(int(start_u * nonbasic), nonbasic - 1)
    tol = 1e-9 * max(1.0, abs(best))
    best_delta = np.inf
    chosen = -1
    evals = 0
    for q in range(count):
        if evals >= max_evals:
            break
        if n_sample == 0:
            r = start + q
            if r >= nonbasic:
                r -= nonbasic
        else:
            r = min(int(sample_u[q] * nonbasic), nonbasic - 1)
        entering = _nonbasic(sorted_basis, size, r)
        _tree_path(entering, m, n, iw[3], iw[4], iw[5], iw[6], iw[7], iw[8])
        theta, leaving = _path_theta(entering, m, n, flows, iw[6], iw[7])
        delta = _path_delta(entering, m, n, arcs, flows, cost, fixed, iw[6], iw[7], theta, eps)
        evals += 1
        tabu = expiry[entering] > iteration or expiry[arcs[leaving]] > iteration
        if tabu and not current + delta < best - tol:
            continue
        if delta < best_delta:
            best_delta = delta
            chosen = entering
    if chosen < 0:
        return evals, current, 0
    _tree_path(chosen, m, n, iw[3], iw[4], iw[5], iw[6], iw[7], iw[8])
    theta, leaving = _path_theta(chosen, m, n, flows, iw[6], iw[7])
    old = _path_apply(chosen, m, n, arcs, flows, iw[6], iw[7], theta, leaving)
    _replace_sorted(sorted_basis, size, old, chosen)
    expiry[chosen] = iteration + tenure + 1
    expiry[old] = iteration + tenure + 1
    return evals, current + best_delta, 1


def _descent_py(arcs, flows, m, n, cost, fixed, eps, current, start_u, max_evals, iw):
    """First-improvement descent over pivots: the non-basic arcs are scanned cyclically from a random
    position, an improving pivot is applied at once, and the descent ends after a full round without an
    improvement or with the budget. Returns (neighbour evaluations, cost)."""
    size = m + n - 1
    nonbasic = m * n - size
    if nonbasic <= 0:
        return 0, current
    sorted_basis = iw[2]
    _adjacency(arcs, size, m, n, iw[3], iw[4], iw[5], iw[6])
    r = min(int(start_u * nonbasic), nonbasic - 1)
    since = 0
    evals = 0
    while since < nonbasic and evals < max_evals:
        entering = _nonbasic(sorted_basis, size, r)
        _tree_path(entering, m, n, iw[3], iw[4], iw[5], iw[6], iw[7], iw[8])
        theta, leaving = _path_theta(entering, m, n, flows, iw[6], iw[7])
        delta = _path_delta(entering, m, n, arcs, flows, cost, fixed, iw[6], iw[7], theta, eps)
        evals += 1
        if delta < -1e-9 * max(1.0, abs(current)):
            old = _path_apply(entering, m, n, arcs, flows, iw[6], iw[7], theta, leaving)
            _replace_sorted(sorted_basis, size, old, entering)
            _adjacency(arcs, size, m, n, iw[3], iw[4], iw[5], iw[6])
            current += delta
            since = 0
        else:
            since += 1
        r += 1
        if r >= nonbasic:
            r = 0
    return evals, current


def _perturb_py(arcs, flows, m, n, cost, fixed, eps, current, pivot_u, count, iw):
    """``count`` pivots with entering arcs drawn uniformly among the non-basic arcs; returns the new cost."""
    size = m + n - 1
    nonbasic = m * n - size
    sorted_basis = iw[2]
    for p in range(count):
        r = min(int(pivot_u[p] * nonbasic), nonbasic - 1)
        entering = _nonbasic(sorted_basis, size, r)
        _adjacency(arcs, size, m, n, iw[3], iw[4], iw[5], iw[6])
        _tree_path(entering, m, n, iw[3], iw[4], iw[5], iw[6], iw[7], iw[8])
        theta, leaving = _path_theta(entering, m, n, flows, iw[6], iw[7])
        current += _path_delta(entering, m, n, arcs, flows, cost, fixed, iw[6], iw[7], theta, eps)
        old = _path_apply(entering, m, n, arcs, flows, iw[6], iw[7], theta, leaving)
        _replace_sorted(sorted_basis, size, old, entering)
    return current


# --- engine tables -------------------------------------------------------------------------
# The plain functions call each other through the module-level names below, which ``table`` binds to the
# compiled kernels (engine "numba") or to the plain ones (engine "python", for the tests).

_PLAIN = {
    "_decode_cost_fc": _decode_cost_fc_py,
    "_decode_arcs": _decode_arcs_py,
    "_find": _find_py,
    "_complete_basis": _complete_basis_py,
    "_nonbasic": _nonbasic_py,
    "_replace_sorted": _replace_sorted_py,
    "_adjacency": _adjacency_py,
    "_tree_path": _tree_path_py,
    "_path_theta": _path_theta_py,
    "_path_delta": _path_delta_py,
    "_path_apply": _path_apply_py,
    "_encode": _encode_py,
    "_plan_cost": _plan_cost_py,
    "_cycle_mutation": _cycle_mutation_py,
    "_first_improvement": _first_improvement_py,
    "_next_generation_x": _next_generation_x_py,
    "_random_batch_cost_fc": _random_batch_cost_fc_py,
    "_anneal_fc": _anneal_fc_py,
    "_nd_search": _nd_search_py,
    "_nd_entering": _nd_entering_py,
    "_cycle_mutation_nd": _cycle_mutation_nd_py,
    "_tabu_iteration": _tabu_iteration_py,
    "_descent": _descent_py,
    "_perturb": _perturb_py,
}
_COMPILED: dict = {}
_BORROWED = ("_tournament", "_two_positions", "_order_crossover", "_shuffle")
_BORROWED_SA = ("_move_from_uniforms", "_apply_move", "_undo_move")

_decode_cost_fc = _decode_cost_fc_py
_decode_arcs = _decode_arcs_py
_find = _find_py
_complete_basis = _complete_basis_py
_nonbasic = _nonbasic_py
_replace_sorted = _replace_sorted_py
_adjacency = _adjacency_py
_tree_path = _tree_path_py
_path_theta = _path_theta_py
_path_delta = _path_delta_py
_path_apply = _path_apply_py
_encode = _encode_py
_plan_cost = _plan_cost_py
_cycle_mutation = _cycle_mutation_py
_first_improvement = _first_improvement_py
_next_generation_x = _next_generation_x_py
_random_batch_cost_fc = _random_batch_cost_fc_py
_anneal_fc = _anneal_fc_py
_nd_search = _nd_search_py
_nd_entering = _nd_entering_py
_cycle_mutation_nd = _cycle_mutation_nd_py
_tabu_iteration = _tabu_iteration_py
_descent = _descent_py
_perturb = _perturb_py
_tournament: Any = None
_two_positions: Any = None
_order_crossover: Any = None
_shuffle: Any = None
_move_from_uniforms: Any = None
_apply_move: Any = None
_undo_move: Any = None


def table(engine: str = "numba") -> dict:
    """Bind the module-level names to one implementation and return its kernels by name."""
    if engine not in ("numba", "python"):
        raise ValueError("engine must be numba or python")
    from tpga import _kernels, sa

    g = globals()
    if engine == "python":
        for name in _BORROWED:
            g[name] = _kernels._PLAIN[name]
        for name in _BORROWED_SA:
            g[name] = sa._PLAIN[name]
        g.update(_PLAIN)
        return _PLAIN
    for name in _BORROWED:
        g[name] = _kernels._COMPILED[name]
    compiled_sa = sa._compiled()
    for name in _BORROWED_SA:
        g[name] = compiled_sa[name]
    if not _COMPILED:
        for name, fn in _PLAIN.items():
            _COMPILED[name] = njit(cache=True)(fn)
    g.update(_COMPILED)
    return _COMPILED
