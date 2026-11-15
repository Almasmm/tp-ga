import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_full_scenario_comparison_accounts_for_unserved_demand():
    catalog = client.get("/scenarios").json()
    scenario = next(item for item in catalog["scenarios"] if item["id"] == "stress-warehouse-outage")
    assert scenario["direction_count"] == 7_776
    response = client.post(
        "/scenarios/stress-warehouse-outage/plan",
        json={"compare": True, "population": 8, "generations": 5, "seed": 42},
    )
    assert response.status_code == 200
    data = response.json()
    for plan in (data["lp"], data["ga"]):
        assert len(plan["warehouses"]) == 24
        assert len(plan["stores"]) == 324
        assert plan["deficit_kg"] == 3_201
        assert sum(row["deficit_kg"] for row in plan["stores"]) == 3_201
        assert sum(row["kg"] for row in plan["shipments"]) == scenario["supply_kg"]
        assert plan["cost_kzt"] == pytest.approx(sum(row["cost_kzt"] for row in plan["shipments"]))
    assert data["ga"]["cost_kzt"] >= data["lp"]["cost_kzt"]
    assert data["ga"]["history"][-1] == pytest.approx(data["ga"]["cost_kzt"])
    assert len(data["ga"]["history"]) == 6


def test_unknown_scenario_and_out_of_range_experiment_are_rejected():
    assert client.post("/scenarios/unknown/plan", json={}).status_code == 404
    assert client.post("/scenarios/day-01/plan", json={"compare": True, "seed": -1}).status_code == 422
