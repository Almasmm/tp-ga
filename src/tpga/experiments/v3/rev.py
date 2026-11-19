"""Answers to a review (amendment 10 of docs/v0.4/PREREGISTRATION.md): the run commands.

Configuration ``experiments/paper-v3-review.yaml`` (``review: true``). It adds two local-search rivals on the
fixed-charge problem, the MIP solver in its usual setting, more instance classes, times with one run at a
time and a second rule for the entering arc of the cycle mutation. The instances, methods and records of
amendments 8 and 9 are read through their own configurations and never rewritten. Everything goes to
``<output>/review``. All run commands together have a time limit; ``review/budget.json`` keeps what each used.
"""

from __future__ import annotations

import functools
import hashlib
import itertools
import json
import multiprocessing
import statistics
import time
import urllib.request
from collections.abc import Callable
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Any

import numpy as np

from tpga.experiments import environment
from tpga.experiments.v2.storage import append_jsonl, read_jsonl, write_atomic
from tpga.experiments.v3 import core, ext
from tpga.experiments.v3.core import STOCHASTIC, ConfigV3, key_of, records
from tpga.fctp import generate_concentrated

Row = dict[str, Any]
ORDER = ("pilot", "tune", "rivals", "generator", "degenerate", "public", "timing", "mipdefault")
SHARED = ("base_seed", "runs", "budget_factor", "mip")


def area(cfg: ConfigV3) -> Path:
    return cfg.output / "review"


def ext_cfg(cfg: ConfigV3) -> ConfigV3:
    """The configuration of amendment 9 (and through it the one of 8.4); seeds, budget and MIP must agree."""
    e = ConfigV3.load(cfg.resolve(cfg.raw["base"]))
    differ = [k for k in SHARED if cfg.raw.get(k) != e.raw.get(k)]
    if differ or e.output != cfg.output:
        raise ValueError(f"the review configuration and its base differ in {differ or ['output']}")
    return e


def lin_cfg(cfg: ConfigV3) -> ConfigV3:
    return ConfigV3.load(cfg.resolve(cfg.raw["linear"]))


def index_of(inst: Row) -> int:
    """Number of an instance inside its cell (the last field of its id)."""
    return int(str(inst["id"]).rsplit("-", 1)[1][:2])


# --- time limit ----------------------------------------------------------------------------


def _spent(cfg: ConfigV3) -> list[Row]:
    path = area(cfg) / "budget.json"
    return list(json.loads(path.read_text(encoding="utf-8"))["commands"]) if path.exists() else []


def used_s(cfg: ConfigV3) -> float:
    return float(sum(c["wall_s"] for c in _spent(cfg) if not c.get("beyond_limit")))


def allowance_s(cfg: ConfigV3, command: str) -> float:
    """Seconds this command may use (10.0 with the correction 10.9): the allowances of the commands up to
    and including this one, minus the time already used, so that time left unused by earlier commands passes
    on; the last command may go on until the limit of all commands minus a margin. With ``--minutes`` the
    given time is used as it is and the start is marked as made beyond the limit."""
    if cfg.raw.get("_minutes") is not None:
        return 60.0 * float(cfg.raw["_minutes"])
    plan = cfg.raw["allowance_min"]
    limit = float(cfg.raw["limit_min"])
    upto = sum(float(plan[c]) for c in ORDER[: ORDER.index(command) + 1])
    if command == ORDER[-1]:
        upto = limit - float(cfg.raw["final_margin_min"])
    return max(0.0, 60.0 * min(upto, limit) - used_s(cfg))


def timed(command: str) -> Callable[[Callable[[ConfigV3, float], Row]], Callable[[ConfigV3], Row]]:
    def wrap(fn: Callable[[ConfigV3, float], Row]) -> Callable[[ConfigV3], Row]:
        @functools.wraps(fn)
        def run(cfg: ConfigV3) -> Row:
            started = time.time()
            limit = allowance_s(cfg, command)
            result = fn(cfg, limit)
            wall = time.time() - started
            entry = {
                "command": command,
                "started": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(started)),
                "allowance_s": limit,
                "wall_s": wall,
                "beyond_limit": cfg.raw.get("_minutes") is not None,
            }
            write_atomic(area(cfg) / "budget.json", {"commands": [*_spent(cfg), entry]})
            return {**result, "allowance_s": limit, "wall_s": wall, "used_total_s": used_s(cfg)}

        return run

    return wrap


# --- methods -------------------------------------------------------------------------------


def grid(cfg: ConfigV3, name: str) -> list[Row]:
    """Configurations of the grid of a rival in the order of the tie rule."""
    g = cfg.raw["rivals"][name]["grid"]
    return [dict(zip(g, combo, strict=True)) for combo in itertools.product(*g.values())]


def selected(cfg: ConfigV3) -> dict[str, Row]:
    path = area(cfg) / "tune" / "selected.json"
    if not path.exists():
        raise RuntimeError(f"{path} is missing: run the command tune first")
    return dict(json.loads(path.read_text(encoding="utf-8"))["selected"])


def rival(cfg: ConfigV3, name: str, choice: Row | None = None) -> Row:
    """Fields of Tabu or ILS with a configuration of its grid (default: the chosen one)."""
    kind = cfg.raw["rivals"][name]["kind"]
    params = dict(selected(cfg)[name]["params"] if choice is None else choice)
    if kind == "tabu":
        config = f"tabu-s{float(params['sample']):g}-T{int(params['tenure'])}"
    else:
        config = f"ils-p{int(params['perturbation'])}-{params['acceptance']}"
    return {"method": name, "kind": kind, "initialization": None, "params": params, "config": config}


def method(cfg: ConfigV3, name: str) -> Row:
    return rival(cfg, name) if name in cfg.raw["rivals"] else ext.method(ext_cfg(cfg), name)


def plan(cfg: ConfigV3, phase: str, items: list[Row], names: list[str], seeds: list[int]) -> list[Row]:
    tasks = []
    for inst in items:
        for name in names:
            fields = method(cfg, name)
            for seed in seeds if fields["kind"] in STOCHASTIC else [None]:
                tasks.append(core.make_task(cfg, phase, inst, fields, seed))
    return tasks


def nd_fields(lin: ConfigV3, name: str, base_name: str) -> Row:
    """A GA with the cycle mutation of ``base_name`` and the rule ``nondegenerate`` for the entering arc."""
    f = core.method_fields(lin, base_name)
    return {**f, "method": name, "entering": "nondegenerate", "config": f["config"] + "-nd", "trace": True}


# --- instances -----------------------------------------------------------------------------


def test_items(cfg: ConfigV3) -> list[Row]:
    """The 40 instances of 8.4 and the 20 instances of 9.4."""
    e = ext_cfg(cfg)
    return core.build_fctp(ext.base(e)) + ext.large_items(e)


def train_items(cfg: ConfigV3) -> list[Row]:
    return ext.tune_items(ext_cfg(cfg))


def pilot_items(cfg: ConfigV3) -> list[Row]:
    return core.fctp_instances(cfg.raw["pilot"]["instances"], area(cfg) / "pilot" / "instances", prefix="p")


def cells(items: list[Row]) -> list[tuple[str, float]]:
    return sorted({(i["size"], i["rho"]) for i in items}, key=lambda c: (int(c[0].split("x")[0]), c[1]))


def generator_items(cfg: ConfigV3, new_only: bool = False) -> list[Row]:
    """Instances of 10.3 b with the fields ``class`` and ``new``. The cells of the class ``uniform`` with the
    values of rho of 8.4 are the instances of 8.4 and 9.4 at the sizes of this section."""
    spec = cfg.raw["generator"]
    sizes = [(int(m), int(n)) for m, n in spec["sizes"]]
    root = area(cfg) / "generator" / "instances"
    uni = spec["uniform"]
    out = [
        {**i, "class": "uniform", "new": True}
        for i in core.fctp_instances(
            {**uni, "sizes": sizes, "count": spec["count"], "cost": spec["cost"], "supply": spec["supply"]},
            root / "uniform",
            prefix=str(uni["prefix"]),
        )
    ]
    con = spec["concentrated"]
    entries = {}
    for s, (m, n) in enumerate(sizes):
        for q, rho in enumerate(con["rho"]):
            for i in range(int(spec["count"])):
                seed = int(con["seed_base"]) + 1000 * s + 100 * q + i
                iid = f"{con['prefix']}{m}x{n}-r{rho:g}-{i:02d}"
                path = root / "concentrated" / f"{iid}.json"
                data = generate_concentrated(m, n, seed, float(rho), {**con, "cost": spec["cost"]})
                entry = {
                    "id": iid,
                    "set": "fctp",
                    "m": m,
                    "n": n,
                    "rho": float(rho),
                    "seed": seed,
                    "fixed_high": data["fixed_high"],
                    "file": path.name,
                    "sha256": core._write_instance(path, data),
                    "generator": "tpga.fctp.generate_concentrated",
                }
                entries[iid] = entry
                out.append({**entry, "path": str(path), "size": f"{m}x{n}", "class": "concentrated", "new": True})
    write_atomic(root / "concentrated" / "manifest.json", {"instances": entries})
    if not new_only:
        wanted = {f"{m}x{n}" for m, n in sizes}
        out += [{**i, "class": "uniform", "new": False} for i in test_items(cfg) if i["size"] in wanted]
    return out


def linear_items(lin: ConfigV3) -> list[Row]:
    return core.build_linear(lin, core.linear_groups(lin, reduced=False), lin.area / "instances")


def train_linear(lin: ConfigV3, iid: str) -> Row:
    """A training instance of the choice of k (8.2), read from its manifest without touching the directory."""
    root = lin.output / "kselect" / "instances"
    entry = json.loads((root / "manifest.json").read_text(encoding="utf-8"))["instances"][iid]
    return {**entry, "path": str(root / entry["file"]), "size": f"{entry['m']}x{entry['n']}"}


def read_fctp_text(path: Path) -> Row:
    """Read a fixed-charge problem from the text layout of the files ``N*.FCTP``: ``m n``, the supplies, the
    demands, ``m`` lines of costs and ``m`` lines of fixed charges (numbers separated by white space)."""
    numbers = path.read_text(encoding="ascii").split()
    m, n = int(numbers[0]), int(numbers[1])
    values = [float(v) for v in numbers[2:]]
    if len(values) != m + n + 2 * m * n:
        raise ValueError(f"{path.name}: {len(values)} numbers after the sizes, {m + n + 2 * m * n} expected")
    supply, demand = values[:m], values[m : m + n]
    cost = np.array(values[m + n : m + n + m * n]).reshape(m, n)
    fixed = np.array(values[m + n + m * n :]).reshape(m, n)
    if abs(sum(supply) - sum(demand)) > 1e-9:
        raise ValueError(f"{path.name}: not balanced")
    return {"supply": supply, "demand": demand, "cost": cost.tolist(), "fixed": fixed.tolist()}


def public_items(cfg: ConfigV3) -> list[Row]:
    """Download (once), check and convert the public instances named in the configuration."""
    spec = cfg.raw["public"]
    source = area(cfg) / "public" / "source"
    root = area(cfg) / "public" / "instances"
    out = []
    for b in spec["instances"]:
        src = source / f"{b['id']}.FCTP"
        if not src.exists():
            src.parent.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(spec["base_url"] + src.name, timeout=60) as fh:  # noqa: S310 - configured
                src.write_bytes(fh.read())
        digest = hashlib.sha256(src.read_bytes()).hexdigest()
        if digest != b["sha256"]:
            raise RuntimeError(f"{src.name}: SHA-256 {digest} is not the value of the configuration")
        data = read_fctp_text(src)
        m, n = len(data["supply"]), len(data["demand"])
        path = root / f"{b['id']}.json"
        core._write_instance(path, data)
        out.append({"id": b["id"], "set": "public", "m": m, "n": n, "rho": None, "path": str(path), "size": f"{m}x{n}"})
    return sorted(out, key=lambda i: (i["m"] * i["n"], i["id"]))


# --- estimates of the time -----------------------------------------------------------------


def pilot_times(cfg: ConfigV3) -> dict[str, float]:
    path = area(cfg) / "pilot.json"
    if not path.exists():
        raise RuntimeError("run the command pilot first: its times decide the reduction rules")
    return dict(json.loads(path.read_text(encoding="utf-8"))["times_s"])


def run_time(times: dict[str, float], task: Row) -> float:
    """Estimated time of an FCTP run: the pilot time of its method at the smallest pilot size that is not
    below the larger side of the instance; a MIP run counts with its limit."""
    if task["kind"] == "mip":
        return float(task["mip"]["time_limit_s"])
    if task["kind"] not in STOCHASTIC:
        return 0.0
    sizes = sorted(int(k.split("|")[1].split("x")[0]) for k in times if k.startswith(task["method"] + "|"))
    side = max(int(task["m"]), int(task["n"]))
    pick = next((s for s in sizes if s >= side), sizes[-1])
    return times[f"{task['method']}|{pick}x{pick}"]


def estimate(cfg: ConfigV3, tasks: list[Row], times: dict[str, float]) -> float:
    return float(cfg.raw["safety"]) * sum(run_time(times, t) for t in tasks) / cfg.workers


# --- commands ------------------------------------------------------------------------------


@timed("pilot")
def pilot(cfg: ConfigV3, limit: float) -> Row:
    """Single runs whose times feed the reduction rules (10.0). Writes ``review/pilot.json``."""
    e, lin = ext_cfg(cfg), lin_cfg(cfg)
    seed = cfg.seeds(1)[0]
    tasks = []
    for inst in pilot_items(cfg):
        for name in (*cfg.raw["rivals"], cfg.raw["pilot"]["ga"]):
            fields = rival(cfg, name, grid(cfg, name)[0]) if name in cfg.raw["rivals"] else ext.method(e, name)
            tasks.append(core.make_task(cfg, "pilot", inst, fields, seed))
    inst = train_linear(lin, cfg.raw["pilot"]["linear_instance"])
    for name, base_name in cfg.raw["degenerate"]["variants"].items():
        tasks.append(core.make_task(lin, "pilot", inst, core.method_fields(lin, base_name), seed))
        tasks.append(core.make_task(lin, "pilot", inst, nd_fields(lin, name, base_name), seed))
    core.run_tasks(cfg, tasks, area(cfg) / "raw" / "pilot.jsonl", "pilot")
    keys = {key_of(t) for t in tasks}
    times = {
        f"{r['method']}|{r['size']}": r["time_s"]
        for r in records(area(cfg) / "raw" / "pilot.jsonl", "pilot")
        if key_of(r) in keys
    }
    write_atomic(area(cfg) / "pilot.json", {"runs": len(tasks), "seed": seed, "times_s": times})
    return {"runs": len(tasks), "times_s": times}


def tune_tasks(cfg: ConfigV3) -> list[Row]:
    seeds = cfg.seeds(int(cfg.raw["tune_runs"]))
    return [
        core.make_task(cfg, "tune", inst, rival(cfg, name, choice), seed)
        for name in cfg.raw["rivals"]
        for inst in train_items(cfg)
        for choice in grid(cfg, name)
        for seed in seeds
    ]


def grid_table(cfg: ConfigV3) -> tuple[list[Row], dict[str, Row]]:
    """Mean training gap of every configuration and the chosen one of each rival (rule of 9.2)."""
    e = ext_cfg(cfg)
    tasks = tune_tasks(cfg)
    rows = ext._complete(records(area(cfg) / "tune" / "records.jsonl", "tune"), tasks, "the grid of 10.1")
    mip = {r["instance"]: r for r in records(e.area / "tune" / "mip.jsonl", "tune-mip")}
    earlier = records(e.area / "tune" / "records.jsonl", "tune")
    z = {}
    for iid, m in mip.items():
        low = min(r["cost"] for r in rows + earlier if r["instance"] == iid)
        if m["proved"] and low < m["cost"] - 1e-6:
            raise RuntimeError(f"a run on {iid} is below the proved optimum")
        z[iid] = float(m["cost"]) if m["proved"] else min(low, float(m["cost"]))
    table: list[Row] = []
    chosen: dict[str, Row] = {}
    for name in cfg.raw["rivals"]:
        part = []
        for rank, choice in enumerate(grid(cfg, name)):
            label = rival(cfg, name, choice)["config"]
            mine = [r for r in rows if r["method"] == name and r["config"] == label]
            part.append(
                {
                    "method": name,
                    "rank": rank,
                    "config": label,
                    **choice,
                    "runs": len(mine),
                    "mean_gap": statistics.fmean(
                        100.0 * (r["cost"] - z[r["instance"]]) / z[r["instance"]] for r in mine
                    ),
                    "time_median_s": statistics.median(r["time_s"] for r in mine),
                    "selected": False,
                }
            )
        best = min(part, key=lambda r: (r["mean_gap"], r["rank"]))
        best["selected"] = True
        chosen[name] = {"params": grid(cfg, name)[best["rank"]], "config": best["config"], "mean_gap": best["mean_gap"]}
        table += part
    return table, chosen


@timed("tune")
def tune(cfg: ConfigV3, limit: float) -> Row:
    """Grids of Tabu and ILS on the training instances of 9.2. Writes ``review/tune``."""
    tasks = tune_tasks(cfg)
    est = estimate(cfg, tasks, pilot_times(cfg))
    if est > limit:
        raise RuntimeError(f"the grids are estimated at {est:.0f} s, above the allowance of {limit:.0f} s")
    summary = core.run_tasks(cfg, tasks, area(cfg) / "tune" / "records.jsonl", "tune")
    table, chosen = grid_table(cfg)
    core.write_csv(area(cfg) / "tune" / "grid.csv", table)
    write_atomic(
        area(cfg) / "tune" / "selected.json",
        {
            "selected": chosen,
            "instances": sorted({t["instance"] for t in tasks}),
            "seeds": cfg.seeds(int(cfg.raw["tune_runs"])),
            "rule": "smallest mean gap over the training instances and seeds; ties: the earlier grid entry",
        },
    )
    return {"selected": chosen, "estimate_s": est, "runs": summary}


def rival_items(cfg: ConfigV3, k70: int, k50: int) -> list[Row]:
    keep = {"70x70": k70, "50x50": k50}
    return [i for i in test_items(cfg) if index_of(i) < keep.get(i["size"], 5)]


def rivals_plan(cfg: ConfigV3) -> Row:
    path = area(cfg) / "rivals.json"
    if not path.exists():
        raise RuntimeError("run the command rivals first")
    return dict(json.loads(path.read_text(encoding="utf-8")))


@timed("rivals")
def rivals(cfg: ConfigV3, limit: float) -> Row:
    """Tabu and ILS with their chosen configurations on the instances of 8.4 and 9.4."""
    times = pilot_times(cfg)
    names = list(cfg.raw["rivals"])
    result: Row = {}
    for k70, k50 in ((5, 5), (3, 5), (2, 5), (1, 5), (3, 3), (2, 2), (1, 1)):
        tasks = plan(cfg, "rivals", rival_items(cfg, k70, k50), names, cfg.seeds())
        est = estimate(cfg, tasks, times)
        result = {"instances_70x70": k70, "instances_50x50": k50, "estimate_s": est, "allowance_s": limit}
        if est <= limit:
            break
    else:
        raise RuntimeError("the rivals do not fit in the allowance even with one instance per large cell")
    write_atomic(area(cfg) / "rivals.json", result)
    result["runs"] = core.run_tasks(cfg, tasks, area(cfg) / "raw" / "rivals.jsonl", "rivals")
    return result


def generator_tasks(cfg: ConfigV3, k: int) -> tuple[list[Row], list[Row]]:
    items = [i for i in generator_items(cfg, new_only=True) if index_of(i) < k]
    names = list(cfg.raw["generator"]["methods"])
    return ext.mip_tasks(cfg, "gen-mip", items), plan(cfg, "gen", items, names, cfg.seeds())


def generator_plan(cfg: ConfigV3) -> Row:
    path = area(cfg) / "generator.json"
    if not path.exists():
        raise RuntimeError("run the command generator first")
    return dict(json.loads(path.read_text(encoding="utf-8")))


@timed("generator")
def generator(cfg: ConfigV3, limit: float) -> Row:
    """New instance classes (10.3 b): the MIP reference and the methods."""
    times = pilot_times(cfg)
    result: Row = {}
    for k in (5, 4, 3, 2, 1):
        mips, runs = generator_tasks(cfg, k)
        est = estimate(cfg, mips + runs, times)
        result = {"instances_per_new_cell": k, "estimate_s": est, "allowance_s": limit}
        if est <= limit:
            break
    else:
        raise RuntimeError("the new classes do not fit in the allowance even with one instance per cell")
    write_atomic(area(cfg) / "generator.json", result)
    result["mip"] = core.run_tasks(cfg, mips, area(cfg) / "raw" / "gen_mip.jsonl", "generator mip")
    result["runs"] = core.run_tasks(cfg, runs, area(cfg) / "raw" / "gen.jsonl", "generator")
    return result


def degenerate_tasks(cfg: ConfigV3, k: int, traced: int) -> tuple[list[Row], list[Row]]:
    """(runs of 10.5 a with the present rule, runs of 10.5 b with the rule ``nondegenerate``)."""
    lin = lin_cfg(cfg)
    spec = cfg.raw["degenerate"]
    items = linear_items(lin)
    tr = spec["trace"]
    trace = []
    for size in tr["sizes"]:
        count = traced if size == spec["reduce_size"] else int(tr["instances"])
        group = [i for i in items if i["set"] == tr["set"] and i["size"] == size][:count]
        for inst in group:
            for base_name in spec["variants"].values():
                fields = {**core.method_fields(lin, base_name), "trace": True}
                trace += [core.make_task(lin, "trace", inst, fields, seed) for seed in lin.seeds(int(tr["runs"]))]
    nd = []
    for inst in items:
        if inst["size"] == spec["reduce_size"] and index_of(inst) >= k:
            continue
        for name, base_name in spec["variants"].items():
            nd += [core.make_task(lin, "nd", inst, nd_fields(lin, name, base_name), seed) for seed in lin.seeds()]
    return trace, nd


def degenerate_plan(cfg: ConfigV3) -> Row:
    path = area(cfg) / "degenerate.json"
    if not path.exists():
        raise RuntimeError("run the command degenerate first")
    return dict(json.loads(path.read_text(encoding="utf-8")))


@timed("degenerate")
def degenerate(cfg: ConfigV3, limit: float) -> Row:
    """Pivots by generation with the present rule (10.5 a) and the GA with the second rule (10.5 b)."""
    lin = lin_cfg(cfg)
    spec = cfg.raw["degenerate"]
    times = pilot_times(cfg)
    old = records(lin.area / "raw" / "runs.jsonl", "main")
    med: dict[tuple[str, str, str], float] = {}
    for base_name in spec["variants"].values():
        for key in {(r["set"], r["size"]) for r in old}:
            mine = [r["time_s"] for r in old if r["method"] == base_name and (r["set"], r["size"]) == key]
            med[(base_name, key[0], key[1])] = statistics.median(mine)
    pilot_size = train_linear(lin, cfg.raw["pilot"]["linear_instance"])["size"]
    ratio = {b: times[f"{name}|{pilot_size}"] / times[f"{b}|{pilot_size}"] for name, b in spec["variants"].items()}

    def seconds(task: Row) -> float:
        b = spec["variants"].get(task["method"], task["method"])
        return med[(b, task["set"], task["size"])] * (ratio[b] if task["method"] in spec["variants"] else 1.0)

    options = [(int(k), int(spec["trace"]["instances"])) for k in spec["counts"]]
    options += [(0, t) for t in range(int(spec["trace"]["instances"]) - 1, 0, -1)]
    result: Row = {}
    for k, traced in options:
        trace, nd = degenerate_tasks(cfg, k, traced)
        every = [seconds(t) for t in trace + nd]
        est = float(cfg.raw["safety"]) * sum(every) / cfg.workers + max(every)
        result = {
            "instances_at_reduce_size": k,
            "traced_instances_at_reduce_size": traced,
            "estimate_s": est,
            "allowance_s": limit,
            "time_ratio_second_rule": ratio,
        }
        if est <= limit:
            break
    else:
        raise RuntimeError("the runs of 10.5 do not fit in the allowance")
    write_atomic(area(cfg) / "degenerate.json", result)
    raw = area(cfg) / "raw"
    # one pool for both parts, so that the processors are used all the time
    todo_trace = {key_of(t) for t in trace}
    done = core.run_tasks(cfg, trace + nd, raw / "linear.jsonl", "degenerate")
    rows = records(raw / "linear.jsonl", "trace")
    known = {(r["instance"], r["method"], r["seed"]): r["cost"] for r in old}
    differ = [
        key_of(r)
        for r in rows
        if key_of(r) in todo_trace and known[(r["instance"], r["method"], r["seed"])] != r["cost"]
    ]
    if differ:
        raise RuntimeError(f"{len(differ)} repeated runs differ from the records of amendment 8, first: {differ[0]}")
    result["runs"] = done
    result["repeated_runs_equal_to_records"] = len(todo_trace)
    return result


@timed("public")
def public(cfg: ConfigV3, limit: float) -> Row:
    """Public instances (10.3 a): the MIP reference and the methods."""
    times = pilot_times(cfg)
    items = public_items(cfg)
    names = list(cfg.raw["public"]["methods"])
    kept: list[Row] = []
    for inst in items:  # in the order (size, name) while they fit
        trial = [*kept, inst]
        tasks = ext.mip_tasks(cfg, "public-mip", trial) + plan(cfg, "public", trial, names, cfg.seeds())
        if estimate(cfg, tasks, times) > limit:
            break
        kept = trial
    mips = ext.mip_tasks(cfg, "public-mip", kept)
    runs = plan(cfg, "public", kept, names, cfg.seeds())
    result: Row = {
        "instances": [i["id"] for i in kept],
        "left_out": [i["id"] for i in items if i not in kept],
        "estimate_s": estimate(cfg, mips + runs, times),
        "allowance_s": limit,
    }
    write_atomic(area(cfg) / "public.json", result)
    result["mip"] = core.run_tasks(cfg, mips, area(cfg) / "raw" / "public_mip.jsonl", "public mip")
    result["runs"] = core.run_tasks(cfg, runs, area(cfg) / "raw" / "public.jsonl", "public")
    return result


def timing_items(cfg: ConfigV3) -> list[Row]:
    count = int(cfg.raw["timing"]["instances_per_cell"])
    return [i for i in test_items(cfg) if index_of(i) < count]


@timed("timing")
def timing(cfg: ConfigV3, limit: float) -> Row:
    """Times with one run at a time on one logical processor (10.4), in rounds of one instance per cell."""
    started = time.time()
    spec = cfg.raw["timing"]
    times = pilot_times(cfg)
    names = list(spec["methods"])
    seeds = cfg.seeds(int(spec["runs"]))
    raw = area(cfg) / "raw"
    cpu = None if spec.get("cpu") is None else int(spec["cpu"])  # None: no binding (tests)
    pinned = environment.pin_to_cpu(cpu) if cpu is not None else False
    items = timing_items(cfg)
    warm = min(items, key=lambda i: i["m"] * i["n"])
    for t in plan(cfg, "warm-up", [warm], names, seeds[:1]):
        core.execute(t)  # compiles the kernels; not recorded

    def round_tasks(group: list[Row]) -> list[Row]:
        tasks = plan(cfg, "timing", group, names, seeds)
        for t in tasks:
            t["cpu"] = cpu
        return tasks

    def round_estimate(group: list[Row]) -> float:
        tasks = round_tasks(group)
        ga = [t for t in tasks if t["method"] == cfg.raw["reference_ga"] and t["seed"] == seeds[0]]
        return float(spec["factor"]) * (sum(run_time(times, t) for t in tasks) + sum(run_time(times, t) for t in ga))

    sizes = sorted({i["size"] for i in items}, key=lambda s: int(s.split("x")[0]))
    dropped: list[str] = []
    rounds: list[Row] = []
    for q in range(int(spec["instances_per_cell"])):
        while True:
            group = [i for i in items if index_of(i) == q and i["size"] not in dropped]
            est = round_estimate(group)
            left = limit - (time.time() - started)
            if est <= left or q > 0 or not group:
                break
            dropped.append(sizes.pop())  # round 0 does not fit: the largest size is left out
        if est > left or not group:
            rounds.append({"round": q, "started": False, "estimate_s": est, "left_s": left})
            break
        t0 = time.time()
        core.run_tasks(cfg, round_tasks(group), raw / "timing.jsonl", f"timing round {q}", workers=1)
        rows = records(raw / "timing.jsonl", "timing")
        limits = ext.median_times(rows, cfg.raw["reference_ga"], group)
        mips = ext.mip_tasks(cfg, "timing-mip", group, limits, label="T")
        core.run_tasks(cfg, mips, raw / "timing_mip.jsonl", f"timing round {q} mip", workers=1)
        rounds.append(
            {
                "round": q,
                "started": True,
                "estimate_s": est,
                "left_s": left,
                "wall_s": time.time() - t0,
                "instances": [i["id"] for i in group],
            }
        )
    result: Row = {"cpu": cpu, "pinned": pinned, "sizes_left_out": dropped, "rounds": rounds}
    write_atomic(area(cfg) / "timing.json", result)
    return result


def mip_default_order(cfg: ConfigV3) -> list[Row]:
    """Instances in the order of 10.0: those with a proved optimum in the reference run first (size, rho,
    index), then the others in rounds of one instance per cell."""
    e = ext_cfg(cfg)
    items = test_items(cfg)
    ref = {r["instance"]: r for r in records(e.area / "raw" / "mip.jsonl", "mip")}
    ref.update({r["instance"]: r for r in records(e.area / "raw" / "large_mip.jsonl", "large-mip")})
    proved = sorted(
        (i for i in items if ref[i["id"]]["proved"]), key=lambda i: (i["m"] * i["n"], i["rho"], index_of(i))
    )
    others = sorted(
        (i for i in items if not ref[i["id"]]["proved"]), key=lambda i: (index_of(i), i["m"] * i["n"], i["rho"])
    )
    return proved + others


def mip_default_task(cfg: ConfigV3, inst: Row) -> Row:
    opts = dict(cfg.raw["mip_default"])
    label = f"threads{int(opts['threads'])}-{float(opts['time_limit_s']):g}s"
    task = core.make_task(cfg, "mip-default", inst, {**ext.MIP, "config": label}, None)
    task["mip"] = opts
    return task


@timed("mipdefault")
def mipdefault(cfg: ConfigV3, limit: float) -> Row:
    """MIP with all threads and the long limit (10.2), one run at a time, each in a fresh process."""
    started = time.time()
    raw = area(cfg) / "raw" / "mip_default.jsonl"
    raw.parent.mkdir(parents=True, exist_ok=True)
    done = {key_of(r) for r in read_jsonl(raw)}
    need = float(cfg.raw["mip_default"]["time_limit_s"])
    ran: list[str] = []
    waiting: list[str] = []
    order = mip_default_order(cfg)
    with environment.keep_awake():
        for inst in order:
            task = mip_default_task(cfg, inst)
            if key_of(task) in done:
                continue
            if waiting or limit - (time.time() - started) < need:
                waiting.append(inst["id"])
                continue
            with ProcessPoolExecutor(max_workers=1, mp_context=multiprocessing.get_context("spawn")) as pool:
                record = pool.submit(core.execute, task).result()
            append_jsonl(raw, record)
            ran.append(inst["id"])
            print(f"mip default: {inst['id']} {record['status']} in {record['time_s']:.0f} s", flush=True)
    result: Row = {
        "order": [i["id"] for i in order],
        "on_disk_before": len(done),
        "ran": ran,
        "not_run_time_rule": waiting,
        "time_limit_s": need,
    }
    write_atomic(area(cfg) / "mip_default.json", result)
    return result
