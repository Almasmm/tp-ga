"""Serve and solve the packaged transportation datasets at their original size."""

import json
import os
from functools import lru_cache
from pathlib import Path
from threading import Lock
from time import perf_counter
from typing import Literal

import numpy as np
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from tpga import GAConfig, TransportProblem, run_ga, solve_lp

router = APIRouter(prefix="/scenarios", tags=["Transportation scenarios"])
experiment_lock = Lock()


DatasetId = Literal["astana-potato", "kazakh-wheat"]


@lru_cache(maxsize=2)
def dataset(dataset_id: DatasetId):
    override = os.environ.get("TPGA_DATASETS_DIR")
    directory = Path(override) if override else Path(__file__).resolve().parents[3] / "datasets"
    legacy = os.environ.get("TPGA_DATASET_DIR") if dataset_id == "astana-potato" else None
    root = Path(legacy) if legacy else directory / dataset_id
    try:
        manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        network = json.loads((root / "network.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise HTTPException(503, "Датасет недоступен") from exc
    return root, manifest, network


class ExperimentRequest(BaseModel):
    compare: bool = False
    population: int = Field(32, ge=8, le=80)
    generations: int = Field(60, ge=5, le=150)
    seed: int = Field(42, ge=0, le=4_294_967_295)


def describe_plan(problem, plan, cost, runtime):
    # The balanced solver may append a dummy row or column. Exclude it from shipments.
    m, n = problem.shape
    real = plan[:m, :n]
    received = real.sum(axis=0)
    shipped = real.sum(axis=1)
    deficit = np.maximum(0, problem.demand - received)
    unused = np.maximum(0, problem.supply - shipped)
    return {
        "cost_kzt": round(cost, 2),
        "runtime_s": runtime,
        "delivered_kg": float(real.sum()),
        "deficit_kg": float(deficit.sum()),
        "unused_kg": float(unused.sum()),
        "stores": [
            {"demand_kg": float(q), "received_kg": float(r), "deficit_kg": float(d)}
            for q, r, d in zip(problem.demand, received, deficit, strict=True)
        ],
        "warehouses": [
            {"supply_kg": float(q), "shipped_kg": float(s), "unused_kg": float(u)}
            for q, s, u in zip(problem.supply, shipped, unused, strict=True)
        ],
        "shipments": [
            {
                "warehouse": int(i),
                "store": int(j),
                "kg": float(real[i, j]),
                "tariff": float(problem.cost[i, j]),
                "cost_kzt": round(float(real[i, j] * problem.cost[i, j]), 2),
            }
            for i, j in zip(*np.nonzero(real > 1e-8), strict=True)
        ],
    }


@router.get("")
def list_scenarios(dataset_id: DatasetId = "astana-potato"):
    _, manifest, network = dataset(dataset_id)
    return {
        "id": manifest["id"],
        "data_kind": manifest["data_kind"],
        "sources": manifest["sources"],
        "scenarios": manifest["scenarios"],
        "network": network,
        "display": manifest.get("display", {}),
    }


@router.get("/benchmark")
def benchmark(dataset_id: DatasetId = "astana-potato"):
    root, _, _ = dataset(dataset_id)
    try:
        return json.loads((root / "benchmark.json").read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise HTTPException(404, "Серия прогонов ещё не сохранена") from exc


@router.post("/{scenario_id}/plan")
def scenario_plan(scenario_id: str, request: ExperimentRequest, dataset_id: DatasetId = "astana-potato"):
    root, manifest, _ = dataset(dataset_id)
    scenario = next((item for item in manifest["scenarios"] if item["id"] == scenario_id), None)
    if scenario is None:
        raise HTTPException(404, "Сценарий не найден")
    if request.compare and not experiment_lock.acquire(blocking=False):
        raise HTTPException(429, "Уже идёт другой эксперимент. Повторите расчёт после его завершения.")
    try:
        problem = TransportProblem.from_json(root / scenario["file"])
        start = perf_counter()
        plan, cost = solve_lp(problem)
        exact = describe_plan(problem, plan, cost, perf_counter() - start)
        comparisons = {"ga": None, "ga_before": None}
        if request.compare:
            for key, method in (("ga_before", "random"), ("ga", "cost-aware")):
                config = GAConfig(
                    population=request.population,
                    generations=request.generations,
                    seed=request.seed,
                    initialization=method,
                )
                result = run_ga(problem, config)
                genetic = describe_plan(problem, result.x, result.cost, result.runtime_s)
                genetic.update(
                    {
                        "gap_percent": 100 * (result.cost - cost) / abs(cost) if cost else None,
                        "evaluations": result.evaluations,
                        "history": result.history,
                        "population": config.population,
                        "generations": config.generations,
                        "seed": config.seed,
                        "initialization": method,
                    }
                )
                comparisons[key] = genetic
        return {"scenario_id": scenario_id, "lp": exact, **comparisons}
    except OSError as exc:
        raise HTTPException(503, "Файл сценария недоступен") from exc
    finally:
        if request.compare:
            experiment_lock.release()
