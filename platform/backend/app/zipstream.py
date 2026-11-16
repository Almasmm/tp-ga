"""Zip archives written to a temporary file and streamed from disk (not built in memory)."""

from __future__ import annotations

import os
import tempfile
import zipfile
from collections.abc import Iterable
from pathlib import Path

from fastapi.responses import FileResponse
from starlette.background import BackgroundTask


def zip_response(files: Iterable[tuple[Path, Path]], filename: str) -> FileResponse:
    """``files``: (path on disk, path inside the archive). The temporary file is removed after sending."""
    fd, tmp = tempfile.mkstemp(suffix=".zip", prefix="tpga-")
    os.close(fd)
    try:
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zf:
            for src, arc in files:
                zf.write(src, arc)
    except BaseException:
        os.unlink(tmp)
        raise
    return FileResponse(
        tmp,
        media_type="application/zip",
        filename=filename,
        background=BackgroundTask(os.unlink, tmp),
    )
