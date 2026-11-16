"""Jobs with SSE and cancellation, traces, plans, artifacts and the run history."""

import json
import time

import pytest
from app import history
from app.main import app
from fastapi.testclient import TestClient

SMALL = {"kind": "matrix", "supply": [20, 30, 20], "demand": [25, 25, 20], "cost": [[8, 6, 3], [5, 4, 9], [2, 7, 6]]}


@pytest.fixture(scope="module")
def client(tmp_path_factory):
    db = tmp_path_factory.mktemp("db") / "runs.db"
    mp = pytest.MonkeyPatch()
    mp.setenv("TPGA_DB_PATH", str(db))
    with TestClient(app) as c:
        yield c
    mp.undo()


def wait_done(client, job_id, timeout=300):  # the first job starts the worker processes
    end = time.time() + timeout
    while time.time() < end:
        job = client.get(f"/jobs/{job_id}").json()
        if job["status"] in ("done", "error", "cancelled"):
            return job
        time.sleep(0.1)
    raise AssertionError("job did not finish")


def test_version(client):
    assert client.get("/health").json() == {"status": "ok"}
    assert client.get("/version").json()["tpga"]


def test_job_runs_methods_and_streams_events(client):
    r = client.post(
        "/jobs",
        json={
            "problem": SMALL,
            "methods": ["VAM", "GA-rand", "RS"],
            "params": {"population": 10, "budget": 400, "seed": 1},
        },
    )
    assert r.status_code == 202
    job_id = r.json()["id"]
    job = wait_done(client, job_id)
    assert job["status"] == "done"
    res = job["result"]["results"]
    assert set(res) == {"LP", "VAM", "GA-rand", "RS"} and res["LP"]["cost"] == 225
    assert res["VAM"]["gap_percent"] == 0 and res["GA-rand"]["evaluations"] <= 400
    with client.stream("GET", f"/jobs/{job_id}/events") as s:
        text = "".join(s.iter_text())
    kinds = [line.split(": ", 1)[1] for line in text.splitlines() if line.startswith("event: ")]
    assert kinds[0] == "started" and kinds[-1] == "done" and "progress" in kinds and kinds.count("method_done") == 4
    data = [json.loads(line[6:]) for line in text.splitlines() if line.startswith("data: ")]
    progress = [d for d in data if d["type"] == "progress"]
    assert all(k in progress[0] for k in ("generation", "best_cost", "gap", "evaluations"))
    assert any(j["id"] == job_id for j in client.get("/jobs").json())


def test_job_cancellation(client):
    big = {"kind": "generated", "m": 120, "n": 120, "seed": 3}
    r = client.post("/jobs", json={"problem": big, "methods": ["RS"], "params": {"budget": 2_000_000, "seed": 0}})
    job_id = r.json()["id"]
    time.sleep(1.0)
    assert client.delete(f"/jobs/{job_id}").json()["status"] in ("cancelling", "cancelled")
    assert wait_done(client, job_id)["status"] == "cancelled"
    assert client.delete(f"/jobs/{job_id}").json()["status"] == "cancelled"  # idempotent


def test_job_validation_and_limits(client):
    assert client.post("/jobs", json={"problem": {"kind": "matrix"}, "methods": ["LP"]}).status_code == 422
    assert client.post("/jobs", json={"problem": SMALL, "methods": []}).status_code == 422
    assert client.post("/jobs", json={"problem": SMALL, "methods": ["SIMPLEX"]}).status_code == 422
    too_big = {"kind": "generated", "m": 201, "n": 5, "seed": 1}
    assert client.post("/jobs", json={"problem": too_big, "methods": ["LP"]}).status_code == 422
    bad = {"problem": SMALL, "methods": ["GA-rand"], "params": {"population": 4, "elite": 4}}
    assert client.post("/jobs", json=bad).status_code == 422
    neg = {**SMALL, "supply": [-1, 30, 20]}
    assert client.post("/jobs", json={"problem": neg, "methods": ["LP"]}).status_code == 422
    missing = {"kind": "scenario", "dataset_id": "kazakh-wheat", "scenario_id": "nope"}
    assert client.post("/jobs", json={"problem": missing, "methods": ["LP"]}).status_code == 404
    assert client.get("/jobs/000000000000").status_code == 404


def test_concurrent_job_limit(client):
    big = {"kind": "generated", "m": 120, "n": 120, "seed": 4}
    body = {"problem": big, "methods": ["RS"], "params": {"budget": 2_000_000}}
    ids = [client.post("/jobs", json=body).json()["id"] for _ in range(2)]
    assert client.post("/jobs", json=body).status_code == 429
    for job_id in ids:
        client.delete(f"/jobs/{job_id}")
    for job_id in ids:
        wait_done(client, job_id)


def test_decoder_and_classical_traces(client):
    ex = client.get("/trace/examples").json()["3x4"]
    problem = {"kind": "matrix", **{k: ex[k] for k in ("supply", "demand", "cost")}}
    d = client.post("/trace/decoder", json={"problem": problem, "permutation": list(range(12))}).json()
    assert d["steps"][0]["quantity"] == 20 and d["cost"] >= d["lp_cost"]
    assert client.post("/trace/decoder", json={"problem": problem, "permutation": [0, 0, 1]}).status_code == 422
    v = client.post("/trace/classical", json={"problem": problem, "method": "VAM"}).json()
    assert v["steps"][0]["row_penalty"] is not None and v["cost"] >= v["lp_cost"]
    big = {"kind": "generated", "m": 11, "n": 10, "seed": 1}
    assert client.post("/trace/decoder", json={"problem": big}).status_code == 413


def test_ga_trace(client):
    r = client.post("/trace/ga", json={"problem": SMALL, "population": 8, "generations": 10, "seed": 2}).json()
    gens = r["generations"]
    assert len(gens) == 11 and gens[-1]["best_cost"] >= r["lp_cost"]
    first = gens[1]["offspring"]
    assert first["tournament_a"]["winner"] in first["tournament_a"]["candidates"]
    assert sorted(first["child"]) == list(range(9))
    bad = {"problem": SMALL, "population": 4, "tournament": 5}
    assert client.post("/trace/ga", json=bad).status_code == 422


def test_plans_for_the_map(client):
    problem = {"kind": "scenario", "dataset_id": "kazakh-wheat", "scenario_id": "year-2024"}
    r = client.post("/plans", json={"problem": problem, "methods": ["LP", "VAM", "GA-cost"]}).json()
    assert set(r["results"]) == {"LP", "VAM", "GA-cost"}
    assert r["results"]["VAM"]["cost"] >= r["lp_optimum"] and r["results"]["LP"]["plan"]


def test_artifacts_read_only(client, tmp_path, monkeypatch):
    root = tmp_path / "paper_artifacts"
    (root / "tables").mkdir(parents=True)
    (root / "figures" / "en").mkdir(parents=True)
    (root / "tables" / "T2_gap.csv").write_text("size,method,gap_mean\n5x5,GA-rand,0.5\n5x5,LP,0\n", encoding="utf-8")
    (root / "figures" / "en" / "F2_convergence.png").write_bytes(b"\x89PNG\r\n")
    (root / "METHODS.md").write_text("# Methods\n", encoding="utf-8")
    (root / "reachability.json").write_text(json.dumps({"instances": 3, "cases": [1, 2, 3]}), encoding="utf-8")
    monkeypatch.setenv("TPGA_ARTIFACTS_DIR", str(root))
    idx = client.get("/artifacts").json()
    assert (
        idx["tables"] == ["T2_gap"]
        and idx["figures"]["en"] == ["F2_convergence"]
        and "cases" not in idx["reachability"]
    )
    t = client.get("/artifacts/tables/T2_gap").json()
    assert t["rows"][0] == {"size": "5x5", "method": "GA-rand", "gap_mean": 0.5}
    assert client.get("/artifacts/figures/en/F2_convergence.png").content.startswith(b"\x89PNG")
    assert client.get("/artifacts/docs/METHODS").text.startswith("# Methods")
    for bad in (
        "/artifacts/tables/..%2Fsecret",
        "/artifacts/tables/X1",
        "/artifacts/docs/secret",
        "/artifacts/figures/de/F1.png",
    ):
        assert client.get(bad).status_code == 404
    assert client.get("/artifacts/convergence", params={"size": "5x5"}).status_code == 404
    z = client.get("/artifacts/download")
    assert z.status_code == 200 and z.content[:2] == b"PK"
    assert client.post("/artifacts/tables/T2_gap").status_code == 405
    monkeypatch.setenv("TPGA_ARTIFACTS_DIR", str(tmp_path / "missing"))
    assert client.get("/artifacts").status_code == 404


def test_history_save_list_delete(client):
    job_id = client.post("/jobs", json={"problem": SMALL, "methods": ["LCM"]}).json()["id"]
    wait_done(client, job_id)
    saved = client.post("/history", json={"job_id": job_id, "title": "small", "notes": "check"}).json()
    assert saved["title"] == "small" and saved["summary"]["LCM"]["cost"] == 225
    assert client.get("/history").json()[0]["id"] == saved["id"]
    full = client.get(f"/history/{saved['id']}").json()
    assert full["results"]["results"]["LP"]["cost"] == 225
    assert client.delete(f"/history/{saved['id']}").status_code == 204
    assert client.get(f"/history/{saved['id']}").status_code == 404
    assert client.delete(f"/history/{saved['id']}").status_code == 404
    assert client.post("/history", json={"job_id": "zzz"}).status_code == 422


def test_migrations_are_reversible(tmp_path):
    from alembic import command
    from alembic.config import Config
    from sqlalchemy import create_engine, inspect

    db = tmp_path / "m.db"
    history.migrate(db)
    cols = {c["name"] for c in inspect(create_engine(f"sqlite:///{db.as_posix()}")).get_columns("runs")}
    assert "notes" in cols
    cfg = Config()
    cfg.set_main_option("script_location", str(history.MIGRATIONS))
    cfg.set_main_option("sqlalchemy.url", f"sqlite:///{db.as_posix()}")
    command.downgrade(cfg, "0001")
    cols = {c["name"] for c in inspect(create_engine(f"sqlite:///{db.as_posix()}")).get_columns("runs")}
    assert "notes" not in cols and "results" in cols
    command.downgrade(cfg, "base")
    assert "runs" not in inspect(create_engine(f"sqlite:///{db.as_posix()}")).get_table_names()
    command.upgrade(cfg, "head")


def test_cors_allows_only_the_local_front_end(client):
    ok = client.options("/health", headers={"Origin": "http://127.0.0.1:3000", "Access-Control-Request-Method": "GET"})
    assert ok.headers.get("access-control-allow-origin") == "http://127.0.0.1:3000"
    bad = client.options("/health", headers={"Origin": "http://evil.example", "Access-Control-Request-Method": "GET"})
    assert "access-control-allow-origin" not in bad.headers
