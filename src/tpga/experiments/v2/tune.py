"""``tpga-exp tune``: parameter tuning on training instances with Optuna (TPE), equal budget per method.

Training instances come from the same generators with seeds offset by 5 000 000, so none coincides with a
test instance. Every trial runs the method on every training instance and seed with the budget-only stop;
the objective is the mean gap (%). The best parameters of every method are written to the frozen file named
in the configuration (``experiments/tuned-v2.yaml``) together with the trial log.
"""

from __future__ import annotations

import datetime as dt
import json
import multiprocessing as mp
import statistics
from concurrent.futures import ProcessPoolExecutor
from typing import Any

import yaml

from tpga.exact import solve_lp_highspy
from tpga.experiments import environment
from tpga.experiments.v2 import methods
from tpga.experiments.v2.config import ConfigV2
from tpga.experiments.v2.instances import build, select
from tpga.experiments.v2.runner import init_worker
from tpga.experiments.v2.tasks import stochastic_tasks

TUNED = {
    "GA-rand": ("ga", "random"),
    "GA-cost": ("ga", "cost-aware"),
    "SA-rand": ("sa", "random"),
    "SA-cost": ("sa", "cost-aware"),
}


def suggest(trial: Any, kind: str, space: dict[str, Any]) -> dict[str, Any]:
    if kind == "sa":
        s = space["sa"]
        return {
            "insertion_probability": trial.suggest_float("insertion_probability", *s["insertion_probability"]),
            "initial_acceptance": trial.suggest_float("initial_acceptance", *s["initial_acceptance"]),
            "final_ratio": trial.suggest_float("final_ratio", *s["final_ratio"], log=True),
        }
    g = space["ga"]
    pop = trial.suggest_int("population", *g["population"], log=True)
    mode = trial.suggest_categorical("mutation_mode", g["mutation_mode"])
    p: dict[str, Any] = {
        "population": pop,
        "crossover_rate": trial.suggest_float("crossover_rate", *g["crossover_rate"]),
        "tournament": min(pop, trial.suggest_int("tournament", *g["tournament"])),
        "elite": min(pop - 1, trial.suggest_int("elite", *g["elite"])),
        "mutation_mode": mode,
    }
    lo, hi = g[mode]
    if mode == "swap_fixed":
        p["mutation_rate"] = trial.suggest_float("swap_fixed", lo, hi, log=True)
    elif mode == "swap_count":
        p["mutation_strength"] = trial.suggest_int("swap_count", lo, hi)
    else:
        p["mutation_strength"] = trial.suggest_float(mode, lo, hi, log=True)
    return p


def run(cfg: ConfigV2, methods_to_tune: list[str] | None = None) -> dict[str, Any]:
    import optuna

    spec = cfg.raw["tuning"]
    train = select(
        build(cfg, split="train", sets=list(spec["sets"]), per_size=int(spec["instances_per_size"])), spec["sets"]
    )
    z = {i.id: solve_lp_highspy(methods.load(str(i.path))).cost for i in train}
    seeds = cfg.seeds(int(spec["seeds"]))
    out_dir = cfg.output / "tuning"
    out_dir.mkdir(parents=True, exist_ok=True)
    classes = environment.cpu_classes()
    manager = mp.Manager()
    cpus = list(range(int(cfg.raw.get("workers", 24))))
    q = manager.Queue()
    for c in cpus:
        q.put(c)
    pool = ProcessPoolExecutor(len(cpus), initializer=init_worker, initargs=(q, classes, None, "normal", 1.0))
    results: dict[str, Any] = {}
    try:
        for name in methods_to_tune or list(TUNED):
            kind, init = TUNED[name]
            log = out_dir / f"{name}.jsonl"
            log.unlink(missing_ok=True)

            def objective(trial: Any, kind: str = kind, init: str = init, name: str = name, log: Any = log) -> float:
                params = suggest(trial, kind, spec["space"])
                override = {**params, "init": init}
                tasks = (
                    stochastic_tasks(
                        cfg,
                        "tune",
                        train,
                        [name],
                        "budget",
                        seeds,
                        params_override={name: override} if kind == "ga" else None,
                    )
                    if kind == "ga"
                    else _sa_tasks(cfg, train, name, params, init, seeds)
                )
                for t in tasks:
                    t["z_star"] = z[t["instance"]]
                gaps = [r["gap"] for r, _ in pool.map(methods.execute, tasks)]
                value = statistics.fmean(gaps)
                with log.open("a", encoding="utf-8", newline="\n") as fh:
                    fh.write(
                        json.dumps({"trial": trial.number, "params": params, "mean_gap": value, "runs": len(gaps)})
                        + "\n"
                    )
                return value

            sampler = optuna.samplers.TPESampler(seed=int(spec["seed"]))
            study = optuna.create_study(direction="minimize", sampler=sampler, study_name=name)
            optuna.logging.set_verbosity(optuna.logging.WARNING)
            study.optimize(objective, n_trials=int(spec["trials"]))
            best = json.loads(log.read_text(encoding="utf-8").splitlines()[study.best_trial.number])
            results[name] = {"params": best["params"], "mean_gap": study.best_value, "trials": len(study.trials)}
    finally:
        pool.shutdown()
        manager.shutdown()
    frozen = {
        "frozen": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "git_commit": environment.describe(cfg.root).get("git_commit"),
        "procedure": {
            k: spec[k] for k in ("sampler", "seed", "trials", "sets", "instances_per_size", "seeds", "objective")
        },
        "training_instances": sorted(i.id for i in train),
        "parameters": {k: v["params"] for k, v in results.items()},
        "best_objective": {k: v["mean_gap"] for k, v in results.items()},
    }
    previous = yaml.safe_load(cfg.tuned_path.read_text(encoding="utf-8")) if cfg.tuned_path.exists() else None
    if previous and methods_to_tune:
        previous["parameters"].update(frozen["parameters"])
        previous["best_objective"].update(frozen["best_objective"])
        frozen = {**previous, "frozen": frozen["frozen"], "git_commit": frozen["git_commit"]}
    text = yaml.safe_dump(frozen, sort_keys=False, allow_unicode=True)
    cfg.tuned_path.write_text(text, encoding="utf-8", newline="\n")
    return frozen


def _sa_tasks(cfg: ConfigV2, train: list, name: str, params: dict[str, Any], init: str, seeds: list[int]):
    from tpga.experiments.v2.tasks import sa_config_id

    tasks = []
    for inst in train:
        budget = cfg.budget(inst.m, inst.n)
        for seed in seeds:
            tasks.append(
                {
                    "phase": "tune",
                    "set": inst.set,
                    "instance": inst.id,
                    "size": inst.size,
                    "m": inst.m,
                    "n": inst.n,
                    "path": str(inst.path),
                    "z_rand": inst.z_rand,
                    "tolerance": cfg.tolerance,
                    "decoder_tol": cfg.decoder_tol,
                    "method": name,
                    "kind": "sa",
                    "config": sa_config_id(params, init, "budget"),
                    "params": params,
                    "initialization": init,
                    "stop": {},
                    "budget": budget,
                    "seed": seed,
                    "curve_points": 0,
                }
            )
    return tasks
