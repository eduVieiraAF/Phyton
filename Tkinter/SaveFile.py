from tkinter import *
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\edu_v\\Python\\",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("Word file", ".doc"),
                                        ("Python file", ".py")
                                    ])
    if file is None:
        return

    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()


window = Tk()
window.title("Python coding by Edu")
# window.iconbitmap('./Tkinter/python.ico')

text = Text(window,
            padx=10,
            pady=10,
            font=("Helvetia", 12))

text.pack()

button = Button(
    text="Save",
    font=("Segoe UI Semibold", 12),
    command=save_file
)

button.pack()

window.mainloop()
