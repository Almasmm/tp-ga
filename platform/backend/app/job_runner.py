"""Body of a calculation job; runs in a worker process and reports through a queue."""

from __future__ import annotations

import time
from typing import Any

from .schemas import GAParamsIn, ProblemSpec, build_problem
from .solvers import solve_method

PROGRESS_INTERVAL_S = 0.1
CANCEL_INTERVAL_S = 0.2


class Cancelled(Exception):
    pass


def run_job(job_id: str, request: dict[str, Any], events: Any, cancel: Any) -> dict[str, Any]:
    """Solve every requested method in order (LP first, for the gap); push progress events to ``events``."""
    spec = ProblemSpec(**request["problem"])
    params = GAParamsIn(**request.get("params", {})).model_dump()
    problem, meta = build_problem(spec)
    methods = list(dict.fromkeys(["LP", *request["methods"]]))
    results: dict[str, Any] = {}
    z_star: float | None = None

    def emit(kind: str, **data: Any) -> None:
        events.put({"job": job_id, "type": kind, "time": time.time(), **data})

    emit("started", problem=meta, methods=methods)
    for method in methods:
        if cancel.get(job_id):
            raise Cancelled()
        emit("method_started", method=method)
        last_emit = last_check = 0.0

        def progress(
            generation: int, evaluations: int, best: float, method: str = method, z_star: float | None = z_star
        ) -> bool:
            nonlocal last_emit, last_check
            now = time.monotonic()
            if now - last_emit >= PROGRESS_INTERVAL_S or generation == 0:
                last_emit = now
                gap = None if not z_star else 100.0 * (best - z_star) / abs(z_star)
                emit("progress", method=method, generation=generation, evaluations=evaluations, best_cost=best, gap=gap)
            if now - last_check >= CANCEL_INTERVAL_S:
                last_check = now
                return bool(cancel.get(job_id))
            return False

        result = solve_method(problem, method, params, z_star, progress)
        if result.get("stop_reason") == "cancelled":
            raise Cancelled()
        if method == "LP":
            z_star = result["cost"]
        results[method] = result
        emit("method_done", method=method, result={k: v for k, v in result.items() if k != "plan"})
    return {"problem": meta, "params": params, "results": results, "lp_optimum": z_star}
