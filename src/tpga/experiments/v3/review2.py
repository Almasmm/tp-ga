"""Run the frozen amendment 11 blocks, checkpointing each completed task."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
from concurrent.futures import FIRST_COMPLETED, ProcessPoolExecutor, wait
from pathlib import Path

for variable in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMBA_NUM_THREADS"):
    os.environ[variable] = "1"

import yaml  # noqa: E402

from tpga.experiments.v3 import core, rev  # noqa: E402

SPEC = Path("experiments/paper-v3-review2.yaml")
SETTINGS = yaml.safe_load(SPEC.read_text(encoding="utf-8"))
ROOT = Path(SETTINGS["output"])
REVIEW = core.ConfigV3.load(SETTINGS["review"])
KEY = ("instance", "seed", "method")


def records(path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def write(path, row):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as out:
        out.write(json.dumps(row, allow_nan=False, default=str) + "\n")


def key(task):
    return tuple(task.get(k) for k in KEY)


def k1_tasks():
    items = [item for item in rev.test_items(REVIEW) if item["m"] in (20, 30, 50, 70)]
    selected = rev.method(REVIEW, "GA-cost-cycle")
    for item in sorted(items, key=lambda i: (i["m"], i["rho"], i["id"])):
        for seed in REVIEW.seeds():
            for method, kind, population in (
                ("a", "independent", 1),
                ("b30", "independent", 30),
                ("b300", "independent", 300),
                ("c30", "population", 30),
                ("c300", "population", 300),
                ("d30", "population", 30),
                ("d300", "population", 300),
            ):
                task = core.make_task(REVIEW, "K1", item, {**selected, "method": method}, seed)
                yield {
                    **task,
                    "kind": kind,
                    "population": population,
                    "ox_rate": float(selected["params"]["crossover_rate"]) if method.startswith("d") else 0.0,
                }
            yield core.make_task(REVIEW, "K1", item, selected, seed)


def execute(task):
    if task["phase"] == "K1":
        from tpga.experiments.v3.review2_fctp import run
    elif task["phase"] == "K8":
        from tpga.experiments.v3.review2_mip import run
    else:
        from tpga.experiments.v3.review2_linear import run
    return {**{k: v for k, v in task.items() if k != "path"}, **run(task)}


def run_block(name, tasks, deadline, workers):
    path = ROOT / "raw" / f"{name}.jsonl"
    done = {key(row) for row in records(path)}
    tasks = list(tasks)
    pending = iter(task for task in tasks if key(task) not in done)
    started = time.time()
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    errors = 0
    stopped = False
    print(f"{name}: {len(done)} of {len(tasks)} already recorded", flush=True)
    pool = ProcessPoolExecutor(max_workers=workers)
    active = {}
    try:
        for _ in range(workers):
            task = next(pending, None)
            if task is not None and time.time() < deadline:
                active[pool.submit(execute, task)] = task
        while active:
            remaining = deadline - time.time()
            if remaining <= 0:
                stopped = True
                break
            finished, _ = wait(active, timeout=min(remaining, 15), return_when=FIRST_COMPLETED)
            for future in finished:
                task = active.pop(future)
                try:
                    row = future.result()
                    write(path, {**row, "runner_revision": revision})
                    done.add(key(task))
                except Exception as error:
                    errors += 1
                    write(ROOT / "errors.jsonl", {"block": name, "key": key(task), "error": repr(error)})
                task = next(pending, None)
                if task is not None and time.time() < deadline:
                    active[pool.submit(execute, task)] = task
            if finished and (len(done) + errors) % 100 < len(finished):
                print(f"{name}: {len(done)}/{len(tasks)} complete, {errors} errors", flush=True)
    finally:
        if active:
            pool.terminate_workers()
        else:
            pool.shutdown()
    write(
        ROOT / "blocks.jsonl",
        {
            "block": name,
            "planned": len(tasks),
            "completed": len(done),
            "errors": errors,
            "elapsed_s": time.time() - started,
            "runner_revision": revision,
            "deadline_reached": stopped,
        },
    )


def session_deadline():
    path = ROOT / "session.json"
    if not path.exists():
        ROOT.mkdir(parents=True, exist_ok=True)
        started = time.time()
        path.write_text(
            json.dumps(
                {
                    "started_epoch": started,
                    "deadline_epoch": started + SETTINGS["seconds"],
                    "code_head": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
                    "config": str(SPEC),
                    "workers": SETTINGS["workers"],
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    return json.loads(path.read_text(encoding="utf-8"))["deadline_epoch"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("block", choices=["K1", "K2", "K3", "K8"])
    block = parser.parse_args().block
    deadline = session_deadline()
    if block == "K1":
        tasks = k1_tasks()
    elif block == "K8":
        from tpga.experiments.v3.review2_mip import tasks as mip_tasks

        tasks = mip_tasks(REVIEW)
    else:
        from tpga.experiments.v3.review2_linear import tasks as linear_tasks

        tasks = linear_tasks(rev.lin_cfg(REVIEW), block)
    run_block(block, tasks, deadline, 1 if block == "K8" else SETTINGS["workers"])


if __name__ == "__main__":
    main()
