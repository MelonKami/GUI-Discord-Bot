import asyncio, websockets

async def websocket_ping(self, websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

class Websocket():
    def __init__(self):
        print('Initialising Websocket server...')

        start_server = websockets.serve(websocket_ping, "0.0.0.0", 8765)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

