import turtle
from random import randint, choice, uniform

def paddle1_up_moving():
    y = paddle1.ycor()
    y += 20
    if y < 270:
        paddle1.sety(y)

def paddle1_down_moving():
    y = paddle1.ycor()
    y -= 20
    if y > -270:
        paddle1.sety(y)

def paddle2_up_moving():
    y = paddle2.ycor()
    y += 20
    if y < 270:
        paddle2.sety(y)

def paddle2_down_moving():
    y = paddle2.ycor()
    y -= 20
    if y > -270:
        paddle2.sety(y)

def random_direction():
    two = [-1, 1]
    x = choice(two)
    y = choice(two)
    return x, y

def random_move():
    y = uniform(1, 3)
    move = y * (0.5)
    return move

def scores(n, m):
    global score1, score2
    scoring.clear()
    score1 += n
    score2 += m
    scoring.write(f"The result is {score1} : {score2}", align="center", font=("Arial", 24, "normal"))

speed = 7
direction, y = random_direction()
y_axis = random_move()

def moving_ball():
    global speed, direction, y_axis, y
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        y *= -1
    
    if ball.xcor() < -290:
        scores(0, 1)
        ball.goto(0, randint(-270, 270))
        direction, y = random_direction()
    if ball.xcor() > 290:
        scores(1, 0)
        ball.goto(0, randint(-270, 270))
        direction, y = random_direction()
    
    ball.sety(ball.ycor() + (y_axis * y * speed))
    ball.setx(ball.xcor() + (direction * speed))
    
    if (-280 < ball.xcor() < -270) and (paddle1.ycor() - 50 < ball.ycor() < paddle1.ycor() + 50):
        direction *= -1
        _, y = random_direction()
    if (270 < ball.xcor() < 280) and (paddle2.ycor() - 50 < ball.ycor() < paddle2.ycor() + 50):
        direction *= -1
        _, y = random_direction()
    
    sc.ontimer(moving_ball, 10)

sc = turtle.Screen()
sc.bgcolor("black")
sc.setup(600, 600)
sc.title("Pong Game")

paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.color("red")
paddle1.penup()
paddle1.goto(-270, 0)

paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.color("blue")
paddle2.penup()
paddle2.goto(270, 0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, randint(-270, 270))

scoring = turtle.Turtle()
scoring.hideturtle()
score1, score2 = 0, 0
scoring.penup()
scoring.goto(0, 260)
scoring.color("white")
scoring.write(f"The result is {score1} : {score2}", align="center", font=("Arial", 24, "normal"))

sc.listen()
sc.onkeypress(paddle1_up_moving, "w")
sc.onkeypress(paddle1_down_moving, "s")
sc.onkeypress(paddle2_up_moving, "Up")
sc.onkeypress(paddle2_down_moving, "Down")

moving_ball()
sc.mainloop()
