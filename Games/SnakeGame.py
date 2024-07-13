import turtle
from random import randint
from time import sleep

sc = turtle.Screen()
sc.setup(700, 700)
sc.title("Snake Game")
sc.bgcolor("black")
sc.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.setposition(-310, -310)
pen.pendown()
pen.color("lime")
pen.pensize(3)
for _ in range(4):
    pen.forward(620)
    pen.left(90)

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(randint(-300, 300), randint(-300, 300))

head = turtle.Turtle()
head.shape("square")
head.color("light green")
head.penup()
head.goto(0, 0)
dir = "stop"

DELAY = 0.1
score = 0
mx = 0
segs = []
scoring = turtle.Turtle()
scoring.hideturtle()
scoring.penup()
scoring.color("white")
scoring.goto(0, 320)
scoring.write(f"Score: {score}, Max Score: {mx}", align="center", font=("Arial", 16))

def direction(direct):
    global dir
    if (direct == "up" and dir != "down") \
    or (direct == "down" and dir != "up") \
    or (direct == "left" and dir != "right") \
    or (direct == "right" and dir != "left"):
        dir = direct

sc.listen()
sc.onkeypress(lambda: direction("up"), 'w')
sc.onkeypress(lambda: direction("down"), 's')
sc.onkeypress(lambda: direction("left"), 'a')
sc.onkeypress(lambda: direction("right"), 'd')

def move():
    if dir == "up":
        head.sety(head.ycor() + 20)
    if dir == "down":
        head.sety(head.ycor() - 20)
    if dir == "left":
        head.setx(head.xcor() - 20)
    if dir == "right":
        head.setx(head.xcor() + 20)

def lost():
    global score, dir, DELAY
    sleep(1)
    dir = "stop"
    for seg in segs:
        seg.goto(1000, 1000)
    segs.clear()
    score = 0
    head.goto(0, 0)
    food.goto(randint(-300, 300), randint(-300, 300))
    scoring.clear()
    scoring.write(f"Score: {score}, Max Score: {mx}", align="center", font=("Arial", 16))
    DELAY = 0.01

while True:
    sc.update()
    if head.xcor() >= 300 or head.xcor() <= -300 or head.ycor() >= 300 or head.ycor() <= -300:
        lost()
        scoring.write(f"Score: {score}, Max Score: {mx}", align="center", font=("Arial", 16))
    if head.distance(food) < 20:
        food.goto(randint(-300, 300), randint(-300, 300))        
        new = turtle.Turtle()
        new.shape("square")
        new.color("light blue")
        new.penup()
        segs.append(new)
        score += 1
        mx = max(mx, score)
        scoring.clear()
        scoring.write(f"Score: {score}, Max Score: {mx}", align="center", font=("Arial", 16))
        DELAY -= 0.001
    for idx in range(len(segs)-1, 0, -1):
        segs[idx].goto(segs[idx-1].pos())
    if len(segs) > 0:
        segs[0].goto(head.pos())
    move()
    for seg in segs:
        if head.distance(seg) < 20:
            lost()
    sleep(DELAY)
    
sc.mainloop()
