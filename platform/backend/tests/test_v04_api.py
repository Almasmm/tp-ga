"""v0.4 endpoints (read only): /artifacts/v2/*, /monitor/state; audit fixes W1, W3, W6."""

from __future__ import annotations

import io
import json
import os
import time
import zipfile

import pytest
from app import jobs
from app.main import MAX_SOLVE_CALLS, app
from fastapi.testclient import TestClient


@pytest.fixture()
def v2(tmp_path, monkeypatch):
    art, docs, exp = tmp_path / "paper_artifacts_v2", tmp_path / "docs", tmp_path / "experiments"
    for d in (
        art / "tables",
        art / "figures" / "en",
        art / "figures" / "ru",
        art / "state",
        art / "instances",
        art / "pilot",
        docs,
        exp,
    ):
        d.mkdir(parents=True)
    (art / "tables" / "T2_gap.csv").write_text("set,size,method,gap_median\nuniform,20x20,VAM,1.5\n", encoding="utf-8")
    (art / "tables" / "A1_methods_pooled.csv").write_text("set\nuniform\n", encoding="utf-8")
    (art / "tables" / "evil.csv").write_text("x\n1\n", encoding="utf-8")
    (art / "figures" / "en" / "boxplot_gap.png").write_bytes(b"\x89PNG")
    (art / "pilot" / "PILOT.md").write_text("# Pilot\n", encoding="utf-8")
    (art / "report.json").write_text(json.dumps({"runs": 3}), encoding="utf-8")
    (art / "run_manifest.json").write_text(
        json.dumps({"invocations": [{"git_commit": "abc", "packages": {"numpy": "2"}}], "phases": {"main": []}}),
        encoding="utf-8",
    )
    (art / "instances" / "manifest.json").write_text(
        json.dumps({"instances": {"a": {"set": "uniform"}, "b": {"set": "ties"}}}), encoding="utf-8"
    )
    (docs / "PREREGISTRATION.md").write_text("# Pre-registration\n", encoding="utf-8")
    (exp / "paper-v2.yaml").write_text("name: paper-v2\n", encoding="utf-8")
    (exp / "tuned-v2.yaml").write_text(
        "frozen: '2026-11-17'\nparameters: {GA-rand: {population: 50}}\ntraining_instances: [x, y]\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("TPGA_ARTIFACTS_V2_DIR", str(art))
    monkeypatch.setenv("TPGA_DOCS_V04_DIR", str(docs))
    monkeypatch.setenv("TPGA_EXPERIMENTS_DIR", str(exp))
    monkeypatch.setenv("TPGA_DB_PATH", str(tmp_path / "runs.db"))
    with TestClient(app) as c:
        yield c, art


def test_index_lists_only_valid_names(v2):
    client, _ = v2
    idx = client.get("/artifacts/v2").json()
    assert idx["available"] is True
    assert idx["tables"] == ["A1_methods_pooled", "T2_gap"]
    assert idx["figures"]["en"] == ["boxplot_gap"]
    assert idx["docs"] == ["PILOT", "PREREGISTRATION"]
    assert idx["report"] == {"runs": 3} and idx["invocations"] == 1


def test_table_figure_doc_and_rejections(v2):
    client, _ = v2
    t = client.get("/artifacts/v2/tables/T2_gap").json()
    assert t["rows"] == [{"set": "uniform", "size": "20x20", "method": "VAM", "gap_median": 1.5}]
    assert client.get("/artifacts/v2/tables/evil").status_code == 404
    assert client.get("/artifacts/v2/tables/..%2Fsecret").status_code == 404
    assert client.get("/artifacts/v2/figures/en/boxplot_gap.png").content == b"\x89PNG"
    assert client.get("/artifacts/v2/figures/de/boxplot_gap.png").status_code == 404
    assert client.get("/artifacts/v2/docs/PREREGISTRATION").text.startswith("# Pre-registration")
    assert client.get("/artifacts/v2/docs/HEAVY_RUN").status_code == 404  # not present in this fixture
    assert client.get("/artifacts/v2/docs/README").status_code == 404  # not in the allowed list
    assert client.get("/artifacts/v2/config/paper-v2").text == "name: paper-v2\n"
    assert client.get("/artifacts/v2/config/secrets").status_code == 404


def test_reproducibility_summary(v2):
    client, _ = v2
    r = client.get("/artifacts/v2/reproducibility").json()
    assert r["configs"]["paper-v2"]["exists"] and len(r["configs"]["paper-v2"]["sha256"]) == 64
    assert r["tuned"]["parameters"] == {"GA-rand": {"population": 50}}
    assert r["tuned"]["training_instances"] == 2
    assert r["instances"] == {"count": 2, "sets": {"uniform": 1, "ties": 1}}
    assert r["run"]["first"]["git_commit"] == "abc"


def test_download_v2_is_a_zip_without_raw(v2):
    client, art = v2
    (art / "raw").mkdir()
    (art / "raw" / "runs.jsonl").write_text("{}\n", encoding="utf-8")
    r = client.get("/artifacts/v2/download")
    assert r.status_code == 200 and r.headers["content-type"] == "application/zip"
    names = zipfile.ZipFile(io.BytesIO(r.content)).namelist()
    assert "paper_artifacts_v2/tables/T2_gap.csv" in names
    assert "docs/v0.4/PREREGISTRATION.md" in names
    assert not any("/raw/" in n for n in names)


def test_monitor_state_missing_fresh_and_stale(v2):
    client, art = v2
    assert client.get("/monitor/state").json() == {"available": False}
    path = art / "state" / "monitor.json"
    path.write_text(json.dumps({"phase": "main", "overall": {"done": 5, "total": 10}}), encoding="utf-8")
    fresh = client.get("/monitor/state").json()
    assert fresh["available"] and not fresh["stale"] and fresh["state"]["phase"] == "main"
    old = time.time() - 3600
    os.utime(path, (old, old))
    assert client.get("/monitor/state").json()["stale"] is True
    path.write_text("{not json", encoding="utf-8")
    assert client.get("/monitor/state").json() == {"available": False}
    assert client.post("/monitor/state").status_code == 405  # read only


def test_solve_rejects_too_many_decoder_calls(v2):
    client, _ = v2
    body = {"supply": [10, 10], "demand": [10, 10], "cost": [[1, 2], [3, 4]], "method": "ga"}
    ok = client.post("/solve", json={**body, "population": 20, "generations": 50, "seed": 1})
    assert ok.status_code == 200
    big = client.post("/solve", json={**body, "population": 1000, "generations": 5000})
    assert big.status_code == 422 and str(MAX_SOLVE_CALLS) in big.text
    lp = client.post("/solve", json={**body, "method": "lp", "population": 1000, "generations": 5000})
    assert lp.status_code == 200  # the cap concerns GA runs only


def test_job_events_keep_sequence_and_thin_progress():
    job = jobs.Job(id="x", request={"methods": ["LP"], "problem": {}})
    job.add({"type": "started"})
    for k in range(jobs.MAX_PROGRESS_EVENTS + 25):
        job.add({"type": "progress", "generation": k})
    job.add({"type": "done"})
    kinds = [e["type"] for e in job.events]
    assert kinds[0] == "started" and kinds[-1] == "done"
    assert kinds.count("progress") == jobs.MAX_PROGRESS_EVENTS
    seqs = [e["seq"] for e in job.events]
    assert seqs == sorted(seqs) and seqs[-1] == jobs.MAX_PROGRESS_EVENTS + 27
    progress = [e["generation"] for e in job.events if e["type"] == "progress"]
    assert progress[0] == 25 and progress[-1] == jobs.MAX_PROGRESS_EVENTS + 24  # the oldest were dropped
