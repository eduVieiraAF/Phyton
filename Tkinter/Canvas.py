from tkinter import *

window = Tk()
window.title("Python coding by Edu")

canvas = Canvas(
    window,
    height=500,
    width=500,
    bg="black",
)

image = PhotoImage(file="python.png")

canvas.create_polygon(250, 0, 500, 500, 0, 500, fill="cyan", outline="pink", width=7)
canvas.create_arc(10, 10, 300, 450, style=PIESLICE, start=180, width=3, outline="green", fill="white", extent=150)
canvas.create_rectangle(50, 50, 450, 20, fill="orange", outline="brown")
canvas.create_line(0, 0, 500, 200, fill="blue", width=5)
canvas.create_line(0, 500, 400, 0, fill="red", width=1)
canvas.create_oval(200, 300, 250, 350, fill="black")
canvas.create_image(30, 70, image=image, anchor=NW)

canvas.pack()

window.mainloop()
