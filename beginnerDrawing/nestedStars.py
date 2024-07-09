import turtle
from random import randint

sc = turtle.Screen()
sc.setup(500, 500)
turtle.colormode(255)
pen = turtle.Turtle()
pen.speed(5)
pen.penup()
pen.goto(0, 100)
pen.pendown()

def draw_star(num, rot, star):
    size = 100
    for _ in range(num):
        a = randint(0, 255)
        b = randint(0, 255)
        c = randint(0, 255)
        
        pen.fillcolor(a, b, c)
        pen.color(a, b, c)
        pen.begin_fill()
        
        for _ in range(5):
            pen.forward(size)
            pen.right(star)
            pen.forward(size)
            pen.right(72 - star)
        
        size -= 3
        pen.end_fill()
        pen.penup()
        pen.right(rot - _)
        pen.forward(size - 15)
        pen.right(rot - _)
        # pen.forward(size - 30)
        pen.pendown()
        
numberOfStars = 20
rotationDegrees = 18
starAngle = 144

draw_star(numberOfStars, rotationDegrees, starAngle)

turtle.done()
