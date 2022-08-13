from time import strftime
from tkinter import *

root = Tk()
root.title("Clock")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("tahoma", 80), background="black", foreground="white")
label.pack(anchor='center')

time()

mainloop()
