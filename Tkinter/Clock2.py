import time
from tkinter import *

bg_colour = "#292929"

def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_pm


master = Tk()
master.resizable(False, False)
master.title("Clock")
master.config(pady=12, padx=12, bg=bg_colour)

canvas = Canvas(
    master,
    height=400,
    width=400,
    bg=bg_colour,
    relief=GROOVE,
    border=4
)
canvas.pack(expand=True, fill='both')

bg = PhotoImage

update_clock()

master.mainloop()
