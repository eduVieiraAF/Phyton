import tkinter as tk

#* Creating a window
root = tk.Tk()

#* Placing a label on root window
msg = tk.Message(root, text = "Hello, World!")
msg.pack()

root.mainloop()