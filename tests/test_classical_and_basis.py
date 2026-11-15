"""Hand-checked cases for NWC, LCM, VAM, the basis tools, the LP report and the plan check.

No textbook instance with a citable page is stored in the repository, so the small cases below
are worked by hand in the comments; random instances are covered in test_properties.py.
"""

import numpy as np
import pytest

from conftest import SMALL_OPT
from tpga import TransportProblem, decode_permutation
from tpga.basis import is_basic, permutation_from_basis
from tpga.classical import METHODS, least_cost, northwest_corner, vogel
from tpga.decoder import decode_trace
from tpga.exact import solve_lp_detailed
from tpga.verify import check_plan


def test_nwc_by_hand(small):
    # supply (20,30,20), demand (25,25,20): (0,0)=20, (1,0)=5, (1,1)=25, (2,2)=20 -> 160+25+100+120
    r = northwest_corner(small)
    assert np.array_equal(r.x, [[20, 0, 0], [5, 25, 0], [0, 0, 20]])
    assert r.cost == 8 * 20 + 5 * 5 + 4 * 25 + 6 * 20 == 405
    assert [(s["row"], s["col"]) for s in r.steps] == [(0, 0), (1, 0), (1, 1), (2, 2)]


def test_lcm_by_hand(small):
    # cheapest cells: (2,0)=2 -> 20, (0,2)=3 -> 20, (1,1)=4 -> 25, (1,0)=5 -> 5
    r = least_cost(small)
    assert np.array_equal(r.x, [[0, 0, 20], [5, 25, 0], [20, 0, 0]])
    assert r.cost == 2 * 20 + 3 * 20 + 4 * 25 + 5 * 5 == SMALL_OPT


def test_vam_by_hand_records_penalties(small):
    r = vogel(small)
    # first step: row penalties (3,1,4), column penalties (3,2,3): row 2 wins, cheapest cell (2,0)
    first = r.steps[0]
    assert first["row_penalty"] == [3.0, 1.0, 4.0] and first["col_penalty"] == [3.0, 2.0, 3.0]
    assert (first["row"], first["col"], first["quantity"], first["line"]) == (2, 0, 20.0, "row")
    assert r.cost == SMALL_OPT and is_basic(r.x)


def test_degenerate_step_removes_row_and_column():
    p = TransportProblem([5, 5], [5, 5], [[1, 2], [3, 1]])
    r = northwest_corner(p)
    assert np.array_equal(r.x, [[5, 0], [0, 5]]) and len(r.steps) == 2
    assert vogel(p).cost == least_cost(p).cost == 10


def test_methods_balance_unbalanced_problems():
    p = TransportProblem([10, 5], [8, 4], [[1, 2], [3, 4]])
    for method in METHODS.values():
        r = method(p)
        assert r.x.shape == (2, 3) and check_plan(p, r.x).feasible


def test_single_row_and_column_cases():
    row = TransportProblem([9], [2, 3, 4], [[5, 1, 3]])
    col = TransportProblem([2, 3, 4], [9], [[5], [1], [3]])
    for p in (row, col):
        r = vogel(p)
        assert r.steps[0]["line"] == "single" and r.cost == 2 * 5 + 3 * 1 + 4 * 3


def test_basis_tools():
    p = TransportProblem([2, 2], [2, 2], [[1, 1], [1, 1]])
    cycle = np.array([[1.0, 1.0], [1.0, 1.0]])
    assert not is_basic(cycle) and permutation_from_basis(p, cycle) is None
    with pytest.raises(ValueError):
        permutation_from_basis(p, np.zeros((3, 3)))


def test_lp_detailed_reports_status_and_time(small):
    for method in ("highs", "highs-ds"):
        r = solve_lp_detailed(small, method=method)
        assert r.status == 0 and r.cost == pytest.approx(SMALL_OPT) and r.time_s > 0 and r.method == method
    x = np.round(solve_lp_detailed(small, method="highs-ds").x)
    assert np.array_equal(decode_permutation(small, permutation_from_basis(small, x)), x)


def test_check_plan_detects_violations(small):
    good = least_cost(small).x
    assert check_plan(small, good).feasible and check_plan(small, good).cost == SMALL_OPT
    bad = good.copy()
    bad[0, 0] += 1
    assert not check_plan(small, bad).feasible
    neg = good.copy()
    neg[0, 0] -= 1
    neg[0, 1] += 1
    assert check_plan(small, neg).min_value < 0 and not check_plan(small, neg).feasible
    assert not check_plan(small, np.zeros((2, 2))).feasible


def test_decode_trace(small):
    steps = decode_trace(small, np.arange(9))
    assert steps[0] == {
        "position": 0,
        "arc": 0,
        "row": 0,
        "col": 0,
        "quantity": 20.0,
        "supply_left": [0.0, 30.0, 20.0],
        "demand_left": [5.0, 25.0, 20.0],
    }
    assert steps[1]["quantity"] == 0.0  # row 0 is exhausted
    assert steps[-1]["supply_left"] == [0.0, 0.0, 0.0]
