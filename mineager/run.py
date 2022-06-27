# SPDX-License-Identifier: MIT

from .websocket import run as run_ws


async def run(*, host: str = "127.0.0.1", port: int = 6900):
    await run_ws(host=host, port=port)
