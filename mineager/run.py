# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING

from .websocket import run as run_ws
from .websocket import default_logger

if TYPE_CHECKING:
    from ssl import SSLContext

    from websockets.typing import LoggerLike


__all__ = ("run",)


async def run(
    *,
    host: str = "0.0.0.0",
    port: int = 6900,
    ssl: SSLContext | None = None,
    logger: LoggerLike | None = default_logger,
):
    await run_ws(host=host, port=port, ssl=ssl, logger=logger)
