"""Tables and figures for the second-review experiments."""

import argparse
import csv
import hashlib
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path
from urllib.request import urlopen

import numpy as np

from tpga.experiments.reporting.stats import paired
from tpga.experiments.v3 import core, rev
from tpga.experiments.v3.review2 import REVIEW, ROOT, records

SRC = ROOT.parent
LINEAR = SRC / "linear/raw/runs.jsonl"
REVIEW_RAW = SRC / "review/raw"
FCTP = SRC / "fctp/raw"
KEY_FIELDS = ("set", "size", "rho", "instance", "method", "seed", "budget", "evals", "time_s", "cost")


def read_csv(path):
    with Path(path).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def table(name, rows, title=None):
    if not rows:
        return
    target = ROOT / "tables" / name
    target.parent.mkdir(parents=True, exist_ok=True)
    fields = list(dict.fromkeys(k for row in rows for k in row))
    with target.with_suffix(".csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(
            {
                key: None if isinstance(value, float) and not math.isfinite(value) else value
                for key, value in row.items()
            }
            for row in rows
        )

    def cell(value):
        if value is None:
            return ""
        if isinstance(value, float):
            return f"{value:.9g}" if math.isfinite(value) else ""
        return str(value).replace("|", r"\|").replace("\n", " ")

    def line(items):
        return "| " + " | ".join(cell(v) for v in items) + " |"

    content = [f"# {title or name}", "", line(fields), line(["---"] * len(fields))]
    content.extend(line(row.get(k) for k in fields) for row in rows)
    target.with_suffix(".md").write_text("\n".join(content) + "\n", encoding="utf-8", newline="\n")


def groups(rows, *columns):
    buckets = defaultdict(list)
    for row in rows:
        buckets[tuple(row.get(c) for c in columns)].append(row)
    return sorted(buckets.items(), key=lambda item: tuple("" if v is None else str(v) for v in item[0]))


def med(rows, field):
    values = [r[field] for r in rows if r.get(field) is not None]
    return statistics.median(values) if values else None


def gap(cost, reference):
    return 100 * (cost - reference) / reference if cost is not None and reference else None


def measured(row, source, name=None):
    count = row.get("evals")
    unit = row.get("evaluation_unit")
    if unit is None:
        if row.get("kind") in ("tabu", "ils"):
            unit = "start + neighbour"
        elif row.get("local_search_evaluations"):
            unit = "decoder + local search"
        elif count is not None:
            unit = "decoder"
        elif row.get("kind") in ("balinski", "classical", "vam_lin"):
            unit, count = "complete objective", 1
    return {**row, "source": str(source.as_posix()), "method": name or row["method"], "evals": count, "unit": unit}


def read_runs(path, name=None):
    return [measured(r, path, name) for r in records(path)]


def by_instance(rows, names, fields):
    return [
        {
            **dict(zip(names, group, strict=True)),
            "runs": len(members),
            **{field: med(members, field) for field in fields},
        }
        for group, members in groups(rows, *names)
    ]


def pairing(rows, pairs, scope, value, expected):
    result = []
    for values, cell in groups(rows, *scope):
        methods = {}
        for r in cell:
            if r.get(value) is not None:
                methods.setdefault(r["method"], {}).setdefault(r["instance"], {})[r["seed"]] = r[value]
        for x, y in pairs:
            a, b = methods.get(x, {}), methods.get(y, {})
            left, right, ids = [], [], []
            for instance in sorted(a.keys() & b.keys()):
                # Classical comparators have one deterministic row for all seeds.
                shared = a[instance].keys() & b[instance].keys()
                if not shared and None in a[instance]:
                    shared = b[instance].keys()
                if not shared and None in b[instance]:
                    shared = a[instance].keys()
                if not shared:
                    continue
                left.append(statistics.median(a[instance].get(seed, a[instance].get(None)) for seed in shared))
                right.append(statistics.median(b[instance].get(seed, b[instance].get(None)) for seed in shared))
                ids.append(instance)
            common = {
                **dict(zip(scope, values, strict=True)),
                "first": x,
                "second": y,
                "instances_expected": expected,
                "instances_used": len(ids),
                "instances": " ".join(ids),
            }
            if ids:
                p = np.asarray(left, dtype=float)
                q = np.asarray(right, dtype=float)
                tied = np.isclose(p, q, atol=1e-9, rtol=1e-9)
                stats = paired(p, np.where(tied, p, q))
                result.append(
                    {**common, "first_median": float(np.median(p)), "second_median": float(np.median(q)), **stats}
                )
            else:
                result.append(common)
    return result


def fctp_report():
    k1 = read_runs(ROOT / "raw/K1.jsonl")
    k1 += [
        r
        for r in read_runs(REVIEW_RAW / "rivals.jsonl")
        if r["m"] in (20, 30, 50, 70) and r["method"] in ("Tabu", "ILS")
    ]
    archived = []
    for source in ("runs", "runs_ft", "large"):
        archived.extend(read_runs(FCTP / f"{source}.jsonl"))
    archived.extend(read_runs(REVIEW_RAW / "rivals.jsonl"))
    mips = []
    for source in ("mip", "large_mip", "mip_time"):
        for row in read_runs(FCTP / f"{source}.jsonl"):
            row["time_limit_s"] = row.get("time_limit_s") or (60 if source != "mip_time" else None)
            row["method"] = "MIP, GA time" if source == "mip_time" else "MIP, 1 thread / 60 s"
            mips.append(row)
    mips.extend(read_runs(REVIEW_RAW / "mip_default.jsonl", "MIP, default threads / 300 s"))
    timing_refs = [r for r in mips if r["method"] == "MIP, GA time"]
    timing_refs.extend(read_runs(REVIEW_RAW / "timing_mip.jsonl", "MIP, one CPU / GA time"))
    mips = [r for r in mips if r["method"] != "MIP, GA time"]
    refs = {}
    for (instance,), rr in groups(archived + mips + timing_refs + k1, "instance"):
        valid_mip = [r for r in rr if r["kind"] == "mip" and r.get("bound") is not None]
        costs = [r["cost"] for r in rr if r.get("cost") is not None]
        if not costs:
            continue
        z = min(costs)
        bound = max((r["bound"] for r in valid_mip if r["bound"] <= z + 1e-6), default=None)
        refs[instance] = {
            "size": rr[0]["size"],
            "rho": rr[0]["rho"],
            "instance": instance,
            "z_best": z,
            "lower_bound": bound,
            "gap_best_to_bound_pct": gap(z, bound),
            "proved": any(r.get("proved") and r["cost"] is not None and abs(r["cost"] - z) <= 1e-6 for r in valid_mip),
            "mip_available": bound is not None,
        }

    def detail(row):
        ref = refs[row["instance"]]
        fields = {
            k: row.get(k)
            for k in (
                *KEY_FIELDS,
                "unit",
                "source",
                "config",
                "time_limit_s",
                "nodes",
                "pivots",
                "zero_pivots",
                "full_evaluations",
                "neighbour_evaluations",
                "local_search_evaluations",
            )
        }
        if row["kind"] in ("independent", "population"):
            fields["config"] = f"{row['kind']}, P={row['population']}, r=4, OX={row['ox_rate']:.8g}"
        return {
            **fields,
            "z_best": ref["z_best"],
            "lower_bound": ref["lower_bound"],
            "gap_best_pct": gap(row.get("cost"), ref["z_best"]),
            "gap_bound_pct": gap(row.get("cost"), ref["lower_bound"]),
        }

    k1_details = [detail(r) for r in k1]
    table("K1_runs", k1_details, "K1 run-level costs and effort")
    fields = ("gap_best_pct", "cost", "budget", "evals", "time_s")
    k1_by = by_instance(k1_details, ("size", "rho", "method", "instance"), fields)
    table("K1_instances", k1_by)
    table("K1_cells", by_instance(k1_by, ("size", "rho", "method"), fields))
    pairs = [
        (x, y)
        for p in (30, 300)
        for x, y in (
            ("a", f"b{p}"),
            (f"b{p}", f"c{p}"),
            (f"c{p}", f"d{p}"),
            (f"d{p}", "GA-cost-cycle"),
        )
    ] + [("a", "ILS"), ("a", "Tabu")]
    table("K1_pairs", pairing(k1_details, pairs, ("size", "rho"), "gap_best_pct", 5))
    table("K1_pairs_pooled", pairing(k1_details, pairs, (), "gap_best_pct", 40))
    table("K7_reference_instances", list(refs.values()))
    cell_refs = []
    for (size, rho), rr in groups(list(refs.values()), "size", "rho"):
        solver_rows = [r for r in mips if r["size"] == size and r["rho"] == rho]
        single = [r for r in solver_rows if r["method"] == "MIP, 1 thread / 60 s"]
        default = [r for r in solver_rows if r["method"] == "MIP, default threads / 300 s"]
        cell_refs.append(
            {
                "size": size,
                "rho": rho,
                "instances": len(rr),
                "proved": sum(r["proved"] for r in rr),
                "bound_available": sum(r["mip_available"] for r in rr),
                "mip_60s_instances": len(single),
                "mip_60s_proved": sum(r["proved"] for r in single),
                "mip_300s_instances": len(default),
                "mip_300s_proved": sum(r["proved"] for r in default),
                "median_lower_bound": med(rr, "lower_bound"),
                "median_z_best": med(rr, "z_best"),
                "median_gap_best_to_bound_pct": med(rr, "gap_best_to_bound_pct"),
            }
        )
    table("K7_reference_cells", cell_refs)
    # K1 ILS and Tabu are already in the archived rivals records.
    all_details = [
        detail(r)
        for r in archived + mips + [r for r in k1 if r["method"] not in ("ILS", "Tabu")]
        if r["instance"] in refs
    ]
    table("K7_runs", all_details)
    fields = ("gap_best_pct", "gap_bound_pct", "cost", "budget", "evals", "time_s", "time_limit_s", "nodes")
    by = by_instance(all_details, ("size", "rho", "method", "source", "config", "unit", "instance"), fields)
    table("K7_methods_by_cell", by_instance(by, ("size", "rho", "method", "source", "config", "unit"), fields))
    return refs


def linear_report():
    archived = read_runs(LINEAR)
    k2 = read_runs(ROOT / "raw/K2.jsonl")
    k2 += [
        r
        for r in archived
        if r["set"] == "uniform"
        and r["m"] in (20, 30, 50)
        and r["method"] in ("GA-rand-tuned", "GA-cost-tuned", "GA-rand-cycle", "GA-cost-cycle")
    ]
    table(
        "K2_runs", [{k: r.get(k) for k in (*KEY_FIELDS, "config", "unit", "source", "gap", "start_cost")} for r in k2]
    )
    fields = ("gap", "budget", "evals", "time_s")
    k2_by = by_instance(k2, ("size", "method", "instance"), fields)
    table("K2_instances", k2_by)
    table("K2_cells", by_instance(k2_by, ("size", "method"), fields))
    pairs = []
    for start in ("rand", "cost"):
        names = [f"GA-{start}-{suffix}" for suffix in ("tuned", "cycle", "reencode-only", "reencode-after_swap")]
        pairs.extend((x, y) for i, x in enumerate(names) for y in names[i + 1 :])
    table("K2_pairs", pairing(k2, pairs, ("size",), "gap", 10))

    scope = ("set", "size", "method")
    fields = ("gap", "gap_norm", "budget", "evals", "time_s")
    by = by_instance(archived, (*scope, "instance"), fields)
    table("K6_instances", by)
    rng = np.random.default_rng(20261120)
    summary = by_instance(by, scope, fields)
    for row, (_, inst) in zip(summary, groups(by, *scope), strict=True):
        row["instances"] = row.pop("runs")
        for metric in ("gap", "gap_norm"):
            values = np.array([r[metric] for r in inst if r.get(metric) is not None], dtype=float)
            if values.size:
                samples = rng.choice(values, (10000, values.size))
                lo, hi = np.quantile(np.median(samples, axis=1), [0.025, 0.975])
                row[f"{metric}_low"], row[f"{metric}_high"] = float(lo), float(hi)
    table("K6_cells", summary)
    split = [
        {**r, "subset": "00–04" if int(r["instance"][-2:]) < 5 else "05–09"}
        for r in archived
        if r["set"] == "uniform" and r["m"] == 100
    ]
    table("K6_100x100_instances", by_instance(split, ("subset", "method", "instance"), fields))
    pairs = rev.lin_cfg(REVIEW).raw["pairs"]
    table("K6_100x100_pairs", pairing(split, pairs, ("subset",), "gap_norm", 5))

    k11 = [r for r in archived if r["size"] == "5x5" and r["set"] == "uniform" and r["method"] == "GA-cost-cycle"]
    table(
        "K11_runs",
        [
            {
                k: r.get(k)
                for k in (*KEY_FIELDS, "pivots", "zero_pivots", "generations", "stop_reason", "optimal", "source")
            }
            for r in k11
        ],
    )
    table(
        "K11_summary",
        [
            {
                "runs": len(k11),
                "instances": len({r["instance"] for r in k11}),
                "evaluations_per_run": med(k11, "evals"),
                "budget_per_run": med(k11, "budget"),
                "zero_pivot_runs": sum(r.get("pivots") == 0 for r in k11),
                "total_pivots": sum(r["pivots"] for r in k11),
                "total_generations": sum(r["generations"] for r in k11),
                "optimal_runs": sum(r["optimal"] for r in k11),
            }
        ],
    )
    return archived, summary


def diagnostics():
    measured_runs = read_runs(ROOT / "raw/K3.jsonl")
    ox, swaps = [], []
    for row in measured_runs:
        detail = {k: row.get(k) for k in (*KEY_FIELDS, "config", "start_cost", "source")}
        for tenth, counters in enumerate(row["ox"], 1):
            ox.append(
                {
                    **detail,
                    "tenth": tenth,
                    **dict(
                        zip(
                            ("ox", "first", "second", "either", "novel"),
                            counters,
                            strict=True,
                        )
                    ),
                }
            )
        for stage, data in row["snapshots"].items():
            swaps.append(
                {
                    **detail,
                    "stage": stage,
                    "snapshot_eval": data["evals"],
                    "draws": data["draws"],
                    **dict(
                        zip(
                            ("positive", "positive_neutral", "open_zero", "open_zero_neutral"),
                            data["counts"],
                            strict=True,
                        )
                    ),
                }
            )
    for row in ox:
        for metric in ("first", "second", "either", "novel"):
            row[metric + "_share"] = row[metric] / row["ox"] if row["ox"] else None
    for row in swaps:
        for metric in ("positive", "open_zero"):
            row[metric + "_share"] = row[metric + "_neutral"] / row[metric] if row[metric] else None
    table("K3_runs_by_tenth", ox)
    fields = ("ox", "first", "second", "either", "novel")
    summary = []
    for (size, method, tenth), rr in groups(ox, "size", "method", "tenth"):
        total = {k: sum(r[k] for r in rr) for k in fields}
        shares = {k + "_share": total[k] / total["ox"] if total["ox"] else None for k in fields[1:]}
        summary.append({"size": size, "method": method, "tenth": tenth, "runs": len(rr), **total, **shares})
    table("K3_by_tenth", summary)
    table("K4_runs", swaps)
    metrics = ("draws", "positive", "positive_neutral", "open_zero", "open_zero_neutral")
    totals = []
    for (size, method, stage), rr in groups(swaps, "size", "method", "stage"):
        t = {k: sum(r[k] for r in rr) for k in metrics}
        totals.append(
            {
                "size": size,
                "method": method,
                "stage": stage,
                "runs": len(rr),
                **t,
                **{k + "_share": t[k + "_neutral"] / t[k] if t[k] else None for k in ("positive", "open_zero")},
            }
        )
    table("K4_by_stage", totals)
    return summary


def starting_plans(archived, refs):
    import gzip
    import time

    from tpga import _xkernels
    from tpga.cycle import _fixed_array
    from tpga.decoder import decoder_eps
    from tpga.fctp import FixedChargeProblem
    from tpga.ga import _arrays
    from tpga.initialization import cost_aware_population
    from tpga.model import TransportProblem

    deadline = json.loads((ROOT / "session.json").read_text(encoding="utf-8"))["deadline_epoch"]
    cache_path = ROOT / "raw/K5_starts.jsonl"
    cache = {(r["instance"], r["method"], r["seed"]): r for r in records(cache_path)}
    source = Path("paper_artifacts/raw/convergence/main.csv.gz")
    base_points = {}
    with gzip.open(source, "rt", encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            if row["method"] == "GA-cost":
                key = (row["instance"], row["config"], row["seed"])
                if key not in base_points or int(row["evals"]) < int(base_points[key]["evals"]):
                    base_points[key] = row
    details = []
    for row in read_csv("paper_artifacts/raw/runs.csv"):
        if row["method"] != "GA-cost" or row["phase"] != "main":
            continue
        first = base_points.get((row["instance"], row["config"], row["seed"]))
        # A legacy run's first retained observation must be within its initial population.
        if first is None or not 0 < int(first["evals"]) <= int(row["population"]):
            continue
        details.append(
            {
                "set": row["suite"],
                "size": row["size"],
                "instance": row["instance"],
                "method": "GA-cost",
                "seed": int(row["seed"]),
                "config": row["config"],
                "budget": int(row["budget"]),
                "evals": int(row["evals"]),
                "time_s": float(row["time_s"]),
                "cost": float(row["cost"]),
                "start_cost": float(first["best_cost"]),
                "reference": float(row["z_star"]),
                "start_source": source.as_posix(),
            }
        )

    known = {}
    for name in ("K1", "K3"):
        for r in records(ROOT / "raw" / f"{name}.jsonl"):
            if r.get("start_cost") is not None:
                known[(r["instance"], r["method"], r["seed"])] = (r["start_cost"], name)
    lin = rev.lin_cfg(REVIEW)
    linear_cfg = {name: core.method_fields(lin, name) for name in ("GA-cost-tuned", "GA-cost-cycle")}
    standard_fctp = core.method_fields(rev.ext.base(rev.ext_cfg(REVIEW)), "GA-cost-cycle")
    large_fctp = rev.method(REVIEW, "GA-cost-cycle")
    fctp_rows = [
        r for p in (FCTP / "runs.jsonl", FCTP / "large.jsonl") for r in records(p) if r["method"] == "GA-cost-cycle"
    ]
    work = [r for r in archived if r["method"] in linear_cfg] + fctp_rows
    paths = {p.stem: p for p in (SRC / "linear/instances").rglob("*.json") if p.stem != "manifest"}
    fctp_paths = {
        p.stem: p
        for root in (SRC / "fctp/instances", SRC / "fctp/large/instances")
        for p in root.rglob("*.json")
        if p.stem != "manifest"
    }
    kernel = _xkernels.table()["_decode_cost_fc"]
    errors = []
    for row in work:
        lookup = (row["instance"], row["method"], row["seed"])
        is_fctp = row["problem"] == "fctp"
        previous = cache.get(lookup)
        # The K1 budget-fill execution keeps the same initial population as the large FCTP method.
        lookup_known = known.get(lookup)
        if is_fctp and row["config"] != large_fctp["config"]:
            lookup_known = None
        if previous is not None:
            value, start_source = previous["start_cost"], previous["start_source"]
        elif lookup_known is not None:
            value, block = lookup_known
            start_source = f"review2/raw/{block}.jsonl"
        else:
            if time.time() >= deadline:
                continue
            replay_started = time.perf_counter()
            if is_fctp:
                fcp = FixedChargeProblem.from_json(fctp_paths[row["instance"]])
                p, start, fixed = fcp.problem, fcp.linearised(), fcp.fixed
                fields = standard_fctp if row["config"] == standard_fctp["config"] else large_fctp
            else:
                p = TransportProblem.from_json(paths[row["instance"]])
                start, fixed = p, None
                fields = linear_cfg[row["method"]]
            m, n = p.shape
            config = fields["params"]
            pop = cost_aware_population(start, config["population"], np.random.default_rng(row["seed"]))
            supply, demand, cost, _ = _arrays(p)
            fx = _fixed_array(fixed, m, n)
            eps = decoder_eps(p)
            value = min(kernel(perm, supply, demand, cost, fx, n, eps) for perm in pop)
            start_source = "initial population replay"
            if value < row["cost"] - 1e-7:
                errors.append(
                    {
                        **dict(zip(("instance", "method", "seed"), lookup, strict=True)),
                        "start_cost": value,
                        "final": row["cost"],
                    }
                )
                continue
            from tpga.experiments.v3.review2 import write

            write(
                cache_path,
                {
                    "instance": row["instance"],
                    "method": row["method"],
                    "seed": row["seed"],
                    "start_cost": value,
                    "start_source": start_source,
                    "replay_time_s": time.perf_counter() - replay_started,
                },
            )
        reference = refs[row["instance"]]["z_best"] if is_fctp else row["z_star"]
        details.append(
            {
                **{k: row.get(k) for k in (*KEY_FIELDS, "config")},
                "start_cost": value,
                "reference": reference,
                "start_source": start_source,
            }
        )
    for row in details:
        row["start_gap_pct"] = gap(row["start_cost"], row["reference"])
        row["final_gap_pct"] = gap(row["cost"], row["reference"])
        row["gap_reduction_pp"] = row["start_gap_pct"] - row["final_gap_pct"]
        row["improved"] = row["cost"] < row["start_cost"] - 1e-7
        row["tie"] = abs(row["cost"] - row["start_cost"]) <= 1e-7
    table("K5_runs", details)
    scope = ("set", "size", "rho", "method")
    fields = ("start_gap_pct", "final_gap_pct", "gap_reduction_pp", "budget", "evals", "time_s")
    across = []
    for group, rr in groups(details, *scope):
        per_inst = by_instance(rr, ("instance",), fields)
        across.append(
            {
                **dict(zip(scope, group, strict=True)),
                "instances": len(per_inst),
                "runs": len(rr),
                **{k: med(per_inst, k) for k in fields},
                "improvements": sum(r["improved"] for r in rr),
                "ties": sum(r["tie"] for r in rr),
                "worse": sum(not r["tie"] and not r["improved"] for r in rr),
            }
        )
    table("K5_cells", across)
    table("K5_invalid_start_replay", errors)
    return len(details), len(work) + sum(
        r["phase"] == "main" and r["method"] == "GA-cost" for r in read_csv("paper_artifacts/raw/runs.csv")
    )


def mip_report(refs):
    details = []
    for row in records(ROOT / "raw/K8.jsonl"):
        reference = refs.get(row["instance"], {}).get("z_best")
        for label, data in row["deadlines"].items():
            details.append(
                {
                    **{
                        k: row[k]
                        for k in (
                            "size",
                            "rho",
                            "instance",
                            "budget",
                            "evals",
                            "time_limit_s",
                            "solver_call_s",
                            "time_s",
                            "nodes",
                            "first_feasible_s",
                            "first_feasible_cost",
                        )
                    },
                    "deadline": label,
                    "deadline_s": data["time_s"] if data else None,
                    "reference": reference,
                    "cost": data["cost"] if data else None,
                    "gap_pct": gap(data["cost"], reference) if data else None,
                }
            )
    table("K8_deadlines", details)
    return len(details)


def public_report():
    spec = REVIEW.raw["public"]
    source = "https://github.com/Tybirk/RL-FCTP/tree/1ab1ba073363c7b650fab7ef1f93b8a7755ba2cb/Java/Glover"
    mip = {r["instance"]: r for r in records(REVIEW_RAW / "public_mip.jsonl")}
    rows = []
    for inst in spec["instances"]:
        name = inst["id"]
        directory = SRC / "review/public/source"
        candidates = sorted(directory.glob(name + ".*"))
        digest = None
        if candidates:
            digest = hashlib.sha256(candidates[0].read_bytes()).hexdigest()
        elif directory.joinpath(name).is_file():
            digest = hashlib.sha256(directory.joinpath(name).read_bytes()).hexdigest()
        if digest != inst["sha256"]:
            url = spec["base_url"] + name + ".FCTP"
            try:
                with urlopen(url, timeout=10) as incoming:
                    digest = hashlib.sha256(incoming.read()).hexdigest()
            except OSError:
                pass
        result = mip[name]
        cplex = inst["published"]["cplex9"]
        barr = inst.get("barr2021")
        cost = result["cost"]
        rows.append(
            {
                "instance": name,
                "size": result["size"],
                "source": source,
                "commit": "1ab1ba073363c7b650fab7ef1f93b8a7755ba2cb",
                "sha256": inst["sha256"],
                "hash_verified": digest == inst["sha256"],
                "MIP": cost,
                "proved": result["proved"],
                "bound": result["bound"],
                "budget": result.get("budget"),
                "evals": None,
                "time_limit_s": result["time_limit_s"],
                "time_s": result["time_s"],
                "nodes": result["nodes"],
                "CPLEX9_Glover_Table3": cplex,
                "Barr2021_Table2": barr,
                "MIP_minus_CPLEX": cost - cplex,
                "MIP_minus_Barr": cost - barr if barr is not None else None,
                "CPLEX_minus_Barr": cplex - barr if barr is not None else None,
            }
        )
    table("K9_public_instances", rows)
    return rows


def provenance():
    manifest_path = SRC / "run_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))["invocations"]

    def revisions(cfg, commands):
        return " ".join(
            dict.fromkeys(
                r["git_commit"]
                for r in manifest
                if r.get("config", {}).get("path") == "experiments/" + cfg and r.get("command") in commands
            )
        )

    v2_dir = Path("paper_artifacts_v2")
    v2 = json.loads((v2_dir / "run_manifest.json").read_text(encoding="utf-8"))["invocations"]
    v2_rev = " ".join(dict.fromkeys(r["git_commit"] for r in v2 if r.get("git_commit")))
    legacy_rev = "0a7a315 (main), eb61ad1 (timing), as recorded in REPORT.md"
    sources = [
        (Path("paper_artifacts"), "paper.yaml", legacy_rev, "v0.3 RQ1–RQ4 and applications"),
        (v2_dir, "paper-v2.yaml", v2_rev, "v0.4 partial archive; see MANUSCRIPT_MAP.md"),
        (
            Path("paper_artifacts_quick"),
            "paper-v2-quick.yaml",
            "see paper_artifacts_quick/run_manifest.json",
            "short v0.4 run",
        ),
        (
            SRC / "linear",
            "paper-v3-cycle.yaml",
            revisions("paper-v3-cycle.yaml", ("run", "extend")),
            "linear comparison and extension",
        ),
        (
            SRC / "fctp",
            "paper-v3-fctp.yaml; paper-v3-fctp-ext.yaml",
            revisions("paper-v3-fctp.yaml", ("run", "benchmark"))
            + " "
            + revisions("paper-v3-fctp-ext.yaml", ("run", "tune")),
            "fixed-charge comparison and extension",
        ),
        (
            SRC / "review",
            "paper-v3-review.yaml",
            revisions(
                "paper-v3-review.yaml",
                (
                    "rivals",
                    "generator",
                    "degenerate",
                    "public",
                    "timing",
                    "mipdefault",
                    "report",
                ),
            ),
            "first review",
        ),
        (ROOT, "paper-v3-review2.yaml", "see session.json, blocks.jsonl and README.md", "second review, exploratory"),
    ]
    rows = []
    for directory, config, revision, purpose in sources:
        for subdir, patterns in (("tables", ("*.csv",)), ("figures", ("*.pdf",))):
            for pattern in patterns:
                for path in sorted((directory / subdir).rglob(pattern)):
                    if directory == ROOT and path.stem == "K10_provenance":
                        continue
                    rows.append(
                        {
                            "artifact": path.stem,
                            "purpose": purpose,
                            "file": path.as_posix(),
                            "configuration": config,
                            "recorded_code_revision": revision,
                        }
                    )
    table("K10_provenance", rows)
    manuscript = (
        ("Table 1", "paper_artifacts_v2/tables/T0_example1.csv"),
        ("Table 2", "experiments/paper-v2.yaml"),
        ("Table 2, tuned parameters", "experiments/tuned-v2.yaml"),
        ("Table 3", "paper_artifacts_v2/tables/T1_instances.csv"),
        ("Table 4", "paper_artifacts_v2/tables/T2_gap.csv"),
        ("Table 5", "paper_artifacts_v2/tables/T5_methods_gap.csv"),
        ("Table 6", "paper_artifacts_v2/tables/T4_factorial.csv"),
        ("Table 7", "paper_artifacts_v2/tables/T10_applied_instances.csv"),
        ("Table 7, Astana summary", "paper_artifacts_v2/tables/T10_applied_summary.csv"),
        ("Figure 1, decoder", "paper_artifacts/figures/en/F1_decoder.pdf"),
        ("Figure 2", "paper_artifacts_v2/figures/en/boxplot_gap.pdf"),
        ("Figure 3", "paper_artifacts_v2/figures/en/convergence.pdf"),
        ("Figure 4", "paper_artifacts_v2/figures/en/time_scaling.pdf"),
        ("Figure 4, v0.3 timing", "paper_artifacts/figures/en/F4_time_scaling.pdf"),
        ("v0.3 factorial comparison", "paper_artifacts/tables/T4_factorial.csv"),
        ("v0.3 paired comparisons", "paper_artifacts/tables/T5_tests.csv"),
    )
    table(
        "K10_manuscript_map",
        [
            {
                "manuscript_item": name,
                "file": path,
                "present": Path(path).is_file(),
                "configuration": path
                if path.startswith("experiments/")
                else (
                    "experiments/paper-v2.yaml" if path.startswith("paper_artifacts_v2/") else "experiments/paper.yaml"
                ),
                "recorded_revision": legacy_rev if path.startswith("paper_artifacts/") else v2_rev,
                "scope": "mapping from the archived manuscript map; v0.4 main archive is partial",
            }
            for name, path in manuscript
        ],
    )
    required = [
        "scripts/normalised_gap.py",
        "scripts/neutrality_check.py",
        "tests/test_proposition3.py",
        "paper_artifacts/tables/T4_factorial.csv",
        "paper_artifacts/tables/T5_tests.csv",
        "paper_artifacts_v2",
        "paper_artifacts_v3",
    ]
    table(
        "K10_required_files",
        [
            {"path": p, "exists": Path(p).exists(), "planned_in_source": True, "planned_in_asset": True}
            for p in required
        ],
    )


def figures(ox, linear):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    directory = ROOT / "figures"
    directory.mkdir(parents=True, exist_ok=True)

    def save(fig, name):
        fig.savefig(directory / f"{name}.pdf", bbox_inches="tight", metadata={"CreationDate": None})
        fig.savefig(directory / f"{name}.jpg", bbox_inches="tight", dpi=300)
        plt.close(fig)

    k1 = read_csv(ROOT / "tables/K1_cells.csv")
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.5), sharey=True, layout="constrained")
    for ax, rho in zip(axes, ("0.2", "1.0"), strict=True):
        for (method,), rr in groups([r for r in k1 if r["rho"] == rho], "method"):
            rows = sorted(rr, key=lambda r: int(r["size"].split("x")[0]))
            ax.plot(
                [int(r["size"].split("x")[0]) for r in rows],
                [float(r["gap_best_pct"]) for r in rows],
                marker=".",
                label=method,
            )
        ax.set(title=f"ρ = {rho}", xlabel="Sources and destinations", xticks=[20, 30, 50, 70])
        ax.grid(alpha=0.25)
    axes[0].set_ylabel("Median gap to best recorded cost (%)")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="outside lower center", ncols=5, frameon=False)
    save(fig, "K1_fctp_population")

    if ox:
        fig, axes = plt.subplots(1, 3, figsize=(10.2, 3.4), sharey=True, layout="constrained")
        for ax, size in zip(axes, ("20x20", "50x50", "100x100"), strict=True):
            for (method,), rr in groups([r for r in ox if r["size"] == size], "method"):
                rows = sorted(rr, key=lambda r: r["tenth"])
                ax.plot([r["tenth"] * 10 for r in rows], [r["novel_share"] for r in rows], marker=".", label=method)
            ax.set(title=size, xlabel="Budget used (%)", ylim=(0, 1), xticks=[20, 40, 60, 80, 100])
            ax.grid(alpha=0.25)
        axes[0].set_ylabel("Share of OX plans new to the population")
        handles, labels = next((ax.get_legend_handles_labels() for ax in axes if ax.lines), ([], []))
        fig.legend(handles, labels, loc="outside lower center", ncols=2, frameon=False)
        save(fig, "K3_ox_novelty")

    fig, ax = plt.subplots(figsize=(7.0, 4.0), layout="constrained")
    for (method,), rr in groups([r for r in linear if r["set"] == "uniform"], "method"):
        if method == "RS":
            continue
        rr = sorted(rr, key=lambda r: int(r["size"].split("x")[0]))
        ax.plot([int(r["size"].split("x")[0]) for r in rr], [r["gap_norm"] for r in rr], ".-", label=method)
    ax.set(
        xlabel="Sources and destinations per instance", ylabel="Median normalised gap", xticks=[5, 10, 20, 30, 50, 100]
    )
    ax.legend(ncols=2, frameon=False)
    ax.grid(alpha=0.25)
    save(fig, "K6_linear_medians")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay-starts", action="store_true")
    args = parser.parse_args()
    refs = fctp_report()
    archive, linear = linear_report()
    ox = diagnostics()
    provenance()
    if args.replay_starts:
        print("K5 covered, planned:", starting_plans(archive, refs), flush=True)
    mip_report(refs)
    public = public_report()
    figures(ox, linear)
    print(f"K9 verified hashes: {sum(r['hash_verified'] for r in public)}/{len(public)}", flush=True)


if __name__ == "__main__":
    main()
