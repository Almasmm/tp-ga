"""Main run of v0.4, phase by phase, with a report after every phase (amendment 7).

Starts ``tpga-exp run --phase <name> --plain`` for every phase in the order below. A phase that ends with an
error is started again (the runner skips every run already on disk), at most ``--retries`` times; a phase
that still fails is left and the next one starts, so one failure does not hold back the rest. After a phase
``tpga-exp report`` runs in the background at idle priority on one logical processor and rewrites the tables,
the figures and ``PROGRESS.md``. Before the timing phase the script waits for that report, so that timing
runs alone. The script keeps the machine awake while it runs and writes ``logs/main-run.log``.

    python scripts/run_main.py --config experiments/paper-v2.yaml

Start it again with the same command after a crash or a reboot: finished runs are not repeated.
"""

# ruff: noqa: E402
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

from tpga.experiments.environment import keep_awake, single_thread_environment

single_thread_environment()  # before NumPy is imported: otherwise OpenBLAS commits about 1.5 GiB here

from tpga.experiments.v2.cli import PHASES
from tpga.experiments.v2.config import ConfigV2
from tpga.experiments.v2.instances import build
from tpga.experiments.v2.methods import key_of
from tpga.experiments.v2.storage import read_parts
from tpga.experiments.v2.tasks import phase_tasks

IDLE = getattr(subprocess, "IDLE_PRIORITY_CLASS", 0)
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)


def exe(name: str) -> str:
    return str(Path(sys.executable).with_name(name + (".exe" if sys.platform == "win32" else "")))


def remaining(cfg: ConfigV2, phase: str) -> int:
    """Planned runs of the phase that are not on disk."""
    done = {key_of(r) for r in read_parts(cfg.output / "raw" / "runs", "runs")}
    return sum(key_of(t) not in done for t in phase_tasks(cfg, phase, build(cfg)))


def start_report(config: str, log_dir: Path, phase: str) -> subprocess.Popen:
    """``tpga-exp report`` at idle priority, pinned to the last logical processor."""
    out = (log_dir / f"report-after-{phase}.txt").open("w", encoding="utf-8")
    proc = subprocess.Popen(
        [exe("tpga-exp"), "report", "--config", config],
        stdout=out,
        stderr=subprocess.STDOUT,
        creationflags=IDLE | NO_WINDOW,
    )
    try:
        import os

        import psutil

        psutil.Process(proc.pid).cpu_affinity([(os.cpu_count() or 1) - 1])
    except Exception:  # noqa: BLE001 - the priority alone already keeps the report out of the way
        pass
    return proc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", required=True)
    ap.add_argument("--phase", action="append", choices=PHASES, help="default: every phase, in the run order")
    ap.add_argument("--retries", type=int, default=3)
    args = ap.parse_args()
    cfg = ConfigV2.load(args.config)
    log_dir = cfg.output / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / "main-run.log"

    def say(text: str) -> None:
        line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} {text}"
        print(line, flush=True)
        with log_path.open("a", encoding="utf-8", newline="\n") as f:
            f.write(line + "\n")

    phases = args.phase or list(PHASES)
    say(f"main run started: phases {', '.join(phases)}")
    report: subprocess.Popen | None = None
    failed: list[str] = []
    with keep_awake():
        for phase in phases:
            if phase == "timing" and report is not None:
                say("waiting for the report before the timing phase (timing runs alone)")
                report.wait()
            left = remaining(cfg, phase)
            say(f"phase {phase}: {left} runs to do")
            attempt = 0
            while left and attempt <= args.retries:
                attempt += 1
                console = (log_dir / f"run-{phase}-console.txt").open("a", encoding="utf-8")
                code = subprocess.call(
                    [exe("tpga-exp"), "run", "--config", args.config, "--phase", phase, "--plain"],
                    stdout=console,
                    stderr=subprocess.STDOUT,
                )
                console.close()
                left = remaining(cfg, phase)
                say(f"phase {phase}: attempt {attempt} ended with code {code}, {left} runs left")
                if code == 130:  # interrupted from the console: stop the whole run
                    say("interrupted; start the same command again to continue")
                    return 130
                if left:
                    time.sleep(20)
            if left:
                failed.append(phase)
                say(f"phase {phase}: NOT FINISHED, {left} runs left after {attempt} attempts")
            else:
                say(f"phase {phase}: done")
            if report is not None:
                report.wait()  # one report at a time
            report = start_report(args.config, log_dir, phase)
            say(f"report started after {phase} (idle priority, one processor)")
        if report is not None:
            report.wait()
            say(f"final report ended with code {report.returncode}")
    say("main run finished" + (f"; unfinished phases: {', '.join(failed)}" if failed else "; every phase is done"))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
