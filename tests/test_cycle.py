"""Cycle mutation (amendment 8.1): encoding, pivots, the two implementations and the GA that uses them."""

from __future__ import annotations

import itertools

import numpy as np
import pytest

from tpga import _xkernels
from tpga._kernels import Kernels
from tpga.basis import is_basic
from tpga.cycle import GAXConfig, cycle_mutation, encode_plan, run_ga_x
from tpga.decoder import decode_permutation, decoder_eps
from tpga.experiments.instances import uniform_instance
from tpga.ga import GAConfig, run_ga
from tpga.model import TransportProblem
from tpga.verify import check_plan

UNIFORM = {"cost_low": 1, "cost_high": 100, "supply_low": 20, "supply_high": 100}
DEGENERATE = {"cost_low": 1, "cost_high": 5, "supply_low": 1, "supply_high": 4}


def instance(m: int, n: int, seed: int, degenerate: bool = False) -> TransportProblem:
    """Integer instance; the degenerate kind has small supplies, so many plans have fewer than m + n - 1
    positive arcs."""
    spec = DEGENERATE if degenerate else UNIFORM
    if degenerate:
        rng = np.random.default_rng(seed)
        a = rng.integers(1, 5, size=m)
        total = int(a.sum())
        if total < n:
            a[0] += n - total
            total = n
        b = 1 + rng.multinomial(total - n, np.full(n, 1 / n))
        return TransportProblem(a, b, rng.integers(1, 6, size=(m, n)))
    return TransportProblem.from_dict(uniform_instance(m, n, seed, spec))


def fast_plan(p: TransportProblem, perm: np.ndarray) -> np.ndarray:
    m, n = p.shape
    return (
        Kernels("numba")
        .decode_plan(np.ascontiguousarray(perm, dtype=np.int64), p.supply.copy(), p.demand.copy(), n, decoder_eps(p))
        .reshape(m, n)
    )


# (a) the encoded permutation decodes to exactly the plan it was built from: 10 000 random basic plans
PLANS = {(5, 5): 2500, (10, 10): 2500, (20, 20): 2000, (30, 30): 1500, (50, 50): 1000, (100, 100): 500}


def test_encoding_reproduces_ten_thousand_random_plans() -> None:
    assert sum(PLANS.values()) == 10_000
    rng = np.random.default_rng(20261119)
    checked = degenerate_plans = 0
    for (m, n), count in PLANS.items():
        problems = [instance(m, n, 100 * m + s, degenerate=s % 2 == 1) for s in range(10)]
        for t in range(count):
            p = problems[t % 10]
            parent = rng.permutation(m * n)
            x = fast_plan(p, parent)
            if t % 3 == 0:  # a plan after pivots, not only a decoded random permutation
                x = fast_plan(p, cycle_mutation(p, parent, 4, rng=rng).permutation)
            degenerate_plans += int(np.count_nonzero(x) < m + n - 1)
            perm = encode_plan(p, x, parent)
            assert np.array_equal(np.sort(perm), np.arange(m * n))
            assert np.array_equal(fast_plan(p, perm), x)
            checked += 1
    assert checked == 10_000
    assert degenerate_plans > 1000  # the completion of the basis is exercised


def test_encoding_keeps_the_parent_order_of_the_other_arcs() -> None:
    p = instance(6, 7, 3)
    rng = np.random.default_rng(1)
    parent = rng.permutation(42)
    x = decode_permutation(p, parent)
    perm = encode_plan(p, x, parent)
    tree = set(perm[:12].tolist())
    assert {int(k) for k in np.flatnonzero(x.ravel() > 0)} <= tree
    assert [g for g in parent.tolist() if g not in tree] == perm[12:].tolist()
    # without a parent the other arcs follow in index order
    assert encode_plan(p, x)[12:].tolist() == [g for g in range(42) if g not in set(encode_plan(p, x)[:12].tolist())]


def test_encoding_python_engine_agrees() -> None:
    rng = np.random.default_rng(5)
    for s in range(60):
        m, n = (int(v) for v in rng.integers(2, 9, size=2))
        p = instance(m, n, s, degenerate=s % 2 == 0)
        parent = rng.permutation(m * n)
        x = decode_permutation(p, parent)
        a = encode_plan(p, x, parent, engine="numba")
        b = encode_plan(p, x, parent, engine="python")
        assert np.array_equal(a, b)
        assert np.array_equal(decode_permutation(p, b), x)


def test_encode_plan_rejects_bad_input() -> None:
    p = TransportProblem([2, 2], [2, 2], [[1, 2], [3, 4]])
    with pytest.raises(ValueError, match="shape"):
        encode_plan(p, np.zeros((3, 2)))
    with pytest.raises(ValueError, match="cycle"):
        encode_plan(TransportProblem([2, 2, 2], [2, 2, 2], np.ones((3, 3))), [[1, 1, 0], [1, 1, 0], [0, 0, 2]])
    with pytest.raises(ValueError, match="more than"):
        encode_plan(p, [[1, 1], [1, 1]])
    with pytest.raises(ValueError, match="permutation"):
        encode_plan(p, [[2, 0], [0, 2]], parent=[0, 0, 1, 2])
    with pytest.raises(ValueError, match="balanced"):
        encode_plan(TransportProblem([3, 2], [2, 2], [[1, 2], [3, 4]]), [[2, 0], [0, 2]])


# (b) the plan after a pivot is feasible; (c) it is unchanged only when theta = 0
@pytest.mark.parametrize("engine", ["numba", "python"])
def test_pivot_keeps_feasibility_and_changes_the_plan_unless_theta_is_zero(engine: str) -> None:
    rng = np.random.default_rng(7)
    trials = 3000 if engine == "numba" else 250
    zero = changed = 0
    for t in range(trials):
        m, n = (int(v) for v in rng.integers(2, 13, size=2))
        p = instance(m, n, t, degenerate=t % 2 == 0)
        parent = rng.permutation(m * n)
        before = decode_permutation(p, parent)
        move = cycle_mutation(p, parent, 1, rng=rng, engine=engine)
        after = decode_permutation(p, move.permutation)
        assert check_plan(p, after).feasible
        assert is_basic(after)
        assert move.pivots == 1
        assert move.cost == pytest.approx(p.total_cost(after))
        same = np.array_equal(before, after)
        assert same == (move.zero_pivots == 1)  # unchanged if and only if theta = 0
        zero += move.zero_pivots
        changed += not same
    assert zero > 0 and changed > 0
    assert zero + changed == trials


def test_single_row_or_column_has_no_pivot() -> None:
    p = TransportProblem([5], [2, 3], [[1, 2]])
    move = cycle_mutation(p, [1, 0], 3, uniforms=[0.1, 0.5, 0.9])
    assert move.pivots == 0 and move.zero_pivots == 0
    assert np.array_equal(decode_permutation(p, move.permutation), [[2, 3]])
    assert cycle_mutation(p, [1, 0], 0).pivots == 0


def test_entering_arc_is_uniform_over_the_non_basic_arcs() -> None:
    """One uniform number per pivot: floor(u N') is the rank of the entering arc among the non-basic arcs."""
    k = _xkernels.table("python")
    basis = np.array([1, 4, 5, 9, 11], dtype=np.int64)
    others = [a for a in range(12) if a not in set(basis.tolist())]
    assert [k["_nonbasic"](basis, 5, r) for r in range(7)] == others
    sorted_basis = basis.copy()
    k["_replace_sorted"](sorted_basis, 5, 5, 0)
    assert sorted_basis.tolist() == [0, 1, 4, 9, 11]
    k["_replace_sorted"](sorted_basis, 5, 1, 10)
    assert sorted_basis.tolist() == [0, 4, 9, 10, 11]
    # the entering arc becomes basic: with u = 0 it is the first non-basic arc of the completed basis
    p = instance(4, 5, 11)
    parent = np.arange(20)
    move = cycle_mutation(p, parent, 1, uniforms=[0.0], engine="python")
    tree_before = set(encode_plan(p, decode_permutation(p, parent), parent)[:8].tolist())
    first = min(a for a in range(20) if a not in tree_before)
    assert first in set(move.permutation[:8].tolist())


def test_cycle_mutation_validates_input() -> None:
    p = instance(3, 3, 1)
    with pytest.raises(ValueError, match="permutation"):
        cycle_mutation(p, [0, 1, 2], 1)
    with pytest.raises(ValueError, match="nonnegative"):
        cycle_mutation(p, np.arange(9), -1)
    with pytest.raises(ValueError, match="uniform"):
        cycle_mutation(p, np.arange(9), 2, uniforms=[0.5])
    with pytest.raises(ValueError, match="engine"):
        cycle_mutation(p, np.arange(9), 1, engine="fortran")
    with pytest.raises(ValueError, match="shape of the cost"):
        cycle_mutation(p, np.arange(9), 1, fixed=np.ones(4))
    with pytest.raises(ValueError, match="nonnegative"):
        cycle_mutation(p, np.arange(9), 1, fixed=-np.ones((3, 3)))


# (d) Numba and Python give the same results
def test_cycle_mutation_is_the_same_in_numba_and_python() -> None:
    rng = np.random.default_rng(3)
    for t in range(150):
        m, n = (int(v) for v in rng.integers(2, 11, size=2))
        p = instance(m, n, t, degenerate=t % 3 == 0)
        parent = rng.permutation(m * n)
        u = rng.random(5)
        fixed = rng.integers(0, 50, size=(m, n)).astype(float) if t % 2 else None
        a = cycle_mutation(p, parent, 5, uniforms=u, fixed=fixed, engine="numba")
        b = cycle_mutation(p, parent, 5, uniforms=u, fixed=fixed, engine="python")
        assert np.array_equal(a.permutation, b.permutation)
        assert (a.cost, a.pivots, a.zero_pivots) == (b.cost, b.pivots, b.zero_pivots)
        if fixed is not None:
            y = decode_permutation(p, a.permutation)
            assert a.cost == pytest.approx(p.total_cost(y) + fixed[y > 0].sum())


def test_decode_arcs_and_fixed_charge_cost_match_the_decoder() -> None:
    rng = np.random.default_rng(9)
    for engine in ("numba", "python"):
        k = _xkernels.table(engine)
        for t in range(40):
            m, n = (int(v) for v in rng.integers(2, 9, size=2))
            p = instance(m, n, t, degenerate=t % 2 == 0)
            perm = rng.permutation(m * n).astype(np.int64)
            x = decode_permutation(p, perm)
            arcs, flows = np.empty(m + n, dtype=np.int64), np.empty(m + n)
            count = k["_decode_arcs"](perm, p.supply, p.demand, n, 0.0, np.empty(m), np.empty(n), arcs, flows)
            dense = np.zeros(m * n)
            dense[arcs[:count]] = flows[:count]
            assert np.array_equal(dense.reshape(m, n), x)
            fixed = rng.integers(0, 30, size=m * n).astype(float)
            cost = p.cost.ravel().copy()
            value = k["_decode_cost_fc"](perm, p.supply, p.demand, cost, fixed, n, 0.0)
            assert value == pytest.approx(p.total_cost(x) + fixed[x.ravel() > 0].sum())
            plain = Kernels(engine).decode_cost(perm, p.supply, p.demand, cost, n)
            assert k["_decode_cost_fc"](perm, p.supply, p.demand, cost, np.zeros(m * n), n, 0.0) == plain
    _xkernels.table("numba")
    with pytest.raises(ValueError, match="engine"):
        _xkernels.table("c")


def swap_pair(mode: str, strength: float, init: str, seed: int) -> tuple:
    p = instance(9, 11, 40 + seed)
    common = dict(population=30, crossover_rate=0.93, tournament=4, elite=2, seed=seed, max_evaluations=4000)
    old = run_ga(
        p, GAConfig(generations=None, mutation_mode=mode, mutation_strength=strength, initialization=init, **common)
    )
    new = run_ga_x(p, GAXConfig(mutation_mode=mode, mutation_strength=strength, initialization=init, **common))
    return old, new


@pytest.mark.parametrize(
    ("mode", "strength", "init"),
    [("swap_scaled", 0.0837, "random"), ("swap_count", 7, "cost-aware"), ("swap_scaled", 0.3, "cost-aware")],
)
def test_swap_modes_of_run_ga_x_reproduce_run_ga(mode: str, strength: float, init: str) -> None:
    for seed in (1, 2):
        old, new = swap_pair(mode, strength, init, seed)
        assert new.cost == old.cost
        assert np.array_equal(new.permutation, old.permutation)
        assert (new.evaluations, new.best_evaluation, new.generations, new.stop_reason) == (
            old.evaluations,
            old.best_evaluation,
            old.generations,
            old.stop_reason,
        )
        assert new.improvements == old.improvements
        assert new.pivots == 0


@pytest.mark.parametrize(("mode", "strength"), [("cycle", 2), ("cycle_scaled", 0.05)])
@pytest.mark.parametrize("init", ["random", "cost-aware"])
def test_cycle_ga_is_the_same_in_numba_and_python(mode: str, strength: float, init: str) -> None:
    p = instance(7, 8, 77)
    cfg = GAXConfig(
        population=20,
        crossover_rate=0.9,
        tournament=3,
        elite=2,
        seed=5,
        max_evaluations=1200,
        mutation_mode=mode,  # type: ignore[arg-type]
        mutation_strength=strength,
        initialization=init,  # type: ignore[arg-type]
    )
    a = run_ga_x(p, cfg, engine="numba")
    b = run_ga_x(p, cfg, engine="python")
    assert a.cost == b.cost
    assert np.array_equal(a.permutation, b.permutation)
    assert (a.evaluations, a.best_evaluation, a.pivots, a.zero_pivots, a.unchanged_offspring) == (
        b.evaluations,
        b.best_evaluation,
        b.pivots,
        b.zero_pivots,
        b.unchanged_offspring,
    )
    assert a.improvements == b.improvements
    # one decoder call per offspring: the budget is respected and every generation costs population - elite
    assert a.evaluations == 20 + a.generations * 18 <= 1200
    assert a.pivots == a.generations * 18 * cfg.moves(7, 8)
    assert check_plan(p, a.x).feasible
    assert a.cost == pytest.approx(p.total_cost(decode_permutation(p, a.permutation)))
    assert a.unchanged_offspring <= a.generations * 18


def test_cycle_ga_reaches_the_optimum_of_a_small_problem() -> None:
    from tpga.exact import solve_lp

    p = instance(6, 6, 123)
    res = run_ga_x(
        p,
        GAXConfig(
            population=40,
            crossover_rate=0.9,
            tournament=3,
            elite=2,
            seed=1,
            max_evaluations=7200,
            mutation_mode="cycle",
            mutation_strength=1,
        ),
    )
    assert res.cost == pytest.approx(solve_lp(p)[1])
    assert res.stop_reason == "budget"


def test_run_ga_x_callback_and_unbalanced_input() -> None:
    p = TransportProblem([5, 6], [4, 3], [[1, 2], [3, 4]])  # unbalanced: a dummy destination is added
    cfg = GAXConfig(population=6, crossover_rate=0.9, tournament=2, elite=1, seed=0, max_evaluations=60)
    seen: list[int] = []
    res = run_ga_x(p, cfg, callback=lambda g, e, c: seen.append(e) or g >= 2)
    assert res.stop_reason == "cancelled" and res.generations == 2 and seen[0] == 6
    assert res.x.shape == (2, 3)
    stopped = run_ga_x(p, cfg, callback=lambda g, e, c: True)
    assert stopped.stop_reason == "cancelled" and stopped.generations == 0
    with pytest.raises(ValueError, match="balanced"):
        run_ga_x(p, cfg, fixed=np.ones((2, 2)))


def test_first_improvement_step_lowers_the_fixed_charge_cost() -> None:
    rng = np.random.default_rng(13)
    improved_total = 0
    for t in range(60):
        m, n = (int(v) for v in rng.integers(3, 9, size=2))
        p = instance(m, n, 500 + t)
        fixed = rng.integers(1, 400, size=m * n).astype(float)
        cost = p.cost.ravel().copy()
        perm = rng.permutation(m * n).astype(np.int64)
        start = float(rng.random())
        out = {}
        for engine in ("numba", "python"):
            k = _xkernels.table(engine)
            q = perm.copy()
            work = (
                np.empty(m),
                np.empty(n),
                np.empty(m + n),
                np.empty((_xkernels.IW_ROWS, _xkernels.iw_columns(m, n)), dtype=np.int64),
                np.zeros(m * n, dtype=np.bool_),
            )
            before = k["_decode_cost_fc"](q, p.supply, p.demand, cost, fixed, n, 0.0)
            used, improved, value = k["_first_improvement"](
                q, p.supply, p.demand, cost, fixed, n, 0.0, start, 10**6, *work
            )
            after = k["_decode_cost_fc"](q, p.supply, p.demand, cost, fixed, n, 0.0)
            assert value == pytest.approx(after)
            assert (after < before) if improved else (after == pytest.approx(before))
            assert 1 <= used <= 1 + m * n - (m + n - 1)
            if not improved:
                assert used == 1 + m * n - (m + n - 1)  # every neighbour was evaluated
            out[engine] = (q.tolist(), int(used), int(improved), float(value))
            # with room for the decoding only, no neighbour is evaluated
            q2 = perm.copy()
            assert k["_first_improvement"](q2, p.supply, p.demand, cost, fixed, n, 0.0, start, 1, *work)[:2] == (1, 0)
            assert np.array_equal(q2, perm)
        assert out["numba"] == out["python"]
        improved_total += out["numba"][2]
    _xkernels.table("numba")
    assert improved_total > 30


def test_local_search_cannot_improve_a_local_optimum() -> None:
    """A plan that no single pivot improves is left as it is: exhaustive check on a tiny problem."""
    p = TransportProblem([3, 4], [2, 2, 3], [[1, 5, 3], [4, 2, 6]])
    fixed = np.array([[10.0, 1.0, 7.0], [3.0, 9.0, 2.0]])
    k = _xkernels.table("numba")
    best = min(
        k["_decode_cost_fc"](np.array(q, dtype=np.int64), p.supply, p.demand, p.cost.ravel(), fixed.ravel(), 3, 0.0)
        for q in itertools.permutations(range(6))
    )
    perm = np.arange(6, dtype=np.int64)
    work = (np.empty(2), np.empty(3), np.empty(5), np.empty((10, 12), dtype=np.int64), np.zeros(6, dtype=np.bool_))
    value = np.inf
    for _ in range(20):  # repeat the step until no neighbour is better
        _, improved, value = k["_first_improvement"](
            perm, p.supply, p.demand, p.cost.ravel(), fixed.ravel(), 3, 0.0, 0.0, 100, *work
        )
        if not improved:
            break
    assert not improved
    assert value >= best


def test_hybrid_counts_local_search_evaluations_in_the_budget() -> None:
    p = instance(8, 8, 9)
    fixed = np.random.default_rng(2).integers(1, 300, size=(8, 8)).astype(float)
    cfg = GAXConfig(
        population=24,
        crossover_rate=0.9,
        tournament=3,
        elite=2,
        seed=4,
        max_evaluations=3000,
        mutation_mode="cycle",
        mutation_strength=1,
        initialization="cost-aware",
        local_search_every=3,
    )
    a = run_ga_x(p, cfg, fixed=fixed, engine="numba")
    b = run_ga_x(p, cfg, fixed=fixed, engine="python")
    assert np.array_equal(a.permutation, b.permutation) and a.cost == b.cost
    assert (a.local_search_calls, a.local_search_evaluations, a.local_search_improvements) == (
        b.local_search_calls,
        b.local_search_evaluations,
        b.local_search_improvements,
    )
    assert a.local_search_calls >= 1 and a.local_search_evaluations >= 2 * a.local_search_calls
    assert a.evaluations == 24 + a.generations * 22 + a.local_search_evaluations <= 3000
    assert a.cost == pytest.approx(p.total_cost(a.x) + fixed[a.x > 0].sum())
    plain = run_ga_x(p, GAXConfig(**{**cfg.__dict__, "local_search_every": 0}), fixed=fixed)
    assert plain.local_search_calls == 0 and plain.evaluations == 24 + plain.generations * 22


@pytest.mark.parametrize(
    ("change", "message"),
    [
        ({"mutation_mode": "swap_fixed"}, "mutation_mode"),
        ({"mutation_mode": "cycle", "mutation_strength": 0.2}, "at least 1"),
        ({"mutation_mode": "cycle_scaled", "mutation_strength": 0.0}, "positive"),
        ({"initialization": "greedy"}, "initialization"),
        ({"population": 1}, "population"),
        ({"crossover_rate": 1.5}, "crossover_rate"),
        ({"tournament": 99}, "tournament"),
        ({"elite": 10}, "elite"),
        ({"max_evaluations": 5}, "max_evaluations"),
        ({"local_search_every": -1}, "local_search_every"),
        ({"decoder_tol": 0.5}, "decoder_tol"),
    ],
)
def test_gax_config_validation(change: dict, message: str) -> None:
    base = dict(population=10, crossover_rate=0.9, tournament=3, elite=2, max_evaluations=100)
    with pytest.raises(ValueError, match=message):
        GAXConfig(**{**base, **change})


def test_moves_per_offspring() -> None:
    base = dict(population=10, crossover_rate=0.9, tournament=3, elite=2, max_evaluations=100)
    assert GAXConfig(mutation_mode="cycle", mutation_strength=4, **base).moves(50, 50) == 4
    assert GAXConfig(mutation_mode="cycle_scaled", mutation_strength=0.05, **base).moves(50, 50) == 5
    assert GAXConfig(mutation_mode="cycle_scaled", mutation_strength=0.05, **base).moves(5, 5) == 1
    assert GAXConfig(mutation_mode="swap_scaled", mutation_strength=0.0837, **base).moves(20, 20) == 3
