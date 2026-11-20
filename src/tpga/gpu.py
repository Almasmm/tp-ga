"""Prototype: the greedy decoder on a CUDA GPU (numba-cuda), one thread per permutation.

Not used by the GA or by the experiment. ``docs/v0.4/GPU.md`` records the benchmark and the decision.
The kernels follow ``tpga._kernels._decode_cost_py`` step by step (same arc order, same early stop), so on
integer data the costs are bitwise equal to the CPU kernel: every partial sum is an integer below 2**53.

Two variants: ``float64`` (any data; consumer GPUs run FP64 at a small fraction of FP32 speed) and
``int64`` (integer supplies, demands and costs only; exact integer arithmetic, converted to float at the end).
"""

from __future__ import annotations

from typing import Any

import numpy as np

try:  # optional: needs ``numba-cuda`` and a CUDA driver
    from numba import cuda

    AVAILABLE = bool(cuda.is_available())
except Exception:  # pragma: no cover - depends on the machine
    cuda = None  # type: ignore[assignment]
    AVAILABLE = False

_KERNELS: dict[str, Any] = {}


def _build() -> None:  # pragma: no cover - needs a GPU
    if _KERNELS:
        return

    @cuda.jit
    def decode_f64(perms, supply, demand, cost, n, eps, a_s, b_s, out):
        r = cuda.grid(1)
        if r >= perms.shape[0]:
            return
        m = supply.shape[0]
        active = 0
        for i in range(m):
            a_s[r, i] = supply[i]
            if supply[i] > eps:
                active += 1
        for j in range(n):
            b_s[r, j] = demand[j]
        total = 0.0
        for t in range(perms.shape[1]):
            if active == 0:
                break
            k = perms[r, t]
            i = k // n
            j = k - i * n
            q = min(a_s[r, i], b_s[r, j])
            if q > eps:
                total += cost[k] * q
                a_s[r, i] -= q
                b_s[r, j] -= q
                if a_s[r, i] <= eps:
                    active -= 1
        out[r] = total

    @cuda.jit
    def decode_i64(perms, supply, demand, cost, n, a_s, b_s, out):
        r = cuda.grid(1)
        if r >= perms.shape[0]:
            return
        m = supply.shape[0]
        active = 0
        for i in range(m):
            a_s[r, i] = supply[i]
            if supply[i] > 0:
                active += 1
        for j in range(n):
            b_s[r, j] = demand[j]
        total = 0
        for t in range(perms.shape[1]):
            if active == 0:
                break
            k = perms[r, t]
            i = k // n
            j = k - i * n
            q = min(a_s[r, i], b_s[r, j])
            if q > 0:
                total += cost[k] * q
                a_s[r, i] -= q
                b_s[r, j] -= q
                if a_s[r, i] <= 0:
                    active -= 1
        out[r] = total

    _KERNELS["float64"] = decode_f64
    _KERNELS["int64"] = decode_i64


class GPUDecoder:  # pragma: no cover - needs a GPU
    """Problem data and scratch kept on the device; ``costs(perms)`` decodes one batch."""

    def __init__(
        self,
        supply: np.ndarray,
        demand: np.ndarray,
        cost: np.ndarray,
        batch: int,
        mode: str = "int64",
        eps: float = 0.0,
        threads: int = 64,
    ) -> None:
        if not AVAILABLE:
            raise RuntimeError("CUDA is not available (install numba-cuda and a CUDA driver)")
        _build()
        self.mode = mode
        self.n = int(demand.size)
        self.eps = float(eps)
        self.threads = threads
        flat = np.ascontiguousarray(cost, dtype=float).ravel()
        if mode == "int64":
            data = np.concatenate([supply, demand, flat])
            if not np.array_equal(data, np.round(data)):
                raise ValueError("the int64 kernel needs integer supplies, demands and costs")
            dt: Any = np.int64
        else:
            dt = np.float64
        self.supply = cuda.to_device(np.asarray(supply, dtype=dt))
        self.demand = cuda.to_device(np.asarray(demand, dtype=dt))
        self.cost = cuda.to_device(flat.astype(dt))
        self.a_s = cuda.device_array((batch, supply.size), dtype=dt)
        self.b_s = cuda.device_array((batch, demand.size), dtype=dt)
        self.out = cuda.device_array(batch, dtype=dt)
        self.batch = batch

    def costs(self, perms: np.ndarray) -> np.ndarray:
        k = perms.shape[0]
        if k > self.batch:
            raise ValueError("batch larger than the allocated scratch")
        d_perms = cuda.to_device(np.ascontiguousarray(perms, dtype=np.int64))
        blocks = (k + self.threads - 1) // self.threads
        if self.mode == "int64":
            _KERNELS["int64"][blocks, self.threads](
                d_perms, self.supply, self.demand, self.cost, self.n, self.a_s, self.b_s, self.out
            )
        else:
            _KERNELS["float64"][blocks, self.threads](
                d_perms, self.supply, self.demand, self.cost, self.n, self.eps, self.a_s, self.b_s, self.out
            )
        res = self.out[:k].copy_to_host()
        return res.astype(np.float64)
