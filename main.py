import turtle

wn = turtle.Screen()
wn.title("ping pong by Lehat")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
scoreA = 0
scoreB = 0

#paddle A
paddleA = turtle.Turtle()
paddleA.speed(1)#speed of animation max
paddleA.shape("square")
paddleA.color("red")
paddleA.shapesize(stretch_wid = 5, stretch_len = 1)
paddleA.penup()
paddleA.goto(-350, 0)
#paddle B
paddleB = turtle.Turtle()
paddleB.speed(1)#speed of animation max
paddleB.shape("square")
paddleB.color("blue")
paddleB.shapesize(stretch_wid = 5, stretch_len = 1)
paddleB.penup()
paddleB.goto(350, 0)
#Ball
ball = turtle.Turtle()
ball.speed(0.2)#speed of animation max
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2 #means that the ball moves 0.1 pixels

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  player B: 0", align="center", font=("Courier", 24, "normal"))

# Main game loop

#functions
def paddleAUp():
    y = paddleA.ycor()
    y += 90
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor()
    y -= 90
    paddleA.sety(y)

def paddleBUp():
    y = paddleB.ycor()
    y += 90
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor()
    y -= 90
    paddleB.sety(y)
      
#keyboard binding
wn.listen() # tells computer to listen for keyboard input
wn.onkeypress(paddleAUp, 'w') # the key is w for function paddleAUp
wn.onkeypress(paddleADown, 's')

wn.onkeypress(paddleBUp, 'Up') 
wn.onkeypress(paddleBDown, 'Down')

while True:
    wn.update()


    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # boarder checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #revers direction
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #revers direction

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}  player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}  player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    # paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350)  and (ball.ycor()< paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350)  and (ball.ycor()< paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        
    
    
"""
the ball changes its speed and the paddles are to slow

have the create a main menu where you can choose to quit or play the game 

maybe even a scoreboard where you write your own name and register the score

have to create a function that ends the game after a number of points (maybe 5)
"""