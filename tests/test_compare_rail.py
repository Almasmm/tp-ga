"""The reconciliation keeps flows feasible and distinguishes planning from billing."""

import pytest
from scripts.compare_rail import compare


@pytest.fixture
def data():
    dates = {"valid_from": "2025-06-01", "valid_to": "2025-06-30"}
    origin, destination = "123456", "654321"
    sources = {"rate_source": "control rate", "capacity_source": "control capacity"}
    return {
        "cohort": {
            "from": dates["valid_from"],
            "to": dates["valid_to"],
            "currency": "KZT",
            "hs4": "1001",
            "equipment": "control equipment",
            "charge_scope": "control charge scope",
            "vat": "excluded",
            "actual_source": "control invoices",
        },
        "shipments": [
            {
                "id": "s1",
                "date": "2025-06-06",
                "lane": "paid",
                "origin": origin,
                "destination": destination,
                "tonnes": 120,
                "paid_kzt": 14000,
            }
        ],
        "lanes": [
            {
                "id": "paid",
                "origin": origin,
                "destination": destination,
                "gateway": "g1",
                "kzt_per_tonne": 100,
                "capacity_tonnes": 140,
                **dates,
                **sources,
            },
            {
                "id": "alternative-a",
                "origin": origin,
                "destination": destination,
                "gateway": "g2",
                "kzt_per_tonne": 60,
                "capacity_tonnes": 45,
                **dates,
                **sources,
            },
            {
                "id": "alternative-b",
                "origin": origin,
                "destination": destination,
                "gateway": "g2",
                "kzt_per_tonne": 60,
                "capacity_tonnes": 45,
                **dates,
                **sources,
            },
        ],
        "gateways": [
            {"id": "g1", "capacity_tonnes": 140, "capacity_source": "control capacity"},
            {"id": "g2", "capacity_tonnes": 50, "capacity_source": "control capacity"},
        ],
    }


def test_shared_gateway_limit_and_cost_decomposition(data):
    result = compare(data)
    assert result["tonnes"] == 120
    assert sum(row["tonnes"] for row in result["plan"] if row["gateway"] == "g2") == 50
    assert result["actual_paid_kzt"] == 14000
    assert result["actual_repriced_kzt"] == 12000
    assert result["optimized_kzt"] == 10000
    assert result["planning_savings_kzt"] == 2000
    assert result["modeled_difference_vs_paid_kzt"] == 4000


def test_rejects_tariffs_that_changed_during_period(data):
    data["lanes"][1]["valid_from"] = "2025-06-15"
    with pytest.raises(ValueError, match="ставка должна покрывать весь период"):
        compare(data)


def test_rejects_baseline_that_exceeds_capacity(data):
    data["gateways"][0]["capacity_tonnes"] = 100
    with pytest.raises(ValueError, match="лимит перехода ниже фактического объёма"):
        compare(data)
