"""Representation analysis (v0.4, non-confirmatory): checked against the decoder and the GA."""

from __future__ import annotations

import numpy as np
import pytest

from helpers import random_balanced
from tpga import GAConfig, decode_permutation, run_ga
from tpga.analysis import representation as rep


@pytest.fixture(scope="module")
def dec() -> rep.Decoder:
    return rep.Decoder(random_balanced(6, 7, 11, zeros=False))


def test_prefix_matches_the_decoded_plan(dec: rep.Decoder) -> None:
    rng = np.random.default_rng(0)
    for _ in range(50):
        perm = rng.permutation(dec.length)
        positive, read = dec.prefix(perm)
        plan = decode_permutation(dec.problem, perm)
        assert positive == int((plan > 0).sum()) == len(dec.positive_cells(perm))
        assert positive <= sum(dec.shape) - 1  # a basic solution
        assert 1 <= read <= dec.length
        # the cells after the prefix do not change the plan: reorder them and decode again
        tail = perm[read:][::-1]
        assert np.array_equal(decode_permutation(dec.problem, np.concatenate([perm[:read], tail])), plan)


def test_costs_match_the_decoder(dec: rep.Decoder) -> None:
    perms = rep.random_parents(dec, 20, np.random.default_rng(1))
    expected = [dec.problem.total_cost(decode_permutation(dec.problem, p)) for p in perms]
    assert dec.costs(perms) == pytest.approx(expected, rel=1e-12)


def test_swap_counts_follow_the_ga_rules() -> None:
    rng = np.random.default_rng(2)
    assert rep.swap_count("swap_count", 3, 10, 10, rng) == 3
    assert rep.swap_count("swap_scaled", 0.1, 10, 10, rng) == 2
    assert rep.swap_count("swap_scaled", 0.001, 10, 10, rng) == 1
    assert {rep.swap_count("swap_fixed", 0.0, 10, 10, rng) for _ in range(20)} == {0}
    assert {rep.swap_count("swap_fixed", 1.0, 10, 10, rng) for _ in range(20)} == {1}
    draws = [rep.swap_count("swap_per_position", 0.1, 10, 10, rng) for _ in range(2000)]
    assert np.mean(draws) == pytest.approx(5.0, abs=0.3)  # E[Binomial(100, 0.1)] / 2
    with pytest.raises(ValueError):
        rep.swap_count("invert", 1, 3, 3, rng)


def test_neutrality_and_locality(dec: rep.Decoder) -> None:
    rng = np.random.default_rng(3)
    parents = rep.random_parents(dec, 200, rng)
    costs = dec.costs(parents)
    none = rep.neutrality(dec, parents, costs, "swap_fixed", 0.0, rng)
    assert none["neutral_share"] == 1.0 and np.isnan(none["neutral_share_mutated"])
    one = rep.neutrality(dec, parents, costs, "swap_count", 1, rng)
    assert 0.0 < one["neutral_share"] < 1.0 and one["mean_swaps"] == 1.0
    rows = rep.locality(dec, parents, costs, float(costs.min()), rng)
    assert [r["k"] for r in rows[:-1]] == list(rep.LOCALITY_K)
    shares = [r["neutral_share"] for r in rows[:-1]]
    assert shares[0] > shares[-1]  # more swaps, fewer neutral offspring
    assert rows[-1]["spearman_k_vs_abs_change"] > 0


def test_heritability_is_a_share(dec: rep.Decoder) -> None:
    rng = np.random.default_rng(4)
    pop = rep.random_parents(dec, 30, rng)
    h = rep.heritability(dec, pop, 40, rng)
    assert 0.0 <= h["inherited_share_min"] <= h["inherited_share"] <= 1.0
    same = np.vstack([pop[0]] * 5)  # identical parents: every positive cell of the child is inherited
    assert rep.heritability(dec, same, 10, rng)["inherited_share"] == 1.0


def test_population_hook_leaves_the_run_unchanged() -> None:
    p = random_balanced(5, 6, 9, zeros=False)
    cfg = GAConfig(population=20, max_evaluations=2_000, seed=7)
    plain = run_ga(p, cfg)
    snaps = rep.Snapshots(2_000, (0.1, 0.5, 1.0))
    hooked = run_ga(p, cfg, population_hook=snaps)
    assert hooked.cost == plain.cost and np.array_equal(hooked.permutation, plain.permutation)
    assert sorted(snaps.kept) == [0.1, 0.5]
    final = snaps.final()
    assert final.shape == (20, 30)
    assert min(rep.Decoder(p).costs(final)) == pytest.approx(plain.cost)  # elitism keeps the best
    assert snaps.last_evaluations == plain.evaluations
