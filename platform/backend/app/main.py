"""tp-ga API: custom problems, packaged datasets, calculation jobs, traces, artifacts and run history.

Meant for local use: run it on 127.0.0.1 only (``scripts/dev.ps1`` does). CORS admits the local
front end only; every input size is limited in :mod:`app.schemas`.
"""

import json
import logging
import os
import time
import uuid
from contextlib import asynccontextmanager
from typing import Literal

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, model_validator

from tpga import GAConfig, TransportProblem, __version__, run_ga, solve_lp

from .artifacts import router as artifacts_router
from .artifacts_v2 import router as artifacts_v2_router
from .history import router as history_router
from .jobs import manager as job_manager
from .jobs import router as jobs_router
from .monitor import router as monitor_router
from .scenarios import router as scenarios_router
from .traces import router as traces_router

MAX_ARCS = 400  # limit for arbitrary matrices submitted to /solve
MAX_SOLVE_CALLS = 1_000_000  # GA decoder calls per synchronous /solve request (about population x generations)


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        msg = record.getMessage()
        try:
            payload = json.loads(msg)
        except ValueError:
            payload = {"message": msg}
        return json.dumps({"ts": self.formatTime(record), "level": record.levelname, "logger": record.name, **payload})


def configure_logging() -> None:
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())
    for name in ("tpga.http", "tpga.jobs"):
        logger = logging.getLogger(name)
        logger.handlers = [handler]
        logger.setLevel(logging.INFO)
        logger.propagate = False


configure_logging()
http_log = logging.getLogger("tpga.http")


@asynccontextmanager
async def lifespan(_: FastAPI):  # type: ignore[no-untyped-def]
    yield
    job_manager.shutdown()


app = FastAPI(title="tp-ga", version=__version__, lifespan=lifespan)
ORIGINS = os.environ.get("TPGA_CORS_ORIGINS", "http://127.0.0.1:3000,http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in ORIGINS if o.strip()],
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["Content-Type"],
)


@app.middleware("http")
async def access_log(request: Request, call_next):  # type: ignore[no-untyped-def]
    rid = uuid.uuid4().hex[:8]
    t0 = time.perf_counter()
    response = await call_next(request)
    http_log.info(
        json.dumps(
            {
                "request": rid,
                "method": request.method,
                "path": request.url.path,
                "status": response.status_code,
                "ms": round(1000 * (time.perf_counter() - t0), 1),
            }
        )
    )
    response.headers["X-Request-Id"] = rid
    return response


app.include_router(scenarios_router)
app.include_router(jobs_router)
app.include_router(traces_router)
app.include_router(artifacts_v2_router)
app.include_router(artifacts_router)
app.include_router(monitor_router)
app.include_router(history_router)


class SolveRequest(BaseModel):
    supply: list[float] = Field(..., min_length=1)
    demand: list[float] = Field(..., min_length=1)
    cost: list[list[float]]
    method: Literal["lp", "ga"] = "lp"
    generations: int = Field(200, ge=1, le=5000)
    population: int = Field(60, ge=4, le=1000)
    seed: int | None = None

    @model_validator(mode="after")
    def _calls(self) -> "SolveRequest":
        if self.method == "ga" and self.population * (self.generations + 1) > MAX_SOLVE_CALLS:
            raise ValueError(
                f"population x (generations + 1) = {self.population * (self.generations + 1)} decoder calls; "
                f"the synchronous limit is {MAX_SOLVE_CALLS}"
            )
        return self


class SolveResponse(BaseModel):
    method: str
    cost: float
    plan: list[list[float]]
    balanced_with_dummy: bool
    lp_optimum: float | None = None
    gap_percent: float | None = None
    evaluations: int | None = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"tpga": __version__}


@app.post("/solve", response_model=SolveResponse)
def solve(req: SolveRequest):
    try:
        p = TransportProblem(req.supply, req.demand, req.cost)
    except ValueError as e:
        raise HTTPException(422, str(e)) from e
    if p.cost.size > MAX_ARCS:
        raise HTTPException(413, f"instance has {p.cost.size} arcs; synchronous limit is {MAX_ARCS}")
    dummy = not p.is_balanced
    x_lp, z_lp = solve_lp(p)
    if req.method == "lp":
        return SolveResponse(method="lp", cost=z_lp, plan=x_lp.tolist(), balanced_with_dummy=dummy, lp_optimum=z_lp)
    r = run_ga(p, GAConfig(population=req.population, generations=req.generations, seed=req.seed))
    gap = None if z_lp == 0 else 100.0 * (r.cost - z_lp) / abs(z_lp)
    # The LP optimum is always returned alongside a GA result: on the classical model exact
    # methods apply, so a heuristic result is only interpretable relative to it.
    return SolveResponse(
        method="ga",
        cost=r.cost,
        plan=r.x.tolist(),
        balanced_with_dummy=dummy,
        lp_optimum=z_lp,
        gap_percent=gap,
        evaluations=r.evaluations,
    )
