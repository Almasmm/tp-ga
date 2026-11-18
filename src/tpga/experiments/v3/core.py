"""Configuration, instances, tasks and the parallel runner of the additional experiment v3.

Two configurations share this module: ``experiments/paper-v3-cycle.yaml`` (choice of k and the linear
problem) and ``experiments/paper-v3-fctp.yaml`` (fixed-charge problem). Every finished run is appended to a
JSON-lines file at once; a new start skips the keys that are already there.
"""

from __future__ import annotations

import hashlib
import json
import signal
import statistics
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import numpy as np
import yaml

from tpga.classical import vogel
from tpga.cycle import GAXConfig, run_ga_x
from tpga.exact import solve_lp_highspy
from tpga.experiments import environment
from tpga.experiments.v2 import instances as v2_instances
from tpga.experiments.v2 import methods as v2_methods
from tpga.experiments.v2.storage import append_jsonl, read_jsonl, write_atomic
from tpga.experiments.v2.tasks import ga_config_id, sa_config_id
from tpga.fctp import (
    FixedChargeProblem,
    balinski,
    generate,
    run_random_search_fc,
    run_sa_fc,
    solve_mip,
    vogel_linearised,
)
from tpga.ga import run_ga, run_random_search
from tpga.model import TransportProblem
from tpga.sa import SAConfig, run_sa
from tpga.verify import check_plan

KEY_FIELDS = ("phase", "instance", "method", "config", "seed")
TOLERANCE = 1e-9
DECODER_TOL = 1e-12
STOCHASTIC = ("rs", "ga", "sa", "gax")


def key_of(row: dict[str, Any]) -> str:
    return "|".join("" if row.get(k) is None else str(row.get(k)) for k in KEY_FIELDS)


class ConfigV3:
    """A v3 configuration file; relative paths are resolved from the repository root."""

    def __init__(self, raw: dict[str, Any], path: Path) -> None:
        self.raw = raw
        self.path = path

    @classmethod
    def load(cls, path: str | Path) -> ConfigV3:
        p = Path(path).resolve()
        data = yaml.safe_load(p.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("problem") not in ("linear", "fctp"):
            raise ValueError("a v3 configuration needs problem: linear or fctp")
        return cls(data, p)

    @property
    def root(self) -> Path:
        if "root" in self.raw:
            return Path(self.raw["root"]).resolve()
        return self.path.parent.parent if self.path.parent.name == "experiments" else self.path.parent

    def resolve(self, value: str | Path) -> Path:
        p = Path(value)
        return p if p.is_absolute() else self.root / p

    @property
    def output(self) -> Path:
        return self.resolve(self.raw["output"])

    @property
    def area(self) -> Path:
        """Directory of this problem inside the output directory (``linear`` or ``fctp``)."""
        return self.output / str(self.raw["problem"])

    @property
    def workers(self) -> int:
        return int(self.raw.get("workers", 1))

    def seeds(self, runs: int | None = None) -> list[int]:
        return [int(self.raw["base_seed"]) + r for r in range(int(self.raw["runs"]) if runs is None else runs)]

    def budget(self, m: int, n: int) -> int:
        return int(self.raw["budget_factor"]) * m * n

    def tuned(self) -> dict[str, dict[str, Any]]:
        data = yaml.safe_load(self.resolve(self.raw["tuned_parameters"]).read_text(encoding="utf-8"))
        return dict(data["parameters"])

    @property
    def selected_path(self) -> Path:
        return self.resolve(self.raw.get("selected_k", Path(self.raw["output"]) / "kselect" / "selected.json"))

    def selected(self) -> dict[str, dict[str, Any]]:
        if not self.selected_path.exists():
            raise RuntimeError(f"{self.selected_path} is missing: run the command kselect first")
        return dict(json.loads(self.selected_path.read_text(encoding="utf-8"))["selected"])

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.path.read_bytes()).hexdigest()


# --- instances -----------------------------------------------------------------------------


def _write_instance(path: Path, data: dict[str, Any]) -> str:
    text = json.dumps(data, separators=(",", ":")) + "\n"
    if not path.exists() or path.read_bytes() != text.encode("utf-8"):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_linear(cfg: ConfigV3, groups: list[dict[str, Any]], root: Path) -> list[dict[str, Any]]:
    """Generate (or verify) linear instances with the generators and the Z_rand rule of v0.4; the optimum
    Z* comes from HiGHS. ``groups`` are entries ``{set, size, first_seed, count, prefix, suffix}``."""
    manifest_path = root / "manifest.json"
    entries = json.loads(manifest_path.read_text(encoding="utf-8"))["instances"] if manifest_path.exists() else {}
    base = int(cfg.raw["instance_seed_base"])
    samples = int(cfg.raw.get("zrand_samples", 1000))
    out = []
    for g in groups:
        m, n = (int(v) for v in g["size"])
        spec = cfg.raw["generators"][g["set"]]
        for k in range(int(g["count"])):
            seed = int(g["first_seed"]) + k
            iid = f"{g['prefix']}{m}x{n}-{k:02d}{g.get('suffix', '')}"
            path = root / g["set"] / f"{iid}.json"
            data = v2_instances.GENERATORS[g["set"]](m, n, seed, spec)
            digest = _write_instance(path, data)
            entry = entries.get(iid)
            if entry is None or entry.get("sha256") != digest:
                problem = TransportProblem.from_dict(data)
                zr_seed = v2_instances.zrand_seed(iid, base)
                entry = {
                    "id": iid,
                    "set": g["set"],
                    "m": m,
                    "n": n,
                    "seed": seed,
                    "file": path.relative_to(root).as_posix(),
                    "sha256": digest,
                    "z_star": solve_lp_highspy(problem).cost,
                    "z_rand": v2_instances.z_rand(problem, samples, zr_seed, DECODER_TOL),
                    "z_rand_samples": samples,
                    "z_rand_seed": zr_seed,
                    "generator": f"tpga.experiments.v2.instances.{v2_instances.GENERATORS[g['set']].__name__}",
                }
                entries[iid] = entry
            out.append({**entry, "path": str(path), "size": f"{m}x{n}"})
    root.mkdir(parents=True, exist_ok=True)
    write_atomic(manifest_path, {"instances": entries})
    return out


def build_fctp(cfg: ConfigV3) -> list[dict[str, Any]]:
    """Generate (or verify) the fixed-charge instances of amendment 8.4."""
    spec = cfg.raw["instances"]
    root = cfg.area / "instances"
    base = int(spec["seed_base"])
    lo, hi = spec["cost"]
    s_lo, s_hi = spec["supply"]
    gen = {"cost_low": lo, "cost_high": hi, "supply_low": s_lo, "supply_high": s_hi}
    entries = {}
    out = []
    for s, (m, n) in enumerate(spec["sizes"]):
        for q, rho in enumerate(spec["rho"]):
            for i in range(int(spec["count"])):
                seed = base + 1000 * s + 100 * q + i
                iid = f"f{m}x{n}-r{rho:g}-{i:02d}"
                path = root / f"{iid}.json"
                data = generate(int(m), int(n), seed, float(rho), gen)
                digest = _write_instance(path, data)
                entry = {
                    "id": iid,
                    "set": "fctp",
                    "m": int(m),
                    "n": int(n),
                    "rho": float(rho),
                    "seed": seed,
                    "fixed_high": data["fixed_high"],
                    "file": path.name,
                    "sha256": digest,
                    "generator": "tpga.fctp.generate",
                }
                entries[iid] = entry
                out.append({**entry, "path": str(path), "size": f"{m}x{n}"})
    write_atomic(root / "manifest.json", {"instances": entries})
    return out


# --- tasks ---------------------------------------------------------------------------------


def method_fields(cfg: ConfigV3, name: str, mutation: dict[str, Any] | None = None) -> dict[str, Any]:
    """Kind, parameters, start and configuration id of a configured method. ``mutation`` replaces the
    mutation of a ``gax`` method (grid of the choice of k); ``mutation: selected`` reads the chosen k."""
    spec = cfg.raw["methods"][name]
    kind = spec["kind"]
    init = spec.get("initialization")
    fields: dict[str, Any] = {"method": name, "kind": kind, "initialization": init, "params": {}, "config": "-"}
    if "tuned" in spec:
        params = dict(cfg.tuned()[spec["tuned"]])
        if kind in ("ga", "gax"):
            if mutation is None and spec.get("mutation") == "selected":
                mutation = cfg.selected()[spec.get("select_as", name)]
            if mutation is not None:
                params["mutation_mode"] = mutation["mode"]
                params["mutation_strength"] = mutation["strength"]
            ls = int(spec.get("local_search_every", 0))
            fields["local_search_every"] = ls
            fields["config"] = ga_config_id(params, str(init), "budget") + (f"-ls{ls}" if ls else "")
        else:
            fields["config"] = sa_config_id(params, str(init), "budget")
        fields["params"] = params
    return fields


def make_task(
    cfg: ConfigV3, phase: str, inst: dict[str, Any], method: dict[str, Any], seed: int | None
) -> dict[str, Any]:
    stochastic = method["kind"] in STOCHASTIC
    budget = cfg.budget(inst["m"], inst["n"]) if stochastic else None
    config = f"B{budget}" if method["kind"] == "rs" else method["config"]
    return {
        **method,
        "config": config,
        "problem": cfg.raw["problem"],
        "phase": phase,
        "set": inst["set"],
        "instance": inst["id"],
        "size": inst["size"],
        "m": inst["m"],
        "n": inst["n"],
        "rho": inst.get("rho"),
        "path": inst["path"],
        "z_star": inst.get("z_star"),
        "z_rand": inst.get("z_rand"),
        "seed": seed if stochastic else None,
        "budget": budget,
        "stop": {},
        "decoder_tol": DECODER_TOL,
        "mip": cfg.raw.get("mip"),
    }


def plan_tasks(
    cfg: ConfigV3, phase: str, items: list[dict[str, Any]], methods: list[str], seeds: list[int]
) -> list[dict[str, Any]]:
    tasks = []
    for inst in items:
        for name in methods:
            fields = method_fields(cfg, name)
            for seed in seeds if fields["kind"] in STOCHASTIC else [None]:
                tasks.append(make_task(cfg, phase, inst, fields, seed))
    return tasks


# --- one run -------------------------------------------------------------------------------


def _gax_config(task: dict[str, Any]) -> GAXConfig:
    p = task["params"]
    return GAXConfig(
        population=int(p["population"]),
        crossover_rate=float(p["crossover_rate"]),
        tournament=int(p["tournament"]),
        elite=int(p["elite"]),
        max_evaluations=int(task["budget"]),
        mutation_mode=p["mutation_mode"],
        mutation_strength=float(p["mutation_strength"]),
        initialization=task["initialization"],
        seed=int(task["seed"]),
        local_search_every=int(task.get("local_search_every", 0)),
        decoder_tol=float(task["decoder_tol"]),
    )


def _run_fields(result: Any) -> dict[str, Any]:
    out = {
        "time_s": result.runtime_s,
        "evals": result.evaluations,
        "best_eval": result.best_evaluation,
        "generations": result.generations,
        "stop_reason": result.stop_reason,
    }
    for name in (
        "pivots",
        "zero_pivots",
        "unchanged_offspring",
        "local_search_calls",
        "local_search_evaluations",
        "local_search_improvements",
    ):
        if hasattr(result, name):
            out[name] = getattr(result, name)
    return out


def _feasible(problem: TransportProblem, x: np.ndarray, label: str) -> float:
    check = check_plan(problem, x, rtol=TOLERANCE)
    if not check.feasible:
        raise RuntimeError(f"infeasible plan from {label}: {check}")
    return max(check.max_row_residual, check.max_col_residual, max(0.0, -check.min_value))


def execute(task: dict[str, Any]) -> dict[str, Any]:
    """Run one task and return its record."""
    record: dict[str, Any] = {
        k: task.get(k) for k in ("problem", *KEY_FIELDS, "set", "size", "m", "n", "rho", "budget", "kind")
    }
    record["started"] = time.time()
    kind = task["kind"]
    label = f"{task['method']} on {task['instance']} seed {task['seed']}"
    if task["problem"] == "linear":
        problem = v2_methods.load(task["path"])
        if kind == "classical":
            t0 = time.perf_counter()
            out = vogel(problem)
            x, cost, extra = out.x, out.cost, {"time_s": time.perf_counter() - t0}
        else:
            if kind == "rs":
                res = run_random_search(problem, int(task["budget"]), seed=int(task["seed"]), decoder_tol=DECODER_TOL)
            elif kind == "ga":
                res = run_ga(problem, v2_methods.ga_config(task))
            elif kind == "sa":
                res = run_sa(problem, v2_methods.sa_config(task))
            else:
                res = run_ga_x(problem, _gax_config(task))
            x, cost, extra = res.x, res.cost, _run_fields(res)
        z = float(task["z_star"])
        if cost < z - TOLERANCE * max(1.0, abs(z)):
            raise RuntimeError(f"{label} reports {cost} below the optimum {z}")
        record.update(
            extra,
            cost=cost,
            z_star=z,
            z_rand=task.get("z_rand"),
            gap=v2_methods.gap(cost, z),
            gap_norm=v2_methods.gap_norm(cost, z, task.get("z_rand")),
            optimal=abs(cost - z) <= TOLERANCE * max(1.0, abs(z)),
            max_residual=_feasible(problem, x, label),
        )
    else:
        fcp = FixedChargeProblem.from_json(task["path"])
        if kind == "mip":
            opts = task.get("mip") or {}
            mip = solve_mip(
                fcp,
                time_limit=float(opts.get("time_limit_s", 60)),
                threads=int(opts.get("threads", 1)),
                rel_gap=float(opts.get("rel_gap", 0.0)),
                abs_gap=float(opts.get("abs_gap", 0.99)),
            )
            record.update(
                cost=mip.cost,
                objective=mip.objective,
                bound=mip.bound,
                mip_gap=mip.gap,
                status=mip.status,
                proved=mip.proved,
                time_s=mip.time_s,
                nodes=mip.nodes,
                highs_version=mip.version,
            )
            if mip.x is not None:
                record["max_residual"] = _feasible(fcp.problem, mip.x, label)
        else:
            if kind == "balinski":
                t0 = time.perf_counter()
                x, cost, lp_value = balinski(fcp)
                extra = {"time_s": time.perf_counter() - t0, "lp_bound": lp_value}
            elif kind == "vam_lin":
                t0 = time.perf_counter()
                x, cost = vogel_linearised(fcp)
                extra = {"time_s": time.perf_counter() - t0}
            else:
                if kind == "rs":
                    res = run_random_search_fc(fcp, int(task["budget"]), seed=int(task["seed"]))
                elif kind == "sa":
                    p = task["params"]
                    res = run_sa_fc(
                        fcp,
                        SAConfig(
                            max_evaluations=int(task["budget"]),
                            insertion_probability=float(p["insertion_probability"]),
                            initial_acceptance=float(p["initial_acceptance"]),
                            final_ratio=float(p["final_ratio"]),
                            initialization=task["initialization"],
                            seed=int(task["seed"]),
                        ),
                    )
                elif kind == "gax":
                    res = run_ga_x(fcp.problem, _gax_config(task), fixed=fcp.fixed, start_problem=fcp.linearised())
                else:
                    raise ValueError(f"unknown method kind {kind!r} for the fixed-charge problem")
                x, cost, extra = res.x, res.cost, _run_fields(res)
            record.update(extra, cost=cost, max_residual=_feasible(fcp.problem, x, label))
    record["finished"] = time.time()
    return record


# --- parallel runner -----------------------------------------------------------------------


def _init_worker() -> None:
    environment.single_thread_environment()
    for sig in ("SIGINT", "SIGBREAK"):
        if hasattr(signal, sig):
            signal.signal(getattr(signal, sig), signal.SIG_IGN)


def _weight(task: dict[str, Any]) -> float:
    """Rough relative duration, used only to start the longest runs first."""
    if task["kind"] == "mip":
        return 1e12
    return float(task["m"] * task["n"]) ** 2 * (2.0 if task["kind"] in ("ga", "gax", "rs") else 1.0)


def run_tasks(cfg: ConfigV3, tasks: list[dict[str, Any]], raw: Path, label: str, workers: int | None = None) -> dict:
    """Run the tasks that are not in ``raw`` yet; append every record to ``raw`` when it is finished."""
    raw.parent.mkdir(parents=True, exist_ok=True)
    done = {key_of(r) for r in read_jsonl(raw)}
    todo = sorted((t for t in tasks if key_of(t) not in done), key=_weight, reverse=True)
    count = cfg.workers if workers is None else workers
    started = time.time()
    failed: list[str] = []
    finished = 0
    last = [started]

    def store(task: dict[str, Any], record: dict[str, Any] | None, error: BaseException | None) -> None:
        nonlocal finished
        if record is not None:
            append_jsonl(raw, record)
            finished += 1
        else:
            failed.append(f"{key_of(task)}: {error!r}")
            append_jsonl(
                raw.with_name("errors.jsonl"), {"key": key_of(task), "error": repr(error), "time": time.time()}
            )
        now = time.time()
        if now - last[0] >= 30 or finished + len(failed) == len(todo):
            last[0] = now
            print(f"{label}: {finished + len(failed)}/{len(todo)} runs, {now - started:.0f} s", flush=True)

    print(f"{label}: {len(todo)} runs to do, {len(tasks) - len(todo)} on disk, {count} at once", flush=True)
    with environment.keep_awake():
        if count <= 1 or len(todo) <= 1:
            for task in todo:
                try:
                    store(task, execute(task), None)
                except Exception as exc:  # noqa: BLE001 - recorded, the other runs go on
                    store(task, None, exc)
        else:
            with ProcessPoolExecutor(max_workers=count, initializer=_init_worker) as pool:
                futures = {pool.submit(execute, t): t for t in todo}
                for fut in as_completed(futures):
                    try:
                        store(futures[fut], fut.result(), None)
                    except Exception as exc:  # noqa: BLE001
                        store(futures[fut], None, exc)
    summary = {
        "label": label,
        "planned": len(tasks),
        "ran": finished,
        "failed": len(failed),
        "wall_s": time.time() - started,
    }
    if failed:
        raise RuntimeError(f"{label}: {len(failed)} runs failed, first: {failed[0]}")
    return summary


def records(raw: Path, phase: str | None = None) -> list[dict[str, Any]]:
    rows = read_jsonl(raw)
    return [r for r in rows if phase is None or r.get("phase") == phase]


# --- commands ------------------------------------------------------------------------------


def linear_groups(cfg: ConfigV3, reduced: bool) -> list[dict[str, Any]]:
    groups = []
    for g in cfg.raw["instances"]:
        count = int(g["reduced_count"]) if reduced and "reduced_count" in g else int(g["count"])
        groups.append({**g, "count": count})
    return groups


def kselect(cfg: ConfigV3) -> dict[str, Any]:
    """Choice of k (amendment 8.2). Writes ``kselect/records.jsonl``, ``kselect.csv`` and ``selected.json``."""
    spec = cfg.raw["kselect"]
    out = cfg.output / "kselect"
    raw = out / "records.jsonl"
    seeds = cfg.seeds(int(spec["runs"]))
    grid = list(spec["grid"])
    variants = list(spec["variants"])
    parallel = int(spec["parallel_runs"])

    def tasks_for(count: int) -> list[dict[str, Any]]:
        groups = [{**g, "count": count} for g in spec["instances"]]
        items = build_linear(cfg, groups, out / "instances")
        return [
            make_task(cfg, "kselect", inst, method_fields(cfg, v, mutation=g), seed)
            for inst in items
            for v in variants
            for g in grid
            for seed in seeds
        ]

    full = tasks_for(int(spec["instances_per_size"]))
    probe_at = spec["probe"]
    probe = [
        t
        for t in full
        if t["instance"] == probe_at["instance"]
        and t["seed"] == seeds[0]
        and t["params"]["mutation_mode"] == probe_at["mode"]
    ]
    assert len(probe) == len(variants), "one probe run per variant"
    run_tasks(cfg, probe, raw, "kselect probe", workers=min(cfg.workers, len(probe)))
    times = {r["method"]: r["time_s"] for r in records(raw) if key_of(r) in {key_of(t) for t in probe}}
    large = max(t["m"] * t["n"] for t in full)
    estimate = 0.0
    for t in full:
        estimate += times[t["method"]] * (1.0 if t["m"] * t["n"] == large else float(spec["small_time_ratio"]))
    estimate /= parallel
    limit = 60.0 * float(spec["time_limit_min"])
    reduced = estimate > limit
    tasks = tasks_for(int(spec["reduced_instances_per_size"])) if reduced else full
    summary = run_tasks(cfg, tasks, raw, "kselect")
    keys = {key_of(t) for t in tasks}
    rows = [r for r in records(raw) if key_of(r) in keys]
    table = []
    for v in variants:
        for rank, g in enumerate(grid):
            label = method_fields(cfg, v, mutation=g)["config"]
            mine = [r for r in rows if r["method"] == v and r["config"] == label]
            assert len(mine) == len(tasks) // (len(variants) * len(grid)), "every run of the grid is on disk"
            by_size = {}
            for size in sorted({r["size"] for r in mine}, key=lambda s: int(s.split("x")[0])):
                by_size[size] = statistics.fmean(r["gap_norm"] for r in mine if r["size"] == size)
            table.append(
                {
                    "variant": v,
                    "k": _k_label(g),
                    "mode": g["mode"],
                    "strength": g["strength"],
                    "rank": rank,
                    "runs": len(mine),
                    "mean_gap_norm": statistics.fmean(r["gap_norm"] for r in mine),
                    "mean_gap_percent": statistics.fmean(r["gap"] for r in mine),
                    **{f"mean_gap_norm_{s}": val for s, val in by_size.items()},
                    "time_median_s": statistics.median(r["time_s"] for r in mine),
                }
            )
    selected = {}
    for v in variants:
        best = min((row for row in table if row["variant"] == v), key=lambda row: (row["mean_gap_norm"], row["rank"]))
        selected[v] = {"mode": best["mode"], "strength": best["strength"], "k": best["k"]}
        for row in table:
            if row["variant"] == v:
                row["selected"] = row is best
    result = {
        "selected": selected,
        "probe_times_s": times,
        "estimate_s": estimate,
        "limit_s": limit,
        "reduced_training_set": reduced,
        "instances": sorted({t["instance"] for t in tasks}),
        "seeds": seeds,
        "wall_s": summary["wall_s"],
        "rule": "smallest mean normalised gap over training instances and seeds; ties: the earlier grid entry",
    }
    write_atomic(out / "selected.json", result)
    write_csv(out / "kselect.csv", table)
    return result


def _k_label(g: dict[str, Any]) -> str:
    return f"round({g['strength']:g}(m+n))" if g["mode"].endswith("scaled") else f"{int(g['strength'])}"


def pilot(cfg: ConfigV3) -> dict[str, Any]:
    """Pilot of the linear protocol and the reduction rule (amendment 8.3). Writes ``linear/pilot.json``."""
    raw = cfg.area / "raw" / "runs.jsonl"
    spec = cfg.raw["pilot"]
    full = build_linear(cfg, linear_groups(cfg, reduced=False), cfg.area / "instances")
    methods = list(cfg.raw["methods"])
    seeds = cfg.seeds()
    first: dict[tuple[str, str], dict[str, Any]] = {}
    for inst in full:
        first.setdefault((inst["set"], inst["size"]), inst)
    tasks = [t for t in plan_tasks(cfg, "main", list(first.values()), methods, seeds[:1]) if t["kind"] in STOCHASTIC]
    summary = run_tasks(cfg, tasks, raw, "pilot")
    keys = {key_of(t) for t in tasks}
    times = {(r["set"], r["size"], r["method"]): r["time_s"] for r in records(raw) if key_of(r) in keys}

    def estimate(items: list[dict[str, Any]]) -> float:
        plan = [t for t in plan_tasks(cfg, "main", items, methods, seeds) if t["kind"] in STOCHASTIC]
        return sum(times[(t["set"], t["size"], t["method"])] for t in plan) / float(spec["parallel_runs"])

    est_full = estimate(full)
    limit = 60.0 * float(spec["limit_min"])
    reduced = est_full > limit
    result = {
        "pilot_runs": len(tasks),
        "pilot_wall_s": summary["wall_s"],
        "times_s": {"|".join(k): v for k, v in sorted(times.items())},
        "parallel_runs": spec["parallel_runs"],
        "estimate_full_s": est_full,
        "limit_s": limit,
        "reduced": reduced,
        "estimate_after_rule_s": estimate(build_linear(cfg, linear_groups(cfg, reduced), cfg.area / "instances")),
        "rule": "estimate above the limit: the groups with reduced_count use that many instances",
    }
    write_atomic(cfg.area / "pilot.json", result)
    return result


def run(cfg: ConfigV3) -> dict[str, Any]:
    """Main runs of the configuration: the linear protocol (after the pilot) or the fixed-charge problem."""
    raw = cfg.area / "raw" / "runs.jsonl"
    methods = list(cfg.raw["methods"])
    if cfg.raw["problem"] == "linear":
        pilot_path = cfg.area / "pilot.json"
        if not pilot_path.exists():
            raise RuntimeError("run the command pilot first: it decides the reduction of the plan")
        reduced = bool(json.loads(pilot_path.read_text(encoding="utf-8"))["reduced"])
        items = build_linear(cfg, linear_groups(cfg, reduced), cfg.area / "instances")
        return run_tasks(cfg, plan_tasks(cfg, "main", items, methods, cfg.seeds()), raw, "linear")
    items = build_fctp(cfg)
    mip_method: dict[str, Any] = {"method": "MIP", "kind": "mip", "config": "-", "params": {}, "initialization": None}
    mip_tasks = [make_task(cfg, "mip", inst, mip_method, None) for inst in items]
    first = run_tasks(cfg, mip_tasks, cfg.area / "raw" / "mip.jsonl", "fctp mip")
    second = run_tasks(cfg, plan_tasks(cfg, "main", items, methods, cfg.seeds()), raw, "fctp")
    return {"mip": first, "main": second, "wall_s": first["wall_s"] + second["wall_s"]}


# --- external benchmark (amendment 8.5) ----------------------------------------------------


def read_fctp_mps(path: Path) -> dict[str, Any]:
    """Read a fixed-charge transportation problem from an MPS file with the layout of the MIPLIB instances
    ``ran12x21``, ``ran13x13`` and ``gr4x6``: equality rows ``A<i>`` (supply) and ``B<j>`` (demand), rows
    ``G<k>`` for ``x_k - M_k y_k <= 0``, columns ``X<k>`` (cost, one A row, one B row, one G row) and binary
    columns ``Y<k>`` (fixed charge, the G row with ``-M_k``). The bound ``M_k`` must not cut off any plan."""
    import gzip

    opener = gzip.open if path.suffix == ".gz" else open
    section = ""
    rows: dict[str, list[str]] = {"A": [], "B": []}
    columns: dict[str, dict[str, float]] = {}
    rhs: dict[str, float] = {}
    with opener(path, "rt", encoding="ascii") as fh:
        for line in fh:
            if not line.strip() or line.startswith("*"):
                continue
            if not line[0].isspace():
                section = line.split()[0]
                continue
            tok = line.split()
            if section == "ROWS" and tok[0] == "E":
                rows[tok[1][0]].append(tok[1])
            elif section == "COLUMNS" and "MARKER" not in line:
                for name, value in zip(tok[1::2], tok[2::2], strict=True):
                    columns.setdefault(tok[0], {})[name] = float(value)
            elif section == "RHS":
                for name, value in zip(tok[1::2], tok[2::2], strict=True):
                    rhs[name] = float(value)
    m, n = len(rows["A"]), len(rows["B"])
    supply = [rhs.get(r, 0.0) for r in rows["A"]]
    demand = [rhs.get(r, 0.0) for r in rows["B"]]
    cost = np.full((m, n), np.nan)
    fixed = np.full((m, n), np.nan)
    link: dict[str, tuple[int, int]] = {}
    for name, col in columns.items():
        if name.startswith("X"):
            i = next(rows["A"].index(r) for r in col if r.startswith("A"))
            j = next(rows["B"].index(r) for r in col if r.startswith("B"))
            cost[i, j] = col.get("COST", 0.0)
            link[next(r for r in col if r.startswith("G"))] = (i, j)
    for name, col in columns.items():
        if name.startswith("Y"):
            g = next(r for r in col if r.startswith("G"))
            i, j = link[g]
            fixed[i, j] = col.get("COST", 0.0)
            if -col[g] < min(supply[i], demand[j]) - 1e-9:
                raise ValueError(f"{path.name}: arc {name} has a capacity below min(a_i, b_j)")
    if np.isnan(cost).any() or np.isnan(fixed).any():
        raise ValueError(f"{path.name}: not a complete fixed-charge transportation problem")
    return {"supply": supply, "demand": demand, "cost": cost.tolist(), "fixed": fixed.tolist()}


def build_benchmark(cfg: ConfigV3) -> list[dict[str, Any]]:
    """Convert the benchmark files named in the configuration to instance files."""
    spec = cfg.raw["benchmark"]
    root = cfg.area / "benchmark" / "instances"
    entries = {}
    out = []
    for b in spec["instances"]:
        src = cfg.resolve(b["file"])
        data = read_fctp_mps(src)
        m, n = len(data["supply"]), len(data["demand"])
        path = root / f"{b['id']}.json"
        entry = {
            "id": b["id"],
            "set": "benchmark",
            "m": m,
            "n": n,
            "rho": None,
            "listed_objective": float(b["objective"]),
            "url": b.get("url"),
            "source_file": _relative(src, cfg.root),
            "source_sha256": hashlib.sha256(src.read_bytes()).hexdigest(),
            "file": path.name,
            "sha256": _write_instance(path, data),
        }
        entries[b["id"]] = entry
        out.append({**entry, "path": str(path), "size": f"{m}x{n}"})
    write_atomic(root / "manifest.json", {"source": spec.get("source"), "instances": entries})
    return out


def benchmark(cfg: ConfigV3) -> dict[str, Any]:
    """Methods of the fixed-charge configuration on the external benchmark instances."""
    items = build_benchmark(cfg)
    raw = cfg.area / "raw"
    mip_method: dict[str, Any] = {"method": "MIP", "kind": "mip", "config": "-", "params": {}, "initialization": None}
    mip_tasks = [make_task(cfg, "benchmark-mip", inst, mip_method, None) for inst in items]
    for t in mip_tasks:
        t["mip"] = cfg.raw["benchmark"].get("mip", t["mip"])
    first = run_tasks(cfg, mip_tasks, raw / "benchmark_mip.jsonl", "benchmark mip")
    tasks = plan_tasks(cfg, "benchmark", items, list(cfg.raw["methods"]), cfg.seeds())
    second = run_tasks(cfg, tasks, raw / "benchmark.jsonl", "benchmark")
    return {
        "instances": [i["id"] for i in items],
        "mip": first,
        "main": second,
        "wall_s": first["wall_s"] + second["wall_s"],
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    import csv

    path.parent.mkdir(parents=True, exist_ok=True)
    fields: list[str] = []
    for row in rows:
        fields += [k for k in row if k not in fields]
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:  # a configuration outside the repository (tests)
        return path.as_posix()


def record_invocation(cfg: ConfigV3, command: str, started: float, result: dict[str, Any]) -> None:
    """Append the command, its time, the software and the machine to ``run_manifest.json``."""
    from tpga.experiments.v2.manifest import versions

    path = cfg.output / "run_manifest.json"
    manifest = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"invocations": []}
    info = environment.describe(cfg.root)
    info.update(
        command=command,
        config={"path": _relative(cfg.path, cfg.root), "sha256": cfg.sha256},
        tuned_parameters_sha256=hashlib.sha256(cfg.resolve(cfg.raw["tuned_parameters"]).read_bytes()).hexdigest(),
        packages=versions(),
        started=time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(started)),
        finished=time.strftime("%Y-%m-%dT%H:%M:%S"),
        wall_s=time.time() - started,
        result={k: v for k, v in result.items() if k not in ("times_s",)},
    )
    manifest["invocations"].append(info)
    path.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(path, manifest)
