from tkinter import *
from tkinter import messagebox

def order():
    food = []
    for i in list_box.curselection():
        food.insert(i, list_box.get(i))
    
    messagebox.showinfo(title="OREDER", message="Bon appetite")        
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
window.config(padx=20, pady=20)
window.title("Python coding by Edu")
window.iconbitmap('./Tkinter/python.ico')

list_box = Listbox(
    window,
    bg="#54abed",
    fg="#041c25",
    font=("Constantia", 22),
    width=12,
    bd=3,
    selectmode=MULTIPLE,
    selectbackground="#f7edb5",
    selectforeground="#4c4808",
    justify="center"
    )

list_box.insert(1, "Pizza")
list_box.insert(2, "Burger")
list_box.insert(3, "Hotdog")
list_box.config(height=list_box.size())
list_box.pack(padx=20, pady=5)

entry_box = Entry(window, font=("Constantia", 16), fg="#244954")
entry_box.pack(padx=20, pady=5)

add_button = Button(window, text="Add", command=add, font=("Arial", 14))
add_button.pack(padx=20, pady=5)

delete_button = Button(
    window, 
    text="delete", 
    command=delete, 
    font=("Arial", 14), 
    fg="#781f19")
delete_button.pack(padx=20, pady=5)

order_button = Button(
    window, 
    text="ORDER",
    font=("Arial", 20), 
    bg="#091551", 
    fg="#deebfc", 
    activebackground="#deebfc", 
    activeforeground="#091551",
    command=order
    )

order_button.pack(padx=20, pady=5)

window.mainloop()