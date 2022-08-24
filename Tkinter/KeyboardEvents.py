from tkinter import *
from tkinter import messagebox


def warn(event):
    messagebox.showwarning(title="WARNING", message="You've hit the \"{}\" key!".format(event.keysym))


window = Tk()
window.title("Python coding by Edu")
window.geometry("250x250+200+250")

window.bind("<Key>", warn)

window.mainloop()
