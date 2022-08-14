import turtle as tt

sc = tt.getscreen()

tt.title("Turtle begins")

tt.right(90)  # tt.right(90)
tt.fd(100)  # tt.forward(100)
tt.lt(90)  # tt.left(90)
tt.bk(100)  # tt.backward(100)

tt.goto(100, 100)

tt.circle(60)
tt.dot(50)

tt.bgcolor('cyan')

tt.shapesize(3, 3, 3)
tt.fillcolor("yellow")

tt.shapesize(5)
tt.fd(100)

tt.mainloop()
