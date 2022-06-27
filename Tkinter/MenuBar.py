from tkinter import *
from tkinter import messagebox

def open_file():
    messagebox.showinfo(title="Open", message="Your file will open.")

def save_file():
    messagebox.showinfo(title="Save", message="Your file will be saved.")
    
def exit_program():
    messagebox.showwarning(title="Exit", message="Guess this is goodbye then...")
    exit()

window = Tk()
window.title("Python coding by Edu")
window.geometry("460x460")
window.iconbitmap('./Tkinter/python.ico')

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)

window.mainloop()
