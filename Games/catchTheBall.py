import turtle
from random import randint, uniform

def random_number():
    uniform_random = uniform(0, 1)
    skewed_random = uniform_random ** 3
    scaled_random = 0.001 + skewed_random * (0.05 - 0.001)
    return scaled_random

def go_to_left():
    x = paddle.xcor()
    x -= 15
    if x > -270:
        paddle.setx(x)

def go_to_right():
    x = paddle.xcor()
    x += 15
    if x < 270:
        paddle.setx(x)

def direction():
    y = random_number()
    left_or_right = randint(0, 1)
    x = 0.5
    if left_or_right == 0:
        x = -0.5
    
    return x, y

x_axis, y_axis = direction()
speed = 5 + y_axis

def moving_game():
    global speed, x_axis, y_axis
    
    ball.sety(ball.ycor() - speed)
    ball.setx(ball.xcor() + x_axis)
    
    if ball.xcor() > 270 or ball.xcor() < -270:
        x_axis *= -1
    
    if ball.ycor() < -320:
        x_ball = randint(-270, 270)
        ball.goto(x_ball, 270)
        scoring_game(-1)
    
    if ball.ycor() < -290 and ball.ycor() > -310 and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50:
        scoring_game(1)
        speed += y_axis
        x_ball = randint(-270, 270)
        ball.goto(x_ball, 270)
        x_axis, y_axis = direction()
    
    sc.ontimer(moving_game, 10)

        
def scoring_game(n):
    global score
    score += n
    scoring.clear()
    scoring.write(f"Score: {score}", align="center", font={"Arial", 24, "normal"})


sc = turtle.Screen()
sc.setup(700, 700)
sc.bgcolor("black")
sc.title("Catch the ball")

scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.goto(0, 300)
score = 0
scoring.write(f"Score: {score}", align="center", font={"Arial", 24, "normal"})
scoring.hideturtle()

paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.color("white")
paddle.penup()
paddle.goto(0, -300)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
x_ball = randint(-270, 270)
ball.goto(x_ball, 270)

sc.listen()
sc.onkeypress(go_to_left, "Left")
sc.onkeypress(go_to_right, "Right")

moving_game()
sc.mainloop()
