import turtle

screen = turtle.Screen()
screen.title("Pong game")
screen.setup(width=1000, height=600)

paddle1 = turtle.Turtle()
# Setting its speed as zero, it moves only when key is pressed
paddle1.speed(0)
# Setting shape, color, and size
paddle1.shape("square")
paddle1.color("brown")
paddle1.shapesize(stretch_wid=6, stretch_len=2)
paddle1.penup()
# The paddle is left-centered initially
paddle1.goto(-400, 0)

paddle2 = turtle.Turtle()
# Setting its speed as zero, it moves only when key is pressed
paddle2.speed(0)
# Setting shape, color, and size
paddle2.shape("square")
paddle2.color("teal")
paddle2.shapesize(stretch_wid=6, stretch_len=2)
paddle2.penup()
# The paddle is right-centered initially
paddle2.goto(400, 0)

ball = turtle.Turtle()
# Setting the speed of ball to 0, it moves based on the dx and dy values
ball.speed(0)
# Setting shape, color, and size
ball.shape("circle")
ball.color("#2e0f44")
ball.penup()
# Ball starts from the centre of the screen
ball.goto(0, 0)
# Setting dx and dy that decide the speed of the ball
ball.dx = 5
ball.dy = -5

player1 = 0
player2 = 0
# Displaying the score
score = turtle.Turtle()
score.speed(0)
score.penup()
# Hiding the turtle to show text
score.hideturtle()
# Locating the scoreboard on top of the screen
score.goto(0, 260)
# Showing the score
score.write("Player1 : 0 Player2: 0", align="center",
            font=("MV Boli", 20, "bold"))

# Function to move the left paddle up


def movePad1Up():
    y = paddle1.ycor()  # Getting the current y-coordinated of the left paddle
    y += 15
    paddle1.sety(y)  # Updating the y-coordinated of the paddle
# Function to move the left paddle down


def movePad1Down():
    y = paddle1.ycor()  # Getting the current y-coordinated of the left paddle
    y -= 15
    paddle1.sety(y)  # Updating the y-coordinated of the paddle
# Function to move the right paddle up


def movePad2Up():
    y = paddle2.ycor()  # Getting the current y-coordinated of the right paddle
    y += 15
    paddle2.sety(y)  # Updating the y-coordinated of the paddle
# Function to move the right paddle down


def movePad2Down():
    y = paddle2.ycor()  # Getting the current y-coordinated of the right paddle
    y -= 15
    paddle2.sety(y)  # Updating the y-coordinated of the paddle


# Matching the
screen.listen()
screen.onkeypress(movePad1Up, "a")
screen.onkeypress(movePad1Down, "s")
screen.onkeypress(movePad2Up, "1")
screen.onkeypress(movePad2Down, "2")

while True:
    # Updating the screen every time with the new changes
    screen.update()
    
    # Moving the ball by updating the coordinates
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    # Checking if ball hits the top of the screen
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1  # Bouncing the ball
        
    # Checking if ball hits the bottom of the screen
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1  # Bouncing the ball
        
    # Checking if the ball hits the left or right walls, the player missed the hit
    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.goto(0, 0)
        if ball.xcor() > 400:
            player2 += 1
        else:
            player1 += 1
        score.clear()  # Clearing the current score
        score.write("Player1 : {} Player2: {}".format(player1, player2), align="center",
                    font=("MV Boli", 20, "bold"))
        
    # Checking if ball hits the left paddle
    if ball.xcor() < -380 and ball.ycor() < paddle1.ycor()+60 and ball.ycor() > paddle1.ycor()-60:
        ball.dx *= -1  # Bouncing the ball
        
    # Checking if ball hits the right paddle
    if ball.xcor() > 380 and ball.ycor() < paddle2.ycor()+60 and ball.ycor() > paddle2.ycor()-60:
        ball.dx *= -1  # Bouncing the ball
