import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_wheat_case_preserves_trade_volumes_and_comparison_budget():
    catalog = client.get("/scenarios", params={"dataset_id": "kazakh-wheat"}).json()
    assert catalog["network"]["coordinate_system"] == "WGS84"
    assert catalog["scenarios"][0]["demand_kg"] == 5_607_981_400
    assert catalog["scenarios"][1]["demand_kg"] == 481_507_500
    response = client.post(
        "/scenarios/year-2024/plan",
        params={"dataset_id": "kazakh-wheat"},
        json={"compare": True, "population": 8, "generations": 5, "seed": 42},
    )
    assert response.status_code == 200
    data = response.json()
    for key in ("lp", "ga_before", "ga"):
        assert data[key]["delivered_kg"] == pytest.approx(5_607_981_400)
        assert data[key]["deficit_kg"] == pytest.approx(0)
    assert data["ga_before"]["initialization"] == "random"
    assert data["ga"]["initialization"] == "cost-aware"
    assert data["ga"]["evaluations"] == data["ga_before"]["evaluations"] == 48


@pytest.mark.parametrize(("dataset", "scenarios", "runs"), [("astana-potato", 33, 198), ("kazakh-wheat", 5, 30)])
def test_packaged_benchmark_covers_every_full_scenario(dataset, scenarios, runs):
    params = {"dataset_id": dataset}
    catalog = client.get("/scenarios", params=params).json()
    summary = client.get("/scenarios/benchmark", params=params).json()
    assert {row["id"] for row in summary["scenarios"]} == {
        row["id"] for row in catalog["scenarios"] if row["event"] != "api_subset"
    }
    assert summary["summary"]["scenarios"] == scenarios
    assert summary["summary"]["runs"] == runs
