import time
from tkinter import *
from tkinter.ttk import *


def start():
    tasks = 500
    x = 0
    speed = 6
    while x < tasks:
        time.sleep(0.05)
        pb['value'] += (speed / tasks) * 100
        x += speed
        task.set(str(x) + "/" + str(tasks) + " tasks completed")
        percent.set(str(int((x / tasks) * 100)) + "%")
        window.update_idletasks()


window = Tk()
window.title("Python coding by Edu")
window.config(padx=25, pady=25)

percent = StringVar()
task = StringVar()

pb = Progressbar(
    window,
    orient=HORIZONTAL,
    length=300,
)

pb.pack(pady=10)

Label(
    window,
    textvariable=percent

).pack()

Label(
    window,
    textvariable=task

).pack()

Button(
    window,
    text="Download",
    command=start
).pack(pady=5)

window.mainloop()
