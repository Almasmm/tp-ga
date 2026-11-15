"""Compare both GA initializations against HiGHS on every full dataset scenario."""

import argparse
import json
import os
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from statistics import mean

import numpy as np

from tpga import GAConfig, TransportProblem, run_ga, solve_lp

POPULATION = 32
GENERATIONS = 60
SEEDS = (42, 7, 2026)


def evaluate(item):
    root, scenario = item
    problem = TransportProblem.from_json(root / scenario["file"])
    balanced = problem.balanced()
    _, optimum = solve_lp(problem)
    runs = []
    for seed in SEEDS:
        for method in ("random", "cost-aware"):
            ga = run_ga(
                problem, GAConfig(population=POPULATION, generations=GENERATIONS, seed=seed, initialization=method)
            )
            if not (
                np.allclose(ga.x.sum(axis=1), balanced.supply, atol=1e-5, rtol=0)
                and np.allclose(ga.x.sum(axis=0), balanced.demand, atol=1e-5, rtol=0)
                and (ga.x >= 0).all()
                and ga.cost >= optimum - max(1e-6, abs(optimum) * 1e-10)
            ):
                raise ValueError(f"Invalid result: {scenario['id']}, {method}, seed {seed}")
            runs.append(
                {
                    "initialization": method,
                    "seed": seed,
                    "cost_kzt": round(ga.cost, 2),
                    "gap_percent": max(0, 100 * (ga.cost - optimum) / abs(optimum)) if optimum else None,
                    "initial_cost_kzt": round(ga.history[0], 2),
                    "evaluations": ga.evaluations,
                }
            )
    return {"id": scenario["id"], "lp_cost_kzt": round(optimum, 2), "runs": runs}


def mean_gap(runs, method):
    gaps = [row["gap_percent"] for row in runs if row["initialization"] == method and row["gap_percent"] is not None]
    return mean(gaps) if gaps else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset", type=Path)
    parser.add_argument("--workers", type=int, default=min(4, os.cpu_count() or 1))
    args = parser.parse_args()
    root = args.dataset.resolve()
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    items = [(root, scenario) for scenario in manifest["scenarios"] if scenario["event"] != "api_subset"]
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        scenarios = []
        for i, result in enumerate(pool.map(evaluate, items), start=1):
            scenarios.append(result)
            print(f"{i}/{len(items)} {result['id']}", flush=True)
    runs = [run for scenario in scenarios for run in scenario["runs"]]
    output = {
        "dataset": manifest["id"],
        "protocol": {"population": POPULATION, "generations": GENERATIONS, "seeds": SEEDS, "reference": "HiGHS"},
        "summary": {
            "scenarios": len(scenarios),
            "runs": len(runs),
            "mean_gap_before_percent": mean_gap(runs, "random"),
            "mean_gap_after_percent": mean_gap(runs, "cost-aware"),
            "improved_scenarios": sum(
                mean_gap(row["runs"], "cost-aware") < mean_gap(row["runs"], "random")
                for row in scenarios
                if mean_gap(row["runs"], "cost-aware") is not None
            ),
        },
        "scenarios": scenarios,
    }
    target = root / "benchmark.json"
    temporary = target.with_suffix(".tmp")
    temporary.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(target)
    print(output["summary"])


if __name__ == "__main__":
    main()
