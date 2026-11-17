"""Memory of a run and a gate that starts a run only when its memory is free.

Windows fails an allocation when the commit limit (RAM plus page file) is used up, even with free RAM, so the
memory a run may use is the smaller of the free RAM and the free commit. The estimates are upper bounds of
the peak private bytes measured on this machine (2026-11-17, numerical libraries limited to one thread):

* GA, population P on m n arcs: 150 MiB + 24 bytes per (individual, arc). Measured: P 4000 on 100x100
  1016 MiB (bound 1066), P 2431 on 200x200 2343 MiB (bound 2376), P 4000 on 200x200 3797 MiB (bound 3812).
* SA and RS on 200x200: 94 and 106 MiB.
* A process that imports NumPy without ``OPENBLAS_NUM_THREADS=1`` commits about 1.5 GiB of OpenBLAS buffers
  before doing any work; the runners set the variable before NumPy is imported.

The tuning admits runs in the given order; the runner lets a later run that fits overtake one that waits for
memory. Results are collected by key or by index, so every
result is the same as without the gate; only the number of runs at once can be smaller.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from concurrent.futures import FIRST_COMPLETED, Executor, Future, wait
from typing import Any

from tpga.experiments.environment import usable_memory_bytes

MIB = 2**20
GIB = 2**30
BASE_BYTES = 150 * MIB
RESERVE_BYTES = 4 * GIB  # left to the system and to other programs


def reserve_bytes(raw: dict[str, Any]) -> int:
    """Memory left free by a run: ``memory_reserve_gib`` of the configuration (default 4 GiB)."""
    return int(float(raw.get("memory_reserve_gib", RESERVE_BYTES / GIB)) * GIB)


def ga_bytes(population: int, arcs: int) -> int:
    return BASE_BYTES + 24 * int(population) * int(arcs)


def task_bytes(task: dict[str, Any]) -> int:
    """Upper bound of the peak memory of one task of the runner or the tuning."""
    arcs = int(task["m"]) * int(task["n"])
    kind = task.get("kind")
    params = task.get("params") or {}
    if kind == "ga" or (kind == "representation" and task.get("part") == "ga"):
        pop = int(params.get("population", 100))
        extra = 0
        if kind == "representation":  # populations kept at the snapshots, plus the last one
            extra = 8 * pop * arcs * (len(task.get("snapshots", [])) + 1)
        return ga_bytes(pop, arcs) + extra
    if kind == "representation":  # random parents and their offspring
        return BASE_BYTES + 16 * int(task.get("random_parents", 1000)) * arcs
    if kind == "lp":  # HiGHS / OR-Tools model; generous
        return BASE_BYTES + 1000 * arcs
    return BASE_BYTES + 64 * arcs  # SA, RS, classical methods


def slots(per_task: int, workers: int, budget: int) -> int:
    """Runs of this size that fit at once (at least 1, at most ``workers``)."""
    return max(1, min(int(workers), int(budget // max(1, per_task))))


class MemoryGate:
    """Admit a run while the estimates of the running ones plus its own fit in ``budget`` and the memory free now
    (other programs may grow) still covers it with the reserve. A run is always admitted when none is running."""

    def __init__(
        self,
        workers: int,
        budget: int | None = None,
        reserve: int = RESERVE_BYTES,
        free_now: Callable[[], int] = usable_memory_bytes,
    ) -> None:
        self.workers = int(workers)
        self.reserve = int(reserve)
        self.free_now = free_now
        self.budget = int(budget if budget is not None else free_now() - reserve)
        self.running: dict[Any, int] = {}
        self.peak_running = 0
        self.held_back = 0  # times a run waited for memory although a worker was free

    @property
    def used(self) -> int:
        return sum(self.running.values())

    def admits(self, need: int) -> bool:
        if not self.running:
            return True
        if len(self.running) >= self.workers:
            return False
        ok = self.used + need <= self.budget and self.free_now() - self.reserve >= need
        if not ok:
            self.held_back += 1
        return ok

    def start(self, key: Any, need: int) -> None:
        self.running[key] = need
        self.peak_running = max(self.peak_running, len(self.running))

    def finish(self, key: Any) -> None:
        self.running.pop(key, None)


def pick(waiting: list[int], needs: list[int], gate: MemoryGate) -> int | None:
    """Position in ``waiting`` of the first run the gate admits now; None when no waiting run fits.

    ``waiting`` holds indices into ``needs`` in the order the runs should start. A run that does not fit is
    passed over together with every later run that needs at least as much.
    """
    if len(gate.running) >= gate.workers:
        return None
    refused: int | None = None
    for pos, i in enumerate(waiting):
        if refused is not None and needs[i] >= refused:
            continue
        if gate.admits(needs[i]):
            return pos
        refused = needs[i]
    return None


def run_gated(
    pool: Executor, fn: Callable[[Any], Any], items: list[Any], need: Callable[[Any], int], gate: MemoryGate
) -> Iterator[tuple[int, Future]]:
    """Submit ``fn(item)`` in the order of ``items`` under ``gate``; yield (index, finished future) as they end."""
    nxt = 0
    running: dict[Future, int] = {}
    while nxt < len(items) or running:
        while nxt < len(items) and gate.admits(need(items[nxt])):
            fut = pool.submit(fn, items[nxt])
            gate.start(fut, need(items[nxt]))
            running[fut] = nxt
            nxt += 1
        done, _ = wait(running, timeout=5.0, return_when=FIRST_COMPLETED)
        for fut in done:
            gate.finish(fut)
            yield running.pop(fut), fut
