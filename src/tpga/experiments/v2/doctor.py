"""``tpga-exp doctor``: read-only checks of the machine before a long run. It changes nothing."""

from __future__ import annotations

import contextlib
import json
import re
import socket
import subprocess
import sys
import time
from dataclasses import dataclass

from tpga.experiments.v2.config import ConfigV2

OVERLAYS = {
    "961cc777-2547-4f9d-8174-7d86181b8a7a": "best power efficiency",
    "00000000-0000-0000-0000-000000000000": "balanced (recommended)",
    "3af9b8d9-7c97-431d-ad78-34a8bfea439f": "better performance",
    "ded574b5-45a0-4f42-8737-46345c09c238": "best performance",
}
PERFORMANCE_PLANS = (
    "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c",  # High performance
    "e9a42b02-d5df-448d-aa00-03f14749eb61",
)  # Ultimate performance


@dataclass
class Check:
    ok: bool
    name: str
    detail: str
    hint: str = ""

    def line(self) -> str:
        tag = "OK        " if self.ok else "ВНИМАНИЕ  "
        return f"{tag}{self.name}: {self.detail}" + ("" if self.ok or not self.hint else f"\n          → {self.hint}")


def _run(cmd: list[str], encoding: str = "oem") -> str:
    try:
        out = subprocess.run(cmd, capture_output=True, timeout=20, check=False).stdout
        return out.decode(encoding if sys.platform == "win32" else "utf-8", errors="replace")
    except (OSError, subprocess.SubprocessError):
        return ""


def _powershell(command: str) -> str:
    return _run(["powershell", "-NoProfile", "-Command", command], encoding="utf-8").strip()


def ac_power() -> Check:
    status = _powershell("(Get-CimInstance Win32_Battery).BatteryStatus")
    if not status:
        return Check(True, "Питание", "батарея не найдена (настольный компьютер или нет данных)")
    on_ac = status.strip() == "2"
    return Check(
        on_ac,
        "Питание от сети",
        "да" if on_ac else f"нет (BatteryStatus={status})",
        "Подключите зарядное устройство: на батарее частоты снижаются и прогон может прерваться.",
    )


def power_mode() -> list[Check]:
    out: list[Check] = []
    scheme = _run(["powercfg", "/getactivescheme"])
    guid = re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", scheme.lower())
    overlay_name = None
    if sys.platform == "win32":
        try:
            import winreg

            with winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\User\PowerSchemes"
            ) as key:
                overlay, _ = winreg.QueryValueEx(key, "ActiveOverlayAcPowerScheme")
                overlay_name = OVERLAYS.get(str(overlay).lower(), f"unknown overlay {overlay}")
        except OSError:
            overlay_name = None
    plan_ok = bool(guid and guid.group(0) in PERFORMANCE_PLANS)
    overlay_ok = overlay_name == "best performance"
    out.append(
        Check(
            plan_ok or overlay_ok,
            "Схема питания",
            scheme.strip() or "нет данных",
            "Параметры → Система → Питание и батарея → Режим питания: «Максимальная производительность» "
            "(при питании от сети). Проверка: powercfg /getactivescheme и повторный doctor.",
        )
    )
    out.append(
        Check(
            overlay_ok,
            "Режим питания Windows 11 (от сети)",
            overlay_name or "нет данных",
            "Тот же переключатель «Режим питания» → «Максимальная производительность».",
        )
    )
    return out


def _ac_index(subgroup: str, setting: str) -> int | None:
    text = _run(["powercfg", "/q", "SCHEME_CURRENT", subgroup, setting])
    values = re.findall(r":\s*(0x[0-9a-fA-F]+)\s*$", text, flags=re.M)
    # the last two indices are the AC and DC values, in that order
    return int(values[-2], 16) if len(values) >= 2 else None


def sleep_settings() -> list[Check]:
    items = [
        ("SUB_SLEEP", "STANDBYIDLE", "Сон от сети", "powercfg /change standby-timeout-ac 0"),
        ("SUB_SLEEP", "HIBERNATEIDLE", "Гибернация от сети", "powercfg /change hibernate-timeout-ac 0"),
        ("SUB_VIDEO", "VIDEOIDLE", "Гашение экрана от сети", "powercfg /change monitor-timeout-ac 0"),
    ]
    out = []
    for sub, setting, name, cmd in items:
        v = _ac_index(sub, setting)
        if v is None:
            out.append(Check(False, name, "нет данных", f"Проверьте вручную; отключить: {cmd}"))
        else:
            disabled = v == 0
            detail = "отключено" if disabled else f"через {v // 60} мин"
            ok = disabled or setting == "VIDEOIDLE"
            out.append(Check(ok, name, detail, f"Перед прогоном: {cmd} (см. docs/v0.4/HEAVY_RUN.md, шаг 2)."))
    return out


def resources(cfg: ConfigV2, expected_bytes: float) -> list[Check]:
    import psutil

    out_dir = cfg.output if cfg.output.exists() else cfg.root
    disk = psutil.disk_usage(str(out_dir))
    mem = psutil.virtual_memory()
    need = 3 * expected_bytes
    return [
        Check(
            disk.free >= need,
            "Свободное место на диске",
            f"{disk.free / 2**30:.0f} ГБ; нужно не меньше {need / 2**30:.1f} ГБ (3 × оценка результатов)",
            "Освободите место на диске с каталогом проекта.",
        ),
        Check(
            mem.available >= 8 * 2**30,
            "Свободная ОЗУ",
            f"{mem.available / 2**30:.1f} из {mem.total / 2**30:.0f} ГБ",
            "Закройте браузер, IDE и другие программы (нужно не меньше 8 ГБ свободной памяти).",
        ),
    ]


def numba_cache() -> Check:
    t0 = time.perf_counter()
    from tpga.experiments.v2.runner import warm_up

    warm_up()
    dt = time.perf_counter() - t0
    return Check(True, "Ядра Numba", f"готовы за {dt:.1f} с" + (" (из кэша)" if dt < 5 else " (скомпилированы сейчас)"))


def package_versions(cfg: ConfigV2) -> Check:
    from tpga.experiments.v2.manifest import path, versions

    p = path(cfg)
    now = versions()
    if not p.exists():
        return Check(
            True,
            "Версии пакетов",
            "манифеста прогона ещё нет; будут записаны при запуске: "
            + ", ".join(f"{k} {v}" for k, v in now.items() if v),
        )
    first = json.loads(p.read_text(encoding="utf-8"))["invocations"][0]["packages"]
    diff = {k: (first.get(k), v) for k, v in now.items() if first.get(k) != v}
    return Check(
        not diff,
        "Версии пакетов",
        "совпадают с манифестом" if not diff else f"отличаются: {diff}",
        "Продолжение прогона на других версиях смешает результаты; верните версии из манифеста.",
    )


def busy_processes(threshold: float = 25.0) -> Check:
    import psutil

    procs = list(psutil.process_iter(["pid", "name"]))
    for p in procs:
        with contextlib.suppress(psutil.Error, OSError):
            p.cpu_percent(None)
    time.sleep(1.5)
    heavy = []
    me = psutil.Process().pid
    for p in procs:
        try:
            if p.pid in (0, me):
                continue
            v = p.cpu_percent(None)
            if v >= threshold:
                heavy.append(f"{p.info['name']} ({v:.0f}%)")
        except (psutil.Error, OSError):
            continue
    return Check(
        not heavy,
        "Процессы, нагружающие CPU",
        ", ".join(heavy) or "нет",
        "Закройте их на время прогона (браузер, синхронизация облака, IDE с индексацией).",
    )


def dev_servers(ports: tuple[int, ...] = (3000, 8000, 8010)) -> Check:
    busy = []
    for port in ports:
        with socket.socket() as s:
            s.settimeout(0.3)
            if s.connect_ex(("127.0.0.1", port)) == 0:
                busy.append(port)
    return Check(
        not busy,
        "Dev-серверы веб-платформы",
        "не запущены" if not busy else f"слушают порты {busy}",
        "Остановите платформу: powershell -ExecutionPolicy Bypass -File scripts/dev.ps1 -Stop "
        "(другие программы на этих портах закройте сами).",
    )


def run(cfg: ConfigV2, expected_bytes: float = 2e9) -> list[Check]:
    checks: list[Check] = [
        ac_power(),
        *power_mode(),
        *sleep_settings(),
        *resources(cfg, expected_bytes),
        numba_cache(),
        package_versions(cfg),
        busy_processes(),
        dev_servers(),
    ]
    return checks
