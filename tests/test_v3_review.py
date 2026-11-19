"""Amendment 10 on a tiny configuration: rivals, new classes, second rule for the entering arc, time rules."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pytest
import yaml

from test_v3_experiment import ROOT, ext_config, fctp_config, linear_config, read_csv
from tpga.experiments.v3 import core, rev
from tpga.experiments.v3.__main__ import main

PUBLIC = "3 4\n5 6 7\n4 4 5 5\n" + "\n".join(
    " ".join(f"{v:.6f}" for v in row)
    for row in [[3, 8, 5, 6], [4, 3, 6, 5], [5, 3, 3, 6], [80, 191, 73, 154], [110, 126, 0, 150], [90, 152, 58, 175]]
)


def review_config(tmp: Path, base: Path, linear: Path) -> Path:
    data = yaml.safe_load((ROOT / "experiments" / "paper-v3-review.yaml").read_text(encoding="utf-8"))
    b = yaml.safe_load(base.read_text(encoding="utf-8"))
    data.update({k: b[k] for k in ("root", "output", "tuned_parameters", "selected_k", "runs", "budget_factor", "mip")})
    data.update(base=str(base), linear=str(linear), workers=1)
    data["pilot"]["instances"].update(sizes=[[3, 3], [5, 5]])
    data["pilot"]["linear_instance"] = "u5x5-00-train"
    data["rivals"]["Tabu"]["grid"] = {"sample": [1.0, 0.5], "tenure": [2, 4]}
    data["rivals"]["ILS"]["grid"] = {"perturbation": [1, 2], "acceptance": ["better", "always"]}
    data["tune_runs"] = 2
    data["generator"].update(sizes=[[4, 4], [5, 5]], count=2)
    data["mip_default"]["time_limit_s"] = 5
    source = tmp / "public"
    source.mkdir(exist_ok=True)
    (source / "N1.FCTP").write_text(PUBLIC, encoding="ascii")
    digest = hashlib.sha256((source / "N1.FCTP").read_bytes()).hexdigest()
    data["public"].update(
        base_url=source.as_uri() + "/",
        instances=[{"id": "N1", "sha256": digest, "published": {"cplex9": 1, "sun_tabu": 2, "ghost_image": 3}}],
    )
    data["timing"].update(cpu=None, instances_per_cell=1, runs=2)
    data["degenerate"].update(reduce_size="5x4", counts=[3, 2, 1, 0])
    data["degenerate"]["trace"].update(sizes=["3x3", "5x4"], instances=2, runs=2)
    data["bootstrap"]["resamples"] = 200
    path = tmp / "review.yaml"
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    return path


@pytest.fixture(scope="module")
def reviewed(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("review")
    cycle = linear_config(tmp)
    fctp = fctp_config(tmp)
    for command, config in (("kselect", cycle), ("pilot", cycle), ("run", cycle), ("extend", cycle), ("run", fctp)):
        assert main([command, "--config", str(config)]) == 0
    extension = ext_config(tmp, fctp)
    for command in ("tune", "run"):
        assert main([command, "--config", str(extension)]) == 0
    path = review_config(tmp, extension, cycle)
    for command in ("pilot", "tune", "rivals", "generator", "degenerate", "public", "timing"):
        assert main([command, "--config", str(path)]) == 0
    return tmp, core.ConfigV3.load(path)


def test_runs_of_the_review(reviewed) -> None:
    tmp, cfg = reviewed
    out = rev.area(cfg)
    spent = json.loads((out / "budget.json").read_text(encoding="utf-8"))["commands"]
    assert [c["command"] for c in spent] == ["pilot", "tune", "rivals", "generator", "degenerate", "public", "timing"]
    assert rev.used_s(cfg) == pytest.approx(sum(c["wall_s"] for c in spent))
    times = rev.pilot_times(cfg)
    assert {"Tabu|3x3", "ILS|5x5", "GA-cost-cycle|5x5", "GA-rand-cycle-nd|5x5", "GA-rand-cycle|5x5"} <= set(times)

    # the grids: 4 configurations each, 4 training instances, 2 seeds; rule and tie order
    grid = read_csv(out / "tune" / "grid.csv")
    assert len(grid) == 8 and all(int(r["runs"]) == 4 * 2 for r in grid)
    chosen = rev.selected(cfg)
    for name in ("Tabu", "ILS"):
        part = [r for r in grid if r["method"] == name]
        best = min(part, key=lambda r: (float(r["mean_gap"]), int(r["rank"])))
        assert best["selected"] == "True" and chosen[name]["config"] == best["config"]
        assert rev.rival(cfg, name)["config"] == best["config"]
    assert all(float(r["mean_gap"]) >= -1e-9 for r in grid)

    # rivals: 12 instances, 2 seeds, 2 methods; the budget and the two counters
    rows = core.records(out / "raw" / "rivals.jsonl", "rivals")
    assert len(rows) == 12 * 2 * 2
    for r in rows:
        assert r["evals"] == r["budget"] == 60 * r["m"] * r["n"]
        assert r["full_evaluations"] == 1 and r["neighbour_evaluations"] == r["evals"] - 1
        assert r["cost"] <= r["start_cost"]
    assert rev.rivals_plan(cfg)["instances_70x70"] == 5

    # new classes: 2 sizes x (2 + 4) cells x 2 instances; concentrated supplies
    items = rev.generator_items(cfg)
    new = [i for i in items if i["new"]]
    assert len(new) == 2 * 6 * 2 and {i["class"] for i in new} == {"uniform", "concentrated"}
    assert sum(not i["new"] for i in items) == 8  # the instances 4x4 of 8.4 and 5x5 of 9.4 in the test
    one = json.loads(Path(next(i["path"] for i in new if i["id"] == "c5x5-r0.2-01")).read_text(encoding="utf-8"))
    assert sum(one["supply"]) == sum(one["demand"]) == 300 and sum(one["supply"][:2]) == 240
    assert one["seed"] == 20330000 + 1000 + 100 + 1
    assert len(core.records(out / "raw" / "gen_mip.jsonl", "gen-mip")) == 24
    assert len(core.records(out / "raw" / "gen.jsonl", "gen")) == 24 * (1 + 3 * 2)
    assert rev.generator_plan(cfg)["instances_per_new_cell"] == 5

    # 10.5: the repeated runs equal the records; the second rule has no pivot with theta = 0 unless it fell back
    trace = core.records(out / "raw" / "linear.jsonl", "trace")
    assert len(trace) == 2 * 2 * 2 * 2
    for r in trace:
        assert r["pivot_trace"][-1] == [r["pivots"], r["zero_pivots"]] and len(r["pivot_trace"]) == r["generations"]
    nd = core.records(out / "raw" / "linear.jsonl", "nd")
    assert len(nd) == 7 * 2 * 2 and {r["method"] for r in nd} == {"GA-rand-cycle-nd", "GA-cost-cycle-nd"}
    assert all(r["zero_pivots"] <= r["fallback_pivots"] for r in nd)
    plan = rev.degenerate_plan(cfg)
    assert plan["instances_at_reduce_size"] == 3 and plan["traced_instances_at_reduce_size"] == 2

    # public file: read as it is, checked by its hash
    data = rev.read_fctp_text(tmp / "public" / "N1.FCTP")
    assert data["supply"] == [5, 6, 7] and data["fixed"][1][2] == 0 and np.shape(data["cost"]) == (3, 4)
    assert len(core.records(out / "raw" / "public.jsonl", "public")) == 1 + 3 * 2

    # timing: one instance per cell, one run at a time, MIP with the median time of the GA as its limit
    timed = core.records(out / "raw" / "timing.jsonl", "timing")
    assert len(timed) == 6 * 3 * 2
    mips = core.records(out / "raw" / "timing_mip.jsonl", "timing-mip")
    assert len(mips) == 6
    ga = sorted(r["time_s"] for r in timed if r["instance"] == mips[0]["instance"] and r["method"] == "GA-cost-cycle")
    assert mips[0]["time_limit_s"] == pytest.approx((ga[0] + ga[1]) / 2)


def test_time_rules(reviewed) -> None:
    _, cfg = reviewed
    # the MIP in its usual setting stops starting runs when the allowance is below one time limit
    assert len(rev.mip_default_order(cfg)) == 12
    assert main(["mipdefault", "--config", str(cfg.path), "--minutes", "0.15"]) == 0
    state = json.loads((rev.area(cfg) / "mip_default.json").read_text(encoding="utf-8"))
    assert 1 <= len(state["ran"]) < 12 and state["ran"] == state["order"][: len(state["ran"])]
    assert state["not_run_time_rule"] == state["order"][len(state["ran"]) :]
    rows = core.records(rev.area(cfg) / "raw" / "mip_default.jsonl", "mip-default")
    assert all(r["threads"] == 0 and r["time_limit_s"] == 5 and r["cpu_s"] >= 0 for r in rows)
    spent = json.loads((rev.area(cfg) / "budget.json").read_text(encoding="utf-8"))["commands"]
    assert spent[-1]["beyond_limit"] and rev.used_s(cfg) == pytest.approx(sum(c["wall_s"] for c in spent[:-1]))
    # time left unused by earlier commands passes on; the last command stops a margin before the limit
    plan = cfg.raw["allowance_min"]
    assert rev.allowance_s(cfg, "tune") == pytest.approx(60 * (plan["pilot"] + plan["tune"]) - rev.used_s(cfg))
    cfg.raw["limit_min"] = rev.used_s(cfg) / 60 + 0.5 + cfg.raw["final_margin_min"]
    assert rev.allowance_s(cfg, "mipdefault") == pytest.approx(30.0)
    cfg.raw["limit_min"] = 0
    assert rev.allowance_s(cfg, "timing") == 0
    with pytest.raises(RuntimeError, match="do not fit"):
        rev.rivals.__wrapped__(cfg, 0.0)
