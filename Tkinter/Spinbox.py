from tkinter import *

win = Tk()
win.geometry('200x100')
win.config(pady=18, padx=8)
win.resizable(False, False)
win.title('Spinbox')

names = ["Bob", "Chris", "Nancy", "Keith"]

spin_box1 = Spinbox(
    win,
    from_=0,
    to=30,
    values=(0, 10, 20, 30),
    width=4
)

spin_box2 = Spinbox(
    win,
    from_=0,
    values=names,
    width=10
)

spin_box1.pack(side=LEFT, padx=4)
spin_box2.pack(side=LEFT, padx=4)

win.mainloop()
