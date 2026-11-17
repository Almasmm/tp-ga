"""Proposition 3 of the article: a swap of two idle arcs that the decoder cannot use is neutral.

Let u < v be two positions of a permutation. If neither arc carries flow in the decoded plan and one endpoint
of the arc at position v is exhausted before step u, the swap of the two positions does not change the plan.
Checked on random and on degenerate instances (small supplies, many equal costs, zero supplies and demands).
"""

from __future__ import annotations

import numpy as np
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from helpers import random_balanced
from tpga import TransportProblem, decode_permutation


def degenerate(m: int, n: int, seed: int) -> TransportProblem:
    """Supplies and demands of 0 to 3 units, costs from {1, 2}: many ties and many exhausted rows at once."""
    rng = np.random.default_rng(seed)
    a = rng.integers(0, 4, size=m)
    if a.sum() == 0:
        a[0] = 1
    b = rng.multinomial(int(a.sum()), np.full(n, 1 / n))
    return TransportProblem(a, b, rng.integers(1, 3, size=(m, n)))


def residual_before(p: TransportProblem, perm: np.ndarray, step: int) -> tuple[np.ndarray, np.ndarray]:
    """Supply and demand left after the decoder has processed the positions 0 .. step - 1."""
    a, b = p.supply.copy(), p.demand.copy()
    n = p.shape[1]
    for k in perm[:step]:
        i, j = divmod(int(k), n)
        q = min(a[i], b[j])
        a[i] -= q
        b[j] -= q
    return a, b


def premise(p: TransportProblem, perm: np.ndarray, x: np.ndarray, u: int, v: int) -> bool:
    """Both arcs idle in the plan ``x`` and an endpoint of the arc at position v exhausted before step u."""
    n = p.shape[1]
    flat = x.ravel()
    if flat[perm[u]] != 0 or flat[perm[v]] != 0:
        return False
    a, b = residual_before(p, perm, u)
    i, j = divmod(int(perm[v]), n)
    return bool(a[i] == 0 or b[j] == 0)


def count_cases(p: TransportProblem, rng: np.random.Generator, perms: int, pairs: int) -> tuple[int, int]:
    """(cases that satisfy the premise, cases among them whose plan changed) over random swaps."""
    size = p.cost.size
    cases = changed = 0
    if size < 2:
        return 0, 0
    for _ in range(perms):
        perm = rng.permutation(size)
        x = decode_permutation(p, perm)
        for _ in range(pairs):
            u, v = sorted(int(t) for t in rng.choice(size, size=2, replace=False))
            if not premise(p, perm, x, u, v):
                continue
            child = perm.copy()
            child[u], child[v] = child[v], child[u]
            cases += 1
            changed += not np.array_equal(decode_permutation(p, child), x)
    return cases, changed


def test_idle_swap_is_neutral_on_random_instances() -> None:
    rng = np.random.default_rng(20261118)
    cases = changed = 0
    for seed in range(120):
        m, n = (int(t) for t in rng.integers(2, 13, size=2))
        c, e = count_cases(random_balanced(m, n, seed, zeros=bool(seed % 2)), rng, perms=6, pairs=25)
        cases, changed = cases + c, changed + e
    assert changed == 0
    assert cases >= 5000  # the premise is common: most arcs are idle and most late arcs are closed


def test_idle_swap_is_neutral_on_degenerate_instances() -> None:
    rng = np.random.default_rng(20261119)
    cases = changed = 0
    for seed in range(120):
        m, n = (int(t) for t in rng.integers(2, 11, size=2))
        c, e = count_cases(degenerate(m, n, seed), rng, perms=6, pairs=25)
        cases, changed = cases + c, changed + e
    assert changed == 0
    assert cases >= 5000


@settings(max_examples=200, deadline=None, suppress_health_check=[HealthCheck.too_slow])
@given(
    m=st.integers(1, 10),
    n=st.integers(1, 10),
    seed=st.integers(0, 2**32 - 1),
    kind=st.sampled_from(["random", "zeros", "degenerate"]),
    data=st.data(),
)
def test_idle_swap_is_neutral_property(m: int, n: int, seed: int, kind: str, data: st.DataObject) -> None:
    p = degenerate(m, n, seed) if kind == "degenerate" else random_balanced(m, n, seed, zeros=kind == "zeros")
    size = p.cost.size
    if size < 2:
        return
    perm = np.array(data.draw(st.permutations(range(size))))
    u = data.draw(st.integers(0, size - 2))
    v = data.draw(st.integers(u + 1, size - 1))
    x = decode_permutation(p, perm)
    if not premise(p, perm, x, u, v):
        return
    child = perm.copy()
    child[u], child[v] = child[v], child[u]
    assert np.array_equal(decode_permutation(p, child), x)


def test_the_premise_is_needed() -> None:
    """Without the exhausted endpoint the swap can change the plan: the test would notice a vacuous premise."""
    p = TransportProblem([1, 1], [1, 1], [[1, 1], [1, 1]])
    perm = np.array([0, 3, 1, 2])  # x11 = 1, x22 = 1; arcs 1 and 2 idle
    x = decode_permutation(p, perm)
    assert not premise(p, perm, x, 0, 2)  # position 0 carries flow
    child = np.array([1, 3, 0, 2])
    assert not np.array_equal(decode_permutation(p, child), x)
