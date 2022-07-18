
from tkinter import *

from numpy import pad

window = Tk()
window.title("Python coding by Edu")
window.geometry("460x460")
window.iconbitmap('./Tkinter/python.ico')


photo = PhotoImage("./Tkinter/burger")
frame = Frame(
    window,
    bg="#9bfbe5",
    padx=15,
    pady=15,
    relief="ridge",
    bd=10
)

button1 = Button(
    frame,
    text="↑",
    font=("Consolas", 25),
    width=3,
    bg="#006c7f",
    fg="#dbe9f4"
)

button2 = Button(
    frame,
    text="←",
    font=("Consolas", 25),
    width=3,
    bg="#006c7f",
    fg="#dbe9f4"
)

button3 = Button(
    frame,
    text="↓",
    font=("Consolas", 25),
    width=3,
    bg="#006c7f",
    fg="#dbe9f4"
)

button4 = Button(
    frame,
    text="→",
    font=("Consolas", 25),
    width=3,
    bg="#006c7f",
    fg="#dbe9f4"
)

Label(frame).pack(side=BOTTOM)


frame.pack(side="bottom")
button1.pack(side=TOP)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

window.mainloop()