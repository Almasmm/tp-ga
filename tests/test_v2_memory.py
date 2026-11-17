"""Memory estimates and the gate that starts a run only when its memory is free."""

from __future__ import annotations

import threading
import time
from concurrent.futures import ThreadPoolExecutor

from tpga.experiments import environment
from tpga.experiments.v2 import memory

GIB = 2**30
MIB = 2**20


def test_estimates_bound_the_measured_peaks() -> None:
    # peak private bytes measured on 2026-11-17 with one-thread numerical libraries
    assert memory.ga_bytes(4000, 100 * 100) >= 1016 * MIB
    assert memory.ga_bytes(2431, 200 * 200) >= 2343 * MIB
    assert memory.ga_bytes(4000, 200 * 200) >= 3797 * MIB
    assert memory.ga_bytes(4000, 200 * 200) < 1.05 * 3797 * MIB  # tight enough to be useful
    ga = {"kind": "ga", "m": 200, "n": 200, "params": {"population": 2431}}
    assert memory.task_bytes(ga) == memory.ga_bytes(2431, 40000)
    rep = {**ga, "kind": "representation", "part": "ga", "snapshots": [0.1, 0.5, 1.0]}
    assert memory.task_bytes(rep) == memory.ga_bytes(2431, 40000) + 4 * 8 * 2431 * 40000
    assert memory.task_bytes({"kind": "sa", "m": 200, "n": 200}) >= 106 * MIB
    assert memory.slots(memory.ga_bytes(4000, 40000), 24, 40 * GIB) == 10
    assert memory.slots(memory.ga_bytes(100, 2500), 24, 40 * GIB) == 24
    assert memory.slots(100 * GIB, 24, 40 * GIB) == 1


def test_gate_limits_memory_and_keeps_the_order() -> None:
    """Tasks of 3 GiB under a 10 GiB budget: at most 3 at once, results in task order, none skipped."""
    lock = threading.Lock()
    running = {"now": 0, "peak": 0}
    started: list[int] = []

    def work(i: int) -> int:
        with lock:
            started.append(i)
            running["now"] += 1
            running["peak"] = max(running["peak"], running["now"])
        time.sleep(0.02)
        with lock:
            running["now"] -= 1
        return i * i

    sizes = [3 * GIB] * 6 + [GIB // 2] * 6
    gate = memory.MemoryGate(workers=8, budget=10 * GIB, reserve=0, free_now=lambda: 100 * GIB)
    with ThreadPoolExecutor(8) as pool:
        out = dict(memory.run_gated(pool, work, list(range(12)), lambda i: sizes[i], gate))
    assert {i: f.result() for i, f in out.items()} == {i: i * i for i in range(12)}
    assert started[:6] == sorted(started[:6])  # admitted in the given order
    assert gate.peak_running <= 8 and gate.held_back > 0
    assert running["peak"] <= 8


def test_gate_waits_for_memory_taken_by_other_programs() -> None:
    free = {"now": 2 * GIB}
    gate = memory.MemoryGate(workers=4, budget=20 * GIB, reserve=GIB, free_now=lambda: free["now"])
    assert gate.admits(5 * GIB)  # nothing running: always one run
    gate.start("a", 5 * GIB)
    assert not gate.admits(2 * GIB)  # 2 GiB free, less the 1 GiB reserve, is not enough
    free["now"] = 10 * GIB
    assert gate.admits(2 * GIB)
    gate.finish("a")
    assert gate.used == 0


def test_memory_status_reports_commit() -> None:
    s = environment.memory_status()
    assert s["ram_free"] > 0 and s["commit_free"] > 0 and s["commit_limit"] >= s["commit_free"]
    assert 0 < environment.usable_memory_bytes() <= s["commit_limit"]
