
from tkinter import *
from tkinter.filedialog import asksaveasfilename

window = Tk()
window.resizable(False,False)
window.title("Note taker")
window.iconbitmap('./Tkinter/Phoenix.ico')
window.config(padx=3, pady=20)

def save():
    file_path = asksaveasfilename(
        defaultextension="txt",
        filetypes=[
            ("Text Files", "*.txt"), ("Python Files", "*.py"), ("All Files", "*.*")
            ],
        initialdir="C:\\Users\\edu_v\\Python\\"
        )
    
    if not file_path:
        return
        with open(file_path, "w") as output_file:
            text = editor.get(1.0, END)
            output_file.write(text)
            
        window.title(f"Entitled - {file_path}")
            

heading = Label(
    window,
    text="Notes",
    font=("MV Boli", 25, "bold"),
    fg="#719bb9"
).pack()

editor = Text(
    window,
    font=("MV Boli", 12),
    fg="#153038",
    padx=10, 
    pady=10,
).pack()

button = Button(
    window,
    text='Save file',
    font=('Consolas',13),
    command=save, 
    bg="#153038",
    fg="white",
    padx=5,
    pady=5
)
button.pack(pady=5)

window.mainloop()