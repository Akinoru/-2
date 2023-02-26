
import random
from tkinter import Tk, Canvas
from tkinter.ttk import Button


root=Tk
canvas=Canvas(root, width=900, height=900, bg = 'white')
window: Tk = Tk()
window.geometry('1000x1000')

def click():
    canvas.clipboard_clear()
    t=int(random.randint(900, 900))
    n=int(random.randint(900, 900))
    u=int(random.randint(900, 900))
    f = int(input(random.randint(1, 3)))
    if f==1:
        canvas.create_oval(t,t,n,n)
    elif f==2:
        canvas.create_polygon(t,t,n,u,u,n)

    elif f==3:
        canvas.create_rectangle(t,t,n,t)

button: Button = Button(window, text="click!", command=click)

window.mainloop()
