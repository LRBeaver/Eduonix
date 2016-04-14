__author__ = 'lyndsay.beaver'
from tkinter import *

root = Tk()

def imageGet(entry):
    data = e.get()
    ans.configure(text = "Movie is: " + str(data))


e = Entry(root)
e.bind("<Return>", imageGet)
e.pack()

ans=Label(root)
ans.pack()

root.geometry("100x100")
'''
entrySpace = Entry(root)
entrySpace.grid(row=0, column = 1)

Button1 = Button(None, text="Find Image", fg = "Blue")
Button1.grid(row=1, column = 1)
'''

root.mainloop()