from tkinter import *
from tkinter import messagebox

def display():
    if (x.get() == 1):
        button.config(state="active")
    
    else:
        messagebox.showwarning(title="Whaaaaat?", message = "How dare you!?")
 
def go_on():
     messagebox.showinfo(title="Good luck", message="Hope you have read the agreement.")
     window.destroy()

window = Tk()
window.title("Python code")
window.config(padx=20)
window.iconbitmap('./Tkinter/python.ico')
window.config(background="#111111")

x = IntVar()

py = PhotoImage(file='./Tkinter/python.png')

check_button = Checkbutton(
    window,
    text="I agree to this document without reading it",
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display,
    fg="#ff552a",
    bg="#111111",
    font=("Arial", 20),
    activebackground="#414040",
    activeforeground="#f6c9aa",
    padx=25,
    pady=15,
    image=py,
    compound="right"
)

button = Button(
    window,
    font=("Consolas", 16),
    text= "Continue",
    state="disabled",
    command=go_on
)

check_button.pack(side="left")
button.pack(side="right")

window.mainloop() 