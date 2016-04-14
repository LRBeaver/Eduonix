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

# x1 = random.randint(5, 50)
# y1 = random.randint(50, 160)
# x2 = random.randint(10, 100)
# y2 = random.randint(40, 260)

def randomRect(num):
    for i in range(0, num):
        x1 = random.randrange(150)
        y1 = random.randrange(150)
        x2 = x1 + random.randrange(150)
        y2 = y1 + random.randrange(150)
        canvas.create_rectangle(x1, y1, x2, y2)



randomRect(150)

#createRect(5,5,40,200)


root.mainloop()
