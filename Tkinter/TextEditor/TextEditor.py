from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from colors import *

stimulator_window = Tk()
stimulator_window.geometry("600x600")
stimulator_window.resizable(False,False)
stimulator_window.iconbitmap('./Tkinter/Phoenix.ico')

heading = Label(
    stimulator_window,
    text="Notes",
    font=("MV Boli", 25, "bold"),
    fg=label_title
).pack()

scrollbar = Scrollbar(stimulator_window).pack(side=RIGHT, fill=Y)

editor = Text(
    stimulator_window,
    width=400,
    height=450,
    # yscrollcommand=scrollbar.set,
    padx=10, 
    pady=10,
    ).pack(fill=BOTH)

stimulator_window.mainloop()