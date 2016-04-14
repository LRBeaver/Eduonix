__author__ = 'lyndsay.beaver'
__author__ = 'lyndsay.beaver'
from tkinter import *
import time


root = Tk()
canvas = Canvas(root, width = 310, height = 310)
canvas.pack()

canvas.create_polygon(10, 10, 10, 60, 50, 35)
for i in range(0, 60):
    canvas.move(1, 5, 0)
    canvas.move(1, 10, 1)
    root.update()
    time.sleep(0.1)

root.mainloop()
