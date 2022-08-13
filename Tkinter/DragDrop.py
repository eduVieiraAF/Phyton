from tkinter import *


def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y

    widget.place(x=x, y=y)


window = Tk()
window.title("Python coding by Edu")
window.geometry("650x650+300+200")
window.iconbitmap('./Tkinter/python.ico')
window.config(padx=3, pady=3)

label = Label(
    window,
    bg="#565b95",
    fg="White",
    text="Label",
    font=("Arial", 20),
    width=10,
    height=5
)

button = Button(
    window,
    bg="#4f6571",
    fg="White",
    text="Button",
    font=("Cambria", 40)
)

label.place(x=0, y=0)
button.place(x=150, y=150)

label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)

button.bind("<Button-1>", drag_start)
button.bind("<B1-Motion>", drag_motion)

window.mainloop()
