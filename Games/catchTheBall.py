import turtle
from random import randint

sc = turtle.Screen()
sc.title("Catch the ball game")
sc.setup(width=600, height=600)
sc.bgcolor("white")

boreder = turtle.Turtle()
boreder.speed(0)
boreder.color("black")
boreder.penup()
boreder.setposition(-290, -290)
boreder.pendown()
boreder.pensize(3)
for i in range(4):
     boreder.forward(580)
     boreder.left(90)
boreder.hideturtle()

paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("orange")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(randint(-250, 250), 250)

ball_speed = 1

score = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font={"Courier", 24, "nomral"})

def scoring():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font={"Courier", 24, "nomral"})

def left_paddle():
    x = paddle.xcor()
    x -= 20
    if x > -250:
        paddle.setx(x)

def right_paddle():
    x = paddle.xcor()
    x += 20
    if x < 250:
        paddle.setx(x)

sc.listen()
sc.onkeypress(right_paddle, "Right")
sc.onkeypress(left_paddle, "Left")

def game():
    global score 
    ball.sety(ball.ycor() - ball_speed)
    
    if ball.ycor() < -290:
        ball.goto(randint(-250, 250), 250)
    
    if ball.ycor() <= -240 and ball.ycor() >= -260 and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50:
        ball.goto(randint(-255, 255), 255)
        score += 1
        scoring()
    
    sc.ontimer(game, 1)
        

game()
sc.mainloop()
