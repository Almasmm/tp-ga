"""Command line of the additional experiment v3."""

from __future__ import annotations

import argparse
import json
import sys
import time

from tpga.experiments import environment

environment.single_thread_environment()  # before NumPy starts its thread pools

from tpga.experiments.v3 import core, ext, report, rev, rev_report  # noqa: E402

COMMANDS = {
    "kselect": core.kselect,
    "pilot": core.pilot,
    "run": core.run,
    "extend": core.extend,
    "benchmark": core.benchmark,
    "report": report.report,
}
# a configuration with ``extension: true`` (amendment 9.2-9.4) has its own commands
EXTENSION = {"tune": ext.tune, "run": ext.run, "report": ext.report}
# a configuration with ``review: true`` (amendment 10)
REVIEW = {
    "pilot": rev.pilot,
    "tune": rev.tune,
    "rivals": rev.rivals,
    "generator": rev.generator,
    "degenerate": rev.degenerate,
    "public": rev.public,
    "timing": rev.timing,
    "mipdefault": rev.mipdefault,
    "report": rev_report.report,
}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m tpga.experiments.v3", description=__doc__)
    ap.add_argument("command", choices=sorted({*COMMANDS, *EXTENSION, *REVIEW}))
    ap.add_argument("--config", required=True)
    ap.add_argument("--minutes", type=float, help="review configuration: time of this command, beyond the limit")
    args = ap.parse_args(argv)
    cfg = core.ConfigV3.load(args.config)
    commands = REVIEW if cfg.raw.get("review") else EXTENSION if cfg.raw.get("extension") else COMMANDS
    if args.minutes is not None:
        if not cfg.raw.get("review"):
            ap.error("--minutes belongs to the review configuration")
        cfg.raw["_minutes"] = args.minutes
    if args.command not in commands:
        ap.error(f"{args.command} is not a command of this configuration; it has {', '.join(sorted(commands))}")
    if args.command in ("kselect", "pilot", "extend") and cfg.raw["problem"] != "linear" and commands is COMMANDS:
        ap.error(f"{args.command} belongs to the linear configuration")
    if args.command == "benchmark" and "benchmark" not in cfg.raw:
        ap.error("the configuration has no benchmark section")
    started = time.time()
    state = core.code_state(cfg)
    result = commands[args.command](cfg)
    core.record_invocation(cfg, args.command, started, result, state)
    print(json.dumps(result, indent=1, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
