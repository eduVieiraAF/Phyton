import tkinter as tk

# * Creating a window
window = tk.Tk()  # instantiate an instance of a window
window.geometry("460x460")
window.title("Phoenix code")
window.iconbitmap('./Tkinter/Phoenix.ico')
window.config(background="#38757b")

# * Placing a label on root window
msg = tk.Message(window, text="Hello, World!", background="#38757b", foreground="white", )
msg.pack()

window.mainloop()  # displays windows, listens for events
