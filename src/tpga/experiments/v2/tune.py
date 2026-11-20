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
from tpga.experiments.v2 import memory, methods
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


JOURNAL = "optuna-journal.log"
RESERVE_BYTES = memory.RESERVE_BYTES


def worst_case_bytes(population: int, arcs: int) -> int:
    """Peak memory of one GA run (see :mod:`tpga.experiments.v2.memory` for the measurements)."""
    return memory.ga_bytes(population, arcs)


def safe_workers(requested: int, per_worker: int, available: int, reserve: int = RESERVE_BYTES) -> int:
    """Largest number of worker processes, at most ``requested``, whose worst case fits in free memory."""
    return max(1, min(int(requested), int((available - reserve) // max(1, per_worker))))


def journal_storage(out_dir: Any) -> Any:
    """Optuna study on disk (one journal file for all tuned methods); a crash loses at most the batch in flight."""
    from optuna.storages import JournalStorage
    from optuna.storages.journal import JournalFileBackend, JournalFileOpenLock

    path = str(out_dir / JOURNAL)
    return JournalStorage(JournalFileBackend(path, lock_obj=JournalFileOpenLock(path)))


def write_log(study: Any, path: Any) -> None:
    """Trial log (one line per finished trial, in trial order), rewritten from the stored study."""
    from optuna.trial import TrialState

    lines = []
    for t in sorted(study.get_trials(deepcopy=False, states=(TrialState.COMPLETE,)), key=lambda t: t.number):
        a = t.user_attrs
        row = {"trial": t.number, "batch": a["batch"], "params": a["params"], "mean_gap": t.value, "runs": a["runs"]}
        lines.append(json.dumps(row))
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text("".join(line + "\n" for line in lines), encoding="utf-8", newline="\n")
    tmp.replace(path)


def recover(study: Any, evaluate: Any) -> dict[str, int]:
    """Bring a study left by a crash back to a state an uninterrupted run passes through.

    A trial that was asked but not told belongs to the batch in flight. If some trial of its batch was already
    told, the batch is finished with the stored parameters (same runs, same values). Otherwise the trial is
    marked FAIL (failed trials are ignored by the sampler) and the whole batch is asked again: the sampler is
    seeded per batch, so it proposes the same parameters again.
    """
    from optuna.trial import Trial, TrialState

    trials = study.get_trials(deepcopy=False)
    told = {t.user_attrs.get("batch") for t in trials if t.state == TrialState.COMPLETE}
    out = {"finished": 0, "failed": 0}
    for t in sorted(trials, key=lambda t: t.number):
        if t.state not in (TrialState.RUNNING, TrialState.WAITING):
            continue
        if t.user_attrs.get("batch") in told and "params" in t.user_attrs:
            value, runs = evaluate([t.user_attrs["params"]])[0]
            Trial(study, t._trial_id).set_user_attr("runs", runs)
            study.tell(t.number, value)
            out["finished"] += 1
        else:
            study.tell(t.number, state=TrialState.FAIL)
            out["failed"] += 1
    return out


def run(
    cfg: ConfigV2, methods_to_tune: list[str] | None = None, *, stop_after_batches: int | None = None
) -> dict[str, Any]:
    """Tune every method (or ``methods_to_tune``); resumes from the journal in ``<output>/tuning`` if present.

    ``stop_after_batches`` ends the run early, between two batches (used by the tests to simulate a crash).
    """
    import time

    import optuna
    from optuna.trial import TrialState

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
    storage = journal_storage(out_dir)
    classes = environment.cpu_classes()
    pop_hi = int(bounds(spec["space"]["ga"]["population"], True)[1])
    per_worker = worst_case_bytes(pop_hi, max(i.m * i.n for i in train))
    workers = int(cfg.raw.get("workers", 24))
    free = environment.usable_memory_bytes()
    print(
        f"workers: {workers} of {workers}; runs start only while their memory is free "
        f"(worst case {per_worker / 2**30:.2f} GB per run, {free / 2**30:.1f} GB usable now)",
        flush=True,
    )
    manager = mp.Manager()
    cpus = list(range(workers))
    q = manager.Queue()
    for c in cpus:
        q.put(c)
    pool = ProcessPoolExecutor(len(cpus), initializer=init_worker, initargs=(q, classes, None, "normal", 1.0))
    results: dict[str, Any] = {}
    parallel = int(spec.get("parallel_trials", 1))
    seed = int(spec["seed"])
    n_trials = int(spec["trials"])
    batches_run = 0
    gate_log: list[dict[str, int]] = []
    started = time.time()
    try:
        with environment.keep_awake():
            for name in methods_to_tune or list(TUNED):
                kind, init = TUNED[name]
                log = out_dir / f"{name}.jsonl"

                def trial_tasks(params: dict[str, Any], kind: str = kind, init: str = init, name: str = name) -> list:
                    if kind == "ga":
                        override = {name: {**params, "init": init}}
                        tasks = stochastic_tasks(cfg, "tune", train, [name], "budget", seeds, params_override=override)
                    else:
                        tasks = _sa_tasks(cfg, train, name, params, init, seeds)
                    for t in tasks:
                        t["z_star"] = z[t["instance"]]
                    return tasks

                def evaluate(batch_params: list[dict[str, Any]], trial_tasks: Any = trial_tasks) -> list:
                    """Mean gap and number of runs of every parameter set; all runs of the batch at once."""
                    jobs = [(b, t) for b, p in enumerate(batch_params) for t in trial_tasks(p)]
                    jobs.sort(key=lambda j: -int(j[1]["m"]) * int(j[1]["n"]))  # the slowest runs start first
                    gate = memory.MemoryGate(workers)  # budget: memory usable at the start of the batch
                    values: list[float | None] = [None] * len(jobs)
                    for i, fut in memory.run_gated(
                        pool, methods.execute, [t for _, t in jobs], memory.task_bytes, gate
                    ):
                        values[i] = float(fut.result()[0]["gap"])
                    gate_log.append({"runs": len(jobs), "peak_running": gate.peak_running, "held": gate.held_back})
                    gaps: list[list[float]] = [[] for _ in batch_params]
                    for (b, _), v in zip(jobs, values, strict=True):  # job order, as before the gate
                        gaps[b].append(float(v))  # type: ignore[arg-type]
                    return [(statistics.fmean(g), len(g)) for g in gaps]

                # Trials run in batches of `parallel_trials` (ask/tell). Batch k is proposed by
                # TPESampler(seed + k, constant_liar): the trials already asked in the batch count as running.
                # A batch is told in trial order after all its runs finished. The proposals depend on the seed
                # and the stored results only, so a run resumed from the journal repeats an uninterrupted one.
                study = optuna.create_study(direction="minimize", study_name=name, storage=storage, load_if_exists=True)
                optuna.logging.set_verbosity(optuna.logging.WARNING)
                fixed = recover(study, evaluate)
                if fixed["finished"] or fixed["failed"]:
                    print(
                        f"{name}: resumed; {fixed['finished']} trials finished, {fixed['failed']} asked again",
                        flush=True,
                    )

                def done(study: Any = study) -> int:
                    return len(study.get_trials(deepcopy=False, states=(TrialState.COMPLETE,)))

                while done() < n_trials:
                    if stop_after_batches is not None and batches_run >= stop_after_batches:
                        return {}
                    k = done() // parallel
                    study.sampler = optuna.samplers.TPESampler(seed=seed + k, constant_liar=parallel > 1)
                    batch = []
                    for _ in range(min(parallel, n_trials - done())):
                        trial = study.ask()
                        params = suggest(trial, kind, spec["space"])
                        trial.set_user_attr("params", params)
                        trial.set_user_attr("batch", k)
                        batch.append((trial, params))
                    values = evaluate([p for _, p in batch])
                    for (trial, _), (value, runs) in zip(batch, values, strict=True):
                        trial.set_user_attr("runs", runs)
                        study.tell(trial, value)
                    batches_run += 1
                    write_log(study, log)
                    print(
                        f"{name}: {done()}/{n_trials} trials, best mean gap {study.best_value:.3f} %, "
                        f"{(time.time() - started) / 60:.1f} min",
                        flush=True,
                    )
                    g = gate_log[-1]
                    print(
                        f"  memory: up to {g['peak_running']} of {workers} runs at once"
                        + (f", a run waited for memory {g['held']} times" if g["held"] else ""),
                        flush=True,
                    )
                write_log(study, log)
                best = study.best_trial
                results[name] = {"params": best.user_attrs["params"], "mean_gap": best.value, "trials": done()}
    finally:
        pool.shutdown()
        manager.shutdown()
    frozen = {
        "frozen": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "git_commit": environment.describe(cfg.root).get("git_commit"),
        "procedure": {
            k: spec[k] for k in ("sampler", "seed", "trials", "sets", "instances_per_size", "seeds", "objective")
        }
        | {
            "parallel_trials": parallel,
            "constant_liar": parallel > 1,
            "sampler_seed": "seed + batch index",
            "storage": f"optuna JournalStorage, {out_dir.name}/{JOURNAL}",
        },
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
