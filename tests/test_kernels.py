"""The compiled kernels against the independent plain-Python decoder and against their own plain versions."""

import numpy as np
import pytest

from helpers import random_balanced
from tpga import GAConfig, TransportProblem, run_ga
from tpga._kernels import Kernels
from tpga.decoder import _decode_valid_permutation
from tpga.ga import run_random_search


def _arrays(p):
    return p.supply.copy(), p.demand.copy(), p.cost.ravel().copy(), p.shape[1]


def test_compiled_decoder_matches_reference_on_10000_permutations():
    nb = Kernels("numba")
    rng = np.random.default_rng(20261116)
    checked = 0
    for k in range(100):
        m, n = int(rng.integers(1, 31)), int(rng.integers(1, 31))
        p = random_balanced(m, n, seed=k)
        if k % 2:  # non-integer data as well
            p = TransportProblem(p.supply * 0.37, p.demand * 0.37, p.cost * 1.13)
            p = p.balanced()
        supply, demand, cost, cols = _arrays(p)
        for _ in range(100):
            perm = rng.permutation(m * n).astype(np.int64)
            ref = _decode_valid_permutation(p, perm)
            plan = nb.decode_plan(perm, supply, demand, cols).reshape(m, n)
            assert np.array_equal(plan, ref)
            assert plan.tobytes() == ref.tobytes()
            assert nb.decode_cost(perm, supply, demand, cost, cols) == pytest.approx(p.total_cost(ref), rel=1e-12)
            checked += 1
    assert checked == 10_000


def test_plain_and_compiled_kernels_agree_bit_for_bit():
    py, nb = Kernels("python"), Kernels("numba")
    rng = np.random.default_rng(1)
    for k in range(30):
        p = random_balanced(int(rng.integers(1, 9)), int(rng.integers(1, 9)), seed=k)
        supply, demand, cost, cols = _arrays(p)
        perm = rng.permutation(p.cost.size).astype(np.int64)
        assert py.decode_cost(perm, supply, demand, cost, cols) == nb.decode_cost(perm, supply, demand, cost, cols)
        assert np.array_equal(py.decode_plan(perm, supply, demand, cols), nb.decode_plan(perm, supply, demand, cols))
        if p.cost.size >= 2:
            u1, u2 = rng.random(2)
            i, j = py.two_positions(u1, u2, p.cost.size)
            assert (i, j) == nb.two_positions(u1, u2, p.cost.size) and 0 <= i < j < p.cost.size
            other = rng.permutation(p.cost.size).astype(np.int64)
            assert np.array_equal(py.order_crossover(perm, other, i, j), nb.order_crossover(perm, other, i, j))
        u = rng.random(max(0, p.cost.size - 1))
        a, b = np.arange(p.cost.size), np.arange(p.cost.size)
        py.shuffle(a, u)
        nb.shuffle(b, u)
        assert np.array_equal(a, b) and sorted(a) == list(range(p.cost.size))


@pytest.mark.parametrize("init", ["random", "cost-aware"])
def test_ga_runs_identically_on_both_engines(init):
    p = random_balanced(5, 7, seed=3)
    cfg = GAConfig(population=16, generations=None, max_evaluations=1500, stagnation=40, seed=9, initialization=init)
    a, b = run_ga(p, cfg, engine="numba"), run_ga(p, cfg, engine="python")
    assert a.history == b.history and a.improvements == b.improvements
    assert a.evaluations == b.evaluations and np.array_equal(a.x, b.x)


def test_random_search_runs_identically_on_both_engines():
    p = random_balanced(4, 6, seed=5)
    a = run_random_search(p, 500, seed=3, engine="numba", batch_floats=200)
    b = run_random_search(p, 500, seed=3, engine="python", batch_floats=200)
    assert a.cost == b.cost and a.improvements == b.improvements and a.evaluations == b.evaluations == 500


def test_unknown_engine():
    with pytest.raises(ValueError):
        Kernels("gpu")
