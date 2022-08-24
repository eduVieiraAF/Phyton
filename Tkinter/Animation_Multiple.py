import time
from tkinter import *
from AnimationBall import *

window = Tk()
window.title("Multiple objects in animation")
window.resizable(False, False)

WIDTH = 500
HEIGHT = 500
X_VELOCITY = 3
Y_VELOCITY = 2

canvas = Canvas(
    window,
    width=WIDTH,
    height=HEIGHT
)

canvas.pack()

big_ball = Ball(canvas, 0, 0, 200, X_VELOCITY-1, Y_VELOCITY-1, "#ffb9cd")
volley_ball = Ball(canvas, 0, 0, 80, X_VELOCITY-1, Y_VELOCITY+1, "#eeedea")
basket_ball = Ball(canvas, 0, 0, 110, X_VELOCITY+1, Y_VELOCITY+5, "#d44500")
tennis_ball = Ball(canvas, 0, 5, 40, X_VELOCITY, Y_VELOCITY+3, "#aea600")
soccer_ball = Ball(canvas, 0, 0, 60, X_VELOCITY + 1, Y_VELOCITY + 2, "#515b62")
marble1 = Ball(canvas, 0, 0, 5, X_VELOCITY+7, Y_VELOCITY+5, "#515b62")
marble2 = Ball(canvas, 0, 0, 8, X_VELOCITY+3, Y_VELOCITY, "#49b675")

while True:    
    big_ball.move()
    volley_ball.move()
    basket_ball.move()
    tennis_ball.move()
    soccer_ball.move()
    marble1.move()
    marble2.move()
    window.update()
    time.sleep(0.01)

# window.mainloop()
