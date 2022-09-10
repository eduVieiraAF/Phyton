from tkinter import *
from tkinter import messagebox


def open_file():
    messagebox.showinfo(title="Open", message="Your file will open.")


def save_file():
    messagebox.showinfo(title="Save", message="Your file will be saved.")


def exit_program():
    messagebox.showwarning(title="Exit", message="Guess this is goodbye then...")
    exit()


def edit_cut():
    messagebox.showinfo(title="Cut", message="Selection cut.")


def edit_copy():
    messagebox.showinfo(title="Copy", message="Selection copied.")


def edit_paste():
    messagebox.showinfo(title="Paste", message="Selection pasted.")


window = Tk()
window.title("Python coding by Edu")
window.geometry("460x460")

fire_image = PhotoImage("./Tkinter/fire.png")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(
    menu_bar,
    tearoff=0
)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open", command=open_file, image=fire_image, compound="left")
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)

edit_menu = Menu(
    menu_bar,
    tearoff=0,
    font=("Ink free", 12)
)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=edit_copy)
edit_menu.add_command(label="Paste", command=edit_paste)

window.mainloop()
