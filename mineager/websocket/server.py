# SPDX-License-Identifier: MIT

from asyncio import Future

from websockets.server import serve

from .handler import handle

stop = Future()


async def run(*, host: str, port: int):
    async with serve(ws_handler=handle, host=host, port=port):
        await stop
