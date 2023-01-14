from tkinter import *

canvas_width = 300
canvas_height = 80

master = Tk()
master.title("Bitmap")
canvas = Canvas(master,
                width=canvas_width,
                height=canvas_height)
canvas.pack()

bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
n_steps = len(bitmaps)
step_x = int(canvas_width / n_steps)

for i in range(0, n_steps):
    canvas.create_bitmap((i + 1) * step_x - step_x / 2, 50, bitmap=bitmaps[i])

mainloop()
