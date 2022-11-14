from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Python coding by Edu")
window.geometry("460x460")

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab #1")
notebook.add(tab2, text="Tab #2")
notebook.pack(expand=True, fill="both")

# Button(tab2, text="Hello").pack()

Label(tab1, text="Hello, Tab #1", width=50, height=25).pack()
Label(tab2, text="Hello, Tab #2", width=50, height=25).pack()

window.mainloop()
