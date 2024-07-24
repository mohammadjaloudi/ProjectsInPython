import turtle

sc = turtle.Screen()
sc.setup(500, 500)
sc.bgcolor("sky blue")

ground = turtle.Turtle()
ground.hideturtle()
ground.penup()
ground.goto(-250, -50)
ground.pendown()

ground.fillcolor("lime")

ground.begin_fill()
for _ in range(4):
    ground.forward(500)
    ground.right(90)
ground.end_fill()

base = turtle.Turtle()
base.hideturtle()
base.penup()
base.goto(-100, -50)
base.pendown()

base.fillcolor("pink")

base.begin_fill()
for _ in range(4):
    if _ % 2 == 0:
        base.forward(200)
        base.left(90)
    else:
        base.forward(130)
        base.left(90)
base.end_fill()

roof = turtle.Turtle()
roof.hideturtle()
roof.penup()
roof.goto(-100, 80)
roof.pendown()

roof.fillcolor("light blue")

roof.begin_fill()
roof.forward(200)
roof.left(135)
roof.forward(142)
roof.left(90)
roof.forward(142)
roof.end_fill()

def draw_window(x, y):
    window = turtle.Turtle()
    window.hideturtle()
    window.penup()
    window.goto(x, y)
    window.pendown()
    window.fillcolor("white")
    
    window.begin_fill()
    for _ in range(4):
        window.forward(35)
        window.right(90)
    window.end_fill()

draw_window(-80, 50)
draw_window(-25, 50)
draw_window(40, 45)
draw_window(-60, 0)

door = turtle.Turtle()
door.hideturtle()
door.penup()
door.goto(-5, -50)
door.pendown()

door.fillcolor("turquoise")

door.begin_fill()
for _ in range(4):
    if _ % 2 == 0:
        door.forward(30)
    else:
        door.forward(45)
    door.left(90)
door.end_fill()
door.goto(25, -50)
door.begin_fill()
for _ in range(4):
    if _ % 2 == 0:
        door.forward(30)
    else:
        door.forward(45)
    door.left(90)
door.end_fill()

sc.mainloop()
