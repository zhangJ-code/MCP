import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://localhost:8765") as websocket:
        message = "Hello, Server!"
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received: {response}")

if __name__ == "__main__":
    asyncio.run(send_message())
