from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog, messagebox


def open_file():
    # noinspection PyBroadException
    try:
        # noinspection SpellCheckingInspection
        file_path = filedialog.askopenfilename(
            initialdir="/home/eduvieira/IdeaProjects/Python",
            title="Pick a file",
            filetypes=(
                ("Text file", ".txt"),
                ("HTML file", ".html"),
                ("Word file", ".doc"),
                ("ODF file", "*.odt"),
                ("Python file", ".py")
            )
        )

        text.delete(0.1, END)
        file = open(file_path, 'r')
        text.insert(END, file.read())
        file.close()


    except Exception:
        print("no file was open ")


def pick_colour():
    color = colorchooser.askcolor()
    color_value = color[1]
    # noinspection PyTypeChecker
    text.config(fg=color_value)


# noinspection PyUnusedLocal
def esc_quit(event):
    if messagebox.askyesno(title="Exit", message="Are you sure you want to exit?"):
        window.destroy()


def save_file():
    if len(text.get("1.0", "end-1c")) == 0:
        messagebox.showerror(title="EMPTY FILE", message="You cannot save an empty file.")

    else:
        # noinspection SpellCheckingInspection
        file = filedialog.asksaveasfile(initialdir="/home/eduvieira/IdeaProjects/Python",
                                        title="Save this file",
                                        filetypes=[
                                            ("Text file", ".txt"),
                                            ("HTML file", ".html"),
                                            ("Word file", ".doc"),
                                            ("ODF file", "*.odt"),
                                            ("Python file", ".py")
                                        ])
        if file is None:
            return

        file_text = str(text.get(1.0, END))
        file.write(file_text)
        text.delete(0.1, END)
        file.close()


window = Tk()
window.title("Python Notes Program")
window.bind("<Escape>", esc_quit)

save_icon = PhotoImage(file="./Tkinter/save.png")
paint_icon = PhotoImage(file="./Tkinter/paint.png")
open_icon = PhotoImage(file="./Tkinter/open.png")

text = Text(
    window,
    padx=10,
    pady=10,
    font=12,
    relief=RIDGE,
    bd=3
)

save_button = Button(
    text="Save file",
    image=save_icon,
    compound=RIGHT,
    command=save_file
)

color_button = Button(
    window,
    text="Pick a colour",
    command=pick_colour,
    image=paint_icon,
    compound=RIGHT
)

open_button = Button(
    window,
    text="Open file",
    image=open_icon,
    compound=RIGHT,
    command=open_file
)

text.pack(padx=8, pady=8)
save_button.pack(padx=8, pady=8, side=LEFT)
color_button.pack(padx=8, pady=8, side=LEFT)
open_button.pack(padx=8, pady=8, side=LEFT)

window.mainloop()
