"""Build the 2024 Kazakhstan wheat export scenarios from the recorded public inputs."""

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def distance_km(origin, destination):
    a, b = math.radians(origin["lat"]), math.radians(destination["lat"])
    dlat = b - a
    dlon = math.radians(destination["lon"] - origin["lon"])
    h = math.sin(dlat / 2) ** 2 + math.cos(a) * math.cos(b) * math.sin(dlon / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def apportion(total, weights):
    """Use integer largest remainders to preserve the scenario total."""
    weight_sum = sum(weights)
    divisions = [divmod(total * weight, weight_sum) for weight in weights]
    quantities = [q for q, _ in divisions]
    for index in sorted(range(len(weights)), key=lambda i: divisions[i][1], reverse=True)[: total - sum(quantities)]:
        quantities[index] += 1
    return quantities


def generate():
    evidence = json.loads((ROOT / "evidence.json").read_text(encoding="utf-8"))
    origins, markets = evidence["regions"], evidence["markets"]
    weights = [row["harvest_kg"] for row in origins]
    costs = [
        [
            round(3.2 + 0.011 * 1.23 * distance_km(origin, market) + market["handling_proxy_kzt_per_kg"], 2)
            for market in markets
        ]
        for origin in origins
    ]
    (ROOT / "instances").mkdir(exist_ok=True)
    catalog = []

    def add(identifier, name, date, event, supply, demand, cost, note, parent=None):
        rel = f"instances/{identifier}.json"
        save(ROOT / rel, {"supply": supply, "demand": demand, "cost": cost})
        total_supply, total_demand = sum(supply), sum(demand)
        catalog.append(
            {
                "id": identifier,
                "title": name,
                "file": rel,
                "date": date,
                "event": event,
                "parent": parent,
                "note": note,
                "warehouse_count": len(supply),
                "store_count": len(demand),
                "direction_count": len(supply) * len(demand),
                "supply_kg": total_supply,
                "demand_kg": total_demand,
                "uncovered_kg": max(0, total_demand - total_supply),
                "unused_stock_kg": max(0, total_supply - total_demand),
            }
        )

    annual = [row["export_2024_kg"] for row in markets]
    supply = apportion(sum(annual), weights)
    add(
        "year-2024",
        "Экспорт за 2024 год",
        "2024-12-31",
        "daily",
        supply,
        annual,
        costs,
        "Фактический экспорт по семи рынкам. Региональные квоты рассчитаны по долям урожая.",
    )
    february = [row["export_202402_kg"] for row in markets]
    add(
        "month-2024-02",
        "Экспорт за февраль 2024",
        "2024-02-29",
        "daily",
        apportion(sum(february), weights),
        february,
        costs,
        "Отчётные объёмы за февраль по тем же рынкам. Ноль означает отсутствие записи в выборке.",
    )
    largest = max(range(len(origins)), key=weights.__getitem__)
    shortage = supply.copy()
    shortage[largest] = round(shortage[largest] * 0.8)
    add(
        "stress-source",
        "Сокращение доступного объёма",
        "2024-12-31",
        "warehouse_outage",
        shortage,
        annual,
        costs,
        "Стресс-тест: экспортная квота Акмолинской области сокращена на 20%.",
        "year-2024",
    )
    demand = [round(kg * 1.15) if market["id"] == "UZB" else kg for market, kg in zip(markets, annual, strict=True)]
    add(
        "stress-demand",
        "Рост спроса в Узбекистане",
        "2024-12-31",
        "export_demand_plus_15_pct",
        supply,
        demand,
        costs,
        "Стресс-тест: плановый объём поставок в Узбекистан увеличен на 15%.",
        "year-2024",
    )
    tariffs = [
        [
            round(value * 1.25, 2) if market["id"] in {"CHN", "AZE"} else value
            for value, market in zip(row, markets, strict=True)
        ]
        for row in costs
    ]
    add(
        "stress-tariff",
        "Удорожание перевозки",
        "2024-12-31",
        "export_tariffs_plus_25_pct",
        supply,
        annual,
        tariffs,
        "Стресс-тест: модельные тарифы для Китая и Азербайджана увеличены на 25%.",
        "year-2024",
    )

    save(
        ROOT / "network.json",
        {
            "coordinate_system": "WGS84",
            "districts": [{"id": market["id"], "name": market["name"]} for market in markets],
            "warehouses": origins,
            "stores": [{**market, "district": market["id"]} for market in markets],
        },
    )
    save(
        ROOT / "manifest.json",
        {
            "id": "kazakh-wheat-2024",
            "data_kind": "public_volumes_with_modeled_transport",
            "commodity": "wheat_and_meslin",
            "city": "Казахстан",
            "units": {"supply": "kg", "demand": "kg", "cost": "KZT/kg"},
            "display": {
                "title": "Экспорт пшеницы",
                "place": "Казахстан",
                "commodity": "Пшеница и меслин",
                "badge": "Факт экспорта · модель перевозок",
                "source_label": "Регион",
                "destination_label": "Рынок",
                "source_plural": "Региональные узлы",
                "destination_plural": "Экспортные рынки",
                "mass_unit": "т",
            },
            "sources": evidence["sources"],
            "network": "network.json",
            "scenarios": catalog,
        },
    )


if __name__ == "__main__":
    generate()
