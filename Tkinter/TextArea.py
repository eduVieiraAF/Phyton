
import string
from tkinter import *
from tkinter import messagebox

def submit():
    input = str(text.get("1.0", END))
    
    if len(input) == 1.0:
        messagebox.showwarning(title="Nothing to send.", message="Write something so we can send to terminal.")
    
    else:
        print(input)
        text.delete(1.0, END)
        messagebox.showinfo(title="Sucessfully submitted.", message="Your text has been sent to terminal.")

window = Tk()
window.title("Python coding by Edu")
window.iconbitmap('./Tkinter/python.ico')

text = Text(
    window,
    font=("Ink Free", 16, "bold"),
    bg="#e5e8e9",
    fg="#2c4345",
    height=15,
    width=80,
    padx=10,
    pady=10,
    bd=2, 
    )
text.pack(padx=10, pady=10)

button = Button(
    window,
    fg="white",
    activeforeground="#2c4345",
    bg="#2c4345",
    activebackground="#8b9a9b",
    text="Submit",
    font=("Arial", 16),
    command=submit
    )
button.pack(padx=10, pady=10)

window.mainloop()