# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING
from asyncio import Future
from ssl import SSLContext

from websockets.server import serve

from .handler import handle

if TYPE_CHECKING:
    from websockets.typing import LoggerLike
    from websockets.server import WebSocketServer

__all__ = ("run_ws",)
stop = Future()


async def run_ws(
    *, host: str, port: int, ssl: SSLContext | None, logger: LoggerLike | None
) -> WebSocketServer:
    return await serve(ws_handler=handle, host=host, port=port, ssl=ssl, logger=logger)
