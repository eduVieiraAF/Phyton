from audioop import add
from tkinter import *

def order():
    food = []
    for i in list_box.curselection():
        food.insert(i, list_box.get(i))
        
    print("Here's your order:")
    
    for i in food:
        print(i)
    
def add():
    list_box.insert(list_box.size(), entry_box.get().capitalize())
    list_box.config(height=list_box.size())
    entry_box.delete(0, END)

def delete():
    for i in reversed(list_box.curselection()):
        list_box.delete(i)
    list_box.config(height=list_box.size())

window = Tk()
window.title("Python coding by Edu")
window.iconbitmap('./Tkinter/python.ico')

list_box = Listbox(
    window,
    bg="#fff9d8",
    fg="#940008",
    font=("Constantia", 22),
    width=12,
    selectmode=MULTIPLE
    )

list_box.insert(1, "Pizza")
list_box.insert(2, "Burger")
list_box.insert(3, "Hotdog")
list_box.config(height=list_box.size())
list_box.pack()

entry_box = Entry(window, font=("Constantia", 16), fg="#244954")
entry_box.pack()

add_button = Button(window, text="Add", command=add, font=("Arial", 14))
add_button.pack()

delete_button = Button(
    window, 
    text="delete", 
    command=delete, 
    font=("Arial", 14), 
    fg="#781f19")
delete_button.pack()

order_button = Button(
    window, 
    text="ORDER",
    font=("Arial", 20), 
    bg="#fbec5d", 
    fg="#760006", 
    activebackground="#fbec5d", 
    activeforeground="White",
    command=order
    )

order_button.pack()

window.mainloop()