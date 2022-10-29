import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title="Make it pretty")
    print(color)
    text_area.config(fg=color[1])


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


def quit_pad():
    pass


window = Tk()
window.title("MyPyPad")
window.geometry("850x600")
window.config(padx=12, pady=12)

file = None
font_name = StringVar(window)
font_name.set("Arial")  # as default font
font_size = StringVar(window)
font_size.set("16")

text_area = Text(
    window,
    relief=SUNKEN,
    font=(font_name.get(), int(font_size.get()) - 2),
    pady=2,
    padx=2
)

scroll_bar = Scrollbar(text_area)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

text_area.grid(sticky=N+E+S+W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

colour_button = Button(
    frame,
    text="Color",
    command=change_color,
    font=(font_name.get(), font_size.get()),
    padx=2,
    pady=2
)

colour_button.grid(row=0, column=0)

window.mainloop()
