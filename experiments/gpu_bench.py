"""Benchmark of the GPU decoder prototype against the CPU kernel (writes docs/v0.4/gpu_bench.json).

    .venv-gpu/Scripts/python experiments/gpu_bench.py

Measures decoding of a batch of random permutations: CPU numba kernel on one core, the same kernel over all
cores (numba prange), and the GPU kernels (int64 and float64; host-to-device copy of the permutations and
the copy back are included). Checks that every GPU cost equals the CPU cost bit for bit.
"""

from __future__ import annotations

import json
import os
import platform
import statistics
import sys
import time
from functools import partial
from pathlib import Path

import numba
import numpy as np
from numba import njit, prange

from tpga import gpu
from tpga._kernels import _decode_cost
from tpga.experiments.instances import uniform_instance
from tpga.model import TransportProblem

SPEC = {"cost_low": 1, "cost_high": 100, "supply_low": 20, "supply_high": 100}
SIZES = [(50, 50), (100, 100), (200, 200)]
BATCHES = [100, 2400]
REPEATS = 5


@njit(cache=False)
def cpu_serial(perms, supply, demand, cost, n, out):
    for r in range(perms.shape[0]):
        out[r] = _decode_cost(perms[r], supply, demand, cost, n, 0.0)


@njit(parallel=True, cache=False)
def cpu_parallel(perms, supply, demand, cost, n, out):
    for r in prange(perms.shape[0]):
        out[r] = _decode_cost(perms[r], supply, demand, cost, n, 0.0)


def timed(fn, repeats: int = REPEATS) -> float:
    fn()  # warm-up and compilation
    ts = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn()
        ts.append(time.perf_counter() - t0)
    return statistics.median(ts)


def main() -> int:
    if not gpu.AVAILABLE:
        print("CUDA not available")
        return 1
    from numba import cuda

    dev = cuda.get_current_device()
    rows = []
    for m, n in SIZES:
        data = uniform_instance(m, n, 12345 + m, SPEC)
        p = TransportProblem.from_dict(data)
        a, b, c = p.supply, p.demand, np.ascontiguousarray(p.cost.ravel())
        rng = np.random.default_rng(1)
        for batch in BATCHES:
            perms = np.argsort(rng.random((batch, m * n)), axis=1).astype(np.int64)
            ref = np.empty(batch)
            t_serial = timed(partial(cpu_serial, perms, a, b, c, n, ref))
            par = np.empty(batch)
            t_par = timed(partial(cpu_parallel, perms, a, b, c, n, par))
            row = {
                "size": f"{m}x{n}",
                "batch": batch,
                "cpu_1core_s": t_serial,
                "cpu_allcores_s": t_par,
                "cpu_threads": numba.get_num_threads(),
                "cpu_parallel_equal": bool(np.array_equal(par, ref)),
            }
            for mode in ("int64", "float64"):
                dec = gpu.GPUDecoder(a, b, p.cost, batch, mode=mode)
                got = dec.costs(perms)
                row[f"gpu_{mode}_s"] = timed(partial(dec.costs, perms))
                row[f"gpu_{mode}_bitwise_equal"] = bool(np.array_equal(got, ref))
                row[f"speedup_{mode}_vs_allcores"] = t_par / row[f"gpu_{mode}_s"]
            rows.append(row)
            print(json.dumps(row))
    out = {
        "device": dev.name.decode() if isinstance(dev.name, bytes) else str(dev.name),
        "compute_capability": list(dev.compute_capability),
        "numba": numba.__version__,
        "numba_cuda": __import__("numba_cuda").__version__,
        "numpy": np.__version__,
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "cpu_count": os.cpu_count(),
        "repeats": REPEATS,
        "rows": rows,
    }
    path = Path(__file__).resolve().parents[1] / "docs" / "v0.4" / "gpu_bench.json"
    path.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
