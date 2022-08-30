from tkinter import *
from tkinter import messagebox


def esc(event):
    if messagebox.askyesno(title="Exit?", message="Are you sure you want to quit?"):
        window.destroy()


window = Tk()
window.title("Menu button")
window.geometry("460x460")
window.config(pady=20)
window.bind("<Escape>", esc)

mb = Menubutton(
    window,
    text="Condiments",
    relief="raised",
    width=15
)
mb.grid()
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()
mustardVar = IntVar()

mb.menu.add_checkbutton(
    label="Mayo",
    variable=mayoVar
)
mb.menu.add_checkbutton(
    label="Ketchup",
    variable=ketchVar
)

mb.menu.add_checkbutton(
    label="Mustard",
    variable=mustardVar
)

mb.pack()

window.mainloop()
