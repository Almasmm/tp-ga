"""Resumable parallel runner of the v0.4 experiment with a live monitor and safe interruption.

Interruption: the first Ctrl+C (or Ctrl+Break) stops submitting new runs and lets the running ones finish;
the second abandons the running ones. Finished records are flushed in both cases; the next start skips every
key already on disk. Workers ignore the console signals so that only the main process decides.
"""

from __future__ import annotations

import multiprocessing as mp
import os
import signal
import sys
import time
from concurrent.futures import FIRST_COMPLETED, Future, ProcessPoolExecutor, wait
from typing import Any

from tpga.experiments import environment
from tpga.experiments.v2 import methods
from tpga.experiments.v2.config import ConfigV2
from tpga.experiments.v2.monitor import Monitor
from tpga.experiments.v2.storage import PartWriter, append_jsonl, clean_temporary, error_record, read_parts

PRIORITIES = {"normal": "NORMAL_PRIORITY_CLASS", "above_normal": "ABOVE_NORMAL_PRIORITY_CLASS"}


def set_priority(name: str) -> bool:
    """Process priority without administrator rights: ``normal`` or ``above_normal`` (never realtime)."""
    if name not in PRIORITIES:
        raise ValueError(f"priority must be one of {sorted(PRIORITIES)}")
    try:
        import psutil

        proc = psutil.Process()
        if sys.platform == "win32":
            proc.nice(getattr(psutil, PRIORITIES[name]))
        else:  # pragma: no cover - Linux: lower niceness needs privileges, keep the default
            return False
        return True
    except Exception:  # noqa: BLE001
        return False


def init_worker(cpu_queue: Any, classes: dict[int, int], status_queue: Any, priority: str, interval: float) -> None:
    environment.single_thread_environment()
    for sig in ("SIGINT", "SIGBREAK"):
        if hasattr(signal, sig):
            signal.signal(getattr(signal, sig), signal.SIG_IGN)
    try:  # HiGHS prints a banner to the C-level stdout; keep the terminal for the monitor
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, 1)
    except OSError:  # pragma: no cover
        pass
    set_priority(priority)
    if cpu_queue is not None:
        cpu = int(cpu_queue.get())
        if environment.pin_to_cpu(cpu):
            methods._STATE["cpu"] = cpu
            methods._STATE["cpu_class"] = classes.get(cpu)
    methods._STATE["queue"] = status_queue
    methods._STATE["interval"] = interval


class Interrupt:
    """Counts console interruptions; installed only in the main process."""

    def __init__(self) -> None:
        self.count = 0
        self._old: dict[int, Any] = {}

    def __enter__(self) -> Interrupt:
        for name in ("SIGINT", "SIGBREAK"):
            if hasattr(signal, name):
                sig = getattr(signal, name)
                self._old[sig] = signal.signal(sig, self._handle)
        return self

    def _handle(self, *_: Any) -> None:
        self.count += 1

    def __exit__(self, *_: Any) -> None:
        for sig, old in self._old.items():
            signal.signal(sig, old)


def done_keys(cfg: ConfigV2) -> set[str]:
    return {methods.key_of(r) for r in read_parts(cfg.output / "raw" / "runs", "runs")}


def warm_up() -> None:
    """Compile (or load from the numba cache) the kernels once in the main process."""
    from tpga import GAConfig, TransportProblem, run_ga
    from tpga.ga import run_random_search
    from tpga.sa import SAConfig, run_sa

    p = TransportProblem.random(3, 4, seed=0)
    run_ga(p, GAConfig(population=6, generations=2, seed=0))
    run_ga(p, GAConfig(population=6, generations=2, seed=0, mutation_mode="swap_count", mutation_strength=2))
    run_random_search(p, 10, seed=0)
    run_sa(p, SAConfig(max_evaluations=200, pilot_moves=10, seed=0))


def execute_tasks(
    cfg: ConfigV2,
    phase: str,
    tasks: list[dict[str, Any]],
    cpus: list[int],
    monitor: Monitor,
    interrupt: Interrupt,
    log_path: Any,
    live: Any = None,
) -> dict[str, int]:
    """Run the tasks whose key is not on disk; returns counts of done, errors and abandoned runs."""
    raw = cfg.output / "raw"
    clean_temporary(raw / "runs")
    clean_temporary(raw / "curves")
    finished = done_keys(cfg)
    todo = [t for t in tasks if methods.key_of(t) not in finished]
    todo.sort(key=lambda t: -(int(t["m"]) * int(t["n"])) * int(t.get("budget") or 1))
    monitor.start_phase(phase, len(todo), len(tasks) - len(todo))
    append_jsonl(
        log_path,
        {
            "time": time.time(),
            "event": "phase_start",
            "phase": phase,
            "todo": len(todo),
            "skipped": len(tasks) - len(todo),
        },
    )
    counts = {"done": 0, "errors": 0, "abandoned": 0}
    if not todo:
        return counts
    runs = PartWriter(raw / "runs", "runs")
    curves = PartWriter(raw / "curves", "curves", max_records=5000)
    classes = environment.cpu_classes()
    manager = mp.Manager()
    cpu_queue = manager.Queue()
    for c in cpus:
        cpu_queue.put(c)
    status = manager.Queue()
    pool = ProcessPoolExecutor(
        max_workers=len(cpus),
        initializer=init_worker,
        initargs=(cpu_queue, classes, status, str(cfg.raw.get("priority", "above_normal")), 1.0),
    )
    pending: dict[Future, dict[str, Any]] = {}
    it = iter(todo)
    aborted = False
    try:
        for t in it:
            pending[pool.submit(methods.execute, t)] = t
            if len(pending) >= 2 * len(cpus):
                break
        while pending:
            if interrupt.count >= 1 and not monitor.message:
                monitor.message = (
                    "Остановка: новые запуски не начинаются, текущие доделываются. "
                    "Повторное Ctrl+C бросит текущие запуски (готовые записи сохранятся)."
                )
                append_jsonl(log_path, {"time": time.time(), "event": "interrupt", "phase": phase})
                for fut in [f for f in pending if f.cancel()]:
                    pending.pop(fut)
            if interrupt.count >= 2:
                aborted = True
                counts["abandoned"] = len(pending)
                break
            done, _ = wait(pending, timeout=0.5, return_when=FIRST_COMPLETED)
            while True:
                try:
                    monitor.status(status.get_nowait())
                except Exception:  # noqa: BLE001 - queue empty
                    break
            for fut in done:
                task = pending.pop(fut)
                try:
                    record, curve_rows = fut.result()
                except Exception as exc:  # noqa: BLE001 - every failure is logged with its traceback
                    counts["errors"] += 1
                    monitor.error()
                    err = error_record(task, exc)
                    append_jsonl(cfg.output / "logs" / "errors.jsonl", err)
                    append_jsonl(log_path, {"event": "error", **err})
                    continue
                runs.add([record])
                if curve_rows:
                    curves.add(curve_rows)
                counts["done"] += 1
                monitor.finished(record)
                append_jsonl(
                    log_path,
                    {
                        "time": time.time(),
                        "event": "run",
                        "key": methods.key_of(record),
                        "gap": record.get("gap"),
                        "time_s": record.get("time_s"),
                    },
                )
                if interrupt.count == 0:
                    nxt = next(it, None)
                    if nxt is not None:
                        pending[pool.submit(methods.execute, nxt)] = nxt
            monitor.tick()
            if live is not None:
                live.update(monitor.render())
    finally:
        runs.flush()
        curves.flush()
        if aborted:
            for proc in list(getattr(pool, "_processes", {}).values()):
                proc.terminate()
            pool.shutdown(wait=False, cancel_futures=True)
        else:
            pool.shutdown(wait=True, cancel_futures=True)
        manager.shutdown()
        append_jsonl(
            log_path,
            {"time": time.time(), "event": "phase_end", "phase": phase, **counts, "interrupted": interrupt.count > 0},
        )
    return counts
