import asyncio
import websockets

async def connect_to_server():
   async with websockets.connect('ws://localhost:8000') as websocket:
      while True:
         # Get user input
         message = input("Enter message: ")

         # Send the message to the server
         await websocket.send(message)

         # Receive a message from the server
         response = await websocket.recv()

         # Print the received message
         print("Received:", response)

# Connect the WebSocket client
asyncio.get_event_loop().run_until_complete(connect_to_server())