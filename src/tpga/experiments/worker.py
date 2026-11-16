"""Execution of one experiment task in a worker process."""

from __future__ import annotations

import statistics
import time
from functools import lru_cache
from pathlib import Path
from typing import Any

import numpy as np

from tpga.classical import METHODS as CLASSICAL
from tpga.exact import solve_lp_detailed
from tpga.experiments import environment
from tpga.ga import GAConfig, GAResult, run_ga, run_random_search
from tpga.model import TransportProblem
from tpga.verify import check_plan

FIELDS = [
    "phase",
    "instance",
    "suite",
    "size",
    "m",
    "n",
    "method",
    "config",
    "population",
    "crossover_rate",
    "mutation_rate",
    "initialization",
    "seed",
    "budget",
    "cost",
    "z_star",
    "gap",
    "optimal",
    "time_s",
    "evals",
    "best_eval",
    "best_gen",
    "generations",
    "stop_reason",
    "feasible",
    "max_residual",
    "dummy_volume",
    "lp_status",
    "time_repeats",
    "cpu",
    "cpu_class",
]
CURVE_FIELDS = ["instance", "method", "config", "seed", "evals", "best_cost", "gap"]

_CPU: dict[str, int | None] = {"cpu": None, "cpu_class": None}


def init_worker(cpu_queue: Any = None, classes: dict[int, int] | None = None) -> None:
    """Process initializer: one thread per library, optional pinning to a logical processor."""
    environment.single_thread_environment()
    if cpu_queue is not None:
        cpu = int(cpu_queue.get())
        if environment.pin_to_cpu(cpu):
            _CPU["cpu"] = cpu
            _CPU["cpu_class"] = (classes or {}).get(cpu)


@lru_cache(maxsize=64)
def load(path: str) -> TransportProblem:
    return TransportProblem.from_json(Path(path))


def dummy_volume(problem: TransportProblem, x: np.ndarray) -> float:
    """Volume on the dummy row or column added by balancing (unmet demand or unused supply)."""
    m, n = problem.shape
    bm, bn = x.shape
    if bm > m:
        return float(x[m:, :].sum())
    if bn > n:
        return float(x[:, n:].sum())
    return 0.0


def is_optimal(cost: float, z_star: float, tol: float) -> bool:
    return abs(cost - z_star) <= tol * max(1.0, abs(z_star))


def gap(cost: float, z_star: float) -> float | None:
    return None if z_star == 0 else 100.0 * (cost - z_star) / abs(z_star)


def _checked(problem: TransportProblem, x: np.ndarray, tol: float, label: str) -> float:
    check = check_plan(problem, x, rtol=tol)
    if not check.feasible:
        raise RuntimeError(f"infeasible plan from {label}: {check}")
    return max(check.max_row_residual, check.max_col_residual, max(0.0, -check.min_value))


def curve(result: GAResult, points: np.ndarray, z_star: float) -> list[tuple[int, float, float | None]]:
    """Best cost at each budget point from the exact improvement record (step function)."""
    evals = np.array([e for e, _ in result.improvements])
    costs = np.array([c for _, c in result.improvements])
    out = []
    for e in points:
        if e > result.evaluations:
            break
        k = int(np.searchsorted(evals, e, side="right")) - 1
        if k >= 0:
            out.append((int(e), float(costs[k]), gap(float(costs[k]), z_star)))
    if not out or out[-1][0] != result.evaluations:
        out.append((result.evaluations, result.cost, gap(result.cost, z_star)))
    return out


def execute(task: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Run one task and return the CSV row and the convergence rows."""
    problem = load(task["path"])
    tol = float(task["tolerance"])
    row: dict[str, Any] = {k: task.get(k) for k in FIELDS}
    row.update(_CPU)
    method = task["method"]
    curve_rows: list[dict[str, Any]] = []
    if method == "LP":
        times: list[float] = []
        lp = None
        for _ in range(int(task["repeats"])):
            lp = solve_lp_detailed(problem, method=task.get("lp_method", "highs"))
            times.append(lp.time_s)
        assert lp is not None
        row.update(
            cost=lp.cost,
            z_star=lp.cost,
            gap=0.0,
            optimal=True,
            time_s=statistics.median(times),
            time_repeats=";".join(f"{t:.6g}" for t in times),
            lp_status=lp.status,
            max_residual=_checked(problem, lp.x, tol, "LP"),
            dummy_volume=dummy_volume(problem, lp.x),
            feasible=True,
        )
        return row, curve_rows
    z_star = float(task["z_star"])
    if method in CLASSICAL:
        times = []
        res = None
        for _ in range(int(task["repeats"])):
            t0 = time.perf_counter()
            res = CLASSICAL[method](problem)
            times.append(time.perf_counter() - t0)
        assert res is not None
        cost = res.cost
        row.update(
            cost=cost,
            time_s=statistics.median(times),
            time_repeats=";".join(f"{t:.6g}" for t in times),
            max_residual=_checked(problem, res.x, tol, method),
            dummy_volume=dummy_volume(problem, res.x),
        )
    else:
        result: GAResult
        if method == "RS":
            result = run_random_search(problem, int(task["budget"]), seed=int(task["seed"]))
        else:
            cfg = GAConfig(
                population=int(task["population"]),
                generations=None,
                crossover_rate=float(task["crossover_rate"]),
                mutation_rate=float(task["mutation_rate"]),
                tournament=int(task["tournament"]),
                elite=int(task["elite"]),
                seed=int(task["seed"]),
                initialization=task["initialization"],
                max_evaluations=int(task["budget"]),
                stagnation=None if task["stagnation"] is None else int(task["stagnation"]),
            )
            result = run_ga(problem, cfg)
        cost = result.cost
        row.update(
            cost=cost,
            time_s=result.runtime_s,
            evals=result.evaluations,
            best_eval=result.best_evaluation,
            best_gen=result.best_generation,
            generations=result.generations,
            stop_reason=result.stop_reason,
            max_residual=_checked(problem, result.x, tol, f"{method} seed {task['seed']}"),
            dummy_volume=dummy_volume(problem, result.x),
        )
        if task.get("curve_points"):
            points = np.unique(np.rint(np.geomspace(1, int(task["budget"]), int(task["curve_points"]))).astype(int))
            for e, c, g in curve(result, points, z_star):
                curve_rows.append(
                    {
                        "instance": task["instance"],
                        "method": method,
                        "config": task["config"],
                        "seed": task["seed"],
                        "evals": e,
                        "best_cost": c,
                        "gap": g,
                    }
                )
    if cost < z_star - tol * max(1.0, abs(z_star)):
        raise RuntimeError(f"{method} on {task['instance']} reports {cost} below the LP optimum {z_star}")
    row.update(z_star=z_star, gap=gap(cost, z_star), optimal=is_optimal(cost, z_star, tol), feasible=True)
    return row, curve_rows
