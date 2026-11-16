"""Run the computational experiment: ``python -m tpga.experiments.run --config experiments/paper.yaml``.

Phases (all by default, in this order): ``reachability``, ``main``, ``factorial``, ``applied``,
``timing``. ``--pilot`` runs only the pilot and prints the estimated duration of the full plan.
Results are appended row by row; a repeated call skips every (instance, method, config, seed)
already present, so an interrupted run resumes where it stopped.
"""

from __future__ import annotations

# Thread limits must be in the environment before NumPy is imported here or in a worker.
from tpga.experiments.environment import single_thread_environment

single_thread_environment()

import argparse  # noqa: E402
import csv  # noqa: E402
import json  # noqa: E402
import multiprocessing as mp  # noqa: E402
import os  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from collections.abc import Iterable  # noqa: E402
from concurrent.futures import FIRST_COMPLETED, Future, ProcessPoolExecutor, wait  # noqa: E402
from pathlib import Path  # noqa: E402
from typing import Any  # noqa: E402

from tpga.experiments import environment, instances, reachability  # noqa: E402
from tpga.experiments.config import GA_METHODS, Config, GAParams  # noqa: E402
from tpga.experiments.instances import Instance  # noqa: E402
from tpga.experiments.worker import CURVE_FIELDS, FIELDS, execute, init_worker  # noqa: E402

PHASES = ("reachability", "main", "factorial", "applied", "stopping", "timing")
CLASSICAL_CODES = ("NWC", "LCM", "VAM")


def log(cfg: Config, message: str) -> None:
    line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}"
    print(line, flush=True)
    path = cfg.output / "logs" / "run.log"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")


# --- results files ---------------------------------------------------------------------------


def key_of(row: dict[str, Any]) -> tuple[str, str, str, str]:
    seed = row.get("seed")
    return (str(row["instance"]), str(row["method"]), str(row["config"]), "" if seed in (None, "") else str(seed))


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


class Appender:
    """Append-only CSV writer that flushes every row."""

    def __init__(self, path: Path, fields: list[str]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        new = not path.exists() or path.stat().st_size == 0
        self.fh = path.open("a", newline="", encoding="utf-8")
        self.writer = csv.DictWriter(self.fh, fieldnames=fields, extrasaction="ignore")
        if new:
            self.writer.writeheader()

    def write(self, rows: Iterable[dict[str, Any]]) -> None:
        for r in rows:
            self.writer.writerow(r)
        self.fh.flush()

    def close(self) -> None:
        self.fh.close()


# --- task construction -----------------------------------------------------------------------


def _base(cfg: Config, phase: str, inst: Instance, method: str, config: str) -> dict[str, Any]:
    return {
        "phase": phase,
        "instance": inst.id,
        "suite": inst.suite,
        "size": inst.size,
        "m": inst.m,
        "n": inst.n,
        "path": str(inst.path),
        "method": method,
        "config": config,
        "seed": "",
        "tolerance": cfg.tolerance,
        "repeats": cfg.lp_repeats,
    }


def lp_tasks(cfg: Config, phase: str, items: list[Instance]) -> list[dict[str, Any]]:
    return [_base(cfg, phase, inst, "LP", "highs") for inst in items]


def classical_tasks(cfg: Config, phase: str, items: list[Instance]) -> list[dict[str, Any]]:
    return [_base(cfg, phase, inst, code, "-") for inst in items for code in CLASSICAL_CODES]


def run_reference(cfg: Config, phase: str, items: list[Instance], out: Path, cpus: list[int], classical: bool) -> int:
    """LP optimum of every instance, then the classical methods (they need the optimum for the gap)."""
    _, errors = execute_tasks(cfg, lp_tasks(cfg, phase, items), out, None, cpus, f"{phase}/LP")
    if classical:
        tasks = _with_z(classical_tasks(cfg, phase, items), z_stars(out))
        _, e = execute_tasks(cfg, tasks, out, None, cpus, f"{phase}/classical")
        errors += e
    return errors


def stochastic_tasks(
    cfg: Config,
    phase: str,
    items: list[Instance],
    methods: list[str],
    params: list[GAParams],
    seeds: list[int],
    curve: bool,
    stagnation: int | None | str = "config",
) -> list[dict[str, Any]]:
    budget = cfg.budget
    stop: int | None = cfg.stagnation if stagnation == "config" else (None if stagnation is None else int(stagnation))
    tasks = []
    for inst in items:
        b = budget.of(inst.m, inst.n)
        for method in methods:
            if method == "RS":
                variants: list[GAParams | None] = [None]
            elif method in GA_METHODS:
                variants = list(params)
            else:
                continue
            for gp in variants:
                for seed in seeds:
                    t = _base(cfg, phase, inst, method, budget.rule_id if gp is None else gp.config_id(budget, stop))
                    t.update(seed=seed, budget=b, curve_points=cfg.convergence_points if curve else 0)
                    if gp is not None:
                        t.update(
                            population=gp.population,
                            crossover_rate=gp.crossover_rate,
                            mutation_rate=gp.mutation_rate,
                            tournament=gp.tournament,
                            elite=gp.elite,
                            initialization=GA_METHODS[method],
                            stagnation=stop,
                        )
                    tasks.append(t)
    return tasks


def factorial_params(cfg: Config, spec: dict[str, Any]) -> list[GAParams]:
    base = cfg.ga_base
    return [
        GAParams(int(p), base.crossover_rate, float(pm), base.tournament, base.elite)
        for p in spec["population"]
        for pm in spec["mutation_rate"]
    ]


# --- execution -------------------------------------------------------------------------------


def _warm_up() -> None:
    """Compile (or load from the numba cache) every kernel once before the workers start."""
    from tpga import GAConfig, TransportProblem, run_ga
    from tpga.ga import run_random_search

    p = TransportProblem.random(3, 4, seed=0)
    run_ga(p, GAConfig(population=6, generations=2, seed=0))
    run_random_search(p, 10, seed=0)


def execute_tasks(
    cfg: Config,
    tasks: list[dict[str, Any]],
    out: Path,
    curve_out: Path | None,
    cpus: list[int],
    label: str,
) -> tuple[int, int]:
    """Run the tasks not yet in ``out`` on one worker per CPU in ``cpus``; return (done, errors)."""
    done_keys = {key_of(r) for r in read_rows(out)}
    todo = [t for t in tasks if key_of(t) not in done_keys]
    todo.sort(key=lambda t: -(int(t["m"]) * int(t["n"])) * (int(t.get("budget") or 0) + 1))
    log(
        cfg,
        f"{label}: {len(tasks)} tasks, {len(tasks) - len(todo)} already done, {len(todo)} to run on {len(cpus)} CPUs",
    )
    if not todo:
        return 0, 0
    classes = environment.cpu_classes()
    manager = mp.Manager()
    queue = manager.Queue()
    for c in cpus:
        queue.put(c)
    writer = Appender(out, FIELDS)
    curves = Appender(curve_out, CURVE_FIELDS) if curve_out is not None else None
    errors_path = cfg.output / "logs" / "errors.log"
    done = errors = 0
    t0 = last = time.time()
    try:
        with ProcessPoolExecutor(max_workers=len(cpus), initializer=init_worker, initargs=(queue, classes)) as pool:
            pending: dict[Future, dict[str, Any]] = {}
            it = iter(todo)
            # keep a bounded number of tasks in flight so that an interruption loses little
            for t in it:
                pending[pool.submit(execute, t)] = t
                if len(pending) >= 4 * len(cpus):
                    break
            while pending:
                finished, _ = wait(pending, return_when=FIRST_COMPLETED)
                for fut in finished:
                    task = pending.pop(fut)
                    try:
                        row, rows = fut.result()
                    except Exception as exc:  # noqa: BLE001 - every failure is logged and counted
                        errors += 1
                        with errors_path.open("a", encoding="utf-8") as fh:
                            fh.write(f"{key_of(task)}: {exc!r}\n")
                        continue
                    writer.write([row])
                    if curves is not None and rows:
                        curves.write(rows)
                    done += 1
                    nxt = next(it, None)
                    if nxt is not None:
                        pending[pool.submit(execute, nxt)] = nxt
                now = time.time()
                if now - last > 60 or not pending:
                    rate = done / max(now - t0, 1e-9)
                    eta = (len(todo) - done - errors) / rate if rate else float("nan")
                    log(cfg, f"{label}: {done}/{len(todo)} done, {errors} errors, ETA {eta / 60:.1f} min")
                    last = now
    finally:
        writer.close()
        if curves is not None:
            curves.close()
    return done, errors


def z_stars(path: Path) -> dict[str, float]:
    return {r["instance"]: float(r["cost"]) for r in read_rows(path) if r["method"] == "LP"}


def _with_z(tasks: list[dict[str, Any]], z: dict[str, float]) -> list[dict[str, Any]]:
    missing = {t["instance"] for t in tasks if t["instance"] not in z}
    if missing:
        raise RuntimeError(f"no LP optimum for {sorted(missing)[:5]}")
    for t in tasks:
        t["z_star"] = z[t["instance"]]
    return tasks


def all_cpus(cfg: Config, key: str) -> list[int]:
    count = int(cfg.raw.get(key, os.cpu_count() or 1))
    return list(range(min(count, os.cpu_count() or 1)))


def performance_cpus() -> list[int]:
    classes = environment.cpu_classes()
    if not classes:  # pragma: no cover - non-Windows: no core classes known
        return list(range(os.cpu_count() or 1))
    top = max(classes.values())
    return sorted(c for c, v in classes.items() if v == top)


def select(items: list[Instance], suites: list[str], sizes: list[list[int]] | None = None) -> list[Instance]:
    wanted = {tuple(s) for s in sizes} if sizes else None
    return [i for i in items if i.suite in suites and (wanted is None or (i.m, i.n) in wanted)]


def run_phase(cfg: Config, name: str, items: list[Instance]) -> int:
    spec = cfg.phase(name)
    raw = cfg.output / "raw"
    runs_csv = raw / "runs.csv"
    cpus = all_cpus(cfg, "workers")
    errors = 0
    if name == "reachability":
        reachability.run(cfg, spec)
        return 0
    if name in ("main", "applied"):
        chosen = select(items, spec["suites"], spec.get("sizes"))
        errors += run_reference(cfg, name, chosen, runs_csv, cpus, classical=True)
        seeds = cfg.seeds(spec.get("runs"))
        tasks = stochastic_tasks(cfg, name, chosen, spec["methods"], [cfg.ga_base], seeds, curve=True)
        _, e = execute_tasks(
            cfg, _with_z(tasks, z_stars(runs_csv)), runs_csv, raw / "convergence" / f"{name}.csv", cpus, name
        )
        return errors + e
    if name == "factorial":
        chosen = select(items, [spec["suite"]], spec["sizes"])
        e = run_reference(cfg, name, chosen, runs_csv, cpus, classical=True)
        methods = [m for m, init in GA_METHODS.items() if init in spec["initialization"]]
        tasks = stochastic_tasks(cfg, name, chosen, methods, factorial_params(cfg, spec), cfg.seeds(), curve=False)
        _, e2 = execute_tasks(cfg, _with_z(tasks, z_stars(runs_csv)), runs_csv, None, cpus, name)
        return e + e2
    if name == "stopping":
        # sensitivity of the stopping rule: the same runs with the stagnation limit removed
        chosen = select(items, [spec["suite"]], spec["sizes"])
        errors += run_reference(cfg, name, chosen, runs_csv, cpus, classical=True)
        tasks = stochastic_tasks(cfg, name, chosen, spec["methods"], [cfg.ga_base], cfg.seeds(), True, stagnation=None)
        _, e = execute_tasks(
            cfg, _with_z(tasks, z_stars(runs_csv)), runs_csv, raw / "convergence" / f"{name}.csv", cpus, name
        )
        return errors + e
    if name == "timing":
        chosen = select(items, [spec["suite"]], spec.get("sizes"))
        cpus = performance_cpus() if spec.get("cpu_class") == "performance" else cpus
        timing_csv = raw / "timing.csv"
        e = run_reference(cfg, name, chosen, timing_csv, cpus, classical=False)
        tasks = stochastic_tasks(cfg, name, chosen, spec["methods"], [cfg.ga_base], cfg.seeds(spec["runs"]), False)
        _, e2 = execute_tasks(cfg, _with_z(tasks, z_stars(timing_csv)), timing_csv, None, cpus, f"{name}/ga")
        return e + e2
    raise ValueError(f"unknown phase {name!r}")  # pragma: no cover - cfg.phase validated it


def pilot(cfg: Config, items: list[Instance]) -> dict[str, Any]:
    """Short run on one instance per size; returns the measured times and the estimate of the full plan."""
    spec = cfg.phase("pilot")
    out_dir = cfg.output / "pilot"
    runs_csv = out_dir / "runs.csv"
    chosen = [i for i in items if i.suite == "uniform" and i.id.endswith("-00")]
    chosen += [i for i in items if i.id in set(spec.get("applied_ids", []))]
    cpus = all_cpus(cfg, "workers")
    run_reference(cfg, "pilot", chosen, runs_csv, cpus, classical=True)
    tasks = stochastic_tasks(cfg, "pilot", chosen, spec["methods"], [cfg.ga_base], cfg.seeds(spec["runs"]), False)
    execute_tasks(cfg, _with_z(tasks, z_stars(runs_csv)), runs_csv, None, cpus, "pilot")
    rows = read_rows(runs_csv)
    per: dict[tuple[str, str], list[float]] = {}
    for r in rows:
        per.setdefault((r["instance"], r["method"]), []).append(float(r["time_s"]))
    mean = {k: sum(v) / len(v) for k, v in per.items()}
    by_size = {
        (i.m, i.n): {m: mean.get((i.id, m)) for m in ("LP", "NWC", "LCM", "VAM", "RS", "GA-rand", "GA-cost")}
        for i in chosen
    }
    estimate = estimate_plan(cfg, items, by_size, {i.id: i for i in chosen})
    result = {"measured_mean_time_s": {f"{m}x{n}": v for (m, n), v in by_size.items()}, **estimate}
    (out_dir / "estimate.json").write_text(json.dumps(result, indent=1), encoding="utf-8")
    return result


def estimate_plan(
    cfg: Config, items: list[Instance], by_size: dict[tuple[int, int], dict[str, float | None]], pilots: dict
) -> dict[str, Any]:
    """Core-seconds of every phase from the pilot means, assuming time depends on size and method only."""
    sec: dict[str, float] = {}

    def t(inst: Instance, method: str) -> float:
        own = by_size.get((inst.m, inst.n))
        if own and own.get(method) is not None:
            return float(own[method] or 0.0)
        # applied instances without a pilot: scale the closest uniform size by m*n
        ref = min(by_size, key=lambda s: abs(s[0] * s[1] - inst.m * inst.n))
        base = by_size[ref].get(method) or 0.0
        return float(base) * inst.m * inst.n / (ref[0] * ref[1])

    for name in ("main", "factorial", "applied", "stopping", "timing"):
        spec = cfg.phase(name)
        if name == "factorial":
            chosen = select(items, [spec["suite"]], spec["sizes"])
            k = len(factorial_params(cfg, spec)) * cfg.runs
            sec[name] = sum(t(i, "GA-rand") * k + t(i, "GA-cost") * k for i in chosen)
        else:
            suites = spec.get("suites", [spec.get("suite")])
            chosen = select(items, suites, spec.get("sizes"))
            runs = int(spec.get("runs", cfg.runs))
            sec[name] = sum(t(i, m) * runs for i in chosen for m in spec["methods"] if m in ("RS", *GA_METHODS))
    workers = len(all_cpus(cfg, "workers"))
    p_cores = len(performance_cpus())
    wall = {k: v / (p_cores if k == "timing" else workers) for k, v in sec.items()}
    return {
        "core_seconds": sec,
        "wall_seconds_estimate": wall,
        "total_wall_hours_estimate": sum(wall.values()) / 3600,
        "workers": workers,
        "performance_cores": p_cores,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m tpga.experiments.run", description=__doc__)
    ap.add_argument("--config", required=True)
    ap.add_argument("--phase", action="append", choices=PHASES, help="run only these phases (repeatable)")
    ap.add_argument("--pilot", action="store_true", help="run the pilot and print the estimated duration")
    args = ap.parse_args(argv)
    cfg = Config.load(args.config)
    cfg.output.mkdir(parents=True, exist_ok=True)
    items = instances.build(cfg)
    _warm_up()
    if args.pilot:
        result = pilot(cfg, items)
        log(
            cfg,
            f"pilot estimate: {result['total_wall_hours_estimate']:.2f} h; "
            f"{json.dumps(result['wall_seconds_estimate'])}",
        )
        return 0
    env_path = cfg.output / "environment.json"
    env = environment.describe(cfg.root)
    env["config"] = str(cfg.path.relative_to(cfg.root)) if cfg.path.is_relative_to(cfg.root) else str(cfg.path)
    previous = json.loads(env_path.read_text(encoding="utf-8")) if env_path.exists() else {}
    env["phases"] = previous.get("phases", {})
    # every invocation keeps its own snapshot (code version, power scheme, ...); the top level is the latest
    invocations = list(previous.get("invocations", []))
    if not invocations and previous.get("git_commit"):
        invocations.append({k: v for k, v in previous.items() if k not in ("phases", "invocations")})
    snapshot = {k: v for k, v in env.items() if k != "phases"}
    snapshot["phases_run"] = list(args.phase or PHASES)
    invocations.append(snapshot)
    env["invocations"] = invocations
    errors = 0
    for name in args.phase or PHASES:
        start = time.time()
        log(cfg, f"phase {name} started")
        e = run_phase(cfg, name, items)
        errors += e
        elapsed = time.time() - start
        env["phases"].setdefault(name, []).append(
            {"started": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(start)), "wall_s": elapsed, "errors": e}
        )
        env_path.write_text(json.dumps(env, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        log(cfg, f"phase {name} finished in {elapsed / 60:.1f} min with {e} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
