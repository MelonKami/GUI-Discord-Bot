import discord, asyncio, websockets
from discord.ext import commands, tasks

async def websocket_ping(self, websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

class Websocket(commands.Cog):
    def __init__(self):
        print('Initialising Websocket server...')
        self.server.start()
        print('Websocket server seamingly started, no clue idk find out lol')
    
    @tasks.loop()
    async def server(self):
        websockets.serve(websocket_ping, "0.0.0.0", 8765)