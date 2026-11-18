"""Fixed-charge transportation problem (FCTP): model, generator, reference solvers and decoder heuristics.

Minimise ``sum c_ij x_ij + sum f_ij [x_ij > 0]`` over the plans of a balanced transportation problem. The
linear-programming optimum of the classical model is not an optimum here; the exact reference is a mixed
integer program (:func:`solve_mip`). The decoder heuristics (random search, simulated annealing and
:func:`tpga.cycle.run_ga_x`) evaluate the true cost of the decoded plan, so they need no change of the
encoding. With all fixed charges zero :func:`run_random_search_fc` and :func:`run_sa_fc` reproduce
:func:`tpga.ga.run_random_search` and :func:`tpga.sa.run_sa` exactly.
"""

from __future__ import annotations

import json
import math
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
from numpy.typing import ArrayLike

from tpga import _xkernels
from tpga.classical import vogel
from tpga.cycle import _fixed_array
from tpga.decoder import DECODER_TOL, decoder_eps
from tpga.ga import GAResult, ProgressCallback, _arrays
from tpga.model import FloatArray, TransportProblem
from tpga.sa import SAConfig


@dataclass(frozen=True)
class FixedChargeProblem:
    """A balanced transportation problem with a fixed charge ``fixed[i, j]`` on every arc that carries flow."""

    problem: TransportProblem
    fixed: FloatArray

    def __init__(self, problem: TransportProblem, fixed: ArrayLike) -> None:
        if not problem.is_balanced:
            raise ValueError("the fixed-charge problem must be balanced")
        f = np.asarray(fixed, dtype=float)
        if f.shape != problem.cost.shape:
            raise ValueError("fixed charges must have the shape of the cost matrix")
        if (f < 0).any() or not np.isfinite(f).all():
            raise ValueError("fixed charges must be finite and nonnegative")
        object.__setattr__(self, "problem", problem)
        object.__setattr__(self, "fixed", f)

    @property
    def shape(self) -> tuple[int, int]:
        return self.problem.shape

    @property
    def big_m(self) -> FloatArray:
        """``M_ij = min(a_i, b_j)``, the largest amount arc ``(i, j)`` can carry."""
        return np.minimum.outer(self.problem.supply, self.problem.demand)

    def total_cost(self, x: ArrayLike, tol: float = DECODER_TOL) -> float:
        """True cost of a plan: variable cost plus the fixed charge of every arc with ``x_ij`` above the
        decoder threshold."""
        plan = np.asarray(x, dtype=float)
        used = plan > decoder_eps(self.problem, tol)
        return float((self.problem.cost * plan).sum() + self.fixed[used].sum())

    def linearised(self) -> TransportProblem:
        """Balinski's linear relaxation: the same problem with costs ``c_ij + f_ij / M_ij`` (arcs with
        ``M_ij = 0`` can carry nothing and keep ``c_ij``)."""
        big = self.big_m
        extra = np.divide(self.fixed, big, out=np.zeros_like(self.fixed), where=big > 0)
        return TransportProblem(self.problem.supply, self.problem.demand, self.problem.cost + extra)

    def to_dict(self) -> dict[str, list]:
        return {**self.problem.to_dict(), "fixed": self.fixed.tolist()}

    @classmethod
    def from_dict(cls, data: dict) -> FixedChargeProblem:
        if "fixed" not in data:
            raise ValueError("instance is missing the field 'fixed'")
        return cls(TransportProblem.from_dict(data), data["fixed"])

    @classmethod
    def from_json(cls, path: str | Path) -> FixedChargeProblem:
        return cls.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))


def generate(m: int, n: int, seed: int, rho: float, spec: dict[str, Any] | None = None) -> dict[str, Any]:
    """Random FCTP instance (amendment 8.4): supplies ``U{supply_low..supply_high}``, demands
    ``1 + multinomial(S - n)``, costs ``U{cost_low..cost_high}`` from ``default_rng(seed)`` exactly as
    :func:`tpga.experiments.instances.uniform_instance`; fixed charges ``U{1..F}`` from
    ``default_rng([seed, 1])`` with ``F = round(2 rho c_mean S / (m + n - 1))`` (at least 1).
    """
    from tpga.experiments.instances import uniform_instance

    s = {"cost_low": 1, "cost_high": 100, "supply_low": 20, "supply_high": 100, **(spec or {})}
    data = uniform_instance(m, n, seed, s)
    total = int(sum(data["supply"]))
    c_mean = float(np.mean(data["cost"]))
    top = max(1, int(round(2.0 * rho * c_mean * total / (m + n - 1))))
    fixed = np.random.default_rng([seed, 1]).integers(1, top + 1, size=(m, n))
    return {**data, "fixed": fixed.tolist(), "rho": rho, "fixed_high": top, "cost_mean": c_mean, "seed": seed}


@dataclass
class MIPResult:
    """Outcome of the HiGHS mixed-integer model: ``cost`` is the true cost of ``x`` recomputed from the plan,
    ``bound`` the best lower bound, ``gap`` = (cost - bound) / cost, ``proved`` True when HiGHS reports an
    optimal solution."""

    x: FloatArray | None
    cost: float | None
    objective: float | None
    bound: float
    gap: float | None
    status: str
    proved: bool
    time_s: float
    nodes: int
    version: str


def solve_mip(
    fcp: FixedChargeProblem,
    time_limit: float = 60.0,
    threads: int = 1,
    rel_gap: float = 0.0,
    abs_gap: float = 0.99,
) -> MIPResult:
    """Exact reference: ``min sum c x + sum f y``, ``x_ij <= M_ij y_ij``, ``y`` binary, supply and demand
    equalities, with HiGHS. With integer data an absolute gap below 1 proves the optimum."""
    import highspy

    p = fcp.problem
    m, n = p.shape
    arcs = m * n
    big = fcp.big_m.ravel()
    inf = highspy.kHighsInf
    h = highspy.Highs()
    h.setOptionValue("output_flag", False)
    h.setOptionValue("threads", int(threads))
    h.setOptionValue("time_limit", float(time_limit))
    h.setOptionValue("mip_rel_gap", float(rel_gap))
    h.setOptionValue("mip_abs_gap", float(abs_gap))
    lp = highspy.HighsLp()
    lp.num_col_ = 2 * arcs
    lp.num_row_ = m + n + arcs
    lp.col_cost_ = np.concatenate([p.cost.ravel(), fcp.fixed.ravel()]).astype(np.float64)
    lp.col_lower_ = np.zeros(2 * arcs)
    lp.col_upper_ = np.concatenate([big, np.ones(arcs)]).astype(np.float64)
    b = np.concatenate([p.supply, p.demand]).astype(np.float64)
    lp.row_lower_ = np.concatenate([b, np.full(arcs, -inf)])
    lp.row_upper_ = np.concatenate([b, np.zeros(arcs)])
    # column k of x: supply row, demand row, link row; column k of y: link row with -M
    start = np.concatenate([np.arange(0, 3 * arcs, 3), 3 * arcs + np.arange(arcs + 1)]).astype(np.int32)
    index = np.empty(4 * arcs, dtype=np.int32)
    value = np.empty(4 * arcs)
    k = np.arange(arcs)
    index[0 : 3 * arcs : 3] = k // n
    index[1 : 3 * arcs : 3] = m + k % n
    index[2 : 3 * arcs : 3] = m + n + k
    value[: 3 * arcs] = 1.0
    index[3 * arcs :] = m + n + k
    value[3 * arcs :] = -big
    lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
    lp.a_matrix_.num_col_ = 2 * arcs
    lp.a_matrix_.num_row_ = m + n + arcs
    lp.a_matrix_.start_ = start
    lp.a_matrix_.index_ = index
    lp.a_matrix_.value_ = value
    lp.integrality_ = [highspy.HighsVarType.kContinuous] * arcs + [highspy.HighsVarType.kInteger] * arcs
    h.passModel(lp)
    t0 = time.perf_counter()
    h.run()
    elapsed = time.perf_counter() - t0
    status = h.getModelStatus()
    info = h.getInfo()
    name = h.modelStatusToString(status)
    bound = float(info.mip_dual_bound)
    has_solution = info.primal_solution_status == highspy.SolutionStatus.kSolutionStatusFeasible
    x = cost = objective = gap = None
    if has_solution:
        x = _clean_plan(p, np.asarray(h.getSolution().col_value)[:arcs].reshape(m, n))
        objective = float(info.objective_function_value)
        cost = fcp.total_cost(x)
        if math.isfinite(bound):  # no bound yet when the limit ends the run before the root relaxation
            gap = max(0.0, (cost - bound) / cost) if cost > 0 else 0.0
    return MIPResult(
        x=x,
        cost=cost,
        objective=objective,
        bound=bound,
        gap=gap,
        status=name,
        proved=status == highspy.HighsModelStatus.kOptimal,
        time_s=elapsed,
        nodes=int(info.mip_node_count),
        version=h.version(),
    )


def _clean_plan(p: TransportProblem, x: FloatArray) -> FloatArray:
    """Plan of the MIP solver without its numerical noise. HiGHS returns amounts within its feasibility
    tolerance (1e-7) of a vertex; with integer supplies and demands every vertex is integer, so the amounts
    are rounded when the rounded plan satisfies the constraints exactly. Otherwise only amounts below 1e-6
    are set to zero."""
    integral = bool(np.array_equal(p.supply, np.rint(p.supply)) and np.array_equal(p.demand, np.rint(p.demand)))
    rounded = np.rint(x)
    if (
        integral
        and float(np.abs(x - rounded).max()) <= 1e-5
        and np.array_equal(rounded.sum(axis=1), p.supply)
        and np.array_equal(rounded.sum(axis=0), p.demand)
    ):
        return np.maximum(rounded, 0.0)
    return np.where(x > 1e-6, x, 0.0)


def balinski(fcp: FixedChargeProblem) -> tuple[FloatArray, float, float]:
    """Balinski's heuristic: optimal plan of the linearised problem, its true cost and the LP value (a lower
    bound of the FCTP optimum)."""
    from tpga.exact import solve_lp_highspy

    res = solve_lp_highspy(fcp.linearised())
    x = np.where(res.x > decoder_eps(fcp.problem), res.x, 0.0)
    return x, fcp.total_cost(x), float(res.cost)


def vogel_linearised(fcp: FixedChargeProblem) -> tuple[FloatArray, float]:
    """Vogel's method on the linearised costs; returns the plan and its true cost."""
    out = vogel(fcp.linearised())
    return out.x, fcp.total_cost(out.x)


def _result(
    fcp: FixedChargeProblem,
    perm: np.ndarray,
    eps: float,
    engine: str,
    **fields: Any,
) -> GAResult:
    p = fcp.problem
    m, n = p.shape
    from tpga._kernels import Kernels

    x = Kernels(engine).decode_plan(perm, *_arrays(p)[:2], n, eps).reshape(m, n)
    return GAResult(x=x, cost=fcp.total_cost(x), permutation=perm, **fields)


def run_random_search_fc(
    fcp: FixedChargeProblem,
    evaluations: int,
    seed: int | None = None,
    engine: str = "numba",
    batch_floats: int = 1 << 20,
    callback: ProgressCallback | None = None,
    decoder_tol: float = DECODER_TOL,
) -> GAResult:
    """Random search with the fixed-charge cost: the algorithm of :func:`tpga.ga.run_random_search`."""
    if evaluations < 1:
        raise ValueError("evaluations must be positive")
    t0 = time.perf_counter()
    k = _xkernels.table(engine)
    p = fcp.problem
    m, n = p.shape
    length = m * n
    supply, demand, cost, n_cols = _arrays(p)
    fixed = _fixed_array(fcp.fixed, m, n)
    eps = decoder_eps(p, decoder_tol)
    rng = np.random.default_rng(seed)
    rows = max(1, batch_floats // max(1, length - 1))
    done, best_cost, best_evaluation = 0, np.inf, 0
    best_uniforms = np.empty(max(0, length - 1))
    improvements: list[tuple[int, float]] = []
    batches, stop_reason = 0, "budget"
    while done < evaluations:
        size = min(rows, evaluations - done)
        uniforms = rng.random((size, max(0, length - 1)))
        out = np.empty(size)
        k["_random_batch_cost_fc"](uniforms, supply, demand, cost, fixed, n_cols, eps, out)
        running = np.minimum.accumulate(out)
        better = np.flatnonzero(running < np.concatenate(([best_cost], running[:-1])))
        for r in better:
            if out[r] < best_cost:
                best_cost = float(out[r])
                best_evaluation = done + int(r) + 1
                best_uniforms = uniforms[r].copy()
                improvements.append((best_evaluation, best_cost))
        done += size
        batches += 1
        if callback is not None and callback(batches, done, best_cost) and done < evaluations:
            stop_reason = "cancelled"
            break
    perm = np.arange(length, dtype=np.int64)
    _xkernels._shuffle(perm, best_uniforms)
    return _result(
        fcp,
        perm,
        eps,
        engine,
        history=[best_cost],
        evaluations=done,
        runtime_s=time.perf_counter() - t0,
        best_evaluation=best_evaluation,
        stop_reason=stop_reason,
        improvements=improvements,
        evaluations_since_improvement=done - best_evaluation,
    )


def run_sa_fc(
    fcp: FixedChargeProblem,
    config: SAConfig,
    callback: ProgressCallback | None = None,
    engine: str = "numba",
    chunk: int = 65536,
) -> GAResult:
    """Simulated annealing with the fixed-charge cost: the algorithm of :func:`tpga.sa.run_sa` (random or
    Vogel start on the linearised costs, pilot sample for the start temperature, geometric cooling to the
    end of the budget). The stagnation stop of ``SAConfig`` is not supported here."""
    if config.stagnation_evaluations is not None:
        raise ValueError("run_sa_fc stops by the budget only")
    t0 = time.perf_counter()
    k = _xkernels.table(engine)
    p = fcp.problem
    m, n = p.shape
    length = m * n
    supply, demand, cost, n_cols = _arrays(p)
    fixed = _fixed_array(fcp.fixed, m, n)
    eps = decoder_eps(p, config.decoder_tol)
    rng = np.random.default_rng(config.seed)
    if config.initialization == "cost-aware":
        from tpga.initialization import vogel_order

        perm = vogel_order(fcp.linearised()).astype(np.int64)
    else:
        perm = rng.permutation(length).astype(np.int64)

    def value_of(q: np.ndarray) -> float:
        return float(k["_decode_cost_fc"](q, supply, demand, cost, fixed, n_cols, eps))

    current = value_of(perm)
    evaluations = 1
    best, best_perm, best_evaluation = current, perm.copy(), 1
    improvements = [(1, current)]
    deltas = []
    if length >= 2:
        pilot = rng.random((config.pilot_moves, 3))
        for u in pilot:
            kind, i, j = _xkernels._move_from_uniforms(u[0], u[1], u[2], length, config.insertion_probability)
            _xkernels._apply_move(perm, kind, i, j)
            value = value_of(perm)
            evaluations += 1
            deltas.append(value - current)
            if value < best:
                best, best_perm, best_evaluation = value, perm.copy(), evaluations
                improvements.append((evaluations, best))
            _xkernels._undo_move(perm, kind, i, j)
    positive = [d for d in deltas if d > 0]
    scale = max(1.0, abs(current))
    t_start = -float(np.mean(positive)) / math.log(config.initial_acceptance) if positive else 1e-6 * scale
    steps_left = max(1, config.max_evaluations - evaluations)
    alpha = config.final_ratio ** (1.0 / steps_left)
    temperature = t_start
    steps_total, stop_reason = 0, "budget"
    while evaluations < config.max_evaluations and length >= 2:
        size = min(chunk, config.max_evaluations - evaluations)
        uniforms = rng.random((size, 4))
        imp_e = np.empty(size, dtype=np.int64)
        imp_c = np.empty(size)
        current, best, temperature, evaluations, best_evaluation, n_imp = k["_anneal_fc"](
            perm,
            current,
            best_perm,
            best,
            uniforms,
            temperature,
            alpha,
            config.insertion_probability,
            supply,
            demand,
            cost,
            fixed,
            n_cols,
            eps,
            evaluations,
            best_evaluation,
            imp_e,
            imp_c,
        )
        steps_total += size
        improvements.extend(zip(imp_e[:n_imp].tolist(), imp_c[:n_imp].tolist(), strict=True))
        if callback is not None and callback(steps_total, evaluations, best):
            stop_reason = "cancelled"
            break
    return _result(
        fcp,
        best_perm,
        eps,
        engine,
        history=[best],
        evaluations=evaluations,
        runtime_s=time.perf_counter() - t0,
        best_evaluation=best_evaluation,
        generations=steps_total,
        stop_reason=stop_reason,
        improvements=[(int(e), float(c)) for e, c in improvements],
        evaluations_since_improvement=evaluations - best_evaluation,
    )
