"""v0.4 code with default parameters reproduces the published v0.3.0 runs.

One uniform instance per size of experiments/paper.yaml, three seeds, GA-rand, GA-cost and RS with the base
configuration; cost, decoder calls, decoder call of the best plan and stop reason must equal the rows of
paper_artifacts/raw/runs.csv. Sizes 50x50 and 100x100 take minutes and carry the "slow" marker.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from helpers import random_balanced
from tpga.experiments import run, worker
from tpga.experiments.config import Config
from tpga.experiments.instances import Instance
from tpga.initialization import vogel_order

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "paper_artifacts" / "raw" / "runs.csv"
SIZES = [(5, 5), (10, 10), (20, 20), (30, 30), (50, 50), (100, 100)]
SLOW = {(50, 50), (100, 100)}


def _vogel_order_v030(problem):
    """Vogel order exactly as implemented in v0.3.0 (reference for L5)."""
    m, n = problem.shape
    supply, demand = problem.supply.copy(), problem.demand.copy()
    first = []
    while (supply > 0).any() and (demand > 0).any():
        rows, cols = np.flatnonzero(supply > 0), np.flatnonzero(demand > 0)
        cost = problem.cost[np.ix_(rows, cols)]
        if min(cost.shape) == 1:
            i, j = map(int, np.unravel_index(np.argmin(cost), cost.shape))
        else:
            two_r = np.partition(cost, 1, axis=1)[:, :2]
            two_c = np.partition(cost, 1, axis=0)[:2, :]
            rp, cp = two_r[:, 1] - two_r[:, 0], two_c[1] - two_c[0]
            i, j = int(np.argmax(rp)), int(np.argmax(cp))
            if rp[i] >= cp[j]:
                j = int(np.argmin(cost[i]))
            else:
                i = int(np.argmin(cost[:, j]))
        i, j = int(rows[i]), int(cols[j])
        q = min(supply[i], demand[j])
        supply[i] -= q
        demand[j] -= q
        first.append(i * n + j)
    remaining = np.ones(m * n, dtype=bool)
    remaining[first] = False
    return np.concatenate((np.asarray(first, dtype=np.int64), np.flatnonzero(remaining)))


@settings(max_examples=200, deadline=None)
@given(m=st.integers(1, 30), n=st.integers(1, 30), seed=st.integers(0, 2**32 - 1), zeros=st.booleans())
def test_vogel_order_equals_v030_implementation(m, n, seed, zeros):
    p = random_balanced(m, n, seed, zeros=zeros)
    assert np.array_equal(vogel_order(p), _vogel_order_v030(p))


@pytest.fixture(scope="module")
def reference():
    if not RUNS.exists():  # pragma: no cover - the artifacts are part of the repository
        pytest.skip("paper_artifacts/raw/runs.csv not present")
    return pd.read_csv(RUNS)


def _cases():
    for m, n in SIZES:
        marks = [pytest.mark.slow] if (m, n) in SLOW else []
        for method in ("GA-rand", "GA-cost", "RS"):
            yield pytest.param(m, n, method, marks=marks, id=f"{m}x{n}-{method}")


@pytest.mark.parametrize(("m", "n", "method"), list(_cases()))
def test_reproduces_v030_runs(reference, m, n, method):
    cfg = Config.load(ROOT / "experiments" / "paper.yaml")
    iid = f"u{m}x{n}-00"
    inst = Instance(
        iid, "uniform", m, n, ROOT / "paper_artifacts" / "instances" / "uniform" / f"{iid}.json", None, True
    )
    tasks = run.stochastic_tasks(cfg, "main", [inst], [method], [cfg.ga_base], cfg.seeds(3), curve=False)
    z = float(reference[(reference.instance == iid) & (reference.method == "LP")].cost.iloc[0])
    for task in tasks:
        row, _ = worker.execute({**task, "z_star": z})
        ref = reference[
            (reference.instance == iid)
            & (reference.method == method)
            & (reference.config == task["config"])
            & (reference.seed == task["seed"])
        ]
        assert len(ref) == 1, (iid, method, task["seed"])
        ref = ref.iloc[0]
        assert row["cost"] == ref["cost"]
        assert row["evals"] == ref["evals"]
        assert row["best_eval"] == ref["best_eval"]
        assert row["stop_reason"] == ref["stop_reason"]
