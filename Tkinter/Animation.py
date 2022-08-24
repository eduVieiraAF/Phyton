import time
from tkinter import *

WIDTH = 500
HEIGHT = 500
X_VELOCITY = 3
Y_VELOCITY = 2

window = Tk()
window.title("Animation")

canvas = Canvas(
    window,
    width=WIDTH,
    height=HEIGHT,
    bg="#111111"
)
canvas.pack()

spaceship = PhotoImage(file='spaceship.png')
my_image = canvas.create_image(0, 0, image=spaceship, anchor=NW)

image_width = spaceship.width()
image_height = spaceship.height()

while True:
    coordinates = canvas.coords(my_image)
    # print(coordinates)

    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        X_VELOCITY = -X_VELOCITY

    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        Y_VELOCITY = -Y_VELOCITY

    canvas.move(my_image, X_VELOCITY, Y_VELOCITY)
    window.update()
    time.sleep(0.01)

window.mainloop()
