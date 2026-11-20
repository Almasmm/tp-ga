"""Single-thread, end-to-end incumbent deadlines for the second review."""

import math
import statistics
import time

import psutil

from tpga.experiments.v3 import rev
from tpga.experiments.v3.review2 import ROOT, records
from tpga.fctp import FixedChargeProblem, solve_mip


def tasks(cfg):
    raw = records(ROOT.parent / "review/raw/timing.jsonl")
    for item in sorted(rev.test_items(cfg), key=lambda i: (i["m"], i["rho"], i["id"])):
        if item["m"] not in (20, 30, 50, 70) or rev.index_of(item) != 0:
            continue
        observations = [
            row["time_s"] for row in raw if row["instance"] == item["id"] and row["method"] == "GA-cost-cycle"
        ]
        yield {
            "phase": "K8",
            "method": "MIP",
            "instance": item["id"],
            "path": item["path"],
            "size": item["size"],
            "rho": item["rho"],
            "ga_time_s": statistics.median(observations) if observations else None,
            "seed": None,
            "budget": None,
        }


def run(task):
    process = psutil.Process()
    allowed = process.cpu_affinity()
    cpu = 2 if 2 in allowed else allowed[0]
    process.cpu_affinity([cpu])
    problem = FixedChargeProblem.from_json(task["path"])
    deadlines = {"0.5 s": 0.5, "5 s": 5.0, "GA time": task["ga_time_s"]}
    limit = max(t for t in deadlines.values() if t is not None)
    incumbents = []

    def observe(elapsed, cost):
        if not incumbents or cost < incumbents[-1][1]:
            incumbents.append((elapsed, cost))

    start = time.perf_counter()
    result = solve_mip(problem, time_limit=limit, threads=1, observe=observe, include_model_time=True)
    elapsed = time.perf_counter() - start
    if result.cost is not None:
        observe(elapsed, result.cost)
    return {
        "evals": None,
        "time_s": elapsed,
        "time_limit_s": limit,
        "solver_call_s": result.time_s,
        "nodes": result.nodes,
        "cpu": cpu,
        "proved": result.proved,
        "cost": result.cost,
        "lower_bound": result.bound if math.isfinite(result.bound) else None,
        "first_feasible_s": incumbents[0][0] if incumbents else None,
        "first_feasible_cost": incumbents[0][1] if incumbents else None,
        "incumbents": incumbents,
        "deadlines": {
            label: {"time_s": t, "cost": min((v for s, v in incumbents if s <= t), default=None)}
            if t is not None
            else None
            for label, t in deadlines.items()
        },
    }
