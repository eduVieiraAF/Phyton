import time
from tkinter import *
from Anim_Polygon_Class import *

window = Tk()
window.title("Python")

canvas = Canvas(
    window,
    height=650,
    width=800,
    bg="black",
)

# image = PhotoImage(file="python.png")

# canvas.create_polygon(250, 0, 500, 500, 0, 500, fill="cyan", outline="pink", width=7)
# canvas.create_arc(10, 10, 300, 450, style=PIESLICE, start=180, width=3, outline="green", fill="white", extent=150)
# canvas.create_rectangle(50, 50, 450, 20, fill="orange", outline="brown")
# canvas.create_line(0, 0, 500, 200, fill="blue", width=5)
# canvas.create_line(0, 500, 400, 0, fill="red", width=1)
# canvas.create_oval(200, 300, 250, 350, fill="black")
# canvas.create_image(300, 300, image=image, anchor=NW)

points = [150, 100, 150, 120, 240, 280, 210, 100, 150, 250, 100, 300]
star = [100, 10, 40, 200, 190, 80, 10, 80, 160, 198]
star2 = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]


big_star_obj1 = MyPolygon(canvas, star, -1, -3, line_color="yellow", color="green", bd_width=10)
big_star_obj2 = MyPolygon(canvas, star, -2, -1, line_color="white", color="blue", bd_width=5)
star_obj1 = MyPolygon(canvas, star2, 3, 2, line_color="white", color="yellow", bd_width=2)
star_obj2 = MyPolygon(canvas, star2, 2, 3, line_color="white", color="cyan", bd_width=3)

canvas.create_polygon(star2, outline="white", fill="gray", width=3)

canvas.pack()

while True:
    big_star_obj2.move()
    star_obj1.move()
    star_obj2.move()
    big_star_obj1.move()
    window.update()
    time.sleep(0.01)

# window.mainloop()
