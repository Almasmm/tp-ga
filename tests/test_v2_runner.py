"""v0.4 runner: full pipeline on a tiny configuration, interruption and resume, monitor, storage, estimate."""

import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest

from tpga.experiments.v2 import doctor, instances, methods, monitor, pilot, storage, tasks
from tpga.experiments.v2.config import ConfigV2
from tpga.experiments.v2.storage import read_parts

ROOT = Path(__file__).resolve().parents[1]


def make_config(tmp: Path, budget_cap: int = 2000, runs: int = 2) -> Path:
    text = (ROOT / "tests" / "data" / "tiny-v2.yaml").read_text(encoding="utf-8")
    text = text.replace("OUTPUT", (tmp / "out").as_posix()).replace("ROOT", ROOT.as_posix())
    text = text.replace("TUNED", (tmp / "tuned.yaml").as_posix())
    text = text.replace("budget: {factor: 40, cap: 2000}", f"budget: {{factor: 100000, cap: {budget_cap}}}")
    text = text.replace("runs: 2\n", f"runs: {runs}\n", 1)
    path = tmp / "cfg.yaml"
    path.write_text(text, encoding="utf-8")
    return path


def cli(*args: str, **kw):  # type: ignore[no-untyped-def]
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    return subprocess.run(
        [sys.executable, "-m", "tpga.experiments.v2.cli", *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
        timeout=600,
        **kw,
    )


@pytest.fixture(scope="module")
def tuned_cfg(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("v2")
    path = make_config(tmp)
    assert cli("tune", "--config", str(path)).returncode == 0
    return tmp, path


def test_full_pipeline(tuned_cfg):
    tmp, path = tuned_cfg
    res = cli("run", "--config", str(path), "--plain")
    assert res.returncode == 0, res.stdout + res.stderr
    cfg = ConfigV2.load(path)
    records = list(read_parts(cfg.output / "raw" / "runs", "runs"))
    keys = [methods.key_of(r) for r in records]
    # 21: representation (5 random-parent tasks, 16 GA runs); 40: wheat (20 reference, 5 x 2 methods x 2 runs)
    assert len(keys) == len(set(keys)) == 208 + 21 + 40
    applied = [r for r in records if r["phase"] == "applied"]
    assert len(applied) == 20 and {r["set"] for r in applied} == {"wheat"}
    assert all(r["z_star"] > 0 for r in applied)
    assert all(r["feasible"] for r in records if r["phase"] != "representation")
    rep_rows = list(read_parts(cfg.output / "raw" / "representation", "representation"))
    measures = {(r["source"], r["measure"]) for r in rep_rows}
    assert {
        ("random", "prefix"),
        ("random", "neutrality"),
        ("random", "locality"),
        ("GA-rand-tuned", "prefix"),
        ("GA-cost-tuned", "heritability"),
    } <= measures
    rep_records = [r for r in records if r["phase"] == "representation"]
    assert sum(r["rows"] for r in rep_records) == len(rep_rows)
    shares = [r["value"] for r in rep_rows if r["metric"] == "neutral_share"]
    assert shares and all(0.0 <= v <= 1.0 for v in shares)
    assert all(r["gap_norm"] is not None for r in records if r["phase"] == "main")
    main = [r for r in records if r["phase"] == "main"]
    assert {r["method"] for r in main} == set(cfg.raw["stochastic_methods"])
    timing = [r for r in records if r["phase"] == "timing" and r["method"] == "LP"]
    assert all(r["solver"] == "highspy" and r["presolve_s"] is not None for r in timing)
    manifest = json.loads((cfg.output / "run_manifest.json").read_text(encoding="utf-8"))
    assert manifest["invocations"][0]["config"]["sha256"] == cfg.sha256
    assert set(manifest["phases"]) == {
        "reference",
        "main",
        "stagnation",
        "legacy",
        "factorial",
        "applied",
        "representation",
        "timing",
    }
    state = json.loads((cfg.output / "state" / "monitor.json").read_text(encoding="utf-8"))
    assert "workers" in state and "system" in state
    assert (cfg.output / "logs").glob("run-*.jsonl")
    # a second call has nothing left to do
    again = cli("run", "--config", str(path), "--plain")
    assert again.returncode == 0 and "осталось в запрошенных фазах: 0" in again.stdout


@pytest.mark.slow
@pytest.mark.skipif(sys.platform != "win32", reason="console control events are Windows-specific")
@pytest.mark.parametrize("signals", [1, 2])
def test_interrupt_and_resume(tmp_path, signals):
    path = make_config(tmp_path, budget_cap=60_000, runs=3)
    assert cli("tune", "--config", str(path)).returncode == 0
    cfg = ConfigV2.load(path)
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    proc = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "tpga.experiments.v2.cli",
            "run",
            "--config",
            str(path),
            "--plain",
            "--phase",
            "reference",
            "--phase",
            "main",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        env=env,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,  # type: ignore[attr-defined]
    )
    runs_dir = cfg.output / "raw" / "runs"
    deadline = time.time() + 180
    while time.time() < deadline:
        if any(r["phase"] == "main" for r in read_parts(runs_dir, "runs")):
            break
        time.sleep(0.2)
    for _ in range(signals):
        proc.send_signal(signal.CTRL_BREAK_EVENT)  # type: ignore[attr-defined]
        time.sleep(0.3)
    out, _ = proc.communicate(timeout=300)
    assert proc.returncode == 130, out
    assert "прерван" in out
    assert not list(runs_dir.glob("*.tmp"))
    partial = list(read_parts(runs_dir, "runs"))
    items = instances.build(cfg)
    expected = sum(len(tasks.phase_tasks(cfg, ph, items)) for ph in ("reference", "main"))
    # LP and classical on 7 synthetic instances, LP and classical on 5 wheat scenarios (amendment 4),
    # 7 instances x 3 seeds x 7 stochastic methods
    assert expected == 7 + 21 + 5 * 4 + 7 * 3 * 7
    assert 0 < len(partial) < expected
    res = cli("run", "--config", str(path), "--plain", "--phase", "reference", "--phase", "main")
    assert res.returncode == 0, res.stdout
    records = list(read_parts(runs_dir, "runs"))
    keys = [methods.key_of(r) for r in records]
    assert len(keys) == len(set(keys)) == expected


def test_storage_parts_are_atomic(tmp_path):
    w = storage.PartWriter(tmp_path, "runs", max_records=2)
    w.add([{"a": 1}])
    assert not list(tmp_path.glob("runs-*.jsonl"))  # still buffered
    w.add([{"a": 2}])
    assert len(list(tmp_path.glob("runs-*.jsonl"))) == 1
    (tmp_path / "runs-x.jsonl.tmp").write_text('{"half":', encoding="utf-8")
    assert [r["a"] for r in read_parts(tmp_path, "runs")] == [1, 2]
    assert storage.clean_temporary(tmp_path) == 1
    log = tmp_path / "log.jsonl"
    storage.append_jsonl(log, {"x": 1})
    with log.open("a", encoding="utf-8") as fh:
        fh.write('{"torn"')
    assert storage.read_jsonl(log) == [{"x": 1}]
    try:
        raise ValueError("boom")
    except ValueError as exc:
        err = storage.error_record({"phase": "p", "method": "m"}, exc)
    assert "boom" in err["traceback"]


def test_instances_and_tasks(tmp_path):
    cfg = ConfigV2.load(make_config(tmp_path))
    items = instances.build(cfg)
    assert len({i.id for i in items}) == len(items) == 8 + 5  # 5 wheat scenarios (applied)
    train = instances.build(cfg, split="train", sets=["uniform"], per_size=1)
    assert not {i.seed for i in items} & {i.seed for i in train}
    for i in items:
        p = methods.load(str(i.path))
        if i.set == "wheat":  # applied data as published: a stress scenario has a market with zero demand
            continue
        assert p.is_balanced and (p.supply > 0).all() and (p.demand > 0).all()
        if i.set == "ties":
            assert p.cost.max() <= 5
    manifest = json.loads((cfg.output / "instances" / "manifest.json").read_text(encoding="utf-8"))
    for e in manifest["instances"].values():
        assert instances._sha(cfg.output / "instances" / e["file"]) == e["sha256"]
        assert (e["z_rand"] is None) == (e["set"] == "lp_scaling")
    with pytest.raises(RuntimeError, match="tpga-exp tune"):
        tasks.phase_tasks(cfg, "main", items)
    with pytest.raises(ValueError):
        tasks.stop_spec({"unknown": 1}, 100)
    assert tasks.stop_spec({"stagnation_evaluations_fraction": 0.1}, 1000) == (
        {"stagnation_evaluations": 100},
        "stagE0.1",
    )
    fac = tasks.factorial_tasks(cfg, items)
    assert len({methods.key_of(t) for t in fac}) == len(fac) == 2 * 2 * 4 * 2 * 2  # pop x modes x init x inst? see cfg
    assert methods.gap_norm(15, 10, 20) == pytest.approx(0.5) and methods.gap_norm(1, 1, None) is None


def test_monitor_renders_and_writes_state(tmp_path):
    m = monitor.Monitor(tmp_path, plain=True, state_interval_s=0)
    m.total = 3
    m.start_phase("main", 3, 0)
    m.status(
        {
            "type": "start",
            "pid": 1,
            "cpu": 0,
            "method": "GA",
            "set": "uniform",
            "size": "5x5",
            "instance": "u5x5-00",
            "seed": 1,
            "budget": 100,
            "time": time.time(),
        }
    )
    m.status({"type": "progress", "pid": 1, "evals": 50, "best_gap": 3.0})
    m.finished(
        {
            "phase": "main",
            "method": "GA",
            "instance": "u5x5-00",
            "seed": 1,
            "gap": 1.0,
            "gap_norm": 0.1,
            "stop_reason": "budget",
            "time_s": 0.5,
        }
    )
    m.status({"type": "done", "pid": 1})
    m.error()
    m.tick()
    snap = json.loads((tmp_path / "state" / "monitor.json").read_text(encoding="utf-8"))
    assert snap["methods"]["GA"]["runs"] == 1 and snap["counts"]["errors"] == 1
    m.workers[2] = {
        "cpu": 1,
        "method": "SA",
        "set": "u",
        "size": "5x5",
        "instance": "x",
        "seed": 2,
        "budget": 9,
        "evals": 1,
        "best_gap": None,
        "started": time.time(),
    }
    m.message = "stop"
    assert m.render() is not None
    assert monitor._dur(None) == "-" and monitor._f(None) == "-"
    assert isinstance(monitor.cpu_temperature(), str)


def test_pilot_estimate_and_reductions(tmp_path, tuned_cfg):
    _, path = tuned_cfg
    cfg = ConfigV2.load(path)
    items = instances.build(cfg)
    per_eval = {}
    for i in items:
        for mname in [*cfg.raw["stochastic_methods"], "GA-P20", "GA-P400"]:
            per_eval[(i.set, i.size, mname)] = 1e-3 if mname != "GA-P20" else 2e-3
    det = {(i.set, i.size, mname): 0.01 for i in items for mname in ("LP", "LP-ortools", "NWC", "LCM", "VAM")}
    est = pilot.estimate_plan(cfg, items, per_eval, det, ratio=1.5, p_cores=8, workers=24)
    assert set(est["phases"]) == set(pilot.PHASES)
    assert est["total_wall_h"] > 0 and abs(sum(p["share"] for p in est["phases"].values()) - 1) < 1e-9
    applied = est["phases"]["applied"]
    assert set(applied["by_set"]) == {"wheat"} and applied["by_set"]["wheat"]["runs"] == applied["runs"]
    assert abs(sum(s["wall_h"] for s in applied["by_set"].values()) - applied["wall_h"]) < 1e-12
    red = pilot.reductions(cfg, items, per_eval, det, capacity=18.0, p_cores=8)
    assert red and all("saves_h" in r for r in red)
    md = pilot.markdown(
        {
            **est,
            "reductions": red,
            "measured": {
                "e_over_p_speed_ratio": 1.5,
                "monitor_overhead": {"overhead_percent": 0.1, "without_s": 1.0, "with_reporting_s": 1.001},
            },
        }
    )
    assert "| total" in md.replace("**", "") and "Possible reductions" in md
    assert "applied: wheat |" in md


def test_doctor_reads_only(tmp_path):
    cfg = ConfigV2.load(make_config(tmp_path))
    checks = doctor.run(cfg, expected_bytes=1e6)
    names = {c.name for c in checks}
    assert {"Свободная ОЗУ", "Ядра Numba"} <= names
    assert names & {"Питание от сети", "Питание"}  # without a battery (CI, desktop) the check is "Питание"
    assert all(c.line().startswith(("OK", "ВНИМАНИЕ")) for c in checks)


def test_pilot_and_doctor_commands(tuned_cfg, capsys):
    from tpga.experiments.v2 import cli as v2cli

    _, path = tuned_cfg
    assert v2cli.main(["pilot", "--config", str(path)]) == 0
    out = capsys.readouterr().out
    assert "Pilot estimate" in out and "Monitor overhead" in out
    cfg = ConfigV2.load(path)
    est = json.loads((cfg.output / "pilot" / "estimate.json").read_text(encoding="utf-8"))
    assert est["measured"]["e_over_p_speed_ratio"] > 0 and est["total_wall_h"] > 0
    assert v2cli.main(["doctor", "--config", str(path)]) == 0
    assert "doctor ничего не меняет" in capsys.readouterr().out


def test_cli_output_is_utf8_when_redirected(tmp_path) -> None:
    """``tpga-exp ... > file`` must not fail on non-ASCII output (Windows code pages)."""
    import subprocess
    import sys

    env = {**__import__("os").environ, "PYTHONIOENCODING": "cp1251"}
    code = "from tpga.experiments.v2 import cli; cli._utf8_output(); print('50×50 → ok')"
    out = subprocess.run([sys.executable, "-c", code], capture_output=True, env=env, check=True).stdout
    assert out.decode("utf-8").strip() == "50×50 → ok"


def test_two_writers_in_the_same_second_keep_both_parts(tmp_path) -> None:
    """Regression: the LP and classical writers of the reference phase used the same part name."""
    from tpga.experiments.v2.storage import PartWriter

    a, b = PartWriter(tmp_path, "runs"), PartWriter(tmp_path, "runs")
    a.add([{"k": 1}])
    a.flush()
    b.add([{"k": 2}])
    b.flush()
    assert sorted(r["k"] for r in read_parts(tmp_path, "runs")) == [1, 2]


def test_runs_by_size_uses_the_first_seeds(tuned_cfg) -> None:
    """Option A of the budget decision: fewer runs at one size, the same first seeds (common random numbers)."""
    import copy

    from tpga.experiments.v2.instances import build

    _, path = tuned_cfg
    cfg = ConfigV2.load(path)
    items = build(cfg)
    full = tasks.phase_tasks(cfg, "main", items)
    raw = copy.deepcopy(cfg.raw)
    raw["runs"] = 3
    raw["phases"]["main"]["runs_by_size"] = {"4x5": 1}
    fewer = tasks.phase_tasks(ConfigV2(raw, cfg.path), "main", items)
    seeds = {t["seed"] for t in fewer if t["size"] == "4x5"}
    assert seeds == {cfg.seeds(1)[0]}
    other = [t for t in fewer if t["size"] != "4x5"]
    assert {t["seed"] for t in other} == set(cfg.seeds(3))
    assert {t["seed"] for t in full if t["size"] == "4x5"} == set(cfg.seeds())


def test_reestimate_matches_the_pilot_on_the_same_measurements(tuned_cfg) -> None:
    _, path = tuned_cfg
    cfg = ConfigV2.load(path)
    if not (cfg.output / "pilot" / "estimate.json").exists():
        assert cli("pilot", "--config", str(path)).returncode == 0
    saved = json.loads((cfg.output / "pilot" / "estimate.json").read_text(encoding="utf-8"))
    again = pilot.reestimate(cfg)
    assert again["total_wall_h"] == pytest.approx(saved["total_wall_h"])
    assert {k: v["runs"] for k, v in again["phases"].items()} == {k: v["runs"] for k, v in saved["phases"].items()}


def test_tuning_record_has_space_overlap_check_and_bounds(tuned_cfg) -> None:
    import yaml

    tmp, _ = tuned_cfg
    frozen = yaml.safe_load((tmp / "tuned.yaml").read_text(encoding="utf-8"))
    assert frozen["training_overlap_with_test"] == 0
    assert sorted(frozen["training_instances"]) == ["u3x3-00-train", "u3x3-01-train", "u4x5-00-train"]
    assert frozen["space"]["sa"]["initial_acceptance"] == {"range": [0.001, 0.95], "log": True}
    assert set(frozen["near_bounds"]) == {"GA-rand", "GA-cost", "SA-rand", "SA-cost"}
    assert 0.001 <= frozen["parameters"]["SA-rand"]["initial_acceptance"] <= 0.95


def test_near_bounds_on_the_sampled_scale() -> None:
    from tpga.experiments.v2 import tune

    space = {
        "sa": {
            "insertion_probability": [0.0, 1.0],
            "initial_acceptance": {"range": [0.001, 0.95], "log": True},
            "final_ratio": [1e-5, 1e-1],
        }
    }
    # log width of [0.001, 0.95] is 6.86, 5 % of it 0.34; log(0.0012 / 0.001) = 0.18 is near the bound
    hits = tune.near_bounds(
        "sa", {"insertion_probability": 0.98, "initial_acceptance": 0.0012, "final_ratio": 1e-3}, space
    )
    assert {(h["parameter"], h["side"]) for h in hits} == {
        ("insertion_probability", "upper"),
        ("initial_acceptance", "lower"),
    }
    # on a linear scale 0.03 would be "near" 0.001; on the log scale it is far from both bounds
    assert (
        tune.near_bounds("sa", {"insertion_probability": 0.5, "initial_acceptance": 0.03, "final_ratio": 1e-3}, space)
        == []
    )
    g = {
        "ga": {
            "population": [20, 400],
            "crossover_rate": [0.5, 1.0],
            "tournament": [2, 7],
            "elite": [1, 5],
            "swap_count": [1, 20],
        }
    }
    params = {
        "population": 100,
        "crossover_rate": 0.99,
        "tournament": 7,
        "elite": 3,
        "mutation_mode": "swap_count",
        "mutation_strength": 1,
    }
    found = {(h["parameter"], h["side"]) for h in tune.near_bounds("ga", params, g)}
    assert found == {("crossover_rate", "upper"), ("tournament", "upper"), ("swap_count", "lower")}
    assert tune.bounds([0.1, 0.9], False) == (0.1, 0.9, False)
    assert tune.per_size_counts({"20x20": 4}) == {"20x20": 4} and tune.per_size_counts(3) == 3


def test_report_after_the_tiny_run_includes_representation(tuned_cfg) -> None:
    """End to end: run (all phases) then report; the representation table and figure are produced."""
    _, path = tuned_cfg
    cfg = ConfigV2.load(path)
    if not (cfg.output / "run_manifest.json").exists():
        assert cli("run", "--config", str(path), "--plain").returncode == 0
    res = cli("report", "--config", str(path))
    assert res.returncode == 0, res.stdout + res.stderr
    table = (cfg.output / "tables" / "representation.csv").read_text(encoding="utf-8")
    assert "neutral_share" in table and "inherited_share" in table and "prefix_share" in table
    assert (cfg.output / "figures" / "en" / "representation_neutrality.pdf").exists()
    summary = json.loads((cfg.output / "report.json").read_text(encoding="utf-8"))
    assert summary["tables"]["representation"] > 0 and summary["tables"]["T2_gap"] > 0


def test_parallel_tuning_is_reproducible(tuned_cfg, tmp_path) -> None:
    """Batches of trials (ask/tell, constant liar) give the same frozen parameters on a second run."""
    import yaml

    tmp, _ = tuned_cfg
    first = yaml.safe_load((tmp / "tuned.yaml").read_text(encoding="utf-8"))
    assert first["procedure"]["parallel_trials"] == 2 and first["procedure"]["constant_liar"] is True
    path = make_config(tmp_path)
    assert cli("tune", "--config", str(path)).returncode == 0
    second = yaml.safe_load((tmp_path / "tuned.yaml").read_text(encoding="utf-8"))
    assert second["parameters"] == first["parameters"]
    assert second["best_objective"] == first["best_objective"]
    log = (tmp_path / "out" / "tuning" / "SA-rand.jsonl").read_text(encoding="utf-8").splitlines()
    assert [json.loads(line)["trial"] for line in log] == [0, 1, 2]


def _trial_log(out: Path, name: str) -> list[tuple[dict, float]]:
    rows = [json.loads(line) for line in (out / "tuning" / f"{name}.jsonl").read_text(encoding="utf-8").splitlines()]
    return [(r["params"], r["mean_gap"]) for r in rows]


def test_tuning_resumes_after_a_crash_with_the_same_trials(tmp_path) -> None:
    """A run stopped between batches and then left with a batch asked but never told (a crash) continues from
    the journal on disk and ends with the same trials, values and frozen parameters as an uninterrupted run."""
    import optuna
    import yaml

    from tpga.experiments.v2 import tune

    (tmp_path / "a").mkdir()
    (tmp_path / "b").mkdir()
    whole = ConfigV2.load(make_config(tmp_path / "a"))
    tune.run(whole, ["GA-rand"])
    cfg = ConfigV2.load(make_config(tmp_path / "b"))
    assert tune.run(cfg, ["GA-rand"], stop_after_batches=1) == {}
    assert len(_trial_log(cfg.output, "GA-rand")) == 2  # batch 0 of size 2 (parallel_trials: 2)
    # the crash: batch 1 asked (parameters stored in the trial) but the process died before telling it
    study = optuna.load_study(study_name="GA-rand", storage=tune.journal_storage(cfg.output / "tuning"))
    study.sampler = optuna.samplers.TPESampler(seed=int(cfg.raw["tuning"]["seed"]) + 1, constant_liar=True)
    trial = study.ask()
    trial.set_user_attr("params", tune.suggest(trial, "ga", cfg.raw["tuning"]["space"]))
    trial.set_user_attr("batch", 1)
    frozen = tune.run(cfg, ["GA-rand"])
    assert _trial_log(cfg.output, "GA-rand") == _trial_log(whole.output, "GA-rand")
    first = yaml.safe_load(whole.tuned_path.read_text(encoding="utf-8"))
    assert frozen["parameters"] == first["parameters"]
    assert frozen["best_objective"] == first["best_objective"]
    states = [
        t.state.name
        for t in optuna.load_study(study_name="GA-rand", storage=tune.journal_storage(cfg.output / "tuning")).trials
    ]
    assert states == ["COMPLETE", "COMPLETE", "FAIL", "COMPLETE"]  # the lost trial was asked again
    assert frozen["procedure"]["sampler_seed"] == "seed + batch index"


def test_recover_finishes_or_repeats_the_batch_in_flight() -> None:
    import optuna
    from optuna.trial import TrialState

    from tpga.experiments.v2 import tune

    study = optuna.create_study(storage=optuna.storages.InMemoryStorage())
    for batch, n in ((0, 2), (1, 1)):
        for _ in range(n):
            t = study.ask()
            t.set_user_attr("params", {"x": t.suggest_float("x", 0, 1)})
            t.set_user_attr("batch", batch)
    study.tell(0, 5.0)  # batch 0 half told: trial 1 is finished with its stored parameters
    seen = []

    def evaluate(params):
        seen.extend(params)
        return [(1.5, 7) for _ in params]

    assert tune.recover(study, evaluate) == {"finished": 1, "failed": 1}
    t = study.trials
    assert seen == [t[1].user_attrs["params"]]
    assert (t[1].state, t[1].value, t[1].user_attrs["runs"]) == (TrialState.COMPLETE, 1.5, 7)
    assert t[2].state == TrialState.FAIL  # batch 1 had nothing told: it is asked again by the caller


def test_workers_fit_the_worst_case_in_memory() -> None:
    from tpga.experiments.v2 import tune

    gib = 2**30
    worst = tune.worst_case_bytes(4000, 100 * 100)
    assert 1054 * 2**20 <= worst < 1.2 * gib  # measured peak 1054 MiB for population 4000 on 100x100
    assert 140 * 2**20 <= tune.worst_case_bytes(20, 100 * 100) < 0.2 * gib  # measured 140 MiB
    assert tune.safe_workers(24, worst, 33 * gib) == 24
    assert tune.safe_workers(24, worst, 14 * gib) == 9
    assert tune.safe_workers(24, worst, 1 * gib) == 1


def test_keep_awake_holds_a_request_only_inside_the_block() -> None:
    from tpga.experiments.environment import keep_awake

    with keep_awake() as ok:
        assert ok is (sys.platform == "win32")
