from tkinter import *


def do_something(event):
    print("Screen Coordinates → " + str(event.x) + " | " + str(event.y))


window = Tk()
window.title("Python coding by Edu")
window.geometry("460x460")

# window.bind("<Button-1>", do_something) left mouse click
# window.bind("<Button-2>", do_something) scroll wheel click
# window.bind("<Button-3>", do_something) right mouse click
# window.bind("<ButtonRelease>", do_something)
# window.bind("<Enter>", do_something)
# window.bind("<Leave>", do_something)
window.bind("<Motion>", do_something)
window.mainloop()
