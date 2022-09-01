import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    pass


def change_font(*args):
    pass


def new_file():
    pass


def open_file():
    pass


def save_file():
    pass


def cut():
    pass


def copy():
    pass


def paste():
    pass


def about():
    pass


def quit():
    pass


window = Tk()
window.title("MyPyPad")
window.geometry("950x660")
window.config(padx=12, pady=12)

file = None
font_name = StringVar(window)
font_name.set("Arial")  # as default font
font_size = StringVar(window)
font_size.set("16")

text_area = Text(
    window,
    relief=SUNKEN,
    font=(font_name.get(), font_size.get()),
    pady=6,
    padx=6
)

scroll_bar = Scrollbar(text_area)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

text_area.grid(sticky=N+E+S+W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

window.mainloop()
