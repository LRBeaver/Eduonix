__author__ = 'lyndsay.beaver'

import tkinter as tk

window = tk.Tk()
text_box = tk.Entry(window)
def SaveText():
    str1=text_box.get()
    fx = open("file1.txt", 'w')
    fx.write(str1)
    fx.close()

btn1 = tk.Button(window, text = 'Save', command = SaveText)

text_box.pack()
btn1.pack()

window.mainloop()
