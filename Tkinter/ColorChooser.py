from tkinter import *
from tkinter import colorchooser
from tkinter import font

window = Tk()
window.title("Python coding by Edu")
window.geometry("450x450")
window.iconbitmap('./Tkinter/python.ico')

def choose_color():
    color = colorchooser.askcolor()
    color_hex = color[1]
    button.config(fg=color_hex)
    window.config(bg=color_hex)

button = Button(
    text="Choose\n color",
    font=("Arial", 20),
    command=choose_color
)

button.pack()

window.mainloop()