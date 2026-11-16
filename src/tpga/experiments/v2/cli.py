"""``tpga-exp``: doctor, pilot, tune, run and report for the v0.4 experiment."""

from __future__ import annotations

# thread limits must be set before NumPy is imported here or in a worker
from tpga.experiments.environment import single_thread_environment

single_thread_environment()

import argparse  # noqa: E402
import os  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from typing import Any  # noqa: E402

PHASES = ("reference", "main", "stagnation", "legacy", "factorial", "timing")


def _cfg(path: str):
    from tpga.experiments.v2.config import ConfigV2

    return ConfigV2.load(path)


def cmd_doctor(args: argparse.Namespace) -> int:
    from tpga.experiments.v2 import doctor

    checks = doctor.run(_cfg(args.config))
    for c in checks:
        print(c.line())
    warnings = sum(not c.ok for c in checks)
    print(f"\n{len(checks) - warnings} OK, {warnings} ВНИМАНИЕ. doctor ничего не меняет.")
    return 0


def cmd_pilot(args: argparse.Namespace) -> int:
    from tpga.experiments.v2 import pilot

    result = pilot.run(_cfg(args.config))
    print((_cfg(args.config).output / "pilot" / "PILOT.md").read_text(encoding="utf-8"))
    return 0 if result else 1


def cmd_tune(args: argparse.Namespace) -> int:
    from tpga.experiments.v2 import tune

    frozen = tune.run(_cfg(args.config), args.method or None)
    for name, value in frozen["best_objective"].items():
        print(f"{name}: mean gap {value:.3f} %  {frozen['parameters'][name]}")
    return 0


def _cpus(cfg: Any, phase: str) -> list[int]:
    from tpga.experiments import environment

    if phase == "timing":
        classes = environment.cpu_classes()
        if classes:
            top = max(classes.values())
            return sorted(c for c, v in classes.items() if v == top)
    return list(range(min(int(cfg.raw.get("workers", 24)), os.cpu_count() or 1)))


def cmd_run(args: argparse.Namespace) -> int:
    from tpga.experiments.v2 import manifest, runner
    from tpga.experiments.v2.instances import build
    from tpga.experiments.v2.methods import key_of
    from tpga.experiments.v2.monitor import Monitor
    from tpga.experiments.v2.storage import read_parts
    from tpga.experiments.v2.tasks import phase_tasks

    cfg = _cfg(args.config)
    if args.priority:
        cfg.raw["priority"] = args.priority
    phases = args.phase or list(PHASES)
    runner.set_priority(str(cfg.raw.get("priority", "above_normal")))
    runner.warm_up()
    items = build(cfg)
    man = manifest.start(cfg, phases)
    log_path = cfg.output / "logs" / f"run-{time.strftime('%Y%m%d')}.jsonl"
    monitor = Monitor(cfg.output, plain=args.plain, state_interval_s=float(cfg.raw.get("state_interval_s", 3)))
    plans = {ph: phase_tasks(cfg, ph, items) for ph in phases}
    monitor.total = sum(len(t) for t in plans.values())
    status = 0
    with runner.Interrupt() as interrupt:
        live = None
        if not args.plain:
            from rich.live import Live

            live = Live(monitor.render(), refresh_per_second=2, screen=False)
            live.start()
        try:
            for ph in phases:
                if interrupt.count:
                    break
                tasks = plans[ph]
                if ph != "reference":
                    z = {
                        r["instance"]: r["cost"]
                        for r in read_parts(cfg.output / "raw" / "runs", "runs")
                        if r["phase"] == "reference" and r["method"] == "LP"
                    }
                    need = [t for t in tasks if t["kind"] not in ("lp",)]
                    missing = sorted({t["instance"] for t in need if t["instance"] not in z})
                    if missing:
                        monitor.message = f"Нет оптимума для {missing[:3]}…: сначала фаза reference."
                        status = 2
                        break
                    for t in need:
                        t["z_star"] = z[t["instance"]]
                started = time.time()
                if ph == "reference":
                    # the classical methods need the optimum for their gap: LP first, then the rest
                    lp = [t for t in tasks if t["kind"] == "lp"]
                    counts = runner.execute_tasks(cfg, ph, lp, _cpus(cfg, ph), monitor, interrupt, log_path, live)
                    z = {
                        r["instance"]: r["cost"]
                        for r in read_parts(cfg.output / "raw" / "runs", "runs")
                        if r["phase"] == "reference" and r["method"] == "LP"
                    }
                    rest = [{**t, "z_star": z.get(t["instance"])} for t in tasks if t["kind"] != "lp"]
                    rest = [t for t in rest if t["z_star"] is not None]
                    if not interrupt.count:
                        more = runner.execute_tasks(cfg, ph, rest, _cpus(cfg, ph), monitor, interrupt, log_path, live)
                        counts = {k: counts[k] + more[k] for k in counts}
                else:
                    counts = runner.execute_tasks(cfg, ph, tasks, _cpus(cfg, ph), monitor, interrupt, log_path, live)
                manifest.phase_done(cfg, man, ph, started, counts, interrupt.count > 0)
                if counts["errors"]:
                    status = 1
        finally:
            if live is not None:
                live.update(monitor.render())
                live.stop()
    done = {key_of(r) for r in read_parts(cfg.output / "raw" / "runs", "runs")}
    remaining = sum(1 for ph in phases for t in plans[ph] if key_of(t) not in done)
    print(
        f"Готово записей: {len(done)}; осталось в запрошенных фазах: {remaining}."
        + (" Прогон прерван; повторный запуск той же команды продолжит с места остановки." if interrupt.count else "")
    )
    return status if not interrupt.count else 130


def cmd_report(args: argparse.Namespace) -> int:
    from tpga.experiments.reporting import build as build_report

    summary = build_report.generate(_cfg(args.config))
    print(build_report.summary_text(summary))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="tpga-exp", description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    for name, fn, helptext in (
        ("doctor", cmd_doctor, "read-only checks of the machine"),
        ("pilot", cmd_pilot, "short runs and an estimate of the full plan"),
        ("tune", cmd_tune, "tune GA and SA on training instances and freeze the parameters"),
        ("run", cmd_run, "run phases (resumable)"),
        ("report", cmd_report, "tables, figures and documents from the raw records"),
    ):
        p = sub.add_parser(name, help=helptext)
        p.add_argument("--config", required=True)
        p.set_defaults(fn=fn)
        if name == "run":
            p.add_argument("--phase", action="append", choices=PHASES)
            p.add_argument("--plain", action="store_true", help="one line per finished run (no TTY needed)")
            p.add_argument("--priority", choices=["normal", "above_normal"])
        if name == "tune":
            p.add_argument("--method", action="append", choices=["GA-rand", "GA-cost", "SA-rand", "SA-cost"])
    args = ap.parse_args(argv)
    return int(args.fn(args))


if __name__ == "__main__":
    sys.exit(main())
