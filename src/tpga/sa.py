"""Simulated annealing on the permutation encoding with the same greedy decoder as the GA.

A step proposes a neighbour of the current permutation (a swap of two positions, or the insertion of one
element at another position), decodes it (one decoder call) and accepts it by the Metropolis rule at
temperature ``T_k = T0 * alpha**k``. ``T0`` comes from a pilot sample of moves from the starting
permutation (those decoder calls count towards the budget): ``T0 = -mean(positive deltas) / ln(p0)`` so
that an average worsening move is accepted with probability ``p0`` at the start; ``alpha`` is chosen so
that the temperature reaches ``T0 * final_ratio`` at the end of the budget. The run record
(``improvements``, ``evaluations``, ``best_evaluation``, ``stop_reason``) has the same meaning as for
:func:`tpga.ga.run_ga`; ``generations`` holds the number of annealing steps.
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass
from typing import Literal

import numpy as np
from numba import njit

from tpga._kernels import Kernels
from tpga.decoder import DECODER_TOL, decoder_eps
from tpga.ga import GAResult, ProgressCallback, _arrays
from tpga.initialization import vogel_order
from tpga.model import TransportProblem


@dataclass(frozen=True)
class SAConfig:
    """Parameters of simulated annealing; ``max_evaluations`` (decoder calls) is required."""

    max_evaluations: int
    insertion_probability: float = 0.5
    initial_acceptance: float = 0.5
    final_ratio: float = 1e-3
    pilot_moves: int = 100
    initialization: Literal["random", "cost-aware"] = "random"
    stagnation_evaluations: int | None = None
    seed: int | None = None
    decoder_tol: float = DECODER_TOL

    def __post_init__(self) -> None:
        if self.max_evaluations < 2 + self.pilot_moves:
            raise ValueError("max_evaluations must exceed the pilot moves")
        if not 0.0 <= self.insertion_probability <= 1.0:
            raise ValueError("insertion_probability must lie in [0, 1]")
        if not 0.0 < self.initial_acceptance < 1.0:
            raise ValueError("initial_acceptance must lie in (0, 1)")
        if not 0.0 < self.final_ratio < 1.0:
            raise ValueError("final_ratio must lie in (0, 1)")
        if self.pilot_moves < 1:
            raise ValueError("pilot_moves must be positive")
        if self.initialization not in ("random", "cost-aware"):
            raise ValueError("initialization must be random or cost-aware")
        if self.stagnation_evaluations is not None and self.stagnation_evaluations < 1:
            raise ValueError("stagnation_evaluations must be positive")


def _apply_move_py(perm, kind, i, j):
    """Swap positions i and j (kind 0) or move the element at i to position j (kind 1), in place."""
    if kind == 0:
        tmp = perm[i]
        perm[i] = perm[j]
        perm[j] = tmp
    else:
        g = perm[i]
        if i < j:
            for t in range(i, j):
                perm[t] = perm[t + 1]
        else:
            for t in range(i, j, -1):
                perm[t] = perm[t - 1]
        perm[j] = g


def _undo_move_py(perm, kind, i, j):
    if kind == 0:
        _apply_move(perm, 0, i, j)
    else:
        _apply_move(perm, 1, j, i)


def _move_from_uniforms_py(u_kind, u_a, u_b, length, insertion_probability):
    kind = 1 if u_kind < insertion_probability else 0
    a = min(int(u_a * length), length - 1)
    b = min(int(u_b * (length - 1)), length - 2)
    if b >= a:
        b += 1
    return kind, a, b


def _anneal_py(
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
    n,
    eps,
    evaluations,
    best_evaluation,
    stagnation,
    imp_evals,
    imp_costs,
):
    """Run ``len(uniforms)`` steps. Returns (steps done, current, best, temperature, evaluations,
    best_evaluation, number of improvements written to ``imp_*``). Stops early when ``stagnation > 0`` and
    no improvement happened in the last ``stagnation`` decoder calls."""
    length = perm.size
    n_imp = 0
    steps = 0
    for s in range(uniforms.shape[0]):
        if stagnation > 0 and evaluations - best_evaluation >= stagnation:
            break
        u = uniforms[s]
        kind, i, j = _move_from_uniforms(u[0], u[1], u[2], length, insertion_probability)
        _apply_move(perm, kind, i, j)
        value = _decode_cost(perm, supply, demand, cost, n, eps)
        evaluations += 1
        steps += 1
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
    return steps, current, best, temperature, evaluations, best_evaluation, n_imp


from tpga._kernels import _decode_cost  # noqa: E402  (rebound by _table)

_apply_move = _apply_move_py
_undo_move = _undo_move_py
_move_from_uniforms = _move_from_uniforms_py
_anneal = _anneal_py
_COMPILED: dict = {}
_PLAIN = {
    "_apply_move": _apply_move_py,
    "_undo_move": _undo_move_py,
    "_move_from_uniforms": _move_from_uniforms_py,
    "_anneal": _anneal_py,
}


def _compiled() -> dict:
    if not _COMPILED:
        from tpga import _kernels

        g = globals()
        g["_decode_cost"] = _kernels._COMPILED["_decode_cost"]
        for name, fn in _PLAIN.items():
            g[name] = njit(cache=True)(fn)
            _COMPILED[name] = g[name]
    return _COMPILED


def _table(engine: str) -> dict:
    from tpga import _kernels

    g = globals()
    if engine == "python":
        g.update(_PLAIN)
        g["_decode_cost"] = _kernels._PLAIN["_decode_cost"]
        return _PLAIN
    table = _compiled()
    g.update(table)
    g["_decode_cost"] = _kernels._COMPILED["_decode_cost"]
    return table


def run_sa(
    problem: TransportProblem,
    config: SAConfig,
    callback: ProgressCallback | None = None,
    engine: str = "numba",
    chunk: int = 65536,
) -> GAResult:
    """Run simulated annealing within ``config.max_evaluations`` decoder calls."""
    if engine not in ("numba", "python"):
        raise ValueError("engine must be numba or python")
    t0 = time.perf_counter()
    table = _table(engine)
    kernels = Kernels(engine)
    p = problem.balanced()
    m, n = p.shape
    length = m * n
    supply, demand, cost, n_cols = _arrays(p)
    eps = decoder_eps(p, config.decoder_tol)
    rng = np.random.default_rng(config.seed)
    perm = (
        vogel_order(p).astype(np.int64)
        if config.initialization == "cost-aware"
        else rng.permutation(length).astype(np.int64)
    )
    current = float(kernels.decode_cost(perm, supply, demand, cost, n_cols, eps))
    evaluations = 1
    best, best_perm, best_evaluation = current, perm.copy(), 1
    improvements = [(1, current)]
    # pilot sample of moves from the start (counted as decoder calls, not accepted)
    deltas = []
    if length >= 2:
        pilot = rng.random((config.pilot_moves, 3))
        for u in pilot:
            kind, i, j = table["_move_from_uniforms"](u[0], u[1], u[2], length, config.insertion_probability)
            table["_apply_move"](perm, kind, i, j)
            value = float(kernels.decode_cost(perm, supply, demand, cost, n_cols, eps))
            evaluations += 1
            deltas.append(value - current)
            if value < best:
                best, best_perm, best_evaluation = value, perm.copy(), evaluations
                improvements.append((evaluations, best))
            table["_undo_move"](perm, kind, i, j)
    positive = [d for d in deltas if d > 0]
    scale = max(1.0, abs(current))
    t_start = -float(np.mean(positive)) / math.log(config.initial_acceptance) if positive else 1e-6 * scale
    steps_left = max(1, config.max_evaluations - evaluations)
    alpha = config.final_ratio ** (1.0 / steps_left)
    temperature = t_start
    stagnation = config.stagnation_evaluations or 0
    steps_total, stop_reason = 0, "budget"
    while evaluations < config.max_evaluations and length >= 2:
        k = min(chunk, config.max_evaluations - evaluations)
        uniforms = rng.random((k, 4))
        imp_e = np.empty(k, dtype=np.int64)
        imp_c = np.empty(k)
        steps, current, best, temperature, evaluations, best_evaluation, n_imp = table["_anneal"](
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
            n_cols,
            eps,
            evaluations,
            best_evaluation,
            stagnation,
            imp_e,
            imp_c,
        )
        steps_total += steps
        improvements.extend(zip(imp_e[:n_imp].tolist(), imp_c[:n_imp].tolist(), strict=True))
        if steps < k:
            stop_reason = "stagnation_evaluations"
            break
        if callback is not None and callback(steps_total, evaluations, best):
            stop_reason = "cancelled"
            break
    x = kernels.decode_plan(best_perm, supply, demand, n_cols, eps).reshape(m, n)
    return GAResult(
        x=x,
        cost=p.total_cost(x),
        history=[best],
        evaluations=evaluations,
        runtime_s=time.perf_counter() - t0,
        best_evaluation=best_evaluation,
        best_generation=0,
        generations=steps_total,
        stop_reason=stop_reason,
        improvements=[(int(e), float(c)) for e, c in improvements],
        permutation=best_perm,
        evaluations_since_improvement=evaluations - best_evaluation,
    )
