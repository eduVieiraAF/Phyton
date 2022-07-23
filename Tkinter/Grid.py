from tkinter import *

window = Tk()
window.title("Python coding by Edu")
window.iconbitmap('./Tkinter/python.ico')
window.config(padx=20, pady=20)


FNLabel = Label(
    window,
    text="First name: ",
    font=("Times New Roman", 16),
    padx=4,
    pady=4,
).grid(row=0, column=0)


FNEntry = Entry(
    window,
    font=("Times New Roman", 14),

).grid(row=0, column=1)

LNLabel = Label(
    window,
    text="Last name: ",
    font=("Times New Roman", 16),
    padx=4,
    pady=4,
).grid(row=1, column=0)


LNEntry = Entry(
    window,
    font=("Times New Roman", 14),

).grid(row=1, column=1)

EmailLabel = Label(
    window,
    text="Email: ",
    font=("Times New Roman", 16),
    padx=4,
    pady=4,
).grid(row=2, column=0)


EmailEntry = Entry(
    window,
    font=("Times New Roman", 14),

).grid(row=2, column=1)

submitBtn = Button(
    window,
    text="Submit",
    font=("Tahoma", 16, "underline"),
    width=22,
    bg="#3d3e40",
    fg="#d9dee3",
).grid(row=3, column=0, columnspan=2)

window.mainloop()