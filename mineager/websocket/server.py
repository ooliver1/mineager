# SPDX-License-Identifier: MIT

from asyncio import Future
from websockets.server import serve

from .handler import handle


stop = Future()


async def run():
    async with serve(ws_handler=handle):
        await stop
