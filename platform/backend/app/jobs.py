"""Asynchronous calculation jobs: ``POST /jobs``, ``GET /jobs/{id}``, SSE events, cancellation."""

from __future__ import annotations

import asyncio
import json
import logging
import multiprocessing as mp
import threading
import time
import uuid
from concurrent.futures import Future, ProcessPoolExecutor
from dataclasses import dataclass, field
from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from .job_runner import Cancelled, run_job
from .schemas import GAParamsIn, MethodCode, ProblemSpec, build_problem

log = logging.getLogger("tpga.jobs")
router = APIRouter(prefix="/jobs", tags=["Jobs"])

MAX_ACTIVE_JOBS = 2
KEEP_FINISHED = 50
FINISHED = {"done", "error", "cancelled"}


class JobRequest(BaseModel):
    problem: ProblemSpec
    methods: list[MethodCode] = Field(..., min_length=1, max_length=7)
    params: GAParamsIn = GAParamsIn()


@dataclass
class Job:
    id: str
    request: dict[str, Any]
    created: float = field(default_factory=time.time)
    status: str = "queued"
    events: list[dict[str, Any]] = field(default_factory=list)
    result: dict[str, Any] | None = None
    error: str | None = None
    progress: dict[str, Any] = field(default_factory=dict)
    future: Future | None = None

    def public(self, with_result: bool = True) -> dict[str, Any]:
        out = {
            "id": self.id,
            "status": self.status,
            "created": self.created,
            "methods": self.request["methods"],
            "problem": self.request["problem"],
            "progress": self.progress,
            "error": self.error,
        }
        if with_result:
            out["result"] = self.result
        return out


class JobManager:
    """Process pool, the event queue from the workers and the cancellation flags."""

    def __init__(self, workers: int = MAX_ACTIVE_JOBS) -> None:
        self.workers = workers
        self.jobs: dict[str, Job] = {}
        self.lock = threading.Lock()
        self._pool: ProcessPoolExecutor | None = None
        self._manager: Any = None
        self._queue: Any = None
        self._cancel: Any = None
        self._reader: threading.Thread | None = None
        self._stop = threading.Event()

    def _start(self) -> None:
        if self._pool is not None:
            return
        self._manager = mp.Manager()
        self._queue = self._manager.Queue()
        self._cancel = self._manager.dict()
        self._pool = ProcessPoolExecutor(max_workers=self.workers)
        self._reader = threading.Thread(target=self._read_events, name="job-events", daemon=True)
        self._reader.start()

    def _read_events(self) -> None:
        while not self._stop.is_set():
            try:
                event = self._queue.get(timeout=0.2)
            except Exception:  # noqa: BLE001 - queue.Empty or a closed manager during shutdown
                continue
            job = self.jobs.get(event.get("job"))
            if job is None:
                continue
            with self.lock:
                if event["type"] == "started":
                    job.status = "running"
                if event["type"] == "progress":
                    job.progress = {k: event[k] for k in ("method", "generation", "evaluations", "best_cost", "gap")}
                job.events.append(event)

    def active(self) -> int:
        return sum(1 for j in self.jobs.values() if j.status not in FINISHED)

    def submit(self, request: JobRequest) -> Job:
        build_problem(request.problem)  # validate here so that errors are HTTP errors, not job errors
        with self.lock:
            if self.active() >= MAX_ACTIVE_JOBS:
                raise HTTPException(429, f"Одновременно выполняется не более {MAX_ACTIVE_JOBS} расчётов")
            self._start()
            job = Job(id=uuid.uuid4().hex[:12], request=request.model_dump())
            self.jobs[job.id] = job
            self._cancel[job.id] = False
            self._trim()
        job.future = self._pool.submit(run_job, job.id, job.request, self._queue, self._cancel)
        job.future.add_done_callback(lambda fut, job=job: self._finish(job, fut))
        log.info(json.dumps({"event": "job_submitted", "job": job.id, "methods": request.methods}))
        return job

    def _finish(self, job: Job, fut: Future) -> None:
        # let the reader thread deliver the remaining progress events first
        deadline = time.time() + 1.0
        while time.time() < deadline and self._queue is not None and not self._queue.empty():
            time.sleep(0.02)
        with self.lock:
            exc = fut.exception()
            if exc is None:
                job.result = fut.result()
                job.status = "done"
                job.events.append({"type": "done", "time": time.time()})
            elif isinstance(exc, Cancelled) or self._cancel.get(job.id):
                job.status = "cancelled"
                job.events.append({"type": "cancelled", "time": time.time()})
            else:
                job.status = "error"
                job.error = str(exc) or exc.__class__.__name__
                job.events.append({"type": "error", "time": time.time(), "message": job.error})
        log.info(json.dumps({"event": "job_finished", "job": job.id, "status": job.status}))

    def cancel(self, job_id: str) -> Job:
        job = self.get(job_id)
        if job.status in FINISHED:
            return job
        self._cancel[job_id] = True
        if job.future is not None and job.future.cancel():  # still queued: never started
            with self.lock:
                job.status = "cancelled"
                job.events.append({"type": "cancelled", "time": time.time()})
        else:
            job.status = "cancelling"
        return job

    def get(self, job_id: str) -> Job:
        job = self.jobs.get(job_id)
        if job is None:
            raise HTTPException(404, "Расчёт не найден")
        return job

    def _trim(self) -> None:
        done = sorted((j for j in self.jobs.values() if j.status in FINISHED), key=lambda j: j.created)
        for j in done[: max(0, len(done) - KEEP_FINISHED)]:
            del self.jobs[j.id]

    def shutdown(self) -> None:
        self._stop.set()
        if self._pool is not None:
            for job_id in list(self.jobs):
                self._cancel[job_id] = True
            self._pool.shutdown(wait=True, cancel_futures=True)
        if self._manager is not None:
            self._manager.shutdown()
        self._pool = self._manager = None


manager = JobManager()


@router.post("", status_code=202)
def create_job(request: JobRequest) -> dict[str, Any]:
    return manager.submit(request).public(with_result=False)


@router.get("")
def list_jobs() -> list[dict[str, Any]]:
    return [j.public(with_result=False) for j in sorted(manager.jobs.values(), key=lambda j: -j.created)]


@router.get("/{job_id}")
def get_job(job_id: str) -> dict[str, Any]:
    return manager.get(job_id).public()


@router.delete("/{job_id}")
def cancel_job(job_id: str) -> dict[str, Any]:
    return manager.cancel(job_id).public(with_result=False)


@router.get("/{job_id}/events")
async def job_events(job_id: str) -> StreamingResponse:
    job = manager.get(job_id)

    async def stream():  # type: ignore[no-untyped-def]
        sent, idle = 0, 0.0
        while True:
            events = job.events[sent:]
            for e in events:
                yield f"event: {e['type']}\ndata: {json.dumps(e, ensure_ascii=False)}\n\n"
            sent += len(events)
            if job.status in FINISHED and sent >= len(job.events):
                return
            if events:
                idle = 0.0
            else:
                idle += 0.15
                if idle >= 10:
                    yield ": keep-alive\n\n"
                    idle = 0.0
            await asyncio.sleep(0.15)

    return StreamingResponse(stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache"})
