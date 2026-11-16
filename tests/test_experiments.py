"""End-to-end run of the experiment pipeline on a tiny configuration."""

import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from tpga.experiments import config as config_mod
from tpga.experiments import environment, instances, report, run, worker
from tpga.experiments.config import Budget, Config, GAParams

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def tiny(tmp_path_factory):
    out = tmp_path_factory.mktemp("exp")
    text = (ROOT / "tests" / "data" / "tiny.yaml").read_text(encoding="utf-8")
    text = text.replace("OUTPUT", (out / "out").as_posix()).replace("ROOT", ROOT.as_posix())
    path = out / "tiny.yaml"
    path.write_text(text, encoding="utf-8")
    assert run.main(["--config", str(path)]) == 0
    assert run.main(["--config", str(path), "--pilot"]) == 0
    return Config.load(path)


def test_config_and_budget(tmp_path):
    b = Budget(200, 20000, 2000000)
    assert b.of(5, 5) == 20000 and b.of(50, 50) == 500000 and b.of(200, 200) == 2000000
    assert "," not in b.rule_id
    assert GAParams(100, 0.9, 0.2, 3, 2).config_id(b, None).endswith("Snone")
    bad = tmp_path / "bad.yaml"
    bad.write_text("output: x\n", encoding="utf-8")
    with pytest.raises(ValueError, match="missing"):
        Config.load(bad)
    bad.write_text("- 1\n", encoding="utf-8")
    with pytest.raises(ValueError, match="mapping"):
        Config.load(bad)
    cfg = Config.load(ROOT / "experiments" / "paper.yaml")
    assert cfg.root == ROOT and cfg.output == ROOT / "paper_artifacts"
    with pytest.raises(ValueError, match="unknown phase"):
        cfg.phase("nope")
    assert config_mod.METHOD_CODES[0] == "LP"


def test_pipeline_outputs(tiny):
    out = tiny.output
    runs = pd.read_csv(out / "raw" / "runs.csv")
    assert set(runs["method"]) == {"LP", "NWC", "LCM", "VAM", "RS", "GA-rand", "GA-cost"}
    assert runs["feasible"].all() and (runs["gap"].dropna() >= -1e-9).all()
    keys = runs[["instance", "method", "config", "seed"]].fillna("").astype(str).agg("|".join, axis=1)
    assert keys.is_unique  # the resume logic never duplicates a run
    assert runs["cpu"].notna().all()
    manifest = json.loads((out / "instances" / "manifest.json").read_text(encoding="utf-8"))
    for e in manifest["instances"]:
        assert instances.sha256(out / "instances" / e["file"]) == e["sha256"]
    reach = json.loads((out / "reachability.json").read_text(encoding="utf-8"))
    assert reach["reproduced"] == reach["instances"] == 20
    assert (out / "raw" / "timing.csv").exists() and (out / "pilot" / "estimate.json").exists()
    # a second call resumes and has nothing left to do
    assert run.main(["--config", str(tiny.path), "--phase", "main"]) == 0
    assert len(pd.read_csv(out / "raw" / "runs.csv")) == len(runs)


def test_report(tiny):
    summary = report.generate(tiny)
    out = tiny.output
    # every factorial cell holds instances x runs rows; the stopping-rule runs (no stagnation) stay out
    t4 = pd.read_csv(out / "tables" / "T4_factorial.csv")
    assert set(t4["runs"]) == {2 * tiny.runs}
    for name in ("T1_instances", "T2_gap", "T3_time", "T4_factorial", "T5_tests", "T6_applied"):
        assert (out / "tables" / f"{name}.csv").exists() and (out / "tables" / f"{name}.md").exists()
    for lang in ("en", "ru"):
        for fig in ("F1_decoder", "F2_convergence", "F3_gap_boxplot", "F4_time_scaling", "F5_factorial_heatmap"):
            assert (out / "figures" / lang / f"{fig}.png").exists() and (out / "figures" / lang / f"{fig}.pdf").exists()
    for doc in ("NUMBERS.md", "METHODS.md", "LIMITATIONS.md", "README.md"):
        assert (out / doc).read_text(encoding="utf-8").startswith("#")
    assert summary["rows"] > 0
    assert report.main(["--config", str(tiny.path)]) == 0


def test_worker_tasks_in_process(tiny):
    """The pool runs tasks in subprocesses; run each kind here as well so the checks are exercised."""
    inst = [i for i in instances.build(tiny) if i.suite == "uniform"][0]
    base = run._base(tiny, "t", inst, "LP", "highs")
    row, _ = worker.execute(base)
    assert row["optimal"] and row["lp_status"] == 0
    z = row["cost"]
    for code in ("NWC", "LCM", "VAM"):
        r, _ = worker.execute({**run._base(tiny, "t", inst, code, "-"), "z_star": z})
        assert r["cost"] >= z and r["feasible"]
    tasks = run.stochastic_tasks(tiny, "t", [inst], ["RS", "GA-rand", "GA-cost"], [tiny.ga_base], [1], True)
    for t in tasks:
        r, curve = worker.execute({**t, "z_star": z})
        assert r["evals"] <= t["budget"] and curve and curve[-1]["evals"] == r["evals"]
    with pytest.raises(RuntimeError, match="below the LP optimum"):
        worker.execute({**tasks[0], "z_star": z + 1e6})


def test_helpers():
    assert worker.gap(110.0, 100.0) == pytest.approx(10.0) and worker.gap(1.0, 0.0) is None
    assert worker.is_optimal(100.0 + 1e-8, 100.0, 1e-9) and not worker.is_optimal(100.0 + 1e-6, 100.0, 1e-9)
    from tpga import TransportProblem

    p = TransportProblem([10, 5], [8, 4], [[1, 2], [3, 4]])
    assert worker.dummy_volume(p, np.array([[8, 0, 2], [0, 4, 1]])) == 3
    q = TransportProblem([8, 4], [10, 5], [[1, 2], [3, 4]])
    assert worker.dummy_volume(q, np.array([[8, 0], [2, 4], [0, 1]])) == 1
    assert report.holm([0.01, 0.04, 0.03]) == pytest.approx([0.03, 0.06, 0.06])
    t = report.paired_test(np.array([1.0, 2.0, 3.0]), np.array([1.0, 2.0, 3.0]))
    assert t["p"] == 1.0 and t["nonzero_differences"] == 0
    fit = report.loglog_fit(np.array([10.0, 100.0, 1000.0]), np.array([1.0, 100.0, 10000.0]))
    assert fit["b"] == pytest.approx(2.0)
    assert report._fmt(None) == "–" and report._fmt(3) == "3" and report._fmt(1e-6).endswith("e-06")


def test_environment_description():
    info = environment.describe(ROOT)
    assert info["python"] and info["packages"]["numpy"]
    assert environment.single_thread_environment() is None
