from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    file_path = filedialog.askopenfilename(
        initialdir="C:\\Users\\edu_v\\Python\\",
        title="Select a file, sir.",
        filetypes= (("Text files","*.txt"), ("Python files", "*.py"))
        )
    # messagebox.showinfo(title="File path", message=file_path)
    file = open(file_path, 'r')
    messagebox.showinfo(title = "File content", message = file.read())
    file.close()

window = Tk()
window.title("Python coding by Edu")
window.geometry("300x150")
window.iconbitmap('./Tkinter/python.ico')

button = Button(
    text="Open\nfile",
    font=("Arial", 14),
    command=open_file
)

button.pack()

window.mainloop()