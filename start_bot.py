import os
#from bot import main
#main.run()

print("Installing dependencies")
os.system("pip install .")
print("Starting bot")

from gui import window

gui = window.Window()
gui.run()
