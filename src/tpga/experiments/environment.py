"""Machine description, CPU core classes and per-process CPU pinning."""

from __future__ import annotations

import contextlib
import ctypes
import datetime as dt
import os
import platform
import subprocess
import sys
from collections.abc import Iterator
from importlib import metadata
from pathlib import Path
from typing import Any

THREAD_VARIABLES = ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMBA_NUM_THREADS")


def single_thread_environment() -> None:
    """Limit numerical libraries to one thread; must run before NumPy is imported in a process."""
    for name in THREAD_VARIABLES:
        os.environ[name] = "1"


def cpu_classes() -> dict[int, int]:
    """Efficiency class of every logical processor (Windows; higher is faster). Empty elsewhere."""
    if sys.platform != "win32":
        return {}
    k32 = ctypes.windll.kernel32  # type: ignore[attr-defined,unused-ignore]
    size = ctypes.c_ulong(0)
    k32.GetSystemCpuSetInformation(None, 0, ctypes.byref(size), None, 0)
    buf = ctypes.create_string_buffer(size.value)
    if not k32.GetSystemCpuSetInformation(buf, size, ctypes.byref(size), None, 0):  # pragma: no cover
        return {}
    raw, out, off = buf.raw, {}, 0
    while off < size.value:
        entry = int.from_bytes(raw[off : off + 4], "little")
        out[raw[off + 14]] = raw[off + 18]
        off += entry
    return out


def pin_to_cpu(cpu: int) -> bool:
    """Restrict the current process to one logical processor."""
    if sys.platform == "win32":
        k32 = ctypes.windll.kernel32  # type: ignore[attr-defined,unused-ignore]
        k32.GetCurrentProcess.restype = ctypes.c_void_p  # pseudo-handle -1 must stay 64-bit
        k32.SetProcessAffinityMask.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
        k32.SetProcessAffinityMask.restype = ctypes.c_int
        return bool(k32.SetProcessAffinityMask(k32.GetCurrentProcess(), 1 << cpu))
    if hasattr(os, "sched_setaffinity"):  # pragma: no cover - Linux
        os.sched_setaffinity(0, {cpu})
        return True
    return False  # pragma: no cover


ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001


@contextlib.contextmanager
def keep_awake() -> Iterator[bool]:
    """Keep Windows from sleeping because of idleness while the block runs (no admin rights, no setting changed).

    ``SetThreadExecutionState`` holds a request of this process only; Windows drops it when the block ends or the
    process exits. It does not stop a sleep the user asks for (lid, power button, Start menu) or a restart.
    Yields whether the request was accepted (False on other systems).
    """
    ok = False
    if sys.platform == "win32":
        k32 = ctypes.windll.kernel32  # type: ignore[attr-defined,unused-ignore]
        k32.SetThreadExecutionState.restype = ctypes.c_uint
        ok = bool(k32.SetThreadExecutionState(ctypes.c_uint(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)))
    try:
        yield ok
    finally:
        if ok:
            ctypes.windll.kernel32.SetThreadExecutionState(ctypes.c_uint(ES_CONTINUOUS))  # type: ignore[attr-defined,unused-ignore]


def _run(cmd: list[str], encoding: str | None = None) -> str:
    try:
        out = subprocess.run(cmd, capture_output=True, timeout=30, check=False).stdout
        # console tools such as powercfg write in the OEM code page, PowerShell and git in the ANSI/UTF-8 one
        return out.decode(encoding or "utf-8", errors="replace").strip()
    except (OSError, subprocess.SubprocessError):  # pragma: no cover
        return ""


def _version(package: str) -> str | None:
    try:
        return metadata.version(package)
    except metadata.PackageNotFoundError:
        return None


def _highs_version() -> str | None:
    try:  # SciPy >= 1.15 bundles highspy bindings
        from scipy.optimize._highspy._core import (  # type: ignore[import-not-found,unused-ignore]
            HIGHS_VERSION_MAJOR,
            HIGHS_VERSION_MINOR,
            HIGHS_VERSION_PATCH,
        )

        return f"{HIGHS_VERSION_MAJOR}.{HIGHS_VERSION_MINOR}.{HIGHS_VERSION_PATCH} (bundled with SciPy)"
    except ImportError:
        return None


def describe(root: Path) -> dict[str, Any]:
    """Facts about the machine and the software, gathered when the experiment runs."""
    info: dict[str, Any] = {
        "recorded_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "os": platform.platform(),
        "machine": platform.machine(),
        "python": sys.version.split()[0],
        "packages": {p: _version(p) for p in ("tpga", "numpy", "scipy", "numba", "llvmlite", "pandas", "matplotlib")},
        "highs": _highs_version(),
        "logical_processors": os.cpu_count(),
        "thread_environment": {name: os.environ.get(name) for name in THREAD_VARIABLES},
    }
    classes = cpu_classes()
    if classes:
        top = max(classes.values())
        info["cpu_efficiency_class"] = {str(k): v for k, v in sorted(classes.items())}
        info["performance_cores"] = sorted(k for k, v in classes.items() if v == top)
        info["efficiency_cores"] = sorted(k for k, v in classes.items() if v != top)
    if sys.platform == "win32":
        ps = "powershell -NoProfile -Command"
        info["cpu"] = _run([*ps.split(), "(Get-CimInstance Win32_Processor).Name"])
        info["physical_cores"] = _run([*ps.split(), "(Get-CimInstance Win32_Processor).NumberOfCores"])
        ram = _run([*ps.split(), "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory"])
        info["ram_gb"] = round(int(ram) / 2**30, 1) if ram.isdigit() else None
        info["power_scheme"] = _run(["powercfg", "/getactivescheme"], encoding="oem")
        battery = _run([*ps.split(), "(Get-CimInstance Win32_Battery).BatteryStatus"])
        # Win32_Battery.BatteryStatus 2 means the system has access to AC power
        info["on_ac_power"] = None if not battery else battery.strip() == "2"
    else:  # pragma: no cover
        info["cpu"] = platform.processor()
    info["git_commit"] = _run(["git", "-C", str(root), "rev-parse", "HEAD"]) or None
    # the runner itself rewrites tracked files under paper_artifacts/, so they do not count as changes to the code
    status = ["git", "-C", str(root), "status", "--porcelain", "--untracked-files=no", "--", ".", ":!paper_artifacts"]
    info["git_dirty"] = bool(_run(status))
    return info
