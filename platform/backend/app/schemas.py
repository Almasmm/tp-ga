"""Request models shared by the routers; every size limit of the interface is enforced here."""

from __future__ import annotations

from typing import Literal

import numpy as np
from fastapi import HTTPException
from pydantic import BaseModel, Field, model_validator

from tpga import TransportProblem

MAX_SIDE = 200  # largest m or n accepted from the interface
MAX_ARCS = MAX_SIDE * MAX_SIDE
MAX_TRACE_ARCS = 100
MethodCode = Literal["LP", "NWC", "LCM", "VAM", "RS", "GA-rand", "GA-cost"]
DatasetId = Literal["astana-potato", "kazakh-wheat"]


class ProblemSpec(BaseModel):
    """A problem given as a matrix, a packaged scenario, a generated instance or a paper instance."""

    kind: Literal["matrix", "scenario", "generated", "paper"] = "matrix"
    supply: list[float] | None = Field(None, max_length=MAX_SIDE)
    demand: list[float] | None = Field(None, max_length=MAX_SIDE)
    cost: list[list[float]] | None = Field(None, max_length=MAX_SIDE)
    dataset_id: DatasetId | None = None
    scenario_id: str | None = Field(None, max_length=64, pattern=r"^[A-Za-z0-9_.-]+$")
    m: int | None = Field(None, ge=1, le=MAX_SIDE)
    n: int | None = Field(None, ge=1, le=MAX_SIDE)
    seed: int | None = Field(None, ge=0, le=2**32 - 1)
    costs: Literal["uniform", "structured"] = "uniform"
    instance_id: str | None = Field(None, max_length=80, pattern=r"^[A-Za-z0-9_./-]+$")

    @model_validator(mode="after")
    def _fields(self) -> ProblemSpec:
        need = {
            "matrix": ("supply", "demand", "cost"),
            "scenario": ("dataset_id", "scenario_id"),
            "generated": ("m", "n", "seed"),
            "paper": ("instance_id",),
        }[self.kind]
        missing = [f for f in need if getattr(self, f) is None]
        if missing:
            raise ValueError(f"fields {missing} are required for kind={self.kind}")
        if self.kind == "matrix" and self.cost is not None and any(len(r) > MAX_SIDE for r in self.cost):
            raise ValueError(f"at most {MAX_SIDE} destinations")
        return self


def build_problem(spec: ProblemSpec) -> tuple[TransportProblem, dict]:
    """Problem and a description of where it came from; HTTP 422/404 on bad input."""
    from tpga.experiments.instances import structured_instance, uniform_instance

    from .paths import datasets_dir, paper_dir

    meta: dict = {"kind": spec.kind}
    try:
        if spec.kind == "matrix":
            p = TransportProblem(spec.supply, spec.demand, spec.cost)
        elif spec.kind == "generated":
            gen = uniform_instance if spec.costs == "uniform" else structured_instance
            params = {"cost_low": 1, "cost_high": 100, "supply_low": 20, "supply_high": 100, "area": 100, "noise": 10}
            data = gen(int(spec.m), int(spec.n), int(spec.seed), params)
            p = TransportProblem.from_dict(data)
            meta.update(m=spec.m, n=spec.n, seed=spec.seed, costs=spec.costs, coordinates=data.get("coordinates"))
        elif spec.kind == "scenario":
            import json

            root = datasets_dir() / str(spec.dataset_id)
            manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
            sc = next((s for s in manifest["scenarios"] if s["id"] == spec.scenario_id), None)
            if sc is None:
                raise HTTPException(404, "Сценарий не найден")
            p = TransportProblem.from_json(root / sc["file"])
            meta.update(dataset_id=spec.dataset_id, scenario_id=spec.scenario_id)
        else:
            import json

            manifest = json.loads((paper_dir() / "instances" / "manifest.json").read_text(encoding="utf-8"))
            entry = next((e for e in manifest["instances"] if e["id"] == spec.instance_id), None)
            if entry is None:
                raise HTTPException(404, "Задача не найдена в артефактах эксперимента")
            data = json.loads((paper_dir() / "instances" / entry["file"]).read_text(encoding="utf-8"))
            p = TransportProblem.from_dict(data)
            meta.update(instance_id=spec.instance_id, coordinates=data.get("coordinates"))
    except (ValueError, KeyError) as exc:
        raise HTTPException(422, str(exc)) from exc
    except OSError as exc:
        raise HTTPException(503, "Данные задачи недоступны") from exc
    if p.cost.size > MAX_ARCS:
        raise HTTPException(413, f"не более {MAX_ARCS} направлений")
    meta.update(m=p.shape[0], n=p.shape[1], balanced=p.is_balanced)
    return p, meta


class GAParamsIn(BaseModel):
    population: int = Field(100, ge=4, le=500)
    crossover_rate: float = Field(0.9, ge=0, le=1)
    mutation_rate: float = Field(0.2, ge=0, le=1)
    tournament: int = Field(3, ge=1, le=20)
    elite: int = Field(2, ge=0, le=50)
    budget: int | None = Field(None, ge=100, le=2_000_000, description="decoder calls; default 200 m n in [20000, 2e6]")
    stagnation: int | None = Field(200, ge=1, le=100_000)
    seed: int = Field(0, ge=0, le=2**32 - 1)

    @model_validator(mode="after")
    def _consistent(self) -> GAParamsIn:
        if self.tournament > self.population or self.elite >= self.population:
            raise ValueError("tournament must not exceed the population and elite must be below it")
        if self.budget is not None and self.budget < self.population:
            raise ValueError("budget must be at least the population")
        return self


def default_budget(m: int, n: int) -> int:
    return int(min(2_000_000, max(20_000, 200 * m * n)))


def plan_cells(x: np.ndarray, m: int, n: int, cost: np.ndarray | None = None) -> list[dict]:
    """Positive cells of the real part of a plan (the dummy row or column is reported separately)."""
    real = x[:m, :n]
    cells = []
    for i, j in zip(*np.nonzero(real > 1e-9), strict=True):
        cell = {"row": int(i), "col": int(j), "quantity": float(real[i, j])}
        if cost is not None:
            cell["unit_cost"] = float(cost[i, j])
        cells.append(cell)
    return cells
