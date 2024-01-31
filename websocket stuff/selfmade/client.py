#!/usr/bin/env python

import asyncio
from websockets.sync.client import connect

def sendMessage(msg):
    with connect("ws://localhost:8765") as websocket:
        websocket.send(msg)
        message = websocket.recv()
        print("Received message: " + message)
async def receiveMessage():
    async with connect("ws://localhost:8765") as websocket:
        async for message in websocket:
            print("Received message: " + message)
            return message

async def echo(websocket):
    async for message in websocket:
        print (message)
        message = await websocket.recv()
        await websocket.send(message)

msg = input("Message: ")
sendMessage(msg)
asyncio.run(echo(websocket))