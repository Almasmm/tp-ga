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
    assert len(keys) == len(set(keys)) == 208
    assert all(r["feasible"] for r in records)
    assert all(r["gap_norm"] is not None for r in records if r["phase"] == "main")
    main = [r for r in records if r["phase"] == "main"]
    assert {r["method"] for r in main} == set(cfg.raw["stochastic_methods"])
    timing = [r for r in records if r["phase"] == "timing" and r["method"] == "LP"]
    assert all(r["solver"] == "highspy" and r["presolve_s"] is not None for r in timing)
    manifest = json.loads((cfg.output / "run_manifest.json").read_text(encoding="utf-8"))
    assert manifest["invocations"][0]["config"]["sha256"] == cfg.sha256
    assert set(manifest["phases"]) == {"reference", "main", "stagnation", "legacy", "factorial", "timing"}
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
    expected = 7 + 21 + 7 * 3 * 7  # LP, classical, 7 instances x 3 seeds x 7 methods
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
    assert len({i.id for i in items}) == len(items) == 8
    train = instances.build(cfg, split="train", sets=["uniform"], per_size=1)
    assert not {i.seed for i in items} & {i.seed for i in train}
    for i in items:
        p = methods.load(str(i.path))
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
