from tkinter import *

tk = Tk()
tk.title("Message widget")
tk.config(pady=15, padx=15)

var = StringVar()

msg = Message(
    tk,
    textvariable=var,
    font=25,
    fg="brown",
    relief=GROOVE
)

var.set("Displaying messages in a simpler way")

msg.pack()

tk.mainloop()
