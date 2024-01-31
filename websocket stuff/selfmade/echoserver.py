#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        print (message)
        message = await websocket.recv()
        await websocket.broadcast(CONNECTIONS, message)

CONNECTIONS = set()
async def handler(websocket):
    CONNECTIONS.add(websocket)
    print(CONNECTIONS)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)
async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
asyncio.run(handler())

