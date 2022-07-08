# SPDX-License-Identifier: MIT

from websockets.server import WebSocketServerProtocol


async def handle(ws: WebSocketServerProtocol):
    async for message in ws:
        print(message)
