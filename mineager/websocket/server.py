# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING
from asyncio import Future
from ssl import SSLContext

from websockets.server import serve

from .handler import handle

if TYPE_CHECKING:
    from websockets.typing import LoggerLike

__all__ = ("run",)
stop = Future()


async def run(
    *, host: str, port: int, ssl: SSLContext | None, logger: LoggerLike | None
):
    async with serve(
        ws_handler=handle, host=host, port=port, ssl_context=ssl, logger=logger
    ):
        await stop
