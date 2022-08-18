from time import strftime
from tkinter import *

root = Tk()
root.title("Clock")
root.resizable(False, False)
root.config(padx=15, pady=15, bg="black")


def time():
    string = strftime('%a | %B %d, %Y\n%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(
    root,
    font=("tahoma", 60),
    background="black",
    foreground="#ff5c40"
)
label.pack(anchor='center')

time()

mainloop()
