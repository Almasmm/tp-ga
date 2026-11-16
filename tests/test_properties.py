"""Property-based checks of the decoder, the classical methods and the basis construction."""

import numpy as np
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from helpers import random_balanced
from tpga import decode_permutation
from tpga.basis import is_acyclic, is_basic, permutation_from_basis, support
from tpga.classical import least_cost, northwest_corner, vogel
from tpga.exact import solve_lp_detailed
from tpga.initialization import vogel_order
from tpga.verify import check_plan

instances = st.builds(
    random_balanced,
    m=st.integers(1, 50),
    n=st.integers(1, 50),
    seed=st.integers(0, 2**32 - 1),
    zeros=st.booleans(),
)
small_instances = st.builds(
    random_balanced, m=st.integers(1, 12), n=st.integers(1, 12), seed=st.integers(0, 2**32 - 1), zeros=st.booleans()
)
SETTINGS = settings(max_examples=150, deadline=None, suppress_health_check=[HealthCheck.too_slow])


@SETTINGS
@given(p=instances, perm_seed=st.integers(0, 2**32 - 1))
def test_decoded_plan_is_feasible_integral_and_basic(p, perm_seed):
    perm = np.random.default_rng(perm_seed).permutation(p.cost.size)
    x = decode_permutation(p, perm)
    check = check_plan(p, x)
    assert check.feasible
    assert check.max_row_residual == 0 and check.max_col_residual == 0  # exact with integer data
    assert (x >= 0).all() and np.array_equal(x, np.round(x))
    m, n = p.shape
    cells = support(x)
    assert len(cells) <= m + n - 1
    assert is_acyclic(cells, m, n)


@SETTINGS
@given(p=instances)
def test_decoder_reproduces_the_three_classical_rules(p):
    m, n = p.shape
    # arcs in row-major order give the north-west corner rule
    assert np.array_equal(decode_permutation(p, np.arange(m * n)), northwest_corner(p).x)
    # arcs sorted by cost, ties by index, give the least-cost method with the same tie rule
    assert np.array_equal(decode_permutation(p, np.argsort(p.cost.ravel(), kind="stable")), least_cost(p).x)
    # the Vogel order used by the cost-aware start gives Vogel's plan
    assert np.array_equal(decode_permutation(p, vogel_order(p)), vogel(p).x)


@SETTINGS
@given(p=small_instances)
def test_classical_plans_are_feasible_basic_and_not_below_the_optimum(p):
    z = solve_lp_detailed(p).cost
    for method in (northwest_corner, least_cost, vogel):
        r = method(p)
        assert check_plan(p, r.x).feasible
        assert is_basic(r.x)
        assert r.cost >= z - 1e-9 * max(1.0, abs(z))
        assert np.array_equal(decode_permutation(p, _complete(r.order, p.cost.size)), r.x)


@SETTINGS
@given(p=small_instances)
def test_permutation_from_the_optimal_basis_decodes_to_the_optimum(p):
    lp = solve_lp_detailed(p, method="highs-ds")
    x = np.round(lp.x)
    assert np.abs(lp.x - x).max() < 1e-6
    assert is_basic(x)
    perm = permutation_from_basis(p, x)
    assert perm is not None
    decoded = decode_permutation(p, perm)
    assert np.array_equal(decoded, x)
    assert p.total_cost(decoded) == lp.cost or abs(p.total_cost(decoded) - lp.cost) <= 1e-9 * max(1.0, lp.cost)


def _complete(order, size):
    rest = [k for k in range(size) if k not in set(order)]
    return np.asarray(order + rest)
