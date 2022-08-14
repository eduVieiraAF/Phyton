from tkinter import *
from tkinter import messagebox


def display():
    if x.get() == 1:
        messagebox.showinfo(title="Agreement", message="You have agreed → Good luck!")

    else:
        messagebox.showwarning(title="Whaaaaat?", message="How dare you!?")


window = Tk()
window.title("Python code")
window.iconbitmap('python.ico')
window.config(background="#111111")

x = IntVar()

py = PhotoImage(file='python.png')

check_button = Checkbutton(
    window,
    text="I agree to this document without reading it",
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display,
    fg="#ff552a",
    bg="#111111",
    font=("Arial", 20),
    activebackground="#414040",
    activeforeground="#f6c9aa",
    padx=25,
    pady=15,
    image=py,
    compound="right"
)

check_button.pack()

window.mainloop()
