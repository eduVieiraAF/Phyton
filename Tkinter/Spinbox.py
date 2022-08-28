from tkinter import *


def get_values():
    value1 = spin_box1.get()
    value2 = spin_box2.get()
    print(value1)
    print(value2)


win = Tk()
win.config(pady=18, padx=8)
win.resizable(False, False)
win.title('Spinbox')

indices = ["0", "10", "20", "30"]
names = ["Bob", "Chris", "Nancy", "Keith"]

spin_box1 = Spinbox(
    win,
    from_=0,
    to=30,
    values=indices,
    width=4
)

spin_box2 = Spinbox(
    win,
    from_=0,
    values=names,
    width=10
)

button = Button(
    win,
    text="Click",
    command=get_values
)

spin_box1.pack(side=LEFT, padx=4)
spin_box2.pack(side=LEFT, padx=4)
button.pack()

win.mainloop()
