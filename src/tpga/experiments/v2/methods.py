"""One run of one method on one instance, as executed by a worker process of the v0.4 runner."""

from __future__ import annotations

import os
import statistics
import time
from functools import lru_cache
from pathlib import Path
from typing import Any

import numpy as np

from tpga.classical import METHODS as CLASSICAL
from tpga.exact import solve_lp_highspy
from tpga.experiments.worker import curve as improvement_curve
from tpga.experiments.worker import dummy_volume
from tpga.ga import GAConfig, GAResult, run_ga, run_random_search
from tpga.model import TransportProblem
from tpga.sa import SAConfig, run_sa
from tpga.verify import check_plan

KEY_FIELDS = ("phase", "set", "instance", "method", "config", "seed")
_STATE: dict[str, Any] = {"queue": None, "cpu": None, "cpu_class": None, "interval": 1.0}


def key_of(row: dict[str, Any]) -> str:
    """Identity of a run: (phase, set, instance, method, config, seed)."""
    return "|".join("" if row.get(k) is None else str(row.get(k)) for k in KEY_FIELDS)


@lru_cache(maxsize=32)
def load(path: str) -> TransportProblem:
    return TransportProblem.from_json(Path(path))


def gap(cost: float, z_star: float) -> float | None:
    return None if z_star == 0 else 100.0 * (cost - z_star) / abs(z_star)


def gap_norm(cost: float, z_star: float, z_rand: float | None) -> float | None:
    """(Z - Z*) / (Z_rand - Z*): 0 at the optimum, 1 at the mean random basic plan."""
    if z_rand is None or z_rand <= z_star:
        return None
    return (cost - z_star) / (z_rand - z_star)


def _report(kind: str, task: dict[str, Any], **data: Any) -> None:
    q = _STATE["queue"]
    if q is None:
        return
    try:  # noqa: SIM105 - keep the explicit comment on why errors are ignored
        q.put_nowait(
            {
                "type": kind,
                "pid": os.getpid(),
                "cpu": _STATE["cpu"],
                "key": key_of(task),
                "method": task["method"],
                "set": task["set"],
                "size": task["size"],
                "instance": task["instance"],
                "seed": task.get("seed"),
                "budget": task.get("budget"),
                "time": time.time(),
                **data,
            }
        )
    except Exception:  # noqa: BLE001 - a full or closed queue must never stop a run
        pass


def _progress(task: dict[str, Any]):
    z = float(task["z_star"])
    started = time.time()
    last = [0.0]

    def callback(_generation: int, evaluations: int, best: float) -> bool:
        now = time.time()
        if now - last[0] >= _STATE["interval"]:
            last[0] = now
            _report("progress", task, evals=evaluations, best_gap=gap(best, z), elapsed=now - started)
        return False

    return callback


def ga_config(task: dict[str, Any]) -> GAConfig:
    p = task["params"]
    stop = task["stop"]
    return GAConfig(
        population=int(p["population"]),
        generations=None,
        crossover_rate=float(p["crossover_rate"]),
        mutation_rate=float(p.get("mutation_rate", 0.2)),
        tournament=int(p["tournament"]),
        elite=int(p["elite"]),
        seed=int(task["seed"]),
        initialization=task["initialization"],
        max_evaluations=int(task["budget"]),
        stagnation=stop.get("stagnation_generations"),
        stagnation_evaluations=stop.get("stagnation_evaluations"),
        mutation_mode=p.get("mutation_mode", "swap_fixed"),
        mutation_strength=float(p.get("mutation_strength", 1.0)),
        decoder_tol=float(task["decoder_tol"]),
    )


def sa_config(task: dict[str, Any]) -> SAConfig:
    p = task["params"]
    return SAConfig(
        max_evaluations=int(task["budget"]),
        insertion_probability=float(p["insertion_probability"]),
        initial_acceptance=float(p["initial_acceptance"]),
        final_ratio=float(p["final_ratio"]),
        pilot_moves=int(p.get("pilot_moves", 100)),
        initialization=task["initialization"],
        stagnation_evaluations=task["stop"].get("stagnation_evaluations"),
        seed=int(task["seed"]),
        decoder_tol=float(task["decoder_tol"]),
    )


def _checked(problem: TransportProblem, x: np.ndarray, tol: float, label: str) -> float:
    check = check_plan(problem, x, rtol=tol)
    if not check.feasible:
        raise RuntimeError(f"infeasible plan from {label}: {check}")
    return max(check.max_row_residual, check.max_col_residual, max(0.0, -check.min_value))


def execute(task: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Run one task; returns the record and the convergence rows (``evals``, ``best_gap``)."""
    problem = load(task["path"])
    tol = float(task["tolerance"])
    kind = task["kind"]
    record: dict[str, Any] = {k: task.get(k) for k in (*KEY_FIELDS, "size", "m", "n", "budget")}
    record.update(cpu=_STATE["cpu"], cpu_class=_STATE["cpu_class"], started=time.time(), z_rand=task.get("z_rand"))
    _report("start", task)
    if kind == "representation":
        from tpga.experiments.v2.representation_phase import execute as representation

        rec, rows = representation(task, problem)
        rec.update(cpu=record["cpu"], cpu_class=record["cpu_class"], started=record["started"], finished=time.time())
        _report("done", task, gap=None, gap_norm=None, stop_reason=None, time_s=rec["time_s"])
        return rec, rows
    curve: list[dict[str, Any]] = []
    if kind == "lp":
        times: list[float] = []
        res: dict[str, Any] | None = None
        for _ in range(int(task.get("repeats", 1))):
            if task["solver"] == "ortools":
                from tpga.network_simplex import solve_min_cost_flow

                flow = solve_min_cost_flow(problem)
                times.append(flow.solve_s)
                res = {"x": flow.x, "cost": flow.cost, "build_s": flow.build_s}
            else:
                h = solve_lp_highspy(problem)
                times.append(h.solver_s)
                res = {
                    "x": h.x,
                    "cost": h.cost,
                    "presolve_s": h.presolve_s,
                    "build_s": h.build_s,
                    "wrapper_s": h.wrapper_s,
                    "highs_version": h.version,
                    "model_status": h.model_status,
                }
        assert res is not None
        x = res.pop("x")
        z = float(task.get("z_star") or res["cost"])
        record.update(
            res,
            solver=task["solver"],
            time_s=statistics.median(times),
            time_repeats=";".join(f"{t:.6g}" for t in times),
        )
        record.update(max_residual=_checked(problem, x, tol, task["method"]), dummy_volume=dummy_volume(problem, x))
        cost = float(record["cost"])
    elif kind == "classical":
        times, out = [], None
        for _ in range(int(task.get("repeats", 1))):
            t0 = time.perf_counter()
            out = CLASSICAL[task["method"]](problem)
            times.append(time.perf_counter() - t0)
        assert out is not None
        cost = out.cost
        z = float(task["z_star"])
        record.update(
            time_s=statistics.median(times),
            max_residual=_checked(problem, out.x, tol, task["method"]),
            dummy_volume=dummy_volume(problem, out.x),
        )
    else:
        z = float(task["z_star"])
        callback = _progress(task)
        result: GAResult
        if kind == "rs":
            result = run_random_search(
                problem,
                int(task["budget"]),
                seed=int(task["seed"]),
                callback=callback,
                decoder_tol=float(task["decoder_tol"]),
            )
        elif kind == "ga":
            result = run_ga(problem, ga_config(task), callback=callback)
        else:
            result = run_sa(problem, sa_config(task), callback=callback)
        cost = result.cost
        record.update(
            time_s=result.runtime_s,
            evals=result.evaluations,
            best_eval=result.best_evaluation,
            best_gen=result.best_generation,
            generations=result.generations,
            gens_since_improvement=result.generations_since_improvement,
            evals_since_improvement=result.evaluations_since_improvement,
            stop_reason=result.stop_reason,
            max_residual=_checked(problem, result.x, tol, f"{task['method']} seed {task['seed']}"),
            dummy_volume=dummy_volume(problem, result.x),
        )
        if task.get("curve_points"):
            points = np.unique(np.rint(np.geomspace(1, int(task["budget"]), int(task["curve_points"]))).astype(int))
            curve = [
                {"key": key_of(task), "evals": e, "best_cost": c, "gap": g}
                for e, c, g in improvement_curve(result, points, z)
            ]
    if cost < z - tol * max(1.0, abs(z)):
        raise RuntimeError(f"{task['method']} on {task['instance']} reports {cost} below the optimum {z}")
    record.update(
        cost=cost,
        z_star=z,
        gap=gap(cost, z),
        gap_norm=gap_norm(cost, z, task.get("z_rand")),
        optimal=abs(cost - z) <= tol * max(1.0, abs(z)),
        feasible=True,
        finished=time.time(),
    )
    _report(
        "done",
        task,
        gap=record["gap"],
        gap_norm=record["gap_norm"],
        stop_reason=record.get("stop_reason"),
        time_s=record["time_s"],
    )
    return record, curve
