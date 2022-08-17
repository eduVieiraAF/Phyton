from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def open_file():
    file_path = filedialog.askopenfilename(
        initialdir="C:\\Users\\edu_v\\Python\\",
        title="Select a file, sir.",
        filetypes=(("Text files", "*.txt"), ("Python files", "*.py"), ("HTML files", "*.html"))
    )
    file = open(file_path, 'r')
    messagebox.showinfo(title="File content", message=file.read())
    file.close()


window = Tk()
window.title("Python coding by Edu")
window.geometry("300x150")

button = Button(
    text="Open\nfile",
    font=("Segoe UI Semibold", 12),
    command=open_file
)

button.pack()

window.mainloop()
