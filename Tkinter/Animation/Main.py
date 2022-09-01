import time
from tkinter import *
from ImageClass import *

window = Tk()
window.title("Mars Attack")
window.resizable(False, False)

canvas = Canvas(
    window,
    width=720,
    height=480
)

canvas.pack()

earth = PhotoImage(file='/home/eduvieira/Dev/Python/Tkinter/earth.png')
canvas.create_image(0, 0, image=earth, anchor=NW)

photo = PhotoImage(file='/home/eduvieira/Dev/Python/Tkinter/spaceship.png')
alien1 = Spaceship(canvas=canvas, x_velocity=3, y_velocity=4, x=0, y=0, photo=photo, anchor=NW)
alien2 = Spaceship(canvas=canvas, x_velocity=4, y_velocity=6, x=20, y=0, photo=photo, anchor=NW)
alien3 = Spaceship(canvas=canvas, x_velocity=4, y_velocity=6, x=100, y=100, photo=photo, anchor=NE)
alien4 = Spaceship(canvas=canvas, x_velocity=10, y_velocity=20, x=100, y=40, photo=photo, anchor=NE)
alien5 = Spaceship(canvas=canvas, x_velocity=10, y_velocity=20, x=600, y=400, photo=photo, anchor=NE)
alien6 = Spaceship(canvas=canvas, x_velocity=18, y_velocity=5, x=600, y=400, photo=photo, anchor=NE)

while True:
    alien1.move()
    alien2.move()
    alien4.move()
    alien6.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
