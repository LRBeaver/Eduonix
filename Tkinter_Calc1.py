__author__ = 'lyndsay.beaver'
__author__ = 'lyndsay.beaver'

from tkinter import *

root = Tk()

def random():
    print("This is a statement")

mainMenu = Menu(root)
root.configure(menu = mainMenu)

subMenu = Menu(mainMenu)

mainMenu.add_cascade(label = "File", menu = subMenu)
subMenu.add_command(label = "Random Func", command = random)
subMenu.add_command(label = "New File", command = random)
subMenu.add_separator()
subMenu.add_command(label = "Supercala", command = random)

root.mainloop()
