"""``GET /monitor/state``: the state file the v0.4 runner rewrites every few seconds (read only).

The platform cannot start, stop or change a run; it only shows the last state the runner wrote.
"""

from __future__ import annotations

import json
import time
from typing import Any

from fastapi import APIRouter

from .paths import paper_v2_dir

router = APIRouter(prefix="/monitor", tags=["Run monitor"])

STALE_AFTER_S = 60.0


@router.get("/state")
def state() -> dict[str, Any]:
    path = paper_v2_dir() / "state" / "monitor.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        mtime = path.stat().st_mtime
    except (OSError, ValueError):
        return {"available": False}
    age = max(0.0, time.time() - mtime)
    return {"available": True, "age_s": age, "stale": age > STALE_AFTER_S, "state": data}
