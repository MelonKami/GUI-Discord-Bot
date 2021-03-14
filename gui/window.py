import websockets, asyncio, json, codecs, os
from time import time, sleep
import tkinter as tk
from websockets import connect
from os import path

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
        print("GUI initiated")
        self.window = tk.Tk()
        self.welcome_page()
        #self.loop = asyncio.get_event_loop()
    
    def window_initialise(self, title, size):
        self.window.destroy()
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(size)
        #self.welcome_page()

    
    def welcome_page(self):
        self.window_initialise("MelonKami", "200x150")
        greeting = tk.Label(text="MelonKami Bot")
        greeting.pack()
        close = tk.Button(master=self.window, text='Quit', command=lambda: self.window.destroy())
        start = tk.Button(master=self.window, text='Start Bot', command=lambda: self.start_bot())
        settings = tk.Button(master=self.window, text='Bot settings', command=lambda: self.settings_page())
        start.pack()
        settings.pack()
        close.pack()
    
    def settings_page(self):
        self.window_initialise("Settings", "350x100")
        token_label = tk.Label(self.window, text='Token')
        token = tk.Entry(master= self.window)
        prefix_label = tk.Label(self.window, text='Prefix')
        back = tk.Button(master=self.window, text='Back', command=lambda: self.welcome_page())
        prefix = tk.Entry(master= self.window)
        submit = tk.Button(master=self.window, text='Save', command=lambda: self.save_settings(token.get(), prefix.get()))
        dependencies_install = tk.Button(master=self.window, text='Install dependencies', command=lambda: self.install_dependencies())
        token_label.grid(column=0, row=0)
        token.grid(column=1, row=0)
        prefix_label.grid(column=0, row=1)
        prefix.grid(column=1, row=1)
        submit.grid(column=1, row=2)
        back.grid(sticky=tk.W, column=1, row=2)
        dependencies_install.grid(column=0, row=2)

    def install_dependencies(self):
        self.window_initialise("Installing dependencies", "500x50")
        
        label = tk.Label(self.window, text="Installing dependencies, please wait")
        label.pack()
        self.window.after(5000, lambda: self.please_wait())

    
    def please_wait(self):
        os.system("pip install .")
        self.welcome_page()


    def save_settings(self, token, prefix):
        print(token)
        print(prefix)

        if path.exists('config.json') == False:
            with open('config.json', 'x') as File:
                json.dump({"token": token, prefix: prefix}, File, indent=4)
        with codecs.open('config.json','r', encoding='utf-8-sig') as File:
            self.config = json.load(File)
        self.config["token"] = token
        self.config["prefix"] = prefix
        with codecs.open('config.json', 'w', encoding='utf8') as File:
            json.dump(self.config, File, sort_keys=True, indent=4, ensure_ascii=False)


        self.welcome_page()


    def quit(self):
        return asyncio.get_event_loop().run_until_complete(self.async_quit())
    
    def start_bot(self):
        self.window.destroy()
        from bot import main
        print('starting bot')
        main.run()

    async def async_quit(self):
        async with EchoWebsocket() as echo:
            await echo.send('quit_bot')
            response = await echo.receive()
            if response == "Success":
                return self.window.destroy()

    def run(self):
        self.window.mainloop()
