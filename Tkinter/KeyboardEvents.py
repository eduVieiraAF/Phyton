from tkinter import *
from tkinter import messagebox


def warn(event):
    messagebox.showwarning(title="WARNING", message="You've hit the {} key!".format(event.keysym))


window = Tk()
window.title("Python coding by Edu")
window.geometry("460x460")
window.iconbitmap('./Tkinter/python.ico')

window.bind("<Key>", warn)

window.mainloop()
