"""Crash-safe result storage: JSON Lines parts written to a temporary file and renamed into place.

A part is never visible half-written, so an interruption (Ctrl+C, power loss) loses at most the records
still in memory; they are recomputed on the next start because their keys are not on disk.
"""

from __future__ import annotations

import json
import os
import time
import traceback
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Any


class PartWriter:
    """Buffer records and write them as ``<prefix>-<time>-<n>.jsonl`` parts (temporary file + rename)."""

    def __init__(self, directory: Path, prefix: str, max_records: int = 50, max_age_s: float = 5.0) -> None:
        self.dir = directory
        self.dir.mkdir(parents=True, exist_ok=True)
        self.prefix = prefix
        self.max_records = max_records
        self.max_age_s = max_age_s
        self.buffer: list[dict[str, Any]] = []
        self.oldest = 0.0
        self.count = 0

    def add(self, records: Iterable[dict[str, Any]]) -> None:
        for r in records:
            if not self.buffer:
                self.oldest = time.time()
            self.buffer.append(r)
        if len(self.buffer) >= self.max_records or (self.buffer and time.time() - self.oldest >= self.max_age_s):
            self.flush()

    def flush(self) -> None:
        if not self.buffer:
            return
        self.count += 1
        name = f"{self.prefix}-{time.strftime('%Y%m%d-%H%M%S')}-{os.getpid()}-{self.count:05d}.jsonl"
        final = self.dir / name
        tmp = self.dir / (name + ".tmp")
        with tmp.open("w", encoding="utf-8", newline="\n") as fh:
            for r in self.buffer:
                fh.write(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n")
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, final)
        self.buffer = []


def read_parts(directory: Path, prefix: str) -> Iterator[dict[str, Any]]:
    """All records of the finished parts; leftover ``.tmp`` files of an interrupted write are ignored."""
    if not directory.exists():
        return
    for path in sorted(directory.glob(f"{prefix}-*.jsonl")):
        with path.open(encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    yield json.loads(line)


def clean_temporary(directory: Path) -> int:
    """Remove ``.tmp`` files left by an interrupted write; returns how many were removed."""
    if not directory.exists():
        return 0
    removed = 0
    for tmp in directory.glob("*.jsonl.tmp"):
        tmp.unlink()
        removed += 1
    return removed


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    """Append one line (logs and errors; a torn last line is skipped by :func:`read_jsonl`)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(record, ensure_ascii=False, separators=(",", ":"), default=str) + "\n")
        fh.flush()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            out.append(json.loads(line))
        except ValueError:
            continue  # a torn last line after a hard interruption
    return out


def error_record(task: dict[str, Any], exc: BaseException) -> dict[str, Any]:
    return {
        "time": time.time(),
        "key": "|".join(str(task.get(k, "")) for k in ("phase", "set", "instance", "method", "config", "seed")),
        "error": repr(exc),
        "traceback": "".join(traceback.format_exception(type(exc), exc, exc.__traceback__)),
    }


def write_atomic(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1, default=str), encoding="utf-8", newline="\n")
    os.replace(tmp, path)
