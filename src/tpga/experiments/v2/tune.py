"""``tpga-exp tune``: parameter tuning on training instances with Optuna (TPE), equal budget per method.

Training instances come from the same generators with seeds offset by 5 000 000, so none coincides with a
test instance. Every trial runs the method on every training instance and seed with the budget-only stop;
the objective is the mean gap (%). The best parameters of every method are written to the frozen file named
in the configuration (``experiments/tuned-v2.yaml``) together with the trial log.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import math
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


def bounds(spec: Any, log_default: bool) -> tuple[float, float, bool]:
    """``[lo, hi]`` (scale as before) or ``{range: [lo, hi], log: bool}``."""
    if isinstance(spec, dict):
        lo, hi = spec["range"]
        return float(lo), float(hi), bool(spec.get("log", log_default))
    lo, hi = spec
    return float(lo), float(hi), log_default


#: parameters of each kind, with the scale used when the space gives a plain [lo, hi]
SA_PARAMS = {"insertion_probability": False, "initial_acceptance": False, "final_ratio": True}
GA_FLOATS = {"crossover_rate": False, "swap_fixed": True, "swap_per_position": True, "swap_scaled": True}
GA_INTS = {"population": True, "tournament": False, "elite": False, "swap_count": False}


def suggest(trial: Any, kind: str, space: dict[str, Any]) -> dict[str, Any]:
    def f(name: str, s: dict[str, Any], log: bool) -> float:
        lo, hi, lg = bounds(s[name], log)
        return float(trial.suggest_float(name, lo, hi, log=lg))

    def i(name: str, s: dict[str, Any], log: bool) -> int:
        lo, hi, lg = bounds(s[name], log)
        return int(trial.suggest_int(name, int(lo), int(hi), log=lg))

    if kind == "sa":
        s = space["sa"]
        return {name: f(name, s, log) for name, log in SA_PARAMS.items()}
    g = space["ga"]
    pop = i("population", g, True)
    mode = trial.suggest_categorical("mutation_mode", g["mutation_mode"])
    p: dict[str, Any] = {
        "population": pop,
        "crossover_rate": f("crossover_rate", g, False),
        "tournament": min(pop, i("tournament", g, False)),
        "elite": min(pop - 1, i("elite", g, False)),
        "mutation_mode": mode,
    }
    if mode == "swap_fixed":
        p["mutation_rate"] = f("swap_fixed", g, True)
    elif mode == "swap_count":
        p["mutation_strength"] = i("swap_count", g, False)
    else:
        p["mutation_strength"] = f(mode, g, True)
    return p


def near_bounds(kind: str, params: dict[str, Any], space: dict[str, Any], share: float = 0.05) -> list[dict[str, Any]]:
    """Parameters within ``share`` of the width of their range from a bound (on the scale they were sampled)."""
    if kind == "sa":
        items = [(name, params[name], space["sa"][name], log) for name, log in SA_PARAMS.items()]
    else:
        g = space["ga"]
        items = [(n, params[n], g[n], log) for n, log in {**GA_INTS, **GA_FLOATS}.items() if n in params]
        mode = params["mutation_mode"]
        value = params["mutation_rate"] if mode == "swap_fixed" else params["mutation_strength"]
        items.append((mode, value, g[mode], {**GA_INTS, **GA_FLOATS}[mode]))
    out = []
    for name, value, spec, log in items:
        lo, hi, lg = bounds(spec, log)
        t = (lambda v: math.log(v)) if lg else (lambda v: v)
        width = t(hi) - t(lo)
        for side, bound in (("lower", lo), ("upper", hi)):
            if abs(t(float(value)) - t(bound)) <= share * width:
                out.append({"parameter": name, "value": value, "side": side, "bound": bound, "log": lg})
    return out


def per_size_counts(spec: Any) -> dict[str, int] | int:
    return {str(k): int(v) for k, v in spec.items()} if isinstance(spec, dict) else int(spec)


def overlap_with_test(cfg: ConfigV2, train: list[Any]) -> int:
    """Number of training instance files whose SHA-256 is in the test manifest (must be 0)."""
    path = cfg.output / "instances" / "manifest.json"
    if not path.exists():
        build(cfg)
    test = {e["sha256"] for e in json.loads(path.read_text(encoding="utf-8"))["instances"].values()}
    return sum(hashlib.sha256(i.path.read_bytes()).hexdigest() in test for i in train)


def run(cfg: ConfigV2, methods_to_tune: list[str] | None = None) -> dict[str, Any]:
    import optuna

    spec = cfg.raw["tuning"]
    counts = per_size_counts(spec["instances_per_size"])
    most = max(counts.values()) if isinstance(counts, dict) else counts
    train = select(build(cfg, split="train", sets=list(spec["sets"]), per_size=most), spec["sets"])
    if isinstance(counts, dict):
        train = [i for i in train if int(i.id.split("-")[1]) < counts.get(i.size, most)]
    overlap = overlap_with_test(cfg, train)
    if overlap:
        raise RuntimeError(f"{overlap} training instances have the SHA-256 of a test instance")
    train.sort(key=lambda i: -i.m * i.n)  # largest first: the slowest runs start at once
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
    parallel = int(spec.get("parallel_trials", 1))
    try:
        for name in methods_to_tune or list(TUNED):
            kind, init = TUNED[name]
            log = out_dir / f"{name}.jsonl"
            log.unlink(missing_ok=True)

            def trial_tasks(params: dict[str, Any], kind: str = kind, init: str = init, name: str = name) -> list:
                if kind == "ga":
                    override = {name: {**params, "init": init}}
                    tasks = stochastic_tasks(cfg, "tune", train, [name], "budget", seeds, params_override=override)
                else:
                    tasks = _sa_tasks(cfg, train, name, params, init, seeds)
                for t in tasks:
                    t["z_star"] = z[t["instance"]]
                return tasks

            # Trials run in batches of `parallel_trials` (ask/tell). TPE with constant_liar treats the trials
            # already asked in the batch as running, and the batch is told in trial order after all its runs
            # finished, so the result depends on the seed only (not on which run finishes first).
            sampler = optuna.samplers.TPESampler(seed=int(spec["seed"]), constant_liar=parallel > 1)
            study = optuna.create_study(direction="minimize", sampler=sampler, study_name=name)
            optuna.logging.set_verbosity(optuna.logging.WARNING)
            n_trials = int(spec["trials"])
            while len(study.trials) < n_trials:
                batch = []
                for _ in range(min(parallel, n_trials - len(study.trials))):
                    trial = study.ask()
                    params = suggest(trial, kind, spec["space"])
                    batch.append((trial, params, trial_tasks(params)))
                jobs = [(b, t) for b, (_, _, tasks) in enumerate(batch) for t in tasks]
                jobs.sort(key=lambda j: -int(j[1]["m"]) * int(j[1]["n"]))  # the slowest runs start first
                futures = [(b, pool.submit(methods.execute, t)) for b, t in jobs]
                gaps: list[list[float]] = [[] for _ in batch]
                for b, fut in futures:
                    gaps[b].append(float(fut.result()[0]["gap"]))
                with log.open("a", encoding="utf-8", newline="\n") as fh:
                    for (trial, params, _), g in zip(batch, gaps, strict=True):
                        value = statistics.fmean(g)
                        study.tell(trial, value)
                        line = {"trial": trial.number, "params": params, "mean_gap": value, "runs": len(g)}
                        fh.write(json.dumps(line) + "\n")
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
        }
        | {"parallel_trials": parallel, "constant_liar": parallel > 1},
        "space": spec["space"],
        "training_instances": sorted(i.id for i in train),
        "training_overlap_with_test": overlap,
        "parameters": {k: v["params"] for k, v in results.items()},
        "best_objective": {k: v["mean_gap"] for k, v in results.items()},
        "near_bounds": {k: near_bounds(TUNED[k][0], v["params"], spec["space"]) for k, v in results.items()},
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
