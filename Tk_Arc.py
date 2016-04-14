__author__ = 'lyndsay.beaver'
from tkinter import *
import random


root = Tk()
canvas = Canvas(root, width = 310, height = 310)
canvas.pack()


#canvas.create_rectangle(20,20, 100,270)
#canvas.create_line(20,20,100,270)
#canvas.create_polygon(40,40, 80, 100, 120, 160, 90, 110)

#def createRect(x1, y1, x2, y2):
#    canvas.create_rectangle(x1, y1, x2, y2, fill = 'blue')

canvas.create_arc(10,10, 200, 80, extent = 45, style = ARC )
canvas.create_arc(10, 80, 200, 80, extent = 90, style = ARC )

canvas.create_text(150, 150, text = "This is my first text", fill = "blue", font = ("Comic Sans", 24))
#randomRect(150)

#createRect(5,5,40,200)


root.mainloop()
