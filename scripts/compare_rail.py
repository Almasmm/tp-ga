"""Compare anonymized paid shipments and a capacity-constrained counterfactual."""

import argparse
import json
import math
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

from scipy.optimize import linprog


def required_text(obj, key):
    value = obj[key]
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key}: требуется непустая строка")
    return value.strip()


def positive(obj, key):
    value = obj[key]
    if type(value) not in (int, float) or not math.isfinite(value) or value <= 0:
        raise ValueError(f"{key}: требуется конечное число больше нуля")
    return value


def station(obj, key):
    value = required_text(obj, key)
    if not re.fullmatch(r"[0-9]{5,6}", value):
        raise ValueError(f"{key}: требуется код станции из 5 или 6 цифр")
    return value


def group(rows, key):
    totals = defaultdict(float)
    for row in rows:
        totals[row[key]] += row["tonnes"]
    return totals


def compare(data):
    meta = data["cohort"]
    start = date.fromisoformat(meta["from"])
    end = date.fromisoformat(meta["to"])
    if start > end:
        raise ValueError("Некорректный период")
    if meta["currency"] != "KZT" or meta["hs4"] != "1001":
        raise ValueError("Требуются расходы в KZT и код ТН ВЭД 1001")
    for key in ("equipment", "charge_scope", "actual_source"):
        required_text(meta, key)
    if meta["vat"] not in ("included", "excluded"):
        raise ValueError("Укажите единый подход к НДС: included или excluded")
    shipments = data["shipments"]
    lanes = data["lanes"]
    if not shipments or not lanes:
        raise ValueError("Нужны оплаченные отправки и сопоставимые ставки по маршрутам")
    gates = data["gateways"]
    limits = {}
    for gate in gates:
        key = required_text(gate, "id")
        if key in limits:
            raise ValueError(f"Дублируется переход {key}")
        required_text(gate, "capacity_source")
        limits[key] = positive(gate, "capacity_tonnes")
    tariff = {}
    for lane in lanes:
        key = required_text(lane, "id")
        if key in tariff:
            raise ValueError(f"Дублируется маршрут {key}")
        station(lane, "origin")
        station(lane, "destination")
        gateway = required_text(lane, "gateway")
        if gateway not in limits:
            raise ValueError(f"{key}: нет лимита перехода {gateway}")
        for field in ("rate_source", "capacity_source"):
            required_text(lane, field)
        if date.fromisoformat(lane["valid_from"]) > start or date.fromisoformat(lane["valid_to"]) < end:
            raise ValueError(f"{key}: ставка должна покрывать весь период расчёта")
        positive(lane, "kzt_per_tonne")
        positive(lane, "capacity_tonnes")
        tariff[key] = lane

    seen, observed_lanes, rows = set(), defaultdict(float), []
    paid, repriced = 0.0, 0.0
    for shipment in shipments:
        key = required_text(shipment, "id")
        if key in seen:
            raise ValueError(f"Дублируется отправка {key}")
        seen.add(key)
        if not start <= date.fromisoformat(shipment["date"]) <= end:
            raise ValueError(f"{key}: отправка вне периода")
        lane_id = required_text(shipment, "lane")
        if lane_id not in tariff:
            raise ValueError(f"{key}: отсутствует ставка для фактического маршрута {lane_id}")
        lane = tariff[lane_id]
        origin, destination = station(shipment, "origin"), station(shipment, "destination")
        if (origin, destination) != (lane["origin"], lane["destination"]):
            raise ValueError(f"{key}: станции отправки и маршрута различаются")
        tonnes = positive(shipment, "tonnes")
        observed_lanes[lane_id] += tonnes
        paid += positive(shipment, "paid_kzt")
        repriced += tonnes * lane["kzt_per_tonne"]
        rows.append({"origin": origin, "destination": destination, "tonnes": tonnes})
    observed_gates = defaultdict(float)
    for lane_id, tonnes in observed_lanes.items():
        lane = tariff[lane_id]
        if tonnes > lane["capacity_tonnes"] + 1e-6:
            raise ValueError(f"{lane_id}: лимит маршрута ниже фактического объёма")
        observed_gates[lane["gateway"]] += tonnes
    for gateway, tonnes in observed_gates.items():
        if tonnes > limits[gateway] + 1e-6:
            raise ValueError(f"{gateway}: лимит перехода ниже фактического объёма")

    supply, demand = group(rows, "origin"), group(rows, "destination")
    candidates = [lane for lane in lanes if lane["origin"] in supply and lane["destination"] in demand]
    balance_rows = [
        (field, k, v) for field, totals in (("origin", supply), ("destination", demand)) for k, v in totals.items()
    ]
    result = linprog(
        [lane["kzt_per_tonne"] for lane in candidates],
        A_eq=[[int(lane[field] == key) for lane in candidates] for field, key, _ in balance_rows],
        b_eq=[value for _, _, value in balance_rows],
        A_ub=[[int(lane["gateway"] == gate) for lane in candidates] for gate in limits],
        b_ub=list(limits.values()),
        bounds=[(0, lane["capacity_tonnes"]) for lane in candidates],
        method="highs",
    )
    if not result.success:
        raise ValueError(f"Не удалось построить допустимый план: {result.message}")
    optimized = float(result.fun)
    if optimized > repriced + max(0.01, 1e-8 * repriced):
        raise ValueError("Результат дороже допустимого факта при тех же ставках")
    return {
        "cohort": meta,
        "shipment_count": len(rows),
        "tonnes": round(sum(supply.values()), 6),
        "actual_paid_kzt": round(paid, 2),
        "actual_repriced_kzt": round(repriced, 2),
        "optimized_kzt": round(optimized, 2),
        "planning_savings_kzt": round(repriced - optimized, 2),
        "planning_savings_pct": round((repriced - optimized) * 100 / repriced, 4),
        "modeled_difference_vs_paid_kzt": round(paid - optimized, 2),
        "paid_minus_repriced_kzt": round(paid - repriced, 2),
        "plan": [
            {
                "lane": lane["id"],
                "origin": lane["origin"],
                "destination": lane["destination"],
                "gateway": lane["gateway"],
                "tonnes": round(float(tonnes), 6),
            }
            for lane, tonnes in zip(candidates, result.x, strict=True)
            if tonnes > 1e-7
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8-sig"))
        print(json.dumps(compare(data), ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, f"Ошибка входных данных: {error}\n")


if __name__ == "__main__":
    main()
