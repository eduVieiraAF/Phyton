from tkinter import *

# init tk
root = Tk()

# create canvas
myCanvas = Canvas(root, bg="white", height=300, width=300)

# draw arcs
coord = 10, 10, 300, 300
arc = myCanvas.create_arc(coord, start=0, extent=150, fill="blue", outline="white", width=10)
arc2 = myCanvas.create_arc(coord, start=150, extent=215, fill="green", outline="white", width=10)

# add to window and show
myCanvas.pack()
root.mainloop()