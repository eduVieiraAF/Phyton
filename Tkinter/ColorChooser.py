from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox

window = Tk()
window.title("Python coding by Edu")
window.geometry("450x450+300+200")
window.iconbitmap('./Tkinter/python.ico')


def choose_color():
    color = colorchooser.askcolor()
    color_hex = color[1]
    button.config(fg=color_hex)
    window.config(bg=color_hex)
    messagebox.showinfo(title="Hexadecimal value", message="Here's the color you've picked out → " + color_hex)


button = Button(
    text="Choose\n color",
    font=("Arial", 20, "bold"),
    command=choose_color
)

button.pack(padx=4, pady=20)

window.mainloop()
