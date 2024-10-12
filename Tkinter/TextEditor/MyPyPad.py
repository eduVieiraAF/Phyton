import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title="Make it pretty")
    print(color)
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(), font_size.get()))

def new_file():
    window.title("untitle.txt → My Python Pad")
    text_area.delete(1.0, END)

def save_file():
    file = filedialog.asksaveasfilename(
        initialfile="untitled.txt",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("HTML files", "*.html")]
    )
    
    if file is None:
        return
    else:    
        try:
            window.title(os.path.basename(file + " → My Python Pad"))
            file = open(file, "w")
        
            file.write(text_area.get(1.0, END))
    
        except Exception:
            showwarning(title="INFO", message="Did not save file.")
    
        finally:
            file.close()

def open_file():
    file = askopenfilename(
        defaultextension=".txt",
        file=[("Text files", "*.txt"), ("HTML files", "*.html")]
    )
    
    try:
        window.title(os.path.basename(file + " → My Python Pad"))
        text_area.delete(1.0, END)
        
        file = open(file, "r")
        text_area.insert(1.0, file.read())
    
    except Exception as e:
        showinfo(title="INFO", message="Did not open file")
        print(e)
    
    finally:
        file.close()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo(title="About this pad", message="This program was coded with love and Pyton by Edu")

def quit_pad():
    window.destroy()

window = Tk()
window.title("untitled.text → My Python Pad")
window.geometry("850x600")
window.config(padx=6, pady=10)

file = None
font_name = StringVar(window)
font_size = StringVar(window)
font_name.set("Arial")
font_size.set("14")

text_area = Text(
    window,
    relief=SUNKEN,
    font=(font_name.get(), int(font_size.get())),
    padx=8,
    pady=2
)

scroll_bar = Scrollbar(text_area)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

text_area.grid(sticky=N+E+S+W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

color_button = Button(
    frame,
    text="Color",
    command=change_color,
    font=(font_name.get(), font_size.get()),
    padx=2,
    pady=2,
)

open_button = Button(
    frame,
    text="Open",
    command = open_file,
    font=(font_name.get(), font_size.get()),
    padx=2,
    pady=2,
)

save_button = Button(
    frame,
    text="Save",
    font=(font_name.get(), font_size.get()),
    command=save_file,
    padx=2,
    pady=2,
)

font_box = OptionMenu(
    frame,
    font_name,
    *font.families(),
    command=change_font,
)

size_box = Spinbox(
    frame,
    from_=8,
    to=42,
    textvariable=font_size,
    command=change_font,
    width=5,
)
    
color_button.grid(row=0, column=0, pady=8)
open_button.grid(row=0, column=1, pady=8)
save_button.grid(row=0, column=2, pady=8)
font_box.grid(row=0, column=3, pady=8)
size_box.grid(row=0, column=4, pady=8)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_pad)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(label="About", command=about)

window.mainloop()