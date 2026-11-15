"""Generators of random balanced instances for the property tests."""

from __future__ import annotations

import numpy as np

from tpga import TransportProblem


def random_balanced(m: int, n: int, seed: int, total: int | None = None, zeros: bool = True) -> TransportProblem:
    """Integer balanced instance; with ``zeros`` some supplies and demands may be zero."""
    rng = np.random.default_rng(seed)
    total = int(total if total is not None else rng.integers(max(m, n), 50 * max(m, n) + 1))
    if zeros:
        a = rng.multinomial(total, rng.dirichlet(np.ones(m)))
        b = rng.multinomial(total, rng.dirichlet(np.ones(n)))
    else:
        a = 1 + rng.multinomial(total - m, np.full(m, 1 / m)) if total >= m else np.ones(m, dtype=int)
        b = 1 + rng.multinomial(int(a.sum()) - n, np.full(n, 1 / n))
        b[0] += int(a.sum() - b.sum())
    c = rng.integers(1, 101, size=(m, n))
    return TransportProblem(a, b, c)
