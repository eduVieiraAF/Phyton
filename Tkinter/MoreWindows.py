from tkinter import *

def tl_window():
    tl = Toplevel() # new window on top of other windows, linked to 'bottom' window
    tl.title("Top level window")
    tl.geometry("280x280")
    tl.iconbitmap('./Tkinter/python.ico')
    tl.focus()

def new_window():
    window2 = Tk() # new independent window
    window2.title("New window")
    window2.geometry("280x280")
    window2.iconbitmap('./Tkinter/python.ico')
    window2.focus()
    window.destroy()

window = Tk()
window.title("Python coding by Edu")
window.geometry("400x350")
window.iconbitmap('./Tkinter/python.ico')

Button(window, text="Top level window", command=tl_window).pack()
Button(window, text="Enterily ne window", command=new_window).pack()

window.mainloop()