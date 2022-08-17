from tkinter import *
from tkinter import filedialog, messagebox


def esc_quit(event):
    if messagebox.askyesno(title="Exit", message="Are you sure you want to exit?"):
        window.destroy()


def save_file():
    if len(text.get("1.0", "end-1c")) == 0:
        messagebox.showerror(title="EMPTY FILE", message="You cannot save an empty file.")

    else:
        file = filedialog.asksaveasfile(initialdir="/home/eduvieira/IdeaProjects/Python",
                                        title="Give it a pretty name",
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
        text.delete(0.1, END)
        file.close()


window = Tk()
window.title("Python")
window.bind("<Escape>", esc_quit)

text = Text(
    window,
    padx=10,
    pady=10,
    font=("Helvetia", 12),
    relief="sunken",
    bd=3
)

text.pack(padx=8, pady=8)

button = Button(
    text="Save",
    font=("Segoe UI Semibold", 12),
    command=save_file
)

button.pack(padx=8, pady=8)

window.mainloop()
