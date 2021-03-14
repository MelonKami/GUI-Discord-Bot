import websockets, asyncio
import tkinter as tk
from websockets import connect

class EchoWebsocket:
    async def __aenter__(self):
        self._conn = connect('ws://0.0.0.0:8765')
        self.websocket = await self._conn.__aenter__()        
        return self

    async def __aexit__(self, *args, **kwargs):
        await self._conn.__aexit__(*args, **kwargs)

    async def send(self, message):
        await self.websocket.send(message)

    async def receive(self):
        return await self.websocket.recv()

class Window:
    def __init__(self):
        self.window_initialise()
        #self.loop = asyncio.get_event_loop()
    
    def window_initialise(self):
        self.window = tk.Tk()
        self.window.title('MelonKami bot')
        self.window.geometry("400x200")
        self.welcome_page()

    
    def welcome_page(self):
        greeting = tk.Label(text="MelonKami Bot")
        greeting.pack()
        close = tk.Button(master=self.window, text='Quit', command=lambda: self.window.destroy())
        start = tk.Button(master=self.window, text='Start Bot', command=lambda: self.start_bot())
        start.pack()
        close.pack()
    
    def quit(self):
        return asyncio.get_event_loop().run_until_complete(self.async_quit())
    
    def start_bot(self):
        from bot import main
        print('starting bot')
        main.run()
        print('bot started')

    async def async_quit(self):
        async with EchoWebsocket() as echo:
            await echo.send('quit_bot')
            response = await echo.receive()
            if response == "Success":
                return self.window.destroy()

    def run(self):
        self.window.mainloop()

"""
Example
class mtest:
    def __init__(self):
        self.wws = EchoWebsocket()
        self.loop = asyncio.get_event_loop()

    def get_ticks(self):
        return self.loop.run_until_complete(self.__async__get_ticks())

    async def __async__get_ticks(self):
        async with self.wws as echo:
            await echo.send(json.dumps({'ticks_history': 'R_50', 'end': 'latest', 'count': 1}))
            return await echo.receive()
"""
