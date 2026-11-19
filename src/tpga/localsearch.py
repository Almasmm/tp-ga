"""Two local-search methods for the fixed-charge transportation problem (amendment 10.1 of the v0.4 plan).

Both work on a basic plan (a spanning tree of ``m + n - 1`` arcs) with the true cost
``sum c x + sum f [x > 0]`` and start from the plan of Balinski's linearisation. A neighbour is the plan after
one pivot; a neighbour evaluation computes ``theta`` and the change of the cost without building the plan.

* :func:`run_tabu` - tabu search over pivots with a short tabu list and an aspiration rule. It is **not** a
  reproduction of the tabu search of Sun, Aronson, McKeown and Drinka (1998): it has no intermediate-term or
  long-term memory and its parameters are its own.
* :func:`run_ils` - iterated local search: first-improvement descent and a perturbation of random pivots.

The budget counts the cost of the start plan as one evaluation and every neighbour evaluation as one.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Literal

import numpy as np

from tpga import _xkernels
from tpga.decoder import DECODER_TOL, decoder_eps
from tpga.fctp import FixedChargeProblem, balinski
from tpga.ga import _arrays
from tpga.model import FloatArray


@dataclass(frozen=True)
class TabuConfig:
    """``sample``: share of the non-basic arcs evaluated in an iteration (1: all of them; below 1: that many
    arcs drawn uniformly with replacement). ``tenure``: iterations an arc that entered or left the basis
    stays tabu."""

    max_evaluations: int
    sample: float = 1.0
    tenure: int = 10
    seed: int | None = None
    decoder_tol: float = DECODER_TOL

    def __post_init__(self) -> None:
        if self.max_evaluations < 1:
            raise ValueError("max_evaluations must be positive")
        if not 0.0 < self.sample <= 1.0:
            raise ValueError("sample must lie in (0, 1]")
        if self.tenure < 0:
            raise ValueError("tenure must be nonnegative")


@dataclass(frozen=True)
class ILSConfig:
    """``perturbation``: random pivots between two descents. ``acceptance``: ``better`` returns to the
    previous local optimum when the new one costs more; ``always`` goes on from the new one."""

    max_evaluations: int
    perturbation: int = 4
    acceptance: Literal["better", "always"] = "better"
    seed: int | None = None
    decoder_tol: float = DECODER_TOL

    def __post_init__(self) -> None:
        if self.max_evaluations < 1:
            raise ValueError("max_evaluations must be positive")
        if self.perturbation < 1:
            raise ValueError("perturbation must be at least 1")
        if self.acceptance not in ("better", "always"):
            raise ValueError("acceptance must be better or always")


@dataclass
class LocalSearchResult:
    """``evaluations = full_evaluations + neighbour_evaluations``; ``generations`` counts the iterations of
    the tabu search or the descents of the iterated local search; ``moves`` the pivots applied."""

    x: FloatArray
    cost: float
    start_cost: float
    evaluations: int
    full_evaluations: int
    neighbour_evaluations: int
    best_evaluation: int
    generations: int
    moves: int
    runtime_s: float
    stop_reason: str = "budget"
    improvements: list[tuple[int, float]] = field(default_factory=list)


class _Search:
    """Basis of the start plan and the arrays the kernels work on."""

    def __init__(self, fcp: FixedChargeProblem, tol: float, engine: str) -> None:
        self.k = _xkernels.table(engine)
        p = fcp.problem
        self.fcp = fcp
        self.m, self.n = p.shape
        m, n = self.m, self.n
        self.size = m + n - 1
        self.nonbasic = m * n - self.size
        _, _, self.cost, _ = _arrays(p)
        self.fixed = np.ascontiguousarray(fcp.fixed.reshape(-1), dtype=np.float64)
        self.eps = decoder_eps(p, tol)
        x0, _, _ = balinski(fcp)
        self.arcs_row = np.empty((_xkernels.IW_ROWS, _xkernels.iw_columns(m, n)), dtype=np.int64)
        self.flows = np.zeros(m + n)
        iw = self.arcs_row
        cells = np.flatnonzero(x0.ravel() > self.eps)
        if cells.size > self.size:
            raise ValueError("the plan of the linearisation is not basic: more than m + n - 1 positive cells")
        iw[0, : cells.size] = cells
        self.flows[: cells.size] = x0.ravel()[cells]
        parent = iw[1]
        parent[: m + n] = np.arange(m + n)
        for arc in cells.tolist():
            ra, rb = self.k["_find"](parent, arc // n), self.k["_find"](parent, m + arc % n)
            if ra == rb:
                raise ValueError("the plan of the linearisation is not basic: its positive cells contain a cycle")
            parent[ra] = rb
        self.k["_complete_basis"](iw[0], self.flows, int(cells.size), m, n, iw[1])
        iw[2, : self.size] = np.sort(iw[0, : self.size])
        self.current = float(self.k["_plan_cost"](iw[0], self.flows, self.size, self.cost, self.fixed, self.eps))

    def args(self) -> tuple[Any, ...]:
        return (self.arcs_row[0], self.flows, self.m, self.n, self.cost, self.fixed, self.eps)

    def snapshot(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        iw = self.arcs_row
        return iw[0, : self.size].copy(), self.flows[: self.size].copy(), iw[2, : self.size].copy()

    def restore(self, state: tuple[np.ndarray, np.ndarray, np.ndarray]) -> None:
        iw = self.arcs_row
        iw[0, : self.size], self.flows[: self.size], iw[2, : self.size] = state

    def plan(self, state: tuple[np.ndarray, np.ndarray, np.ndarray]) -> FloatArray:
        flat = np.zeros(self.m * self.n)
        arcs, flows, _ = state
        flat[arcs] = np.where(flows > self.eps, flows, 0.0)
        return flat.reshape(self.m, self.n)


def _finish(
    s: _Search,
    best: tuple[np.ndarray, np.ndarray, np.ndarray],
    best_cost: float,
    start_cost: float,
    evaluations: int,
    best_evaluation: int,
    rounds: int,
    moves: int,
    improvements: list[tuple[int, float]],
    t0: float,
) -> LocalSearchResult:
    x = s.plan(best)
    cost = s.fcp.total_cost(x)
    if abs(cost - best_cost) > 1e-6 * max(1.0, abs(cost)):
        raise RuntimeError(f"the cost kept by the search ({best_cost}) differs from the cost of its plan ({cost})")
    return LocalSearchResult(
        x=x,
        cost=cost,
        start_cost=start_cost,
        evaluations=evaluations,
        full_evaluations=1,
        neighbour_evaluations=evaluations - 1,
        best_evaluation=best_evaluation,
        generations=rounds,
        moves=moves,
        runtime_s=time.perf_counter() - t0,
        improvements=improvements,
    )


def run_tabu(fcp: FixedChargeProblem, config: TabuConfig, engine: str = "numba") -> LocalSearchResult:
    """Tabu search over pivots from the plan of Balinski's linearisation (see the module text)."""
    t0 = time.perf_counter()
    s = _Search(fcp, config.decoder_tol, engine)
    step = s.k["_tabu_iteration"]
    rng = np.random.default_rng(config.seed)
    budget = config.max_evaluations
    evaluations = 1
    start_cost = current = s.current
    best, best_cost, best_evaluation = s.snapshot(), current, 1
    improvements = [(1, current)]
    expiry = np.zeros(s.m * s.n, dtype=np.int64)
    n_sample = 0 if config.sample >= 1.0 else max(1, int(round(config.sample * s.nonbasic)))
    none = np.empty(0)
    iteration = moves = 0
    while evaluations < budget and s.nonbasic > 0:
        if n_sample:
            sample_u, start_u = rng.random(n_sample), 0.0
        else:
            sample_u, start_u = none, float(rng.random())
        used, current, moved = step(
            *s.args(),
            current,
            best_cost,
            sample_u,
            n_sample,
            start_u,
            expiry,
            iteration,
            int(config.tenure),
            budget - evaluations,
            s.arcs_row,
        )
        evaluations += int(used)
        moves += int(moved)
        iteration += 1
        if current < best_cost - 1e-9 * max(1.0, abs(best_cost)):
            best, best_cost, best_evaluation = s.snapshot(), float(current), evaluations
            improvements.append((evaluations, best_cost))
    return _finish(s, best, best_cost, start_cost, evaluations, best_evaluation, iteration, moves, improvements, t0)


def run_ils(fcp: FixedChargeProblem, config: ILSConfig, engine: str = "numba") -> LocalSearchResult:
    """Iterated local search over pivots from the plan of Balinski's linearisation (see the module text)."""
    t0 = time.perf_counter()
    s = _Search(fcp, config.decoder_tol, engine)
    descent, perturb = s.k["_descent"], s.k["_perturb"]
    rng = np.random.default_rng(config.seed)
    budget = config.max_evaluations
    evaluations = 1
    start_cost = current = s.current
    best, best_cost, best_evaluation = s.snapshot(), current, 1
    improvements = [(1, current)]
    descents = moves = 0
    incumbent, incumbent_cost = best, current
    first = True
    while evaluations < budget and s.nonbasic > 0:
        if not first:
            count = min(config.perturbation, budget - evaluations)
            current = float(perturb(*s.args(), current, rng.random(count), count, s.arcs_row))
            evaluations += count
            moves += count
        used, current = descent(*s.args(), current, float(rng.random()), budget - evaluations, s.arcs_row)
        evaluations += int(used)
        current = float(current)
        descents += 1
        tol = 1e-9 * max(1.0, abs(best_cost))
        if current < best_cost - tol:
            best, best_cost, best_evaluation = s.snapshot(), current, evaluations
            improvements.append((evaluations, best_cost))
        if first or config.acceptance == "always" or current <= incumbent_cost + tol:
            incumbent, incumbent_cost = s.snapshot(), current
        else:
            s.restore(incumbent)
            current = incumbent_cost
        first = False
    return _finish(s, best, best_cost, start_cost, evaluations, best_evaluation, descents, moves, improvements, t0)
