"""Live view of the parameter tuning (read-only).

Shows the progress of every tuned method, the best training gap so far next to the result of round 1,
the best parameters with their position in the search range (and whether they sit at a bound), a chart of
the trials, the best and the latest trials, whether the tuning process is alive, and whether the memory
would suffice for the largest population of the search range.

Run from the repository root:

    .venv\\Scripts\\python scripts\\watch_tuning.py

Ctrl+C closes the view only; the tuning keeps running. The script reads files and never writes.
"""

from __future__ import annotations

import argparse
import contextlib
import json
import math
import re
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import psutil
import yaml
from rich.console import Console, Group
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress_bar import ProgressBar
from rich.table import Table
from rich.text import Text

ROOT = Path(__file__).resolve().parents[1]
METHODS = ["GA-rand", "GA-cost", "SA-rand", "SA-cost"]
GIB = 2**30

# Scales as sampled by tpga.experiments.v2.tune (True = log scale). Kept in step with that module.
SA_PARAMS = {"insertion_probability": False, "initial_acceptance": False, "final_ratio": True}
GA_FLOATS = {"crossover_rate": False, "swap_fixed": True, "swap_per_position": True, "swap_scaled": True}
GA_INTS = {"population": True, "tournament": False, "elite": False, "swap_count": False}


def worst_case_bytes(population: int, arcs: int) -> int:
    """Peak memory of one GA run (same rule as tpga.experiments.v2.tune.worst_case_bytes)."""
    return 150 * 2**20 + 24 * int(population) * int(arcs)


with contextlib.suppress(Exception):  # prefer the library's definitions; the view also works without it
    from tpga.experiments.v2 import tune as _tune

    SA_PARAMS, GA_FLOATS, GA_INTS = _tune.SA_PARAMS, _tune.GA_FLOATS, _tune.GA_INTS
    worst_case_bytes = _tune.worst_case_bytes  # noqa: F811

# Wall time of each method in round 1 (minutes), from the tuning session of 2026-11-17 (09:25-13:13).
# Used only to estimate the remaining time of methods that have not started yet.
ROUND1_MINUTES = {"GA-rand": 85.0, "GA-cost": 89.0, "SA-rand": 27.0, "SA-cost": 27.0}

SHORT = {
    "population": "P",
    "crossover_rate": "pc",
    "tournament": "t",
    "elite": "e",
    "insertion_probability": "p_ins",
    "initial_acceptance": "p0",
    "final_ratio": "final_ratio",
}

RE_PROGRESS = re.compile(
    r"^(GA-rand|GA-cost|SA-rand|SA-cost): (\d+)/(\d+) trials, best mean gap ([\d.]+) %, ([\d.]+) min"
)
RE_START = re.compile(r"\[I (\d{4}-\d\d-\d\d \d\d:\d\d:\d\d),\d+\] A new study created .* name: (\S+)")
RE_DONE = re.compile(r"^(GA-rand|GA-cost|SA-rand|SA-cost): mean gap ([\d.]+) %")
RE_WORKERS = re.compile(r"^workers: (\d+) of (\d+)")


@dataclass
class MethodState:
    name: str
    trials: list[dict[str, Any]] = field(default_factory=list)
    target: int = 100
    started: datetime | None = None
    elapsed_min: float | None = None  # from the last progress line of the console
    logged_done: int = 0
    finished: bool = False
    round1_best: float | None = None
    round1_params: dict[str, Any] | None = None

    @property
    def done(self) -> int:
        return max(len(self.trials), self.logged_done)

    @property
    def scored(self) -> list[dict[str, Any]]:
        ok = [t for t in self.trials if isinstance(t.get("mean_gap"), (int, float))]
        return sorted(ok, key=lambda t: t.get("trial", 0))

    @property
    def best(self) -> dict[str, Any] | None:
        ok = self.scored
        return min(ok, key=lambda t: t["mean_gap"]) if ok else None


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue  # a line being written
    return out


def load_tuning(config: Path) -> dict[str, Any]:
    try:
        return yaml.safe_load(config.read_text(encoding="utf-8"))["tuning"]
    except Exception:  # noqa: BLE001
        return {}


def bounds(spec: Any, log_default: bool) -> tuple[float, float, bool]:
    if isinstance(spec, dict):
        lo, hi = spec["range"]
        return float(lo), float(hi), bool(spec.get("log", log_default))
    lo, hi = spec
    return float(lo), float(hi), log_default


def param_rows(
    method: str, params: dict[str, Any], space: dict[str, Any]
) -> list[tuple[str, Any, float, float, bool, float]]:
    """(name, value, lo, hi, log, position 0..1 on the sampled scale)."""
    rows: list[tuple[str, Any, float, float, bool, float]] = []
    if not space:
        return rows
    if method.startswith("SA"):
        items = [(n, params.get(n), space["sa"][n], lg) for n, lg in SA_PARAMS.items()]
    else:
        g = space["ga"]
        scales = {**GA_INTS, **GA_FLOATS}
        items = [(n, params.get(n), g[n], scales[n]) for n in ("population", "crossover_rate", "tournament", "elite")]
        mode = params.get("mutation_mode")
        if mode in g:
            value = params.get("mutation_rate") if mode == "swap_fixed" else params.get("mutation_strength")
            items.append((mode, value, g[mode], scales[mode]))
    for name, value, spec, log in items:
        if value is None:
            continue
        lo, hi, lg = bounds(spec, log)
        f = math.log if lg else (lambda v: v)
        pos = (f(float(value)) - f(lo)) / (f(hi) - f(lo)) if f(hi) > f(lo) else 0.0
        rows.append((name, value, lo, hi, lg, min(1.0, max(0.0, pos))))
    return rows


def fmt(v: Any) -> str:
    if isinstance(v, bool) or v is None:
        return str(v)
    if isinstance(v, int):
        return f"{v}"
    if isinstance(v, float):
        if v == 0:
            return "0"
        if abs(v) < 1e-3 or abs(v) >= 1e4:
            return f"{v:.2e}"
        return f"{v:.4g}"
    return str(v)


def short_params(method: str, p: dict[str, Any]) -> str:
    if method.startswith("SA"):
        p_ins, p0, fr = (fmt(p.get(k)) for k in ("insertion_probability", "initial_acceptance", "final_ratio"))
        return f"p_ins {p_ins}  p0 {p0}  fr {fr}"
    mode = p.get("mutation_mode", "?")
    strength = fmt(p.get("mutation_rate", p.get("mutation_strength")))
    head = f"P {p.get('population')}  pc {fmt(p.get('crossover_rate'))}  t {p.get('tournament')}  e {p.get('elite')}"
    return f"{head}  {mode} {strength}"


def position_bar(pos: float, width: int = 22, at_bound: bool = False) -> Text:
    k = min(width - 1, max(0, round(pos * (width - 1))))
    t = Text("[", style="dim")
    for i in range(width):
        t.append("●" if i == k else "─", style=("bold red" if at_bound else "bold yellow") if i == k else "dim")
    t.append("]", style="dim")
    return t


def trial_chart(trials: list[dict[str, Any]], width: int, height: int, reference: float | None) -> Text:
    """Every trial as a dot, the best value so far as a line, round 1 as a dashed line; trial number on x.

    The y range runs from the best value to the 90th percentile of all trials, so a few very bad trials do not
    flatten the picture; trials above it are drawn on the top row as ▲.
    """
    gaps = [float(t["mean_gap"]) for t in trials]
    if not gaps or width < 10 or height < 3:
        return Text("ещё нет испытаний", style="dim")
    label_w = 7
    w = max(5, width - label_w)
    lo = min(gaps + ([reference] if reference is not None else []))
    srt = sorted(gaps)
    hi = max(srt[min(len(srt) - 1, int(0.9 * (len(srt) - 1)))], reference or lo, lo + 1e-9)
    hi = hi + 0.05 * (hi - lo)

    def row(v: float) -> int:  # 0 = top
        return min(height - 1, max(0, round((hi - v) / (hi - lo) * (height - 1))))

    grid = [[(" ", "")] * w for _ in range(height)]
    n = len(gaps)
    col = [min(w - 1, int(i * w / max(n, 1))) for i in range(n)]
    if reference is not None:
        r = row(reference)
        for x in range(0, w, 2):
            grid[r][x] = ("╌", "magenta")
    best = math.inf
    for i, g in enumerate(gaps):
        new = g < best
        best = min(best, g)
        if g > hi:
            grid[0][col[i]] = ("▲", "dim")
        elif grid[row(g)][col[i]][0] in (" ", "╌"):
            grid[row(g)][col[i]] = ("•", "dim cyan")
        if new:
            grid[row(g)][col[i]] = ("★", "bold green")
    best = math.inf
    for x in range(w):  # best-so-far line under the dots
        idx = [i for i in range(n) if col[i] <= x]
        if not idx:
            continue
        best = min(gaps[i] for i in idx)
        r = row(best)
        if grid[r][x][0] in (" ", "╌"):
            grid[r][x] = ("━", "green")
    out = Text()
    for y in range(height):
        value = hi - y * (hi - lo) / (height - 1)
        label = f"{value:6.1f} " if y in (0, height - 1, height // 2) else " " * label_w
        out.append(label, style="dim")
        for ch, st in grid[y]:
            out.append(ch, style=st)
        out.append("\n")
    axis = " " * label_w + "0" + " " * max(0, w - len(str(n - 1)) - 1) + str(n - 1)
    out.append(axis, style="dim")
    return out


def own_minutes(states: dict[str, MethodState], s: MethodState) -> float:
    """Minutes spent on method ``s``: the console reports minutes since the start of the whole tuning."""
    before = [states[m].elapsed_min or 0.0 for m in METHODS[: METHODS.index(s.name)]]
    return max(0.0, (s.elapsed_min or 0.0) - max(before, default=0.0))


class Watcher:
    def __init__(self, tuning_dir: Path, console_log: Path, round1_dir: Path, config: Path) -> None:
        self.tuning_dir, self.console_log, self.round1_dir, self.config = tuning_dir, console_log, round1_dir, config
        tuning = load_tuning(config)
        self.space = tuning.get("space", {})
        self.target = int(tuning.get("trials", 100))
        self.batch_size = int(tuning.get("parallel_trials", 1))
        self.max_arcs = 0
        with contextlib.suppress(Exception):
            sizes = [s for v in tuning["sets"].values() for s in v]
            self.max_arcs = max(int(m) * int(n) for m, n in sizes)
        self.pop_hi = 0
        with contextlib.suppress(Exception):
            self.pop_hi = int(bounds(self.space["ga"]["population"], True)[1])
        psutil.cpu_percent(interval=None)

    def collect(self) -> tuple[dict[str, MethodState], list[str], int | None]:
        states = {m: MethodState(m, target=self.target) for m in METHODS}
        lines: list[str] = []
        workers = None
        if self.console_log.exists():
            lines = self.console_log.read_text(encoding="utf-8", errors="replace").splitlines()
        for line in lines:
            if (m := RE_START.search(line)) and m.group(2) in states:
                states[m.group(2)].started = datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S")
            elif m := RE_PROGRESS.match(line):
                s = states[m.group(1)]
                s.logged_done, s.target, s.elapsed_min = int(m.group(2)), int(m.group(3)), float(m.group(5))
            elif m := RE_DONE.match(line):
                states[m.group(1)].finished = True
            elif m := RE_WORKERS.match(line):
                workers = int(m.group(1))
        for name, s in states.items():
            s.trials = read_jsonl(self.tuning_dir / f"{name}.jsonl")
            r1 = [
                t for t in read_jsonl(self.round1_dir / f"{name}.jsonl") if isinstance(t.get("mean_gap"), (int, float))
            ]
            if r1:
                b = min(r1, key=lambda t: t["mean_gap"])
                s.round1_best, s.round1_params = b["mean_gap"], b["params"]
            if s.done >= s.target:
                s.finished = True
        return states, lines, workers

    @staticmethod
    def current(states: dict[str, MethodState]) -> MethodState:
        for m in METHODS:
            if not states[m].finished:
                return states[m]
        return states[METHODS[-1]]

    def eta_minutes(self, states: dict[str, MethodState]) -> tuple[float | None, dict[str, float | None]]:
        cur = self.current(states)
        per: dict[str, float | None] = {}
        speed = None  # observed time relative to round 1 for the running method
        if cur.elapsed_min and cur.done:
            per_trial = own_minutes(states, cur) / cur.done
            per[cur.name] = per_trial * (cur.target - cur.done)
            speed = (per_trial * cur.target) / ROUND1_MINUTES[cur.name]
        for m in METHODS:
            s = states[m]
            if s.finished:
                per[m] = 0.0
            elif m != cur.name:
                per[m] = ROUND1_MINUTES[m] * speed if speed else None
        if any(v is None for v in per.values()):
            return None, per
        return float(sum(v for v in per.values() if v)), per

    @staticmethod
    def tuning_process() -> tuple[int | None, float]:
        """PID and resident memory of the tuning process tree (tpga-exp and its workers)."""
        for p in psutil.process_iter(["name", "pid"]):
            try:
                if (p.info["name"] or "").lower().startswith("tpga-exp"):
                    rss = 0
                    for c in [p, *p.children(recursive=True)]:
                        with contextlib.suppress(psutil.Error):
                            rss += c.memory_info().rss
                    return p.info["pid"], rss / GIB
            except psutil.Error:
                continue
        return None, 0.0

    def memory_panel(self, cur: MethodState, workers: int | None, tuning_gib: float) -> Group:
        """Would the memory suffice if the sampler proposes the largest population of the range?"""
        vm = psutil.virtual_memory()
        free = vm.available / GIB
        usable = free + tuning_gib  # memory the tuning holds now is reused by its next runs
        lines = []
        if not (workers and self.max_arcs and self.pop_hi):
            return Group(Text("нет данных о числе процессов или диапазоне популяции", style="dim"))
        if cur.name.startswith("SA"):
            lines.append(Text("SA: память не зависит от популяции, риска нет.", style="green"))
        last = [t for t in cur.scored if t.get("batch") == max((t.get("batch", -1) for t in cur.scored), default=-1)]
        pop_now = max((int(t["params"].get("population", 0)) for t in last), default=0)
        need_now = workers * worst_case_bytes(pop_now, self.max_arcs) / GIB if pop_now else 0.0
        need_max = workers * worst_case_bytes(self.pop_hi, self.max_arcs) / GIB
        fits = int(usable // (worst_case_bytes(self.pop_hi, self.max_arcs) / GIB))
        side = int(math.isqrt(self.max_arcs))
        if pop_now:
            lines.append(
                Text(
                    f"Последняя пачка: P до {pop_now} → до {need_now:.1f} ГБ на {workers} процессов",
                    style="red" if need_now > usable else "",
                )
            )
        ok = need_max <= usable
        lines.append(
            Text(
                f"Худший случай диапазона: P {self.pop_hi} на {side}×{side} → {need_max:.1f} ГБ; "
                f"доступно расчёту ≈ {usable:.1f} ГБ (свободно {free:.1f} + у настройки {tuning_gib:.1f})",
                style="green" if ok else "bold red",
            )
        )
        if not ok and not cur.name.startswith("SA"):
            lines.append(
                Text(
                    f"НЕ ХВАТИТ: поместится ~{min(fits, workers)} из {workers} процессов. Закройте лишние программы "
                    "(браузер, Docker, WSL/vmmem, лишние окна VS Code); python.exe не трогайте.",
                    style="bold white on red",
                )
            )
        return Group(*lines)

    def render(self, width: int = 200, height: int = 50) -> Layout:
        states, lines, workers = self.collect()
        cur = self.current(states)
        total_done = sum(min(s.done, s.target) for s in states.values())
        total = sum(s.target for s in states.values())
        eta, per = self.eta_minutes(states)
        now = datetime.now()
        pid, tuning_gib = self.tuning_process()
        narrow = width < 150

        # activity: the log is written once per batch, so the normal gap is one batch time
        mtimes = [p.stat().st_mtime for p in [self.console_log, self.tuning_dir / f"{cur.name}.jsonl"] if p.exists()]
        idle_min = (time.time() - max(mtimes)) / 60 if mtimes else None
        batch_min = own_minutes(states, cur) / cur.done * self.batch_size if cur.elapsed_min and cur.done else None
        cpu = psutil.cpu_percent(interval=None)
        all_finished = all(s.finished for s in states.values())
        late = idle_min is not None and idle_min > max(10.0, 3 * (batch_min or 0))
        if all_finished:
            status = Text("ЗАВЕРШЕНА", style="bold green")
        elif pid is None:
            status = Text("ПРОЦЕСС НАСТРОЙКИ НЕ НАЙДЕН", style="bold white on red")
        elif late:
            status = Text(f"НЕТ ЗАПИСЕЙ {idle_min:.0f} мин: проверьте процесс", style="bold white on red")
        else:
            status = Text(f"ИДЁТ · процесс {pid}", style="bold green")

        # header
        head = Table.grid(expand=True)
        head.add_column(ratio=3)
        head.add_column(ratio=2, justify="right")
        head.add_row(
            Text("Настройка параметров v0.4 · раунд 2", style="bold"), Text(now.strftime("%d.%m %H:%M:%S"), style="dim")
        )
        bar = ProgressBar(total=total, completed=total_done, width=None, complete_style="green")
        eta_txt = "оценка появится после первой пачки"
        if eta is not None:
            eta_txt = f"осталось ≈ {eta / 60:.1f} ч, окончание ≈ {(now + timedelta(minutes=eta)).strftime('%H:%M')}"
        if all_finished:
            eta_txt = "все методы закончены"
        head.add_row(
            Group(Text(f"Всего {total_done} из {total} испытаний ({100 * total_done / total:.0f} %)"), bar),
            Group(status, Text(eta_txt, style="dim")),
        )

        # methods
        mt = Table(expand=True, header_style="bold", box=None, pad_edge=False)
        mt.add_column("Метод", no_wrap=True)
        mt.add_column("Прогресс", ratio=3)
        mt.add_column("Испыт.", justify="right", no_wrap=True)
        mt.add_column("Лучший gap, %", justify="right", no_wrap=True)
        mt.add_column("Раунд 1, %", justify="right", no_wrap=True)
        mt.add_column("Разница", justify="right", no_wrap=True)
        mt.add_column("Мин/испыт.", justify="right", no_wrap=True)
        mt.add_column("Осталось", justify="right", no_wrap=True)
        for m in METHODS:
            s = states[m]
            b = s.best
            mark = "▶ " if s is cur and not s.finished else ("✓ " if s.finished else "  ")
            style = "bold" if s is cur else ("green" if s.finished else "dim")
            rate = f"{own_minutes(states, s) / s.done:.2f}" if s.elapsed_min and s.done else "—"
            left = per.get(m)
            left_txt = "готово" if s.finished else ("—" if left is None else f"{left:.0f} мин")
            best_txt, diff_txt = Text("—", style="dim"), Text("—", style="dim")
            if b:
                best_txt = Text(f"{b['mean_gap']:.2f}")
                if s.round1_best is not None:
                    d = b["mean_gap"] - s.round1_best
                    col = "green" if d < 0 else "yellow"
                    best_txt.stylize(col)
                    diff_txt = Text(f"{d:+.2f}", style=col)
            mt.add_row(
                Text(mark + m, style=style),
                ProgressBar(total=s.target, completed=min(s.done, s.target), complete_style="cyan"),
                f"{s.done}/{s.target}",
                best_txt,
                "—" if s.round1_best is None else f"{s.round1_best:.2f}",
                diff_txt,
                rate,
                left_txt,
            )

        # best parameters of the running method, next to round 1
        pt = Table(expand=True, box=None, header_style="bold")
        pt.add_column("Параметр", no_wrap=True)
        pt.add_column("Значение", justify="right", no_wrap=True)
        pt.add_column("Положение в диапазоне", no_wrap=True)
        pt.add_column("Диапазон", style="dim", no_wrap=True)
        pt.add_column("Раунд 1", justify="right", style="magenta", no_wrap=True)
        b = cur.best
        notes: list[Text] = []
        r1 = cur.round1_params or {}
        r1_values = {n: v for n, v, *_ in param_rows(cur.name, r1, self.space)} if r1 else {}
        if b:
            hits = []
            for name, value, lo, hi, lg, pos in param_rows(cur.name, b["params"], self.space):
                at = pos <= 0.05 or pos >= 0.95
                if at:
                    hits.append(SHORT.get(name, name))
                pt.add_row(
                    SHORT.get(name, name),
                    Text(fmt(value), style="bold red" if at else ""),
                    position_bar(pos, at_bound=at),
                    f"{fmt(lo)} … {fmt(hi)}{' (log)' if lg else ''}",
                    fmt(r1_values[name]) if name in r1_values else "—",
                )
            notes.append(
                Text(
                    "У границы (в пределах 5 %): " + ", ".join(hits) + ". Повторно не расширяется (поправка 2).",
                    style="red",
                )
                if hits
                else Text("Ни один параметр не у границы.", style="green")
            )
            if r1 and r1.get("mutation_mode") != b["params"].get("mutation_mode"):
                notes.append(Text(f"Раунд 1 выбрал другую мутацию: {short_params(cur.name, r1)}", style="magenta"))
            title_p = f"Лучшие параметры {cur.name}: испытание {b['trial']}, gap {b['mean_gap']:.2f} %"
        else:
            title_p = f"Лучшие параметры {cur.name}: ещё нет законченных испытаний"
        params_panel = Panel(Group(pt, *notes), title=title_p, border_style="cyan")

        # sizes of the middle area (rows and columns available to the panels)
        mid_h = max(10, height - 5 - 8 - 8)
        col_w = width if narrow else width // 2
        params_h = 1 + max(1, len(pt.rows)) + len(notes)  # header row, parameter rows, notes

        # chart of all trials
        # left column: params panel (params_h + 2 rows), then the chart panel: 2 borders, axis and legend rows
        chart_h = max(4, (mid_h - (params_h + 2) - 4) if not narrow else 10)
        chart = trial_chart(cur.scored, col_w - 7, chart_h, cur.round1_best)  # borders, padding, rounding
        legend = Text.assemble(
            ("• испытание  ", "dim cyan"),
            ("★ новый лучший  ", "bold green"),
            ("━ лучший  ", "green"),
            ("╌ раунд 1  ", "magenta"),
            ("▲ выше шкалы", "dim"),
        )
        chart_panel = Panel(Group(chart, legend), title=f"Все испытания {cur.name}, gap %", border_style="cyan")

        # best five and latest trials
        def trial_table(rows: list[dict[str, Any]], marks: set[int]) -> Table:
            t = Table(expand=True, box=None, header_style="bold")
            t.add_column("#", justify="right", no_wrap=True)
            t.add_column("Параметры", no_wrap=True, overflow="ellipsis")
            t.add_column("gap, %", justify="right", no_wrap=True)
            for r in rows:
                g = r["mean_gap"]
                new = r.get("trial") in marks
                t.add_row(
                    str(r.get("trial")),
                    short_params(cur.name, r.get("params", {})),
                    Text(("★ " if new else "") + f"{g:.2f}", style="bold green" if new else ""),
                )
            return t

        marks, run_best = set(), math.inf
        for t in cur.scored:
            if t["mean_gap"] < run_best:
                run_best = t["mean_gap"]
                marks.add(t.get("trial"))
        top = sorted(cur.scored, key=lambda t: t["mean_gap"])[:5]
        best_panel = Panel(trial_table(top, set()), title=f"Лучшие 5 испытаний {cur.name}", border_style="cyan")
        # rows left for the latest trials: under the params and chart panels (narrow) or under the best five
        left_rows = height - 5 - 8 - 12 - (params_h + 2) - (chart_h + 4) if narrow else mid_h - 9
        n_latest = max(5, left_rows - 3)  # panel borders and the header row
        latest_panel = Panel(
            trial_table(cur.scored[-n_latest:], marks),
            title=f"Последние испытания {cur.name} (★ новый лучший)",
            border_style="cyan",
        )

        # machine
        vm = psutil.virtual_memory()
        bat = psutil.sensors_battery() if hasattr(psutil, "sensors_battery") else None
        power = "—" if bat is None else ("сеть" if bat.power_plugged else f"БАТАРЕЯ {bat.percent:.0f} %")
        boot = datetime.fromtimestamp(psutil.boot_time())
        mach = Table.grid(expand=True)
        for _ in range(2):
            mach.add_column()
        cells = [
            Text(
                f"ЦП {cpu:.0f} %" + ("" if cpu >= 50 else " (между пачками это нормально)"),
                style="green" if cpu >= 50 else "yellow",
            ),
            Text(
                f"Память {vm.used / GIB:.1f} / {vm.total / GIB:.0f} ГБ, свободно {vm.available / GIB:.1f} ГБ",
                style="red" if vm.available < 3 * GIB else "",
            ),
            Text(f"Настройка: {tuning_gib:.1f} ГБ, {workers or '—'} процессов"),
            Text(f"Питание: {power}", style="bold red" if power.startswith("БАТАРЕЯ") else ""),
            Text(f"Компьютер включён с {boot.strftime('%d.%m %H:%M')}", style="dim"),
            Text(
                ""
                if idle_min is None
                else f"Последняя запись {idle_min:.1f} мин назад"
                + (f" (пачка ≈ {batch_min:.1f} мин)" if batch_min else ""),
                style="dim",
            ),
            Text(f"Старт {cur.name}: {cur.started.strftime('%H:%M') if cur.started else '—'}", style="dim"),
            Text("Ctrl+C закрывает только это окно", style="dim"),
        ]
        step = 2
        for i in range(0, len(cells), step):
            mach.add_row(*cells[i : i + step])
        mem_panel = Panel(
            self.memory_panel(cur, workers, tuning_gib), title="Память на большие популяции", border_style="yellow"
        )

        layout = Layout()
        layout.split_column(
            Layout(Panel(head, border_style="green"), name="head", size=5),
            Layout(Panel(mt, title="Методы", border_style="green"), name="methods", size=8),
            Layout(name="mid", ratio=1),
            Layout(name="foot", size=8 if not narrow else 12),
        )
        if narrow:
            layout["mid"].split_column(
                Layout(params_panel, size=params_h + 2),
                Layout(chart_panel, size=chart_h + 4),
                Layout(latest_panel),
            )
            layout["foot"].split_column(
                Layout(mem_panel, size=6), Layout(Panel(mach, title="Компьютер", border_style="green"))
            )
        else:
            layout["mid"].split_row(Layout(name="left"), Layout(name="right"))
            layout["mid"]["left"].split_column(Layout(params_panel, size=params_h + 2), Layout(chart_panel))
            layout["mid"]["right"].split_column(Layout(best_panel, size=9), Layout(latest_panel))
            layout["foot"].split_row(Layout(mem_panel), Layout(Panel(mach, title="Компьютер", border_style="green")))
        return layout


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tuning-dir", default=str(ROOT / "paper_artifacts_v2" / "tuning"))
    ap.add_argument("--log", default=str(ROOT / "paper_artifacts_v2" / "logs" / "tune-round2-console.txt"))
    ap.add_argument("--round1-dir", default=str(ROOT / "paper_artifacts_v2" / "tuning" / "round1"))
    ap.add_argument("--config", default=str(ROOT / "experiments" / "paper-v2.yaml"))
    ap.add_argument("--interval", type=float, default=5.0, help="seconds between refreshes")
    ap.add_argument("--once", action="store_true", help="print one frame and exit")
    ap.add_argument("--size", help="WIDTHxHEIGHT for --once (default: the terminal size)")
    a = ap.parse_args()
    w = Watcher(Path(a.tuning_dir), Path(a.log), Path(a.round1_dir), Path(a.config))
    if a.once:
        psutil.cpu_percent(interval=0.5)
        cw, ch = (int(v) for v in a.size.split("x")) if a.size else Console().size
        console = Console(width=cw, height=ch)
        console.print(w.render(cw, ch), height=ch)
        return
    try:
        with Live(screen=True, refresh_per_second=4) as live:
            while True:
                size = live.console.size
                live.update(w.render(size.width, size.height))
                time.sleep(a.interval)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
