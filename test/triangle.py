#!python3

import tkinter as tk
from tkinter import *


def heron(a,b,c):
    import math
    s = (a + b + c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def basic(a,b):
    return a * b /2

def calculate():
    sides = []
    for i in ent:
        if i.get() != "":
            num = float(i.get())
        else:
            num = 0
        sides.append(num)
    if sides[0] != 0 and sides[1] != 0 and sides[2] != 0:
        area = heron(sides[0],sides[1],sides[2])
    elif sides[2] !=0 and sides[3] != 0:
        area = basic(sides[2],sides[3])
    else:
        area = None

    print(area)
    return area
        


win = tk.Tk()
win.geometry("500x500")
triangle = PhotoImage(file="triangle.png")
label1 = Label(win,image=triangle)

ent = []
label1.place(x=0,y=0)
entcd = [{"x":160,"y":100},
    {"x":390,"y":130},
    {"x":240,"y":240},
    {"x":300,"y":120}
    ]
for i in range(0,4):
    ent.append(Entry(win, width=4))
    ent[i].place( x=entcd[i]["x"], y=entcd[i]["y"])

data = "Enter in as much information about the\ntriangle shown and I will calculate the area"
instructions = Label(win, text=data)
instructions.place(x=8,y=280)

button = Button(win,text="Calculate!", command = calculate)
button.place(x=300,y=290)
win.mainloop()