"""Running one method on one problem with a uniform result shape (used by jobs and plans)."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import Any

import numpy as np

from tpga import GAConfig, TransportProblem, run_ga
from tpga.classical import METHODS as CLASSICAL
from tpga.exact import solve_lp_detailed
from tpga.ga import run_random_search
from tpga.verify import check_plan

from .schemas import default_budget, plan_cells


def dummy_volume(problem: TransportProblem, x: np.ndarray) -> float:
    m, n = problem.shape
    return float(x[m:, :].sum() + x[:, n:].sum())


def _curve(improvements: list[tuple[int, float]], limit: int = 400) -> list[list[float]]:
    if len(improvements) <= limit:
        return [[e, c] for e, c in improvements]
    idx = np.unique(np.linspace(0, len(improvements) - 1, limit).astype(int))
    return [[improvements[i][0], improvements[i][1]] for i in idx]


def solve_method(
    problem: TransportProblem,
    method: str,
    params: dict[str, Any],
    z_star: float | None,
    progress: Callable[[int, int, float], bool | None] | None = None,
) -> dict[str, Any]:
    """Result of one method: cost, gap, time, plan cells and, for GA and RS, the run record."""
    m, n = problem.shape
    out: dict[str, Any] = {"method": method}
    t0 = time.perf_counter()
    if method == "LP":
        lp = solve_lp_detailed(problem)
        x, cost = lp.x, lp.cost
        out["status"] = lp.status
    elif method in CLASSICAL:
        r = CLASSICAL[method](problem)
        x, cost = r.x, r.cost
    else:
        budget = params.get("budget") or default_budget(m, n)
        if method == "RS":
            res = run_random_search(problem, int(budget), seed=int(params["seed"]), callback=progress)
        else:
            cfg = GAConfig(
                population=int(params["population"]),
                generations=None,
                crossover_rate=float(params["crossover_rate"]),
                mutation_rate=float(params["mutation_rate"]),
                tournament=int(params["tournament"]),
                elite=int(params["elite"]),
                seed=int(params["seed"]),
                initialization="random" if method == "GA-rand" else "cost-aware",
                max_evaluations=int(budget),
                stagnation=params.get("stagnation"),
            )
            res = run_ga(problem, cfg, callback=progress)
        x, cost = res.x, res.cost
        out.update(
            evaluations=res.evaluations,
            best_evaluation=res.best_evaluation,
            generations=res.generations,
            stop_reason=res.stop_reason,
            budget=int(budget),
            curve=_curve(res.improvements),
        )
    out["time_s"] = time.perf_counter() - t0
    check = check_plan(problem, x)
    if not check.feasible:  # pragma: no cover - every method returns feasible plans
        raise RuntimeError(f"{method} returned an infeasible plan")
    out.update(
        cost=float(cost),
        gap_percent=None if not z_star else 100.0 * (cost - z_star) / abs(z_star),
        dummy_volume=dummy_volume(problem, x),
        plan=plan_cells(x, m, n),
    )
    return out
