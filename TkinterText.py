__author__ = 'lyndsay.beaver'
from tkinter import *

root = Tk()

#topFrame = Frame(root)
#topFrame.pack()

#botFrame = Frame(root)
#botFrame.pack(side=BOTTOM)

theLabel = Label(root, text="This is the main window")
theLabel.grid(row=0, column = 0)
#theLabel.pack(side=TOP)

Button1 = Button(None, text="Button One!", fg = "Blue")
Button1.grid(row=1, column = 0)
#Button1.pack(side=LEFT)

Button2 = Button(None, text="Button Two!", fg = "Blue")
Button2.grid(row=0, column = 1)
#Button2.pack(side=RIGHT)

Button3 = Button(None, text="Button Three!", fg = "Blue")
Button3.grid(row=1, column = 0)
#Button3.pack(side=LEFT)

Button4 = Button(None, text="Button Four!", fg = "Blue")
Button4.grid(row=0, column = 2)
#Button4.pack(side=RIGHT)

root.mainloop()
