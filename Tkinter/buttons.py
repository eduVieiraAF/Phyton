from tkinter import *

count = 0


def click():
    global count
    if count == 10:
        print("Jesus! How many more times ya gon' click!?")

    if count == 20:
        print("Are you kidding me??")
    count += 1
    print("You've clicked {} times.".format(count))


window = Tk()
window.geometry("460x460")
window.title("Phoenix code")
window.iconbitmap('./Tkinter/Phoenix.ico')

photo = PhotoImage(file='./Tkinter/spaceship.png')

button = Button(
    window,
    text="Click me!",
    command=click,
    font=("Comic Sans", 40),
    fg="#e7eef5",
    bg="Black",
    activeforeground="#562f7e",
    activebackground="Black",
    image=photo,
    compound="bottom"
)

button.pack()

window.mainloop()
