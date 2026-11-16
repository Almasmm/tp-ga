"""``tpga-exp pilot``: short runs on one instance per (set, size) and method; estimate of the full plan.

Budget-only runs scale linearly with the number of decoder calls, so the pilot measures the time per decoder
call with a shortened budget and multiplies it by the full budget. Phases with a stagnation stop are
estimated with the full budget (an upper bound). Times are converted to performance-core seconds with a
measured E/P speed ratio; quality phases use all cores, the timing phase the performance cores only.
"""

from __future__ import annotations

import json
import multiprocessing as mp
import statistics
import time
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from typing import Any

from tpga.experiments import environment
from tpga.experiments.v2 import methods
from tpga.experiments.v2.config import ConfigV2
from tpga.experiments.v2.instances import InstanceV2, build
from tpga.experiments.v2.runner import init_worker
from tpga.experiments.v2.tasks import phase_tasks, reference_tasks, stochastic_tasks

PHASES = ("reference", "main", "stagnation", "legacy", "factorial", "timing")


def _pool_run(tasks: list[dict[str, Any]], cpus: list[int]) -> list[dict[str, Any]]:
    classes = environment.cpu_classes()
    manager = mp.Manager()
    q = manager.Queue()
    for c in cpus:
        q.put(c)
    with ProcessPoolExecutor(len(cpus), initializer=init_worker, initargs=(q, classes, None, "normal", 1.0)) as pool:
        out = [r for r, _ in pool.map(methods.execute, tasks)]
    manager.shutdown()
    return out


def _cores() -> tuple[list[int], list[int]]:
    classes = environment.cpu_classes()
    if not classes:  # pragma: no cover - non-Windows: treat every core as a performance core
        import os

        return list(range(os.cpu_count() or 1)), []
    top = max(classes.values())
    return sorted(c for c, v in classes.items() if v == top), sorted(c for c, v in classes.items() if v != top)


def speed_ratio(cfg: ConfigV2, inst: InstanceV2, z: float) -> float:
    """Time on an efficiency core divided by time on a performance core for the same GA task."""
    p_cores, e_cores = _cores()
    if not e_cores:
        return 1.0
    task = stochastic_tasks(cfg, "pilot", [inst], ["GA-rand-base"], "budget", [cfg.seeds(1)[0]])[0]
    task.update(budget=200_000, z_star=z)
    rows = _pool_run([task, dict(task)], [p_cores[0], e_cores[0]])
    by_class = {r["cpu_class"]: r["time_s"] for r in rows}
    top = max(by_class)
    return max(by_class.values()) / by_class[top] if len(by_class) == 2 else 1.0


def monitor_overhead(cfg: ConfigV2, inst: InstanceV2, z: float, repeats: int = 3) -> dict[str, float]:
    """Run time of one GA task with and without 1 Hz status reporting through a manager queue."""
    from tpga.ga import run_ga
    from tpga.model import TransportProblem

    task = stochastic_tasks(cfg, "pilot", [inst], ["GA-rand-base"], "budget", [cfg.seeds(1)[0]])[0]
    task.update(budget=300_000, z_star=z)
    problem = TransportProblem.from_json(task["path"])
    manager = mp.Manager()
    methods._STATE.update(queue=manager.Queue(), interval=1.0)
    with_cb, without = [], []
    for _ in range(repeats):
        t0 = time.perf_counter()
        run_ga(problem, methods.ga_config(task))
        without.append(time.perf_counter() - t0)
        t0 = time.perf_counter()
        run_ga(problem, methods.ga_config(task), callback=methods._progress(task))
        with_cb.append(time.perf_counter() - t0)
    methods._STATE.update(queue=None)
    manager.shutdown()
    a, b = statistics.median(without), statistics.median(with_cb)
    return {"without_s": a, "with_reporting_s": b, "overhead_percent": 100.0 * (b - a) / a}


def run(cfg: ConfigV2) -> dict[str, Any]:
    out_dir = cfg.output / "pilot"
    out_dir.mkdir(parents=True, exist_ok=True)
    items = build(cfg)
    firsts = {(i.set, i.m, i.n): i for i in items if i.id.split("-")[1] == "00"}
    p_cores, e_cores = _cores()
    all_cores = sorted(p_cores + e_cores)[: int(cfg.raw.get("workers", 24))]
    # 1. LP and classical methods on the pilot instances (real cost)
    ref = reference_tasks(cfg, "pilot", list(firsts.values()), ["LP"], repeats=1)
    lp_rows = _pool_run(ref, all_cores)
    z = {r["instance"]: r["cost"] for r in lp_rows}
    other_ref = [
        t
        for t in reference_tasks(cfg, "pilot", list(firsts.values()), ["LP-ortools", "NWC", "LCM", "VAM"], repeats=1)
        if not (t["method"] != "LP-ortools" and t["set"] == "lp_scaling")
    ]
    for t in other_ref:
        t["z_star"] = z[t["instance"]]
    lp_rows += _pool_run(other_ref, all_cores)
    det_time = {(r["set"], r["size"], r["method"]): r["time_s"] for r in lp_rows}
    # 2. stochastic methods with a shortened budget
    stoch = []
    for inst in firsts.values():
        if inst.set == "lp_scaling":
            continue
        full = cfg.budget(inst.m, inst.n)
        for name in cfg.raw["stochastic_methods"]:
            t = stochastic_tasks(cfg, "pilot", [inst], [name], "budget", [cfg.seeds(1)[0]])[0]
            t.update(budget=int(min(full, max(20_000, full // 50))), z_star=z[inst.id])
            stoch.append(t)
        for pop in (20, 400):  # population changes the per-call overhead of the factorial plan
            if (inst.set, inst.m) in (("uniform", 20), ("uniform", 50)):
                override = {
                    "population": pop,
                    "crossover_rate": 0.9,
                    "tournament": 3,
                    "elite": 2,
                    "mutation_rate": 0.2,
                    "mutation_mode": "swap_fixed",
                    "init": "random",
                }
                t = stochastic_tasks(
                    cfg,
                    "pilot",
                    [inst],
                    [f"P{pop}"],
                    "budget",
                    [cfg.seeds(1)[0]],
                    params_override={f"P{pop}": override},
                )[0]
                t.update(method=f"GA-P{pop}", budget=int(min(full, max(20_000, full // 50))), z_star=z[inst.id])
                stoch.append(t)
    rows = _pool_run(stoch, all_cores)
    uniform = sorted((i for i in firsts.values() if i.set == "uniform"), key=lambda i: i.m * i.n)
    calib = next((i for i in uniform if (i.m, i.n) == (50, 50)), uniform[-1])
    small = next((i for i in uniform if (i.m, i.n) == (20, 20)), uniform[0])
    ratio = speed_ratio(cfg, calib, z[calib.id])
    top = max(environment.cpu_classes().values() or [0])
    per_eval: dict[tuple[str, str, str], float] = {}
    for r in rows:
        t = r["time_s"] / max(1, r["evals"])
        if r.get("cpu_class") is not None and r["cpu_class"] != top:
            t /= ratio  # to performance-core seconds
        per_eval[(r["set"], r["size"], r["method"])] = t
    overhead = monitor_overhead(cfg, small, z[small.id])
    # 3. estimate of every phase from its full task list
    estimate = estimate_plan(cfg, items, per_eval, det_time, ratio, len(p_cores), len(all_cores))
    result = {
        "measured": {
            "per_eval_s_performance_core": {"|".join(k): v for k, v in sorted(per_eval.items())},
            "deterministic_s": {"|".join(k): v for k, v in sorted(det_time.items())},
            "e_over_p_speed_ratio": ratio,
            "monitor_overhead": overhead,
        },
        **estimate,
    }
    (out_dir / "estimate.json").write_text(json.dumps(result, indent=1) + "\n", encoding="utf-8", newline="\n")
    (out_dir / "PILOT.md").write_text(markdown(result), encoding="utf-8", newline="\n")
    return result


def _task_seconds(t: dict[str, Any], per_eval: dict, det_time: dict, cfg: ConfigV2) -> float:
    key = (t["set"], t["size"], t["method"])
    if t["kind"] in ("lp", "classical"):
        return det_time.get(key, 0.0) * int(t.get("repeats", 1))
    if t["phase"] == "factorial":
        pop = int(t["params"]["population"])
        lo = per_eval.get((t["set"], t["size"], "GA-P20"))
        hi = per_eval.get((t["set"], t["size"], "GA-P400"))
        if lo is not None and hi is not None:
            # per-call time = a + b / P through the two measured populations
            b = (lo - hi) / (1 / 20 - 1 / 400)
            a = hi - b / 400
            return (a + b / pop) * int(t["budget"])
    return per_eval.get(key, 0.0) * int(t["budget"])


def estimate_plan(
    cfg: ConfigV2, items: list[InstanceV2], per_eval: dict, det_time: dict, ratio: float, p_cores: int, workers: int
) -> dict[str, Any]:
    capacity = p_cores + (workers - p_cores) / ratio  # performance-core equivalents
    phases: dict[str, Any] = {}
    detail: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    for name in PHASES:
        tasks = phase_tasks(cfg, name, items)
        core_s = 0.0
        for t in tasks:
            s = _task_seconds(t, per_eval, det_time, cfg)
            core_s += s
            detail[name][f"{t['set']} {t['size']} {t['method']}"] += s
        wall = core_s / (p_cores if name == "timing" else capacity)
        phases[name] = {"runs": len(tasks), "core_s": core_s, "wall_h": wall / 3600}
    total = sum(p["wall_h"] for p in phases.values())
    for p in phases.values():
        p["share"] = p["wall_h"] / total if total else 0.0
    top = sorted(((ph, k, v) for ph, d in detail.items() for k, v in d.items()), key=lambda x: -x[2])[:12]
    return {
        "phases": phases,
        "total_wall_h": total,
        "capacity_performance_cores": capacity,
        "largest_items": [
            {"phase": ph, "item": k, "wall_h": v / ((p_cores if ph == "timing" else capacity) * 3600)}
            for ph, k, v in top
        ],
        "reductions": reductions(cfg, items, per_eval, det_time, capacity, p_cores) if total > 24 else [],
    }


def reductions(
    cfg: ConfigV2, items: list[InstanceV2], per_eval: dict, det_time: dict, capacity: float, p_cores: int
) -> list[dict[str, Any]]:
    """Candidate reductions with the time they save; the user chooses."""
    out = []
    tasks = {ph: phase_tasks(cfg, ph, items) for ph in PHASES}

    def hours(ts: list[dict[str, Any]], cap: float) -> float:
        return sum(_task_seconds(t, per_eval, det_time, cfg) for t in ts) / (cap * 3600)

    t200 = [t for t in tasks["main"] if t["size"] == "200x200"]
    for cap in (4_000_000, 2_000_000, 1_000_000):
        # a lower cap shortens every budget-limited run above it, in every phase
        saved, sizes = 0.0, set()
        for ph, ts in tasks.items():
            cores = p_cores if ph == "timing" else capacity
            for t in ts:
                if t["kind"] not in ("lp", "classical") and int(t["budget"]) > cap:
                    saved += _task_seconds(t, per_eval, det_time, cfg) * (1 - cap / int(t["budget"])) / (cores * 3600)
                    sizes.add(t["size"])
        label = ", ".join(sorted(sizes, key=lambda s: int(s.split("x")[0]) * int(s.split("x")[1])))
        out.append({"option": f"budget cap {cap:,} decoder calls (shortens runs at {label})", "saves_h": saved})
    seeds10 = [t for t in t200 if int(t["seed"]) - int(cfg.raw["base_seed"]) >= 10]
    out.append({"option": "200x200 in the main phase with 10 runs instead of 30", "saves_h": hours(seeds10, capacity)})
    base = [t for t in t200 if t["method"].endswith("-base")]
    out.append({"option": "drop the base GA configurations at 200x200", "saves_h": hours(base, capacity)})
    tim = [t for t in tasks["timing"] if t["size"] == "200x200" and t["kind"] not in ("lp",)]
    out.append({"option": "timing phase without 200x200 for GA and SA", "saves_h": hours(tim, p_cores)})
    fac = [t for t in tasks["factorial"] if int(t["params"]["population"]) == 400]
    out.append({"option": "factorial plan without population 400", "saves_h": hours(fac, capacity)})
    return sorted(out, key=lambda r: -r["saves_h"])


def markdown(result: dict[str, Any]) -> str:
    m = result["measured"]
    lines = [
        "# Pilot estimate of the v0.4 run",
        "",
        "| Phase | Runs | Estimated wall time, h | Share |",
        "|---|---|---|---|",
    ]
    for name, p in result["phases"].items():
        lines.append(f"| {name} | {p['runs']:,} | {p['wall_h']:.2f} | {100 * p['share']:.1f} % |")
    lines += [
        f"| **total** | {sum(p['runs'] for p in result['phases'].values()):,} "
        f"| **{result['total_wall_h']:.2f}** | 100 % |",
        "",
        f"* E/P speed ratio (same GA task): {m['e_over_p_speed_ratio']:.2f}; quality phases use "
        f"{result['capacity_performance_cores']:.1f} performance-core equivalents, "
        "the timing phase 8 performance cores.",
        f"* Monitor overhead (1 Hz status through a queue): {m['monitor_overhead']['overhead_percent']:.2f} % "
        f"({m['monitor_overhead']['without_s']:.3f} s without, "
        f"{m['monitor_overhead']['with_reporting_s']:.3f} s with).",
        "* Phases with a stagnation stop are estimated with the full budget (upper bound).",
        "",
        "## Largest items",
        "",
        "| Phase | Item | h |",
        "|---|---|---|",
        *[f"| {r['phase']} | {r['item']} | {r['wall_h']:.2f} |" for r in result["largest_items"]],
    ]
    if result["reductions"]:
        lines += [
            "",
            "## Possible reductions (choose; not applied)",
            "",
            "| Option | Saves, h |",
            "|---|---|",
            *[f"| {r['option']} | {r['saves_h']:.2f} |" for r in result["reductions"]],
        ]
    return "\n".join(lines) + "\n"
