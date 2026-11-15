"""Step-by-step traces for the teaching pages and synchronous plans for the map."""

from __future__ import annotations

from typing import Any, Literal

import numpy as np
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from tpga import GAConfig
from tpga.classical import METHODS as CLASSICAL
from tpga.decoder import decode_permutation, decode_trace
from tpga.exact import solve_lp
from tpga.ga_trace import trace_ga

from .schemas import MAX_TRACE_ARCS, GAParamsIn, MethodCode, ProblemSpec, build_problem, default_budget
from .solvers import solve_method

router = APIRouter(tags=["Traces"])

EXAMPLES = {
    "3x4": {
        "title": "3 × 4",
        "supply": [30, 45, 25],
        "demand": [20, 30, 25, 25],
        "cost": [[8, 6, 10, 9], [9, 12, 13, 7], [14, 9, 16, 5]],
    },
    "4x5": {
        "title": "4 × 5",
        "supply": [40, 35, 30, 45],
        "demand": [25, 30, 35, 20, 40],
        "cost": [[12, 7, 9, 15, 6], [8, 14, 11, 5, 13], [10, 6, 16, 9, 12], [7, 11, 8, 13, 10]],
    },
}


def _small(spec: ProblemSpec):  # type: ignore[no-untyped-def]
    problem, meta = build_problem(spec)
    p = problem.balanced()
    if p.cost.size > MAX_TRACE_ARCS:
        raise HTTPException(413, f"для пошагового режима не более {MAX_TRACE_ARCS} направлений")
    return problem, p, meta


def _matrix(p) -> dict[str, Any]:  # type: ignore[no-untyped-def]
    return {"supply": p.supply.tolist(), "demand": p.demand.tolist(), "cost": p.cost.tolist()}


@router.get("/trace/examples")
def examples() -> dict[str, Any]:
    return EXAMPLES


class DecoderTraceRequest(BaseModel):
    problem: ProblemSpec
    permutation: list[int] | None = Field(None, max_length=MAX_TRACE_ARCS)
    seed: int = Field(0, ge=0, le=2**32 - 1)


@router.post("/trace/decoder")
def trace_decoder(req: DecoderTraceRequest) -> dict[str, Any]:
    problem, p, meta = _small(req.problem)
    perm = (
        np.asarray(req.permutation)
        if req.permutation is not None
        else np.random.default_rng(req.seed).permutation(p.cost.size)
    )
    try:
        steps = decode_trace(p, perm)
        x = decode_permutation(p, perm)
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
    _, z = solve_lp(p)
    cost = p.total_cost(x)
    return {
        "problem": _matrix(p),
        "meta": meta,
        "permutation": perm.tolist(),
        "steps": steps,
        "plan": x.tolist(),
        "cost": cost,
        "lp_cost": z,
        "gap_percent": 100 * (cost - z) / z if z else None,
    }


class ClassicalTraceRequest(BaseModel):
    problem: ProblemSpec
    method: Literal["NWC", "LCM", "VAM"]


@router.post("/trace/classical")
def trace_classical(req: ClassicalTraceRequest) -> dict[str, Any]:
    _, p, meta = _small(req.problem)
    r = CLASSICAL[req.method](p)
    _, z = solve_lp(p)
    return {
        "problem": _matrix(p),
        "meta": meta,
        "method": req.method,
        "steps": r.steps,
        "order": r.order,
        "plan": r.x.tolist(),
        "cost": r.cost,
        "lp_cost": z,
        "gap_percent": 100 * (r.cost - z) / z if z else None,
    }


class GATraceRequest(BaseModel):
    problem: ProblemSpec
    population: int = Field(12, ge=4, le=60)
    generations: int = Field(40, ge=1, le=300)
    crossover_rate: float = Field(0.9, ge=0, le=1)
    mutation_rate: float = Field(0.2, ge=0, le=1)
    tournament: int = Field(3, ge=1, le=10)
    elite: int = Field(2, ge=0, le=10)
    initialization: Literal["random", "cost-aware"] = "random"
    seed: int = Field(0, ge=0, le=2**32 - 1)


@router.post("/trace/ga")
def trace_genetic(req: GATraceRequest) -> dict[str, Any]:
    _, p, meta = _small(req.problem)
    if req.tournament > req.population or req.elite >= req.population:
        raise HTTPException(422, "турнир не больше популяции, элита меньше популяции")
    cfg = GAConfig(
        population=req.population,
        generations=req.generations,
        crossover_rate=req.crossover_rate,
        mutation_rate=req.mutation_rate,
        tournament=req.tournament,
        elite=req.elite,
        seed=req.seed,
        initialization=req.initialization,
    )
    trace = trace_ga(p, cfg)
    _, z = solve_lp(p)
    return {"problem": _matrix(p), "meta": meta, "lp_cost": z, **trace}


class PlansRequest(BaseModel):
    problem: ProblemSpec
    methods: list[MethodCode] = Field(["LP", "VAM", "GA-cost"], min_length=1, max_length=7)
    params: GAParamsIn = GAParamsIn(budget=50_000)


MAX_SYNC_BUDGET = 200_000


@router.post("/plans")
def plans(req: PlansRequest) -> dict[str, Any]:
    """Plans of several methods for the map; the GA budget is capped so that the call stays short."""
    problem, meta = build_problem(req.problem)
    m, n = problem.shape
    params = req.params.model_dump()
    params["budget"] = min(params.get("budget") or default_budget(m, n), MAX_SYNC_BUDGET)
    lp = solve_method(problem, "LP", params, None)
    out = {"LP": lp}
    for method in req.methods:
        if method != "LP":
            out[method] = solve_method(problem, method, params, lp["cost"])
    return {"problem": meta, "params": params, "results": out, "lp_optimum": lp["cost"]}
