__author__ = 'lyndsay.beaver'

from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title", "Did you know that the world just blew up?")

answer = tkinter.messagebox.askquestion("Question 1", "Are you human?")
if answer == "Yes":
    tkinter.messagebox.showinfo("Congrats", "Thank god! It's good to know another human is out there")

if answer == "No":
    tkinter.messagebox.showinfo("Alien", "You are 100% confirmed an alien")

root.mainloop()
