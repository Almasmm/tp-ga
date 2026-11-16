"""Build the Astana potato transport benchmark with the Python standard library."""

import argparse
import json
import math
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 20261109
START = date(2026, 10, 1)
DISTRICTS = (
    # ID, name, public pavilion count, simulated local center in km.
    ("alm", "Алматы", 82, (6, 0)),
    ("bai", "Байконыр", 66, (0, 6)),
    ("esi", "Есиль", 35, (1, -6)),
    ("nur", "Нура", 24, (-6, -4)),
    ("sar", "Сарайшык", 11, (7, -5)),
    ("sry", "Сарыарка", 106, (-5, 3)),
)
WEEKDAY_FACTORS = (0.90, 0.92, 0.95, 0.98, 1.10, 1.22, 1.13)


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def distribute(total, weights):
    """Allocate integer kilograms proportionally, preserving the total."""
    weight_sum = sum(weights)
    quotas = [total * weight / weight_sum for weight in weights]
    values = [int(quota) for quota in quotas]
    order = sorted(range(len(values)), key=lambda i: quotas[i] - values[i], reverse=True)
    for i in order[: total - sum(values)]:
        values[i] += 1
    return values


def make_network(rng):
    warehouses, stores = [], []
    for district, _, count, center in DISTRICTS:
        for index in range(1, 5):
            x, y = (round(value * 1.45 + rng.uniform(-2.5, 2.5), 3) for value in center)
            warehouses.append({"id": f"W-{district}-{index:02}", "district": district, "x_km": x, "y_km": y})
        for index in range(1, count + 1):
            x, y = (round(value + rng.uniform(-2.2, 2.2), 3) for value in center)
            stores.append({"id": f"S-{district}-{index:03}", "district": district, "x_km": x, "y_km": y})
    return warehouses, stores


def make_tariffs(rng, warehouses, stores):
    tariffs = []
    for warehouse in warehouses:
        handling = rng.uniform(4.0, 7.0)
        rate = rng.uniform(0.34, 0.57)
        row = []
        for store in stores:
            distance = math.hypot(warehouse["x_km"] - store["x_km"], warehouse["y_km"] - store["y_km"])
            modeled_km = 1.25 * distance + 0.8
            row.append(handling + rate * modeled_km + rng.uniform(0, 0.8))
        tariffs.append(row)
    return tariffs


def generate(root):
    rng = random.Random(SEED)
    instances = root / "instances"
    instances.mkdir(parents=True, exist_ok=True)
    warehouses, stores = make_network(rng)
    base_tariffs = make_tariffs(rng, warehouses, stores)
    size_ranges = rng.choices(((55, 115), (115, 225), (225, 420)), weights=(44, 41, 15), k=len(stores))
    store_sizes = [rng.randint(low, high) for low, high in size_ranges]
    warehouse_sizes = [rng.uniform(0.60, 1.50) for _ in warehouses]
    scenarios = []

    def add_instance(name, day, event, supply, demand, cost, parent=None):
        # Keep one matrix row per line so the JSON stays compact.
        matrix = ",\n".join("    " + json.dumps(row) for row in cost)
        payload = (
            f'{{\n  "supply": {json.dumps(supply)},\n  "demand": {json.dumps(demand)},\n'
            f'  "cost": [\n{matrix}\n  ]\n}}\n'
        )
        relative = f"instances/{name}.json"
        (root / relative).write_text(payload, encoding="utf-8", newline="\n")
        available, requested = sum(supply), sum(demand)
        scenarios.append(
            {
                "id": name,
                "file": relative,
                "date": day.isoformat(),
                "event": event,
                "parent": parent,
                "supply_kg": available,
                "demand_kg": requested,
                "uncovered_kg": max(0, requested - available),
                "unused_stock_kg": max(0, available - requested),
                "warehouse_count": len(supply),
                "store_count": len(demand),
                "direction_count": len(supply) * len(demand),
            }
        )

    for offset in range(30):
        day = START + timedelta(days=offset)
        day_factor = WEEKDAY_FACTORS[day.weekday()] * rng.uniform(0.94, 1.06)
        demand = [round(size * day_factor * rng.uniform(0.84, 1.16)) for size in store_sizes]
        if offset in {0, 14, 29}:
            supply_factor = 1.0
        elif offset in {5, 11, 19, 25}:
            supply_factor = rng.uniform(0.87, 0.96)
        else:
            supply_factor = rng.uniform(1.04, 1.17)
        weights = [size * rng.uniform(0.80, 1.20) for size in warehouse_sizes]
        supply = distribute(round(sum(demand) * supply_factor), weights)
        tariff_factor = rng.uniform(0.97, 1.03)
        cost = [[round(value * tariff_factor, 2) for value in row] for row in base_tariffs]
        base_name = f"day-{offset + 1:02}"
        add_instance(base_name, day, "daily", supply, demand, cost)

        if offset == 0:
            outage_supply = supply.copy()
            outage_warehouse = max(range(len(supply)), key=supply.__getitem__)
            outage_supply[outage_warehouse] = 0
            add_instance("stress-warehouse-outage", day, "warehouse_outage", outage_supply, demand, cost, base_name)
            peak_demand = [
                round(quantity * 1.35) if store["district"] == "sry" else quantity
                for store, quantity in zip(stores, demand, strict=True)
            ]
            add_instance(
                "stress-district-demand", day, "district_demand_plus_35_pct", supply, peak_demand, cost, base_name
            )
            higher_cost = []
            for warehouse, row in zip(warehouses, cost, strict=True):
                affected = {"esi", "nur"} - {warehouse["district"]}
                higher_cost.append(
                    [
                        round(value * 1.30, 2) if store["district"] in affected else value
                        for value, store in zip(row, stores, strict=True)
                    ]
                )
            add_instance(
                "stress-district-tariffs", day, "incoming_tariffs_plus_30_pct", supply, demand, higher_cost, base_name
            )

            wi = list(range(0, len(warehouses), 3))
            si = [i * len(stores) // 40 for i in range(40)]
            pilot_demand = [demand[i] for i in si]
            pilot_supply = distribute(sum(pilot_demand), [supply[i] for i in wi])
            pilot_cost = [[cost[i][j] for j in si] for i in wi]
            add_instance("pilot", day, "api_subset", pilot_supply, pilot_demand, pilot_cost, base_name)
            scenarios[-1]["warehouse_ids"] = [warehouses[i]["id"] for i in wi]
            scenarios[-1]["store_ids"] = [stores[i]["id"] for i in si]

    write_json(
        root / "network.json",
        {
            "coordinate_system": "simulated_local_grid_km",
            "districts": [
                {"id": code, "name": name, "published_pavilion_count": count} for code, name, count, _ in DISTRICTS
            ],
            "warehouses": warehouses,
            "stores": stores,
        },
    )
    write_json(
        root / "manifest.json",
        {
            "id": "astana-potato-v1",
            "data_kind": "synthetic_benchmark_with_public_context",
            "commodity": "potato",
            "city": "Astana",
            "seed": SEED,
            "units": {"supply": "kg", "demand": "kg", "cost": "KZT/kg"},
            "sources": [
                {
                    "url": "https://www.gov.kz/org/astana/press/article/details/247537",
                    "use": "District counts of all pavilion categories, used to size the simulated network.",
                },
                {
                    "url": "https://www.gov.kz/org/astana/press/news/details/921167?lang=ru",
                    "use": "Historical potato contract context, not a numerical input to the scenarios.",
                },
            ],
            "network": "network.json",
            "scenarios": scenarios,
        },
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent)
    generate(parser.parse_args().output)
