from tkinter import *

window = Tk()
window.title("Python coding by Edu")
window.iconbitmap('./Tkinter/python.ico')

canvas = Canvas(
    window,
    height=500,
    width=500
)

canvas.create_rectangle(50, 50, 450, 230, fill="orange")
canvas.create_polygon(250, 0, 500, 500, 0, 500, fill="cyan", outline="pink", width=7)
canvas.create_line(0, 0, 500, 500, fill="blue", width=5)
canvas.create_line(0, 500, 400, 0, fill="red", width=3)
canvas.create_arc(10, 10, 200, 500, style=ARC, start=180)

canvas.pack()

window.mainloop()
