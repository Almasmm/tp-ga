"""Second-review FCTP population controls."""

import time

import numpy as np
from numba import njit

from tpga import _xkernels
from tpga._kernels import _order_crossover, _two_positions
from tpga.cycle import _work, run_ga_x
from tpga.experiments.v3 import core
from tpga.fctp import FixedChargeProblem
from tpga.localsearch import _Search

_kernels = _xkernels.table()
_adjacency = _kernels["_adjacency"]
_complete_basis = _kernels["_complete_basis"]
_decode_arcs = _kernels["_decode_arcs"]
_encode = _kernels["_encode"]
_nonbasic = _kernels["_nonbasic"]
_path_apply = _kernels["_path_apply"]
_path_theta = _kernels["_path_theta"]
_plan_cost = _kernels["_plan_cost"]
_tree_path = _kernels["_tree_path"]


@njit(cache=True)
def pivot(arcs, flows, m, n, draw, iw):
    size = m + n - 1
    sorted_basis = np.sort(arcs[:size])
    entering = _nonbasic(sorted_basis, size, int(draw * (m * n - size)))
    _adjacency(arcs, size, m, n, iw[3], iw[4], iw[5], iw[6])
    _tree_path(entering, m, n, iw[3], iw[4], iw[5], iw[6], iw[7], iw[8])
    theta, leaving = _path_theta(entering, m, n, flows, iw[6], iw[7])
    _path_apply(entering, m, n, arcs, flows, iw[6], iw[7], theta, leaving)
    return theta


@njit(cache=True)
def tournament(values, d1, d2):
    a, b = int(d1 * values.size), int(d2 * values.size)
    return a if values[a] <= values[b] else b


@njit(cache=True)
def advance(arcs, flows, fit, supply, demand, cost, fixed, eps, draws, assignments, ox_rate, work):
    m, n = supply.size, demand.size
    size = m + n - 1
    a, b, candidate_flows, iw, in_basis = work
    candidate = iw[0]
    left = np.arange(m * n)
    right = left.copy()
    child = left.copy()
    kept = np.zeros(m * n, dtype=np.bool_)
    zero = accepted = crossed = 0
    for index in range(draws.shape[0]):
        u = draws[index]
        parent = assignments[index]
        if parent < 0:
            parent = tournament(fit, u[0], u[1])
        if ox_rate > 0 and u[2] < ox_rate:
            other = tournament(fit, u[3], u[4])
            for pos in range(m * n):
                left[pos] = pos
                right[pos] = pos
            _encode(left, arcs[parent], size, m, n, iw[9], iw[1], iw[8], in_basis)
            _encode(right, arcs[other], size, m, n, iw[9], iw[1], iw[8], in_basis)
            i, j = _two_positions(u[5], u[6], m * n)
            _order_crossover(left, right, i, j, child, kept)
            used = _decode_arcs(child, supply, demand, n, eps, a, b, candidate, candidate_flows)
            _complete_basis(candidate, candidate_flows, used, m, n, iw[1])
            crossed += 1
        else:
            candidate[:size] = arcs[parent]
            candidate_flows[:size] = flows[parent]
        zero += pivot(candidate, candidate_flows, m, n, u[7], iw) <= eps
        value = _plan_cost(candidate, candidate_flows, size, cost, fixed, eps)
        if value <= fit[parent] + 1e-9 * max(1.0, abs(fit[parent])):
            fit[parent] = value
            arcs[parent] = candidate[:size]
            flows[parent] = candidate_flows[:size]
            accepted += 1
    return zero, accepted, crossed


def run(task):
    fcp = FixedChargeProblem.from_json(task["path"])
    t0 = time.perf_counter()
    budget = task["budget"]
    kind = task["kind"]
    if kind == "gax":
        result = run_ga_x(fcp.problem, core._gax_config(task), fcp.fixed, fcp.linearised(), fill_budget=True)
        core._feasible(fcp.problem, result.x, task["method"])
        return {
            **core._run_fields(result),
            "cost": result.cost,
            "start_cost": result.history[0],
            "evaluation_unit": "decoder",
        }
    search = _Search(fcp, task["decoder_tol"], "numba")
    p = fcp.problem
    m, n = p.shape
    size = m + n - 1
    rng = np.random.default_rng(task["seed"])
    count = task["population"]
    arc_rows = np.tile(search.arcs_row[0, :size], (count, 1))
    flow_rows = np.tile(search.flows[:size], (count, 1))
    fit = np.empty(count)
    fit[0] = search.current
    for slot in range(1, count):
        for draw in rng.random(4):
            pivot(arc_rows[slot], flow_rows[slot], m, n, draw, search.arcs_row)
        fit[slot] = _plan_cost(arc_rows[slot], flow_rows[slot], size, search.cost, search.fixed, search.eps)
    initial = float(fit.min())
    if kind == "independent":
        allocations = np.full(count, budget // count - 1, dtype=np.int64)
        allocations[: budget % count] += 1
        assignments = np.repeat(np.arange(count), allocations)
    else:
        assignments = np.full(budget - count, -1, dtype=np.int64)
    work = _work(m, n, m * n)
    zero = accepted = crossed = 0
    for start in range(0, assignments.size, 8192):
        batch = assignments[start : start + 8192]
        z, a, c = advance(
            arc_rows,
            flow_rows,
            fit,
            p.supply,
            p.demand,
            search.cost,
            search.fixed,
            search.eps,
            rng.random((batch.size, 8)),
            batch,
            task["ox_rate"],
            work,
        )
        zero += z
        accepted += a
        crossed += c
    slot = int(np.argmin(fit))
    plan = search.plan((arc_rows[slot], flow_rows[slot], arc_rows[slot]))
    core._feasible(p, plan, task["method"])
    cost = fcp.total_cost(plan)
    if not np.isclose(cost, fit[slot], rtol=1e-10, atol=1e-9):
        raise RuntimeError("objective mismatch")
    return {
        "cost": cost,
        "start_cost": initial,
        "evals": count + assignments.size,
        "pivots": assignments.size,
        "zero_pivots": zero,
        "accepted": accepted,
        "crossovers": crossed,
        "evaluation_unit": "complete objective",
        "time_s": time.perf_counter() - t0,
    }
