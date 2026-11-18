"""Fixed-charge transportation problem (amendment 8.4): model, generator, MIP reference and heuristics."""

from __future__ import annotations

import itertools
import json

import numpy as np
import pytest

from tpga.decoder import decode_permutation
from tpga.fctp import (
    FixedChargeProblem,
    balinski,
    generate,
    run_random_search_fc,
    run_sa_fc,
    solve_mip,
    vogel_linearised,
)
from tpga.ga import run_random_search
from tpga.model import TransportProblem
from tpga.sa import SAConfig, run_sa
from tpga.verify import check_plan


def small(seed: int = 1, m: int = 5, n: int = 6, rho: float = 1.0) -> FixedChargeProblem:
    return FixedChargeProblem.from_dict(generate(m, n, seed, rho))


def test_generator_follows_the_rule_of_the_amendment() -> None:
    from tpga.experiments.instances import uniform_instance

    d = generate(10, 10, 20300000, 0.2)
    base = uniform_instance(10, 10, 20300000, {"cost_low": 1, "cost_high": 100, "supply_low": 20, "supply_high": 100})
    assert (d["supply"], d["demand"], d["cost"]) == (base["supply"], base["demand"], base["cost"])
    total, c_mean = sum(d["supply"]), float(np.mean(d["cost"]))
    assert d["fixed_high"] == round(2 * 0.2 * c_mean * total / 19)
    f = np.array(d["fixed"])
    assert f.shape == (10, 10) and f.min() >= 1 and f.max() <= d["fixed_high"]
    assert generate(10, 10, 20300000, 0.2) == d  # deterministic
    assert generate(10, 10, 20300000, 1.0)["fixed_high"] == round(2 * 1.0 * c_mean * total / 19)
    assert generate(10, 10, 20300001, 0.2)["fixed"] != d["fixed"]
    assert all(20 <= a <= 100 for a in d["supply"]) and sum(d["supply"]) == sum(d["demand"])


def test_model_cost_linearisation_and_io(tmp_path) -> None:
    p = TransportProblem([3, 4], [2, 2, 3], [[1, 5, 3], [4, 2, 6]])
    fcp = FixedChargeProblem(p, [[10, 1, 7], [3, 9, 2]])
    x = np.array([[2, 0, 1], [0, 2, 2]], dtype=float)
    assert fcp.total_cost(x) == (2 * 1 + 1 * 3 + 2 * 2 + 2 * 6) + (10 + 7 + 9 + 2)
    assert fcp.shape == (2, 3)
    assert fcp.big_m.tolist() == [[2, 2, 3], [2, 2, 3]]
    lin = fcp.linearised()
    assert lin.cost.tolist() == [[1 + 10 / 2, 5 + 1 / 2, 3 + 7 / 3], [4 + 3 / 2, 2 + 9 / 2, 6 + 2 / 3]]
    path = tmp_path / "f.json"
    path.write_text(json.dumps(fcp.to_dict()), encoding="utf-8")
    again = FixedChargeProblem.from_json(path)
    assert np.array_equal(again.fixed, fcp.fixed) and np.array_equal(again.problem.cost, p.cost)
    with pytest.raises(ValueError, match="fixed"):
        FixedChargeProblem.from_dict(p.to_dict())
    with pytest.raises(ValueError, match="balanced"):
        FixedChargeProblem(TransportProblem([3, 5], [2, 2, 3], p.cost), np.ones((2, 3)))
    with pytest.raises(ValueError, match="shape"):
        FixedChargeProblem(p, np.ones((3, 2)))
    with pytest.raises(ValueError, match="nonnegative"):
        FixedChargeProblem(p, -np.ones((2, 3)))
    # an arc that can carry nothing keeps its cost in the linearisation
    zero = FixedChargeProblem(TransportProblem([0, 4], [2, 2], [[1, 5], [4, 2]]), [[10, 1], [3, 9]])
    assert zero.linearised().cost[0].tolist() == [1, 5]


def test_mip_optimum_equals_the_best_decoded_permutation() -> None:
    """The FCTP optimum is attained at a vertex and every vertex is a decoded permutation: on a 2 x 3 problem
    the minimum over all 720 permutations equals the MIP optimum."""
    for seed in range(6):
        rng = np.random.default_rng(seed)
        a = rng.integers(2, 9, size=2)
        b = 1 + rng.multinomial(int(a.sum()) - 3, np.full(3, 1 / 3))
        p = TransportProblem(a, b, rng.integers(1, 20, size=(2, 3)))
        fcp = FixedChargeProblem(p, rng.integers(1, 60, size=(2, 3)))
        best = min(fcp.total_cost(decode_permutation(p, q)) for q in itertools.permutations(range(6)))
        mip = solve_mip(fcp, time_limit=30)
        assert mip.proved and mip.status == "Optimal"
        assert mip.cost == pytest.approx(best)
        assert mip.bound <= mip.cost + 1e-6 and mip.gap is not None and mip.gap * mip.cost < 1.0
        assert check_plan(p, mip.x).feasible


def test_mip_bounds_and_the_linearisation_heuristics() -> None:
    fcp = small(3, 6, 6)
    mip = solve_mip(fcp, time_limit=30)
    assert mip.proved and mip.x is not None and mip.cost is not None
    x_b, cost_b, lp_value = balinski(fcp)
    assert check_plan(fcp.problem, x_b).feasible
    assert lp_value <= mip.cost + 1e-6 <= cost_b + 2e-6  # LP of the linearisation is a lower bound
    assert cost_b == pytest.approx(fcp.total_cost(x_b))
    x_v, cost_v = vogel_linearised(fcp)
    assert check_plan(fcp.problem, x_v).feasible and cost_v >= mip.cost - 1e-6
    assert mip.nodes >= 0 and mip.time_s >= 0 and isinstance(mip.version, str)


def test_mip_time_limit_reports_a_bound_without_proof() -> None:
    fcp = small(5, 15, 15)
    mip = solve_mip(fcp, time_limit=0.05)
    assert not mip.proved
    assert mip.status != "Optimal"
    assert np.isfinite(mip.bound)
    if mip.cost is not None:  # a feasible plan was found before the limit
        assert mip.bound <= mip.cost + 1e-6 and 0 <= mip.gap <= 1
        assert check_plan(fcp.problem, mip.x).feasible


@pytest.mark.parametrize("engine", ["numba", "python"])
def test_zero_fixed_charges_reproduce_the_linear_methods(engine: str) -> None:
    fcp = small(8)
    zero = FixedChargeProblem(fcp.problem, np.zeros(fcp.shape))
    a = run_random_search(fcp.problem, 700, seed=3, engine=engine, batch_floats=3000)
    b = run_random_search_fc(zero, 700, seed=3, engine=engine, batch_floats=3000)
    assert (a.cost, a.best_evaluation, a.improvements) == (b.cost, b.best_evaluation, b.improvements)
    assert np.array_equal(a.permutation, b.permutation) and b.evaluations == 700
    for init in ("random", "cost-aware"):
        cfg = SAConfig(max_evaluations=900, seed=4, initialization=init, pilot_moves=30)
        c = run_sa(fcp.problem, cfg, engine=engine, chunk=256)
        d = run_sa_fc(zero, cfg, engine=engine, chunk=256)
        assert (c.cost, c.best_evaluation, c.evaluations, c.improvements) == (
            d.cost,
            d.best_evaluation,
            d.evaluations,
            d.improvements,
        )
        assert np.array_equal(c.permutation, d.permutation)


def test_heuristics_minimise_the_true_cost_and_engines_agree() -> None:
    fcp = small(11)
    out = {}
    for engine in ("numba", "python"):
        rs = run_random_search_fc(fcp, 600, seed=1, engine=engine)
        sa = run_sa_fc(fcp, SAConfig(max_evaluations=800, seed=2, pilot_moves=20), engine=engine)
        for res in (rs, sa):
            assert check_plan(fcp.problem, res.x).feasible
            assert res.cost == pytest.approx(fcp.total_cost(res.x))
            assert res.cost == pytest.approx(res.improvements[-1][1])
            assert res.stop_reason == "budget"
        out[engine] = (rs.cost, rs.best_evaluation, sa.cost, sa.best_evaluation, sa.permutation.tolist())
    assert out["numba"] == out["python"]
    assert run_sa_fc(fcp, SAConfig(max_evaluations=800, seed=2, pilot_moves=20)).cost >= solve_mip(fcp, 30).cost - 1e-6


def test_fc_drivers_validate_and_can_be_cancelled() -> None:
    fcp = small(2, 4, 4)
    with pytest.raises(ValueError, match="positive"):
        run_random_search_fc(fcp, 0)
    with pytest.raises(ValueError, match="budget only"):
        run_sa_fc(fcp, SAConfig(max_evaluations=500, stagnation_evaluations=10))
    rs = run_random_search_fc(fcp, 500, seed=1, batch_floats=150, callback=lambda b, e, c: True)
    assert rs.stop_reason == "cancelled" and rs.evaluations < 500
    sa = run_sa_fc(fcp, SAConfig(max_evaluations=500, seed=1), chunk=100, callback=lambda s, e, c: True)
    assert sa.stop_reason == "cancelled" and sa.evaluations < 500


def test_mip_plan_is_cleaned_of_solver_noise() -> None:
    """With integer supplies and demands the reference plan is integer and exactly feasible; the instance is
    one on which HiGHS returned amounts 1e-7 away from the vertex."""
    from tpga.fctp import _clean_plan

    fcp = FixedChargeProblem.from_dict(generate(10, 10, 20300100, 1.0))
    mip = solve_mip(fcp, time_limit=60)
    assert mip.x is not None and np.array_equal(mip.x, np.rint(mip.x))
    assert check_plan(fcp.problem, mip.x, rtol=0.0).feasible
    assert mip.cost == float(round(mip.cost))
    p = TransportProblem([3, 4], [2, 2, 3], [[1, 5, 3], [4, 2, 6]])
    exact = np.array([[2.0, 0.0, 1.0], [0.0, 2.0, 2.0]])
    noisy = exact + np.array([[1e-7, 0.0, -1e-7], [-1e-7, 0.0, 1e-7]])
    assert np.array_equal(_clean_plan(p, noisy), exact)
    far = np.array([[1.6, 0.4, 1.0], [0.4, 1.6, 2.0]])  # not near a vertex: left as it is
    assert np.array_equal(_clean_plan(p, far), far)
    fractional = TransportProblem([2.5, 4.5], [2, 2, 3], p.cost)  # non-integer data: only tiny amounts are cut
    plan = np.array([[2.0, 0.5, 1e-9], [0.0, 1.5, 3.0]])
    assert np.array_equal(_clean_plan(fractional, plan), [[2.0, 0.5, 0.0], [0.0, 1.5, 3.0]])
