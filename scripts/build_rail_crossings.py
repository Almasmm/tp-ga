"""Trace station-to-station connections along OSM railway edges, not straight lines."""

import heapq
import json
import math
import xml.etree.ElementTree as ET
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen

API = "https://api.openstreetmap.org/api/0.6/"
CHINA = "https://www.gov.kz/org/mfa-beijing/activities/2110?lang=ru"
WHEAT = "https://ktzh-gp.kz/en/media/news/news_main_section_ru/25333/"
CROSSINGS = [
    ("dostyk", "Китай", ("Достык", 4025083258), ("Алашанькоу", 243517635), (82.44, 45.145, 82.60, 45.28), CHINA, WHEAT),
    (
        "altynkol",
        "Китай",
        ("Алтынколь", 4046956026),
        ("Хоргос", 6316474613),
        (80.27, 44.12, 80.48, 44.19),
        CHINA,
        WHEAT,
    ),
    (
        "saryagash",
        "Узбекистан",
        ("Сарыагаш", 4041813395),
        ("Келес", 2201442488),
        (69.13, 41.395, 69.22, 41.478),
        "https://kgd.gov.kz/sites/default/files/files_framework/soglashenie_zk_s_ruz_rus.pdf",
        None,
    ),
]


def read(path):
    with urlopen(Request(API + path, headers={"User-Agent": "TPGA Rail Research/1.0"}), timeout=35) as response:
        return ET.fromstring(response.read())


def length(a, b):
    return 111.195 * math.hypot((a[0] - b[0]) * math.cos(math.radians((a[1] + b[1]) / 2)), a[1] - b[1])


def crossing(config):
    slug, country, start, end, bounds, source, shipment = config
    west, south, east, north = bounds
    step = 0.020 if slug == "saryagash" else 0.045
    nx, ny = math.ceil((east - west) / step), math.ceil((north - south) / step)
    for_grid = [
        (
            west + (east - west) * i / nx,
            south + (north - south) * j / ny,
            west + (east - west) * (i + 1) / nx,
            south + (north - south) * (j + 1) / ny,
        )
        for i in range(nx)
        for j in range(ny)
    ]
    paths = ["map?bbox=" + ",".join(f"{x:.6f}" for x in b) for b in for_grid]
    with ThreadPoolExecutor(max_workers=3) as pool:
        tiles = list(pool.map(read, paths))
    points, ways = {}, {}
    for tile in tiles:
        for node in tile.findall("node"):
            points[int(node.attrib["id"])] = (float(node.attrib["lon"]), float(node.attrib["lat"]))
        for way in tile.findall("way"):
            tags = {tag.attrib["k"]: tag.attrib["v"] for tag in way.findall("tag")}
            if tags.get("railway") == "rail":
                ways[int(way.attrib["id"])] = [int(n.attrib["ref"]) for n in way.findall("nd")]
    graph = defaultdict(list)
    for nodes in ways.values():
        for a, b in zip(nodes, nodes[1:], strict=False):
            if a not in points or b not in points:
                continue
            distance = length(points[a], points[b])
            graph[a].append((b, distance))
            graph[b].append((a, distance))

    def snap(station):
        _, station_id = station
        p = points[station_id]
        nearest = min(graph, key=lambda n: length(points[n], p))
        if length(points[nearest], p) > 0.5:
            raise ValueError(f"{slug}: station more than 500 m from the mapped rail")
        return nearest

    a, b = snap(start), snap(end)
    queue = [(0.0, a)]
    predecessor, distances = {}, {a: 0.0}
    while queue:
        distance, u = heapq.heappop(queue)
        if distance > distances[u]:
            continue
        if u == b:
            break
        for v, weight in graph[u]:
            candidate = distance + weight
            if candidate < distances.get(v, math.inf):
                distances[v] = candidate
                predecessor[v] = u
                heapq.heappush(queue, (candidate, v))
    if b not in distances or distances[b] < 1 or distances[b] > 2 * length(points[a], points[b]):
        raise ValueError(f"{slug}: no plausible continuous track")
    nodes = [b]
    while nodes[-1] != a:
        nodes.append(predecessor[nodes[-1]])
    print(f"{slug}: {len(nodes)} nodes, {distances[b]:.2f} mapped km", flush=True)
    return {
        "type": "Feature",
        "properties": {
            "id": slug,
            "country": country,
            "stations": [start[0], end[0]],
            "station_osm_ids": [start[1], end[1]],
            "source": source,
            "shipment": shipment,
        },
        "geometry": {"type": "LineString", "coordinates": [points[n] for n in reversed(nodes)]},
    }


if __name__ == "__main__":
    features = [crossing(config) for config in CROSSINGS]
    output = Path(__file__).resolve().parents[1] / "platform/web/public/maps/rail-crossings.json"
    data = json.dumps({"type": "FeatureCollection", "features": features}, ensure_ascii=False)
    output.write_text(data + "\n", encoding="utf-8")
