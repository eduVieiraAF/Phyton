from tkinter import *
from tkinter import messagebox


def ciao(event):
    if messagebox.askyesno(title="Exit?", message="Are you sure you want to quit?"):
        window.destroy()


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)


def move_left(event):
    label.place(x=label.winfo_x() - 10, y=label.winfo_y())


def move_right(event):
    label.place(x=label.winfo_x() + 10, y=label.winfo_y())


window = Tk()
window.title("Moving an object")
window.geometry("900x700")
window.config(bg="black")

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<Escape>", ciao)

spaceship = PhotoImage(file="spaceship.png")

label = Label(
    window,
    image=spaceship,
    bg="black"
)

label.place(x=0, y=0)

window.mainloop()
