from cProfile import label
from tkinter import *
from tkinter import messagebox

def click():
    txt = entry.get().upper()
    
    if txt == "SOFIA":
        messagebox.showinfo(title="Mensagem", message="Linda do papai!!!")
    
    elif txt == "EDUARDO":
        messagebox.showinfo(title="Mensagem", message="Papai bobinho!")
    
    elif txt == "CAMILA":
        messagebox.showinfo(title="Mensagem", message="Helloooooooooooooooo!!!")
        
    elif txt == "YUKARI":
        messagebox.showinfo(title="Mensagem", message="Nome em JOÃOPONEIS!")
        
    else:
        messagebox.showinfo(title="Mensagem", message="Não conheço esse.")
    
    entry.delete(0, END)
        
window = Tk()

window.title("Python coding by Edu")
window.iconbitmap('./Tkinter/python.ico')
window.geometry("500x500")

label = Label(
     window, 
    text="Digite um nome:", 
    font=("Arial", 40,"bold"), 
    fg="#562f7e",
    bg="#e7eef5",
    relief=SUNKEN, #border
    bd=5, #border width
    padx=20,
    pady=20,
    compound="top"
)

label.pack()

entry = Entry(
    window,
    font=("Arial", 25),
    fg="#82c59c",
    bg="#3d3d3e",
)

entry.pack()

button = Button(
    window,
    text="Click aqui",
    font=("Consolas", 30),
    fg="#562f7e",
    bg="#e7eef5",
    activebackground="#e7eef5",
    command=click
    )

button.pack()

window.mainloop()