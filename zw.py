from email import message
from tkinter import *
from tkinter import messagebox

if messagebox.askokcancel(title="Let's go?", message= "Are you sure you wish to continue?"):
    print("ok")

else:
    print("Cancel")
    
if messagebox.askquestion(title= "Question", message = "Hmm"):
    print("yes")
else:
    print("no")

options = messagebox.askyesnocancel(title="3 options", message="What now?")
print(options)

