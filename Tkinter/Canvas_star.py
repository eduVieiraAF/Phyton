from tkinter import *

canvas_width = 400
canvas_height = 400
python_green = "#476042"


def polygon_star(canvas, x, y, p, t, outline=python_green, fill='yellow', width=1):
    points = []
    for i in (1, -1):
        points.extend((x, y + i * p))
        points.extend((x + i * t, y + i * t))
        points.extend((x + i * p, y))
        points.extend((x + i * t, y - i * t))

    print(points)

    canvas.create_polygon(points, outline=outline, fill=fill, width=width)


master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

p = 50
t = 15

n_steps = 10
step_x = int(canvas_width / n_steps)
step_y = int(canvas_height / n_steps)

for i in range(1, n_steps):
    polygon_star(w, i * step_x, i * step_y, p, t, outline='red', fill='gold', width=3)
    polygon_star(w, i * step_x, canvas_height - i * step_y, p, t, outline='red', fill='gold', width=3)

mainloop()
