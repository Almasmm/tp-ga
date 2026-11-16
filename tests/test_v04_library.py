"""v0.4 library features: mutation modes (L1), stagnation in decoder calls (L2), HiGHS timing (L3),
OR-Tools (L4), simulated annealing (L6), decoder tolerance (L8)."""

import numpy as np
import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from helpers import random_balanced
from tpga import GAConfig, TransportProblem, decode_permutation, run_ga, solve_lp
from tpga.classical import vogel
from tpga.decoder import decoder_eps
from tpga.exact import solve_lp_detailed, solve_lp_highspy
from tpga.network_simplex import solve_min_cost_flow
from tpga.sa import SAConfig, run_sa

MODES = [("swap_count", 3), ("swap_per_position", 0.2), ("swap_scaled", 0.25)]


@pytest.mark.parametrize(("mode", "strength"), MODES)
def test_mutation_modes_run_identically_on_both_engines(mode, strength):
    p = random_balanced(5, 6, seed=4)
    cfg = GAConfig(
        population=12, generations=None, max_evaluations=800, seed=3, mutation_mode=mode, mutation_strength=strength
    )
    a, b = run_ga(p, cfg), run_ga(p, cfg, engine="python")
    assert a.history == b.history and a.evaluations == b.evaluations and np.array_equal(a.x, b.x)
    assert p.is_feasible(a.x)


def test_mutation_modes_change_the_search_but_not_feasibility():
    p = random_balanced(8, 9, seed=1)
    _, z = solve_lp(p)
    costs = {}
    for mode, strength in [("swap_fixed", 0.2), *MODES]:
        r = run_ga(
            p,
            GAConfig(
                population=20,
                generations=None,
                max_evaluations=4000,
                seed=0,
                mutation_mode=mode,
                mutation_strength=strength,
            ),
        )
        assert p.is_feasible(r.x) and r.cost >= z - 1e-9
        costs[mode] = r.history
    assert len({tuple(h) for h in costs.values()}) > 1


@pytest.mark.parametrize(
    "kwargs",
    [
        {"mutation_mode": "nope"},
        {"mutation_mode": "swap_count", "mutation_strength": 0.2},
        {"mutation_mode": "swap_per_position", "mutation_strength": 1.5},
        {"mutation_mode": "swap_scaled", "mutation_strength": 0},
        {"stagnation_evaluations": 0},
        {"decoder_tol": 0.1},
    ],
)
def test_invalid_v04_config(kwargs):
    with pytest.raises(ValueError):
        GAConfig(**kwargs)


def test_stagnation_in_decoder_calls():
    p = random_balanced(6, 6, seed=2)
    r = run_ga(p, GAConfig(population=10, generations=None, stagnation_evaluations=200, seed=1))
    assert r.stop_reason == "stagnation_evaluations"
    assert r.evaluations_since_improvement >= 200 > r.evaluations_since_improvement - 8
    assert r.generations_since_improvement == r.generations - r.best_generation
    assert (
        run_ga(
            p, GAConfig(population=10, generations=None, stagnation_evaluations=10**6, max_evaluations=500, seed=1)
        ).stop_reason
        == "budget"
    )


def test_highspy_and_ortools_match_linprog():
    for seed in range(5):
        p = random_balanced(7, 9, seed=seed, zeros=False)
        z = solve_lp_detailed(p).cost
        h = solve_lp_highspy(p)
        f = solve_min_cost_flow(p)
        assert h.cost == pytest.approx(z, rel=1e-9) and f.cost == pytest.approx(z, rel=1e-9)
        assert p.is_feasible(h.x) and p.is_feasible(f.x)
        assert h.model_status == "Optimal" and h.solver_s > 0 and h.presolve_s >= 0 and h.build_s > 0
    unbalanced = TransportProblem([10, 5], [8, 4], [[1, 2], [3, 4]])
    assert solve_lp_highspy(unbalanced).cost == pytest.approx(solve_lp(unbalanced)[1])
    with pytest.raises(ValueError, match="integer"):
        solve_min_cost_flow(TransportProblem([1.5, 1], [2.5], [[1], [2]]))


def test_simulated_annealing():
    p = random_balanced(6, 7, seed=3)
    _, z = solve_lp(p)
    cfg = SAConfig(max_evaluations=3000, seed=2, insertion_probability=0.3)
    a, b = run_sa(p, cfg), run_sa(p, cfg, engine="python")
    assert a.cost == b.cost and a.improvements == b.improvements and a.evaluations == b.evaluations == 3000
    assert p.is_feasible(a.x) and a.cost >= z - 1e-9 and a.improvements[-1] == (a.best_evaluation, a.cost)
    cost = run_sa(p, SAConfig(max_evaluations=500, initialization="cost-aware", seed=0))
    assert cost.cost <= vogel(p).cost + 1e-9  # starts from Vogel's plan and keeps the best
    stag = run_sa(p, SAConfig(max_evaluations=10**6, stagnation_evaluations=300, seed=0))
    assert stag.stop_reason == "stagnation_evaluations" and stag.evaluations < 10**6
    tiny = run_sa(TransportProblem([3], [3], [[2]]), SAConfig(max_evaluations=200, pilot_moves=10))
    assert tiny.cost == 6
    seen = []
    run_sa(p, SAConfig(max_evaluations=2000, seed=1), callback=lambda g, e, c: seen.append(e), chunk=500)
    assert seen and seen[-1] == 2000
    assert (
        run_sa(p, SAConfig(max_evaluations=2000, seed=1), callback=lambda *a: True, chunk=500).stop_reason
        == "cancelled"
    )
    for bad in (
        {"max_evaluations": 50},
        {"max_evaluations": 500, "insertion_probability": 2},
        {"max_evaluations": 500, "initial_acceptance": 1},
        {"max_evaluations": 500, "final_ratio": 0},
        {"max_evaluations": 500, "pilot_moves": 0},
        {"max_evaluations": 500, "initialization": "x"},
        {"max_evaluations": 500, "stagnation_evaluations": 0},
    ):
        with pytest.raises(ValueError):
            SAConfig(**bad)
    with pytest.raises(ValueError):
        run_sa(p, cfg, engine="gpu")


@settings(max_examples=150, deadline=None)
@given(m=st.integers(1, 25), n=st.integers(1, 25), seed=st.integers(0, 2**32 - 1), perm_seed=st.integers(0, 2**31))
def test_tolerance_does_not_change_integer_plans(m, n, seed, perm_seed):
    p = random_balanced(m, n, seed)
    perm = np.random.default_rng(perm_seed).permutation(m * n)
    assert np.array_equal(decode_permutation(p, perm, tol=0.0), decode_permutation(p, perm, tol=1e-12))


def test_tolerance_treats_tiny_residuals_as_zero():
    # supply 1 + 1e-15 against demand 1: the residual 1e-15 is noise, not a shipment
    p = TransportProblem([1.0 + 1e-15, 1.0], [1.0, 1.0 + 1e-15], [[1.0, 5.0], [5.0, 1.0]])
    assert decoder_eps(p) == pytest.approx(1e-12 * (1 + 1e-15))
    exact = decode_permutation(p, [0, 1, 2, 3], tol=0.0)
    tolerant = decode_permutation(p, [0, 1, 2, 3], tol=1e-12)
    assert exact[0, 1] > 0 and tolerant[0, 1] == 0
