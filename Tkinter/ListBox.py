from tkinter import *

def order():
    print("{} will be prepared...".format(list_box.get(list_box.curselection())))

window = Tk()
window.geometry("750x600")
window.title("Python coding by Edu")
window.iconbitmap('./Tkinter/python.ico')

list_box = Listbox(
    window,
    bg="#fff9d8",
    fg="#940008",
    font=("Constantia", 22),
    width=8
    )

list_box.insert(1, "Pizza")
list_box.insert(2, "Burger")
list_box.insert(3, "Hotdog")

list_box.config(height=list_box.size())

list_box.pack()

order_button = Button(
    window, 
    text="ORDER",
    font=("Arial", 20), 
    bg="#fbec5d", 
    fg="#760006", 
    activebackground="#fbec5d", 
    activeforeground="White",
    command=order)

order_button.pack()

window.mainloop()