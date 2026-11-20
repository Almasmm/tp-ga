"""Regression checks for the second-review controls."""

import json

import numpy as np
import pytest

from tpga.cycle import GAXConfig, run_ga_x
from tpga.experiments.v3 import review2_fctp, review2_report
from tpga.experiments.v3.review2_linear import observe_ox, observe_swaps
from tpga.fctp import generate
from tpga.model import TransportProblem


@pytest.mark.parametrize(
    ("kind", "population", "rate"),
    [("independent", 1, 0.0), ("independent", 3, 0.0), ("population", 3, 0.0), ("population", 3, 1.0)],
)
def test_matched_fctp_evaluation_count_and_feasibility(tmp_path, kind, population, rate):
    path = tmp_path / "fctp.json"
    path.write_text(json.dumps(generate(4, 4, 17, 0.2)), encoding="utf-8")
    row = review2_fctp.run(
        {
            "path": path,
            "method": "control",
            "budget": 113,
            "kind": kind,
            "seed": 12,
            "population": population,
            "ox_rate": rate,
            "decoder_tol": 1e-12,
        }
    )
    assert row["evals"] == 113
    assert row["pivots"] == 113 - population
    assert row["cost"] <= row["start_cost"]
    assert row["crossovers"] == (113 - population if rate else 0)


def test_ox_diagnostics_do_not_change_the_run():
    p = TransportProblem([2, 3], [1, 4], [[4, 1], [3, 2]])
    cfg = GAXConfig(4, 1.0, 2, 1, 26, mutation_mode="swap_count", seed=7)
    counts = np.zeros((10, 5), dtype=np.int64)
    seen = []

    def ox(used, pop, fit, uniforms):
        observe_ox(pop, fit, uniforms, 2, 1.0, p.supply, p.demand, 1e-12, used, 26, counts)

    def population(used, pop, final):
        draws = np.random.default_rng(1).random((2, 64, 2))
        counters = observe_swaps(pop, draws, p.supply, p.demand, 1e-12)
        assert (counters[1::2] <= counters[::2]).all()
        seen.append((used, final))

    baseline = run_ga_x(p, cfg)
    instrumented = run_ga_x(p, cfg, generation_hook=ox, population_hook=population)
    assert baseline.cost == instrumented.cost
    assert baseline.evaluations == instrumented.evaluations == 25
    assert seen[0] == (4, False)
    assert seen[-1] == (25, True)
    assert counts[:, 0].sum() == 21
    assert np.all(counts[:, 3] + counts[:, 4] <= counts[:, 0])
    assert run_ga_x(p, cfg, fill_budget=True).evaluations == 26
    assert run_ga_x(p, cfg, reencode="only").evaluations == 25
    assert run_ga_x(p, cfg, reencode="after_swap").evaluations == 25


def test_analysis_uses_matched_seeds_and_preserves_zeroes(tmp_path, monkeypatch):
    rows = [
        {"instance": "i", "seed": 1, "method": "a", "gap": 0.0},
        {"instance": "i", "seed": 2, "method": "a", "gap": 100.0},
        {"instance": "i", "seed": 1, "method": "b", "gap": 2.0},
    ]
    (result,) = review2_report.pairing(rows, [("a", "b")], (), "gap", 1)
    assert (result["wins_x"], result["ties"], result["wins_y"]) == (1, 0, 0)
    assert result["first_median"] == 0.0
    monkeypatch.setattr(review2_report, "ROOT", tmp_path)
    review2_report.table("paired", [result])
    (loaded,) = review2_report.read_csv(tmp_path / "tables/paired.csv")
    assert loaded["first_median"] == "0.0"
    assert loaded["hl_ci_low"] == ""
    assert (tmp_path / "tables/paired.md").is_file()


def test_published_controls_can_rebuild_tables(tmp_path, monkeypatch):
    import shutil
    from pathlib import Path

    source = Path("paper_artifacts_v3/review2")
    if not (source / "raw/K3.jsonl").is_file():
        pytest.skip("requires the published amendment 11 raw records")
    shutil.copytree(source / "raw", tmp_path / "raw")
    shutil.copyfile(source / "session.json", tmp_path / "session.json")
    monkeypatch.setattr(review2_report, "ROOT", tmp_path)
    refs = review2_report.fctp_report()
    _, linear = review2_report.linear_report()
    ox = review2_report.diagnostics()
    review2_report.provenance()
    review2_report.mip_report(refs)
    review2_report.figures(ox, linear)
    assert len(refs) == 60
    assert len(linear) == 56
    pooled = review2_report.read_csv(tmp_path / "tables/K1_pairs_pooled.csv")
    assert len(pooled) == 10 and {r["instances_used"] for r in pooled} == {"40"}
    (pivots,) = review2_report.read_csv(tmp_path / "tables/K11_summary.csv")
    assert pivots["runs"] == pivots["zero_pivot_runs"] == "100"
    assert pivots["total_pivots"] == "0"
    assert (tmp_path / "figures/K3_ox_novelty.pdf").stat().st_size > 1000
    assert (tmp_path / "figures/K6_linear_medians.jpg").stat().st_size > 1000


def test_compiled_and_reference_diagnostics_agree():
    from tpga.experiments.v3 import review2_linear

    supply, demand = np.array([2.0, 3.0]), np.array([1.0, 4.0])
    chromosomes = np.array([[0, 1, 2, 3], [3, 2, 1, 0], [2, 1, 0, 3]], dtype=np.int64)
    fit = np.array([3.0, 2.0, 1.0])
    draws = np.random.default_rng(5).random((12, 10))
    a, b = np.zeros((10, 5), dtype=np.int64), np.zeros((10, 5), dtype=np.int64)
    args = (chromosomes, fit, draws, 2, 0.9, supply, demand, 1e-12, 3, 30)
    review2_linear.observe_ox(*args, a)
    review2_linear.observe_ox.py_func(*args, b)
    assert np.array_equal(a, b)
    swaps = np.random.default_rng(6).random((3, 64, 2))
    args = (chromosomes, swaps, supply, demand, 1e-12)
    assert np.array_equal(review2_linear.observe_swaps(*args), review2_linear.observe_swaps.py_func(*args))


def test_linear_controls_replay_the_archived_configuration():
    from tpga.experiments.v3 import rev, review2, review2_linear

    lin = rev.lin_cfg(review2.REVIEW)
    controls = list(review2_linear.tasks(lin, "K2"))
    traces = list(review2_linear.tasks(lin, "K3"))
    assert len(controls) == 1200 and len(traces) == 108
    assert {item["reencode"] for item in controls} == {"only", "after_swap"}
    record = review2_linear.run(controls[0])
    assert record["evals"] <= controls[0]["budget"]
    assert record["cost"] <= record["start_cost"]
    # A shortened diagnostic tests seed controls without rerunning the published large instance.
    candidate = {**traces[0], "budget": 2 * traces[0]["params"]["population"]}
    baseline = review2_linear.run({**candidate, "phase": "test"})
    audited = review2_linear.run({**candidate, "archived_cost": baseline["cost"], "archived_evals": baseline["evals"]})
    assert audited["cost"] == baseline["cost"]
    assert len(audited["snapshots"]) == 3


def test_runner_checkpoints_completed_tasks_and_errors(tmp_path, monkeypatch):
    import time
    from concurrent.futures import Future

    from tpga.experiments.v3 import review2

    class LocalExecutor:
        def __init__(self, max_workers):
            assert max_workers == 2

        def submit(self, function, item):
            future = Future()
            try:
                future.set_result(function(item))
            except RuntimeError as error:
                future.set_exception(error)
            return future

        def shutdown(self):
            return None

    monkeypatch.setattr(review2, "ROOT", tmp_path)
    monkeypatch.setattr(review2, "ProcessPoolExecutor", LocalExecutor)
    deadline = review2.session_deadline()
    assert review2.session_deadline() == deadline
    base = {"instance": "A", "seed": 1, "method": "x"}
    other = {**base, "method": "y"}

    def run(task):
        if task == other:
            raise RuntimeError("deliberate failure")
        return {**task, "cost": 2.0}

    monkeypatch.setattr(review2, "execute", run)
    review2.run_block("test", [base, other], deadline, 2)
    review2.run_block("test", [base, other], time.time() - 1, 2)
    saved = review2.records(tmp_path / "raw/test.jsonl")
    assert len(saved) == 1 and saved[0]["cost"] == 2
    assert len(review2.records(tmp_path / "errors.jsonl")) == 1
