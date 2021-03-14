import websockets, asyncio
import tkinter as tk


async def quit():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("quit")
        response = await websocket.recv()
        if response == "success":
            Window.window.destroy()

class Window():
    def __init__(self):
        self.window_initialise()
    
    def window_initialise(self):
        self.window = tk.Tk()
        self.window.title('MelonKami bot')
        self.window.geometry("400x200")
        self.welcome_page()

    
    async def welcome_page(self):
        greeting = tk.Label(text="MelonKami's Bot")
        greeting.pack()
        close = tk.Button(master=self.window, text='Quit', command=await quit())
        close.pack()
    

    def run(self):
        self.window.mainloop()
