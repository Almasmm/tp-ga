"""Linear GA controls and read-only OX/population diagnostics."""

import hashlib
import json

import numpy as np
from numba import njit

from tpga import _xkernels
from tpga._kernels import _decode_plan, _order_crossover, _tournament, _two_positions
from tpga.cycle import run_ga_x
from tpga.experiments.v2 import methods as v2_methods
from tpga.experiments.v3 import core

_decode_arcs = _xkernels.table()["_decode_arcs"]
METHODS = ("GA-rand-tuned", "GA-cost-tuned", "GA-rand-cycle", "GA-cost-cycle")


def tasks(cfg, block):
    root = cfg.area / "instances"
    archived = {}
    if block == "K3":
        for line in (cfg.area / "raw/runs.jsonl").read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            archived[row["instance"], row["method"], row["seed"]] = row
    items = json.loads((root / "manifest.json").read_text(encoding="utf-8"))["instances"].values()
    sizes = (20, 30, 50) if block == "K2" else (20, 50, 100)
    for entry in sorted(items, key=lambda i: (i["m"], i["id"])):
        if entry["set"] != "uniform" or entry["m"] not in sizes:
            continue
        if block == "K3" and int(entry["id"].rsplit("-", 1)[1]) >= 3:
            continue
        path = root / entry["file"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError(f"archived instance hash mismatch: {path}")
        item = {**entry, "path": str(path), "size": f"{entry['m']}x{entry['n']}"}
        for seed in cfg.seeds(10 if block == "K2" else 3):
            for method in METHODS:
                fields = core.method_fields(cfg, method)
                if block == "K2" and method.endswith("-tuned"):
                    for variant in ("only", "after_swap"):
                        modified = {
                            **fields,
                            "method": method.replace("tuned", "reencode-" + variant),
                            "config": fields["config"] + "-reencode-" + variant,
                        }
                        yield {**core.make_task(cfg, block, item, modified, seed), "reencode": variant}
                elif block == "K3":
                    baseline = archived[item["id"], method, seed]
                    yield {
                        **core.make_task(cfg, block, item, fields, seed),
                        "archived_cost": baseline["cost"],
                        "archived_evals": baseline["evals"],
                    }


@njit(cache=True)
def signature(arcs, flows, count):
    # The hash only locates candidates. Equality is checked on arc/flow pairs.
    value = np.uint64(0)
    for i in range(count):
        word = np.uint64(arcs[i] + 1) * np.uint64(0x9E3779B97F4A7C15) ^ np.uint64(flows[i])
        word = (word ^ (word >> np.uint64(30))) * np.uint64(0xBF58476D1CE4E5B9)
        value ^= word ^ (word >> np.uint64(27))
    return value


@njit(cache=True)
def equal_plan(index, count, counts, arcs, flows, dense):
    if counts[index] != count:
        return False
    for pos in range(count):
        if dense[arcs[index, pos]] != flows[index, pos]:
            return False
    return True


@njit(cache=True)
def observe_ox(pop, fit, uniforms, tournament, rate, supply, demand, eps, used, budget, out):
    m, n = supply.size, demand.size
    size, length = pop.shape
    width = m + n - 1
    a, b = np.empty(m), np.empty(n)
    arcs = np.empty((size, width), dtype=np.int64)
    flows = np.empty((size, width))
    counts = np.empty(size, dtype=np.int64)
    hashes = np.empty(size, dtype=np.uint64)
    for slot in range(size):
        count = _decode_arcs(pop[slot], supply, demand, n, eps, a, b, arcs[slot], flows[slot])
        counts[slot] = count
        hashes[slot] = signature(arcs[slot], flows[slot], count)
    order = np.argsort(hashes)
    ordered_hashes = hashes[order]
    scratch = np.arange(size)
    kept = np.zeros(length, dtype=np.bool_)
    child = np.empty(length, dtype=np.int64)
    ca, cf = np.empty(width, dtype=np.int64), np.empty(width)
    dense = np.zeros(length)
    base = tournament * 2
    for index, u in enumerate(uniforms):
        if u[base] >= rate:
            continue
        left = _tournament(fit, u[:tournament], scratch)
        right = _tournament(fit, u[tournament:base], scratch)
        i, j = _two_positions(u[base + 1], u[base + 2], length)
        _order_crossover(pop[left], pop[right], i, j, child, kept)
        count = _decode_arcs(child, supply, demand, n, eps, a, b, ca, cf)
        h = signature(ca, cf, count)
        for p in range(count):
            dense[ca[p]] = cf[p]
        eq_left = hashes[left] == h and equal_plan(left, count, counts, arcs, flows, dense)
        eq_right = hashes[right] == h and equal_plan(right, count, counts, arcs, flows, dense)
        present = eq_left or eq_right
        if not present:
            pos = np.searchsorted(ordered_hashes, h)
            while pos < size and ordered_hashes[pos] == h:
                if equal_plan(order[pos], count, counts, arcs, flows, dense):
                    present = True
                    break
                pos += 1
        for p in range(count):
            dense[ca[p]] = 0
        tenth = min(9, ((used + index + 1) * 10 - 1) // budget)
        out[tenth, 0] += 1
        out[tenth, 1] += eq_left
        out[tenth, 2] += eq_right
        out[tenth, 3] += eq_left or eq_right
        out[tenth, 4] += not present


@njit(cache=True)
def observe_swaps(pop, draws, supply, demand, eps):
    m, n = supply.size, demand.size
    length = m * n
    counts = np.zeros(4, dtype=np.int64)
    for slot in range(draws.shape[0]):
        chromosome = pop[slot]
        plan = _decode_plan(chromosome, supply, demand, n, eps)
        a, b = supply.copy(), demand.copy()
        close_a = np.full(m, length)
        close_b = np.full(n, length)
        for pos, arc in enumerate(chromosome):
            q = plan[arc]
            if q > eps:
                i, j = arc // n, arc % n
                a[i] -= q
                b[j] -= q
                if a[i] <= eps:
                    close_a[i] = pos
                if b[j] <= eps:
                    close_b[j] = pos
        other = chromosome.copy()
        for u in draws[slot]:
            i, j = _two_positions(u[0], u[1], length)
            left, right = chromosome[i], chromosome[j]
            positive = plan[left] > eps or plan[right] > eps
            open_zero = plan[right] <= eps and min(close_a[right // n], close_b[right % n]) >= i
            if positive or open_zero:
                other[i], other[j] = right, left
                neutral = np.array_equal(plan, _decode_plan(other, supply, demand, n, eps))
                other[i], other[j] = left, right
                counts[0] += positive
                counts[1] += positive and neutral
                counts[2] += open_zero
                counts[3] += open_zero and neutral
    return counts


def run(task):
    problem = v2_methods.load(task["path"])
    cfg = core._gax_config(task)
    bins = np.zeros((10, 5), dtype=np.int64)
    snapshots = {}
    rng = np.random.default_rng(20261120 + int(task["seed"]) - 20261116)

    def generation(used, pop, fit, uniforms):
        observe_ox(
            pop,
            fit,
            uniforms,
            cfg.tournament,
            cfg.crossover_rate,
            problem.supply,
            problem.demand,
            task["decoder_tol"],
            used,
            task["budget"],
            bins,
        )

    def population(used, pop, final):
        if final:
            label = "final"
        elif not snapshots:
            label = "initial"
        elif 2 * used >= task["budget"] and "half" not in snapshots:
            label = "half"
        else:
            return
        draws = rng.random((min(16, len(pop)), 64, 2))
        counts = observe_swaps(pop, draws, problem.supply, problem.demand, task["decoder_tol"])
        snapshots[label] = {"evals": used, "draws": draws.shape[0] * draws.shape[1], "counts": counts.tolist()}

    diagnostic = task["phase"] == "K3"
    result = run_ga_x(
        problem,
        cfg,
        reencode=task.get("reencode"),
        generation_hook=generation if diagnostic else None,
        population_hook=population if diagnostic else None,
    )
    core._feasible(problem, result.x, task["method"])
    if diagnostic and (result.cost != task["archived_cost"] or result.evaluations != task["archived_evals"]):
        raise RuntimeError("diagnostic run differs from the archived article run")
    return {
        **core._run_fields(result),
        "cost": result.cost,
        "start_cost": result.history[0],
        "evaluation_unit": "decoder",
        "gap": 100 * (result.cost - task["z_star"]) / task["z_star"],
        "ox": bins.tolist() if diagnostic else None,
        "snapshots": snapshots if diagnostic else None,
    }
