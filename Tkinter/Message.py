from tkinter import *

tk = Tk()
tk.title("Message widget")
tk.config(pady=15, padx=15)

var = StringVar()

msg = Message(
    tk,
    textvariable=var,
    fg="red",
    font=("Ink Free", 22),
    relief=RAISED,
    justify=CENTER
)

var.set("Displaying messages in a simpler way")

msg.pack()

tk.mainloop()
