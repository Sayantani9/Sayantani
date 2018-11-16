import tkinter as tkr
import time

"""Create Canvas"""
tk = tkr.Tk()
canvas = tkr.Canvas(tk, width=300, height=400)
canvas.grid()

"""Draw Ball"""
ball = canvas.create_oval(15,15,60,60,fill="orange")

x = 1
y = 4

"""Move Ball"""
while True:
    canvas.move(ball,x,y)

    """Pos[Left,Top,Right,Buttom]"""

    pos = canvas.coords(ball)
    if pos[3] >= 400 or pos[1] <= 0:
                y = -y
    if pos[2] >= 300 or pos[0] <= 0:
                x = -x
    tk.update()
    time.sleep(0.015)
    pass

tk.mainloop()
