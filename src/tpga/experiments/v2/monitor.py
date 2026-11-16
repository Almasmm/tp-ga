"""Live view of a running experiment: rich terminal screen, plain log lines, and a state file for the web."""

from __future__ import annotations

import statistics
import subprocess
import sys
import time
from collections import deque
from pathlib import Path
from typing import Any

from tpga.experiments.v2.storage import write_atomic

NO_DATA = "нет данных"


def cpu_temperature() -> str:
    """CPU temperature if the system reports it without administrator rights; otherwise ``нет данных``."""
    try:
        import psutil

        sensors = getattr(psutil, "sensors_temperatures", None)
        if sensors:
            data = sensors()
            for entries in data.values():
                if entries:
                    return f"{entries[0].current:.0f} °C"
    except Exception:  # noqa: BLE001
        pass
    if sys.platform == "win32":
        try:
            out = subprocess.run(
                [
                    "powershell",
                    "-NoProfile",
                    "-Command",
                    "(Get-CimInstance -Namespace root/wmi -ClassName MSAcpi_ThermalZoneTemperature "
                    "-ErrorAction Stop | Select-Object -First 1).CurrentTemperature",
                ],
                capture_output=True,
                text=True,
                timeout=8,
                check=False,
            ).stdout.strip()
            if out.isdigit():
                return f"{int(out) / 10 - 273.15:.0f} °C (ACPI)"
        except (OSError, subprocess.SubprocessError):
            pass
    return NO_DATA


class Monitor:
    """Collects worker status and finished runs; renders with rich or prints plain lines."""

    def __init__(self, output: Path, plain: bool = False, state_interval_s: float = 3.0) -> None:
        self.output = output
        self.plain = plain
        self.state_interval_s = state_interval_s
        self.workers: dict[int, dict[str, Any]] = {}
        self.recent: deque[dict[str, Any]] = deque(maxlen=10)
        self.gaps: dict[str, list[float]] = {}
        self.counts = {"errors": 0, "infeasible": 0, "retries": 0, "skipped": 0}
        self.phase = ""
        self.phase_total = self.phase_done = 0
        self.total = self.done = 0
        self.started = time.time()
        self.phase_started = time.time()
        self.last_state = 0.0
        self.last_plain = time.time()
        self.message = ""
        self.temperature = cpu_temperature()
        self.temperature_checked = time.time()
        self.system: dict[str, Any] = {}

    # --- events -----------------------------------------------------------------------------
    def start_phase(self, name: str, total: int, skipped: int) -> None:
        self.phase, self.phase_total, self.phase_done = name, total, 0
        self.counts["skipped"] += skipped
        self.phase_started = time.time()
        self.gaps = {}
        if self.plain:
            print(f"[{time.strftime('%H:%M:%S')}] phase {name}: {total} runs to do, {skipped} already done", flush=True)

    def status(self, event: dict[str, Any]) -> None:
        pid = int(event["pid"])
        if event["type"] == "start":
            self.workers[pid] = {**event, "evals": 0, "best_gap": None, "started": event["time"]}
        elif event["type"] == "progress" and pid in self.workers:
            self.workers[pid].update(evals=event.get("evals"), best_gap=event.get("best_gap"))
        elif event["type"] == "done":
            self.workers.pop(pid, None)

    def finished(self, record: dict[str, Any]) -> None:
        self.done += 1
        self.phase_done += 1
        self.recent.appendleft(record)
        if record.get("gap") is not None:
            self.gaps.setdefault(record["method"], []).append(float(record["gap"]))
        if self.plain:
            print(
                f"[{time.strftime('%H:%M:%S')}] {record['phase']} {record['method']} {record['instance']} "
                f"seed={record.get('seed')} gap={_f(record.get('gap'))} gap_norm={_f(record.get('gap_norm'))} "
                f"stop={record.get('stop_reason') or '-'} t={record.get('time_s', 0):.2f}s",
                flush=True,
            )

    def error(self) -> None:
        self.counts["errors"] += 1

    # --- derived values ---------------------------------------------------------------------
    def rate_per_min(self) -> float:
        elapsed = max(1e-9, time.time() - self.phase_started)
        return 60.0 * self.phase_done / elapsed

    def eta_s(self) -> float | None:
        rate = self.rate_per_min()
        return None if rate <= 0 else 60.0 * (self.phase_total - self.phase_done) / rate

    def sample_system(self) -> None:
        try:
            import psutil

            disk = psutil.disk_usage(str(self.output if self.output.exists() else self.output.parent))
            mem = psutil.virtual_memory()
            self.system = {
                "cpu_percent": psutil.cpu_percent(percpu=True),
                "ram_free_gb": mem.available / 2**30,
                "ram_total_gb": mem.total / 2**30,
                "disk_free_gb": disk.free / 2**30,
            }
        except Exception:  # noqa: BLE001 - the monitor must never stop the run
            self.system = {}
        if time.time() - self.temperature_checked > 60:
            self.temperature = cpu_temperature()
            self.temperature_checked = time.time()
        self.system["temperature"] = self.temperature

    def snapshot(self) -> dict[str, Any]:
        now = time.time()
        return {
            "updated": now,
            "phase": self.phase,
            "message": self.message,
            "overall": {"done": self.done, "total": self.total, "elapsed_s": now - self.started},
            "phase_progress": {
                "done": self.phase_done,
                "total": self.phase_total,
                "rate_per_min": self.rate_per_min(),
                "eta_s": self.eta_s(),
                "elapsed_s": now - self.phase_started,
            },
            "workers": [
                {
                    "cpu": w.get("cpu"),
                    "method": w["method"],
                    "set": w["set"],
                    "size": w["size"],
                    "instance": w["instance"],
                    "seed": w.get("seed"),
                    "evals": w.get("evals"),
                    "budget": w.get("budget"),
                    "best_gap": w.get("best_gap"),
                    "running_s": now - w["started"],
                }
                for w in sorted(self.workers.values(), key=lambda w: (w.get("cpu") is None, w.get("cpu")))
            ],
            "recent": [
                {k: r.get(k) for k in ("method", "instance", "seed", "gap", "gap_norm", "stop_reason", "time_s")}
                for r in self.recent
            ],
            "methods": {m: {"runs": len(g), "median_gap": statistics.median(g)} for m, g in sorted(self.gaps.items())},
            "system": self.system,
            "counts": dict(self.counts),
        }

    def tick(self) -> None:
        """Periodic work: system sample, state file, plain summary."""
        now = time.time()
        if now - self.last_state >= self.state_interval_s:
            self.sample_system()
            write_atomic(self.output / "state" / "monitor.json", self.snapshot())
            self.last_state = now
        if self.plain and now - self.last_plain >= 60:
            eta = self.eta_s()
            print(
                f"[{time.strftime('%H:%M:%S')}] summary {self.phase}: {self.phase_done}/{self.phase_total}, "
                f"{self.rate_per_min():.1f} runs/min, ETA {_dur(eta)}, errors {self.counts['errors']}",
                flush=True,
            )
            self.last_plain = now

    # --- rich rendering ---------------------------------------------------------------------
    def render(self):
        from rich.console import Group
        from rich.panel import Panel
        from rich.progress_bar import ProgressBar
        from rich.table import Table
        from rich.text import Text

        snap = self.snapshot()
        head = Table.grid(expand=True)
        head.add_column(ratio=1)
        head.add_column(ratio=1)
        ph, ov = snap["phase_progress"], snap["overall"]
        head.add_row(
            Text(f"Всего: {ov['done']}/{ov['total']}  прошло {_dur(ov['elapsed_s'])}"),
            Text(
                f"Фаза {self.phase}: {ph['done']}/{ph['total']}  {ph['rate_per_min']:.1f} запусков/мин  "
                f"прошло {_dur(ph['elapsed_s'])}  ETA {_dur(ph['eta_s'])}"
            ),
        )
        head.add_row(
            ProgressBar(total=max(1, ov["total"]), completed=ov["done"]),
            ProgressBar(total=max(1, ph["total"]), completed=ph["done"]),
        )
        workers = Table(title="Воркеры", expand=True, show_lines=False)
        for col in ("ядро", "метод", "набор", "размер", "задача", "сид", "вызовы / бюджет", "лучший gap", "время"):
            workers.add_column(col, no_wrap=True)
        for w in snap["workers"]:
            workers.add_row(
                str(w["cpu"]),
                w["method"],
                w["set"],
                w["size"],
                w["instance"],
                str(w["seed"] or "-"),
                f"{w['evals'] or 0:,}/{w['budget'] or 0:,}",
                _f(w["best_gap"]),
                _dur(w["running_s"]),
            )
        recent = Table(title="Последние запуски", expand=True)
        for col in ("метод", "задача", "сид", "gap", "gap_norm", "остановка", "время"):
            recent.add_column(col, no_wrap=True)
        for r in snap["recent"]:
            recent.add_row(
                r["method"],
                r["instance"],
                str(r["seed"] or "-"),
                _f(r["gap"]),
                _f(r["gap_norm"]),
                r["stop_reason"] or "-",
                f"{(r['time_s'] or 0):.2f}s",
            )
        methods = Table(title=f"Методы в фазе {self.phase}", expand=True)
        methods.add_column("метод")
        methods.add_column("запусков", justify="right")
        methods.add_column("медиана gap, %", justify="right")
        for m, s in snap["methods"].items():
            methods.add_row(m, str(s["runs"]), _f(s["median_gap"]))
        sysd = snap["system"]
        cpu = sysd.get("cpu_percent") or []
        cores = " ".join(f"{i}:{v:.0f}" for i, v in enumerate(cpu)) or NO_DATA
        c = snap["counts"]
        err_style = "bold red" if c["errors"] or c["infeasible"] else ""
        system = Text.assemble(
            f"CPU % по ядрам: {cores}\n",
            f"ОЗУ свободно: {sysd.get('ram_free_gb', 0):.1f} / {sysd.get('ram_total_gb', 0):.1f} ГБ   "
            f"диск свободно: {sysd.get('disk_free_gb', 0):.0f} ГБ   ",
            f"температура CPU: {sysd.get('temperature', NO_DATA)}\n",
            (
                f"ошибки: {c['errors']}  недопустимые планы: {c['infeasible']}  повторы: {c['retries']}  "
                f"пропущено (уже готово): {c['skipped']}",
                err_style,
            ),
        )
        parts = [head, workers, recent, methods, Panel(system, title="Система")]
        if self.message:
            parts.append(Panel(Text(self.message, style="bold yellow")))
        return Group(*parts)


def _f(v: Any) -> str:
    return "-" if v is None else f"{float(v):.3g}"


def _dur(s: float | None) -> str:
    if s is None:
        return "-"
    s = int(s)
    return f"{s // 3600}:{(s % 3600) // 60:02d}:{s % 60:02d}"
