import tkinter as tk
from tkinter import * 
import math

win = tk.Tk()
win.geometry("500x380")

answer = StringVar()

def calc():
    a = e1.get()
    b = e2.get()
    c = e3.get()
    x = e4.get()
    if a =="" and c=="" and b !="" and x !="":
        b = float(b)
        x = float(x)
        area = b * x / 2
    elif x=="" and a !="" and b !="" and c !="":
        a = float(a)
        b = float(b)
        c = float(c)
        s = (a+b+c)/2
        area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    else:
        area = "Cannot be calculated"
    answer.set(area)
    

trianglephoto = PhotoImage(file="triangle.png")
l1 = Label(win, image=trianglephoto)
e1 = Entry(win, width=7)
e2 = Entry(win, width=7)
e3 = Entry(win, width=7)
e4 = Entry(win, width=7)
l2 = Label(win, text="Enter in as much information about the \n triangle shown and I will calculate the area")
b1 = Button(win, text="Calculate!", command=calc)
l3 = Label(win, textvariable=answer)

l1.place(x=0, y=0)
e1.place(x=165, y=115)
e4.place(x=305, y=135)
e3.place(x=395, y=145)
e2.place(x=245, y=245)
l2.place(x=50, y=320)
b1.place(x=340, y=320)
l3.place(x=200, y=290)

win.mainloop()
