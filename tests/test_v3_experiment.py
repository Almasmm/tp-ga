"""Additional experiment v3 on a tiny configuration: choice of k, pilot rule, runs, resume and report."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import pytest
import yaml

from tpga.experiments.v3 import core, report
from tpga.experiments.v3.__main__ import main
from tpga.ga import GAConfig, run_ga
from tpga.model import TransportProblem

ROOT = Path(__file__).resolve().parents[1]

TUNED = {
    "parameters": {
        "GA-rand": {
            "population": 12,
            "crossover_rate": 0.95,
            "tournament": 3,
            "elite": 1,
            "mutation_mode": "swap_scaled",
            "mutation_strength": 0.1,
        },
        "GA-cost": {
            "population": 16,
            "crossover_rate": 0.9,
            "tournament": 4,
            "elite": 2,
            "mutation_mode": "swap_count",
            "mutation_strength": 2,
        },
        "SA-rand": {"insertion_probability": 0.4, "initial_acceptance": 0.2, "final_ratio": 0.01},
        "SA-cost": {"insertion_probability": 0.3, "initial_acceptance": 0.01, "final_ratio": 0.001},
    }
}


def linear_config(tmp: Path, workers: int = 1, limit_min: float = 30, kselect_limit: float = 8) -> Path:
    data = yaml.safe_load((ROOT / "experiments" / "paper-v3-cycle.yaml").read_text(encoding="utf-8"))
    (tmp / "tuned.yaml").write_text(yaml.safe_dump(TUNED), encoding="utf-8")
    data.update(
        root=str(ROOT),
        output=str(tmp / "out"),
        tuned_parameters=str(tmp / "tuned.yaml"),
        runs=2,
        workers=workers,
        budget_factor=40,
        zrand_samples=50,
    )
    data["instances"] = [
        {"set": "uniform", "size": [3, 3], "first_seed": 100, "count": 2, "prefix": "u"},
        {"set": "uniform", "size": [5, 4], "first_seed": 200, "count": 3, "prefix": "v3u", "reduced_count": 2},
        {"set": "structured", "size": [4, 4], "first_seed": 300, "count": 2, "prefix": "s"},
    ]
    data["kselect"].update(
        instances=[
            {"set": "uniform", "size": [3, 3], "first_seed": 900, "prefix": "u", "suffix": "-train"},
            {"set": "uniform", "size": [5, 5], "first_seed": 950, "prefix": "u", "suffix": "-train"},
        ],
        instances_per_size=2,
        reduced_instances_per_size=1,
        runs=2,
        time_limit_min=kselect_limit,
        probe={"instance": "u5x5-00-train", "mode": "cycle_scaled"},
    )
    data["pilot"]["limit_min"] = limit_min
    path = tmp / "cycle.yaml"
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    return path


def fctp_config(tmp: Path, workers: int = 1) -> Path:
    data = yaml.safe_load((ROOT / "experiments" / "paper-v3-fctp.yaml").read_text(encoding="utf-8"))
    data.update(
        root=str(ROOT),
        output=str(tmp / "out"),
        tuned_parameters=str(tmp / "tuned.yaml"),
        selected_k=str(tmp / "out" / "kselect" / "selected.json"),
        runs=2,
        workers=workers,
        budget_factor=60,
    )
    data["instances"].update(sizes=[[3, 3], [4, 4]], count=2)
    data["mip"]["time_limit_s"] = 20
    data["methods"]["GA-hybrid"]["local_search_every"] = 2
    path = tmp / "fctp.yaml"
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    return path


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


@pytest.fixture(scope="module")
def finished(tmp_path_factory):
    """The whole experiment on tiny instances, in this process (one worker)."""
    tmp = tmp_path_factory.mktemp("v3")
    cycle = linear_config(tmp)
    fctp = fctp_config(tmp)
    for command, config in (
        ("kselect", cycle),
        ("pilot", cycle),
        ("run", cycle),
        ("report", cycle),
        ("run", fctp),
        ("report", fctp),
    ):
        assert main([command, "--config", str(config)]) == 0
    return tmp, core.ConfigV3.load(cycle), core.ConfigV3.load(fctp)


def test_choice_of_k_takes_the_smallest_mean_normalised_gap(finished) -> None:
    tmp, cfg, _ = finished
    out = tmp / "out" / "kselect"
    chosen = json.loads((out / "selected.json").read_text(encoding="utf-8"))
    table = read_csv(out / "kselect.csv")
    assert len(table) == 2 * 4 and not chosen["reduced_training_set"]
    assert chosen["instances"] == ["u3x3-00-train", "u3x3-01-train", "u5x5-00-train", "u5x5-01-train"]
    for variant in ("GA-rand-cycle", "GA-cost-cycle"):
        rows = [r for r in table if r["variant"] == variant]
        assert all(int(r["runs"]) == 4 * 2 for r in rows)
        best = min(rows, key=lambda r: (float(r["mean_gap_norm"]), int(r["rank"])))
        assert [r["selected"] for r in rows].count("True") == 1 and best["selected"] == "True"
        assert chosen["selected"][variant]["k"] == best["k"]
        assert cfg.selected()[variant]["mode"] == best["mode"]
    assert {r["k"] for r in table} == {"1", "2", "4", "round(0.05(m+n))"}
    # the records of the grid are complete and carry the normalised gap
    rows = core.records(out / "records.jsonl", "kselect")
    assert len(rows) == 2 * 4 * 4 * 2 and all(r["gap_norm"] is not None and r["gap"] >= -1e-9 for r in rows)


def test_linear_run_is_complete_and_matches_the_library(finished) -> None:
    tmp, cfg, _ = finished
    pilot = json.loads((cfg.area / "pilot.json").read_text(encoding="utf-8"))
    assert not pilot["reduced"] and pilot["pilot_runs"] == 3 * 7 and pilot["estimate_full_s"] >= 0
    rows, items = report.linear_rows(cfg)
    assert len(items) == 7 and len(rows) == 7 * (1 + 7 * 2)
    assert all(r["max_residual"] == 0 and r["gap"] >= -1e-9 for r in rows)
    # GA-rand-tuned is tpga.ga.run_ga with the tuned parameters: the record equals a direct call
    rec = next(
        r for r in rows if r["method"] == "GA-rand-tuned" and r["instance"] == "v3u5x4-01" and r["seed"] == 20261117
    )
    inst = next(i for i in items if i["id"] == "v3u5x4-01")
    direct = run_ga(
        TransportProblem.from_json(inst["path"]),
        GAConfig(
            population=12,
            generations=None,
            crossover_rate=0.95,
            tournament=3,
            elite=1,
            seed=20261117,
            max_evaluations=40 * 20,
            mutation_mode="swap_scaled",
            mutation_strength=0.1,
        ),
    )
    assert rec["cost"] == direct.cost and rec["evals"] == direct.evaluations and rec["budget"] == 800
    cyc = [r for r in rows if r["method"].endswith("-cycle")]
    assert cyc and all(r["pivots"] > 0 and r["evals"] <= r["budget"] and r["stop_reason"] == "budget" for r in cyc)
    assert all(":" in r["config"] and "cycle" in r["config"] for r in cyc)
    manifest = json.loads((cfg.area / "instances" / "manifest.json").read_text(encoding="utf-8"))["instances"]
    assert manifest["v3u5x4-02"]["seed"] == 202 and manifest["u3x3-00"]["z_star"] <= manifest["u3x3-00"]["z_rand"]


def test_linear_report_tables_and_tests(finished) -> None:
    _, cfg, _ = finished
    tables = cfg.area / "tables"
    t1 = read_csv(tables / "T1_gap.csv")
    assert len(t1) == 3 * 8
    vam = next(r for r in t1 if r["method"] == "VAM" and r["size"] == "5x4")
    assert int(vam["runs"]) == 3 and int(vam["instances"]) == 3
    t2 = read_csv(tables / "T2_tests.csv")
    assert len(t2) == 3 * 5
    for r in t2:
        assert int(r["wins_a"]) + int(r["ties"]) + int(r["losses_a"]) == int(r["n"])
        assert 0 <= float(r["p"]) <= float(r["p_holm"]) <= 1
        assert float(r["smallest_possible_p"]) == 2 / 2 ** int(r["n"])
    wide = read_csv(tables / "T3_by_size.csv")
    assert {r["value"] for r in wide} == {"gap", "gap_norm", "time_s"} and "uniform 5x4" in wide[0]
    t4 = read_csv(tables / "T4_cycle_counters.csv")
    assert len(t4) == 3 * 2 and all(0 <= float(r["share_pivots_theta_zero"]) <= 1 for r in t4)
    assert (tables / "T1_gap.md").read_text(encoding="utf-8").startswith("# Linear problem")
    for name in ("linear_gap_norm.pdf", "linear_gap_norm.jpg"):
        assert (cfg.area / "figures" / name).stat().st_size > 1000


def test_fctp_run_and_report(finished) -> None:
    _, _, cfg = finished
    rows, mip, items = report.fctp_rows(cfg)
    assert len(items) == 2 * 2 * 2 and len(mip) == 8 and all(m["proved"] for m in mip)
    assert len(rows) == 8 * (2 + 6 * 2)
    f1 = read_csv(cfg.area / "tables" / "F1_mip_instances.csv")
    assert all(r["z_best_source"] == "MIP (proved optimum)" for r in f1)
    assert all(float(r["z_best_gap_to_bound_percent"]) < 1e-6 for r in f1)
    f2 = read_csv(cfg.area / "tables" / "F2_gap.csv")
    assert len(f2) == 4 * 8 and all(float(r["gap_min"]) >= -1e-9 for r in f2)
    hybrid = [r for r in f2 if r["method"] == "GA-hybrid"]
    assert all(float(r["local_search_calls_mean"]) >= 1 for r in hybrid)
    f3 = read_csv(cfg.area / "tables" / "F3_tests.csv")
    assert [r["scope"] for r in f3] == ["all instances"] * 4 + ["rho = 0.2"] * 4 + ["rho = 1"] * 4
    assert int(f3[0]["n"]) == 8 and int(f3[4]["n"]) == 4
    cells = read_csv(cfg.area / "tables" / "F3_cells.csv")
    assert len(cells) == 4 * 4 and "p" not in cells[0]
    summary = read_csv(cfg.area / "tables" / "F1_mip_summary.csv")
    assert [int(r["proved_optimal"]) for r in summary] == [2, 2, 2, 2]
    assert (cfg.area / "figures" / "fctp_gap.pdf").stat().st_size > 1000
    manifest = json.loads((cfg.output / "run_manifest.json").read_text(encoding="utf-8"))
    assert [i["command"] for i in manifest["invocations"]] == ["kselect", "pilot", "run", "report", "run", "report"]
    assert manifest["invocations"][0]["config"]["path"].endswith("cycle.yaml")
    assert all(i["git_state_taken"] == "start" and len(i["git_commit"]) == 40 for i in manifest["invocations"])
    state = core.code_state(core.ConfigV3.load(ROOT / "experiments" / "paper-v3-cycle.yaml"))
    assert state["git_commit"] == manifest["invocations"][-1]["git_commit"] and isinstance(state["git_dirty"], bool)


def test_a_second_start_runs_nothing_and_the_pool_gives_the_same_records(finished, tmp_path, capsys) -> None:
    tmp, cfg, fctp = finished
    assert core.run(cfg)["ran"] == 0
    again = core.run(fctp)
    assert again["mip"]["ran"] == 0 and again["main"]["ran"] == 0
    capsys.readouterr()
    # the same linear plan with two worker processes: identical costs for every key
    other = core.ConfigV3.load(linear_config(tmp_path, workers=2))
    (tmp_path / "out" / "kselect").mkdir(parents=True)
    (tmp_path / "out" / "kselect" / "selected.json").write_text(cfg.selected_path.read_text(encoding="utf-8"))
    core.pilot(other)
    assert core.run(other)["failed"] == 0
    first = {core.key_of(r): r["cost"] for r in core.records(cfg.area / "raw" / "runs.jsonl")}
    second = {core.key_of(r): r["cost"] for r in core.records(other.area / "raw" / "runs.jsonl")}
    assert first == second


def test_reduction_rules_apply_when_the_estimate_is_above_the_limit(finished, tmp_path) -> None:
    _, done, _ = finished
    cfg = core.ConfigV3.load(linear_config(tmp_path, limit_min=0.0, kselect_limit=0.0))
    chosen = core.kselect(cfg)
    assert chosen["reduced_training_set"] and chosen["instances"] == ["u3x3-00-train", "u5x5-00-train"]
    pilot = core.pilot(cfg)
    assert pilot["reduced"] and pilot["estimate_after_rule_s"] <= pilot["estimate_full_s"]
    core.run(cfg)
    rows, items = report.linear_rows(cfg)
    assert sorted(i["id"] for i in items if i["size"] == "5x4") == ["v3u5x4-00", "v3u5x4-01"]
    assert len(rows) == 6 * (1 + 7 * 2)
    first = report.report(cfg)
    assert first["neutrality_figure"] is False and first["extension_tests"] == 0
    assert not (cfg.area / "tables" / "T2_tests_extension.csv").exists()
    assert len(report.linear_rows(done)[1]) == 7  # the other configuration keeps its full plan
    # amendment 9.1: the command extend runs the instance that the rule left out; the tests are given three times
    assert core.extend(cfg)["ran"] == 1 + 7 * 2 and core.extended(cfg)
    rows, items = report.linear_rows(cfg)
    assert len(items) == 7 and len(rows) == 7 * (1 + 7 * 2)
    assert report.report(cfg)["extension_tests"] == 3 * 5
    split = read_csv(cfg.area / "tables" / "T2_tests_extension.csv")
    assert [(r["instances"], int(r["n"])) for r in split[::5]] == [
        ("first 2 (plan after the pilot rule)", 2),
        ("added 1 (amendment 9.1)", 1),
        ("all 3", 3),
    ]
    assert {r["size"] for r in split} == {"5x4"}
    assert core.extend(cfg)["ran"] == 0
    assert report.extension_tests(done, report.linear_rows(done)[1], {}) == []  # nothing was reduced there


def test_errors_and_command_line(finished, tmp_path, capsys) -> None:
    _, cfg, fctp = finished
    with pytest.raises(SystemExit):
        main(["kselect", "--config", str(fctp.path)])
    bad = tmp_path / "bad.yaml"
    bad.write_text("problem: other\n", encoding="utf-8")
    with pytest.raises(ValueError, match="linear or fctp"):
        core.ConfigV3.load(bad)
    fresh = core.ConfigV3.load(linear_config(tmp_path))
    with pytest.raises(RuntimeError, match="kselect first"):
        fresh.selected()
    (tmp_path / "out" / "kselect").mkdir(parents=True)
    (tmp_path / "out" / "kselect" / "selected.json").write_text(cfg.selected_path.read_text(encoding="utf-8"))
    with pytest.raises(RuntimeError, match="pilot first"):
        core.run(fresh)
    with pytest.raises(RuntimeError, match="extend completes"):
        core.extend(fresh)
    with pytest.raises(SystemExit):
        main(["extend", "--config", str(fctp.path)])
    # a failing run is recorded and reported, the others are kept
    inst = core.build_linear(fresh, core.linear_groups(fresh, False), fresh.area / "instances")[:1]
    tasks = core.plan_tasks(fresh, "main", inst, ["VAM", "RS"], fresh.seeds(1))
    tasks[1]["z_star"] = 10**9  # an optimum above every plan: the check of the record must fail
    with pytest.raises(RuntimeError, match="1 runs failed"):
        core.run_tasks(fresh, tasks, tmp_path / "raw.jsonl", "broken")
    assert len(core.records(tmp_path / "raw.jsonl")) == 1
    assert "below the optimum" in (tmp_path / "errors.jsonl").read_text(encoding="utf-8")
    with pytest.raises(ValueError, match="unknown method kind"):
        core.execute(
            {**tasks[0], "problem": "fctp", "kind": "classical", "path": str(next(fctp.area.glob("instances/f*.json")))}
        )
    capsys.readouterr()


def test_neutrality_figure_from_the_script_summary(tmp_path) -> None:
    summary = tmp_path / "operators_summary.csv"
    assert report.figure_neutrality(summary, tmp_path) is False
    summary.write_text(
        "set,size,operator,unchanged_share_median\n"
        "uniform,5x5,swap_scaled,0.58\nuniform,10x10,swap_scaled,0.52\n"
        "uniform,5x5,cycle,0.05\nuniform,10x10,cycle,0.02\nstructured,20x20,cycle,0.01\n",
        encoding="utf-8",
    )
    assert report.figure_neutrality(summary, tmp_path) is True
    assert (tmp_path / "neutrality_operators.pdf").stat().st_size > 1000
    summary.write_text("set,size,operator,unchanged_share_median\nstructured,20x20,cycle,0.01\n", encoding="utf-8")
    assert report.figure_neutrality(summary, tmp_path) is False


def write_mps(path: Path, fcp, capacity_factor: float = 1.0, drop_last_y: bool = False) -> None:
    """A fixed-charge problem in the MPS layout of the MIPLIB instances (see core.read_fctp_mps)."""
    m, n = fcp.shape
    lines = ["*NAME: tiny", "NAME          tiny", "ROWS", " N  COST"]
    lines += [f" E  A{i}" for i in range(m)] + [f" E  B{j}" for j in range(n)]
    lines += [f" L  G{k}" for k in range(m * n)] + ["COLUMNS"]
    for k in range(m * n):
        i, j = divmod(k, n)
        lines += [f"    X{k}  COST  {fcp.problem.cost[i, j]:g}", f"    X{k}  A{i}  1  G{k}  1", f"    X{k}  B{j}  1"]
    lines.append("    MARKER    'MARKER'    'INTORG'")
    for k in range(m * n - int(drop_last_y)):
        i, j = divmod(k, n)
        lines += [f"    Y{k}  COST  {fcp.fixed[i, j]:g}", f"    Y{k}  G{k}  {-capacity_factor * fcp.big_m[i, j]:g}"]
    lines += ["    MARKEND   'MARKER'    'INTEND'", "RHS"]
    lines += [f"    RHS  A{i}  {fcp.problem.supply[i]:g}" for i in range(m)]
    lines += [f"    RHS  B{j}  {fcp.problem.demand[j]:g}" for j in range(n)]
    lines += ["BOUNDS"] + [f" BV bnd  Y{k}" for k in range(m * n)] + ["ENDATA"]
    import gzip

    with gzip.open(path, "wt", encoding="ascii") as fh:
        fh.write("\n".join(lines) + "\n")


def test_external_benchmark_reader_run_and_table(finished, tmp_path, capsys) -> None:
    import numpy as np

    from tpga.fctp import FixedChargeProblem, generate, solve_mip

    _, linear, _ = finished
    problems = {name: FixedChargeProblem.from_dict(generate(3, 4, seed, 1.0)) for name, seed in (("a", 1), ("b", 2))}
    entries = []
    for name, fcp in problems.items():
        write_mps(tmp_path / f"{name}.mps.gz", fcp)
        data = core.read_fctp_mps(tmp_path / f"{name}.mps.gz")
        assert np.array_equal(data["fixed"], fcp.fixed) and np.array_equal(data["cost"], fcp.problem.cost)
        assert data["supply"] == fcp.problem.supply.tolist() and data["demand"] == fcp.problem.demand.tolist()
        entries.append(
            {"id": name, "file": str(tmp_path / f"{name}.mps.gz"), "objective": solve_mip(fcp, 30).cost, "url": "u"}
        )
    write_mps(tmp_path / "cut.mps.gz", problems["a"], capacity_factor=0.5)
    with pytest.raises(ValueError, match="capacity below"):
        core.read_fctp_mps(tmp_path / "cut.mps.gz")
    write_mps(tmp_path / "part.mps.gz", problems["a"], drop_last_y=True)
    with pytest.raises(ValueError, match="not a complete"):
        core.read_fctp_mps(tmp_path / "part.mps.gz")

    path = fctp_config(tmp_path)
    (tmp_path / "tuned.yaml").write_text(yaml.safe_dump(TUNED), encoding="utf-8")
    (tmp_path / "out" / "kselect").mkdir(parents=True)
    (tmp_path / "out" / "kselect" / "selected.json").write_text(linear.selected_path.read_text(encoding="utf-8"))
    with pytest.raises(SystemExit):
        main(["benchmark", "--config", str(linear.path)])
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["benchmark"] = {"source": "test files.", "mip": {"time_limit_s": 20, "abs_gap": 1e-6}, "instances": entries}
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    for command in ("benchmark", "run", "report"):
        assert main([command, "--config", str(path)]) == 0
    cfg = core.ConfigV3.load(path)
    ref = read_csv(cfg.area / "tables" / "B1_benchmark_reference.csv")
    assert [r["instance"] for r in ref] == ["a", "b"] and all(r["highs_proved"] == "True" for r in ref)
    assert all(abs(float(r["highs_minus_listed"])) < 1e-6 for r in ref)
    table = read_csv(cfg.area / "tables" / "B2_benchmark_gap.csv")
    assert len(table) == 2 * 8 and all(float(r["gap_min"]) >= -1e-9 for r in table)
    assert all(int(r["runs"]) == (1 if r["method"] in ("Balinski", "VAM-lin") else 2) for r in table)
    manifest = json.loads((cfg.area / "benchmark" / "instances" / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["source"] == "test files." and len(manifest["instances"]["a"]["source_sha256"]) == 64
    capsys.readouterr()
