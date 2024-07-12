import turtle
from random import shuffle

click_positions = []
curr = None
card_index = None

def get_mouse_click_coor(x, y):
    global curr, card_index
    
    card_index = num(x, y)
    
    if card_index is not None:
        click_positions.append(card_index)
        reveal_card(card_index)
        
        if len(click_positions) % 2 == 0:
            first_card = click_positions[-2]
            second_card = click_positions[-1]
            
            if numbers[first_card] == numbers[second_card] and first_card != second_card and visited[first_card] == visited[second_card] == True:
                visited[first_card] = False
                visited[second_card] = False
                print(f"Match found: {numbers[first_card]}")
            else:
                print(f"No match: {numbers[first_card]}, {numbers[second_card]}")
                turtle.ontimer(hide_cards, 100)

numbers = [1, 1, 2, 2, 3, 3, 4, 4]
visited = [True] * 8
shuffle(numbers)

def num(x, y):
    if -200 <= x <= -100 and 50 <= y <= 150:
        return 0
    if -100 <= x <= 0 and 50 <= y <= 150:
        return 1
    if 0 <= x <= 100 and 50 <= y <= 150:
        return 2
    if 100 <= x <= 200 and 50 <= y <= 150:
        return 3
    if -200 <= x <= -100 and -50 <= y <= 50:
        return 4
    if -100 <= x <= 0 and -50 <= y <= 50:
        return 5
    if 0 <= x <= 100 and -50 <= y <= 50:
        return 6
    if 100 <= x <= 200 and -50 <= y <= 50:
        return 7
    return None

def draw_cards():
    card.color("white", "light green")
    for i in range(4):
        card.begin_fill()
        for j in range(4):
            card.forward(100)
            card.left(90)
        card.end_fill()
        card.penup()
        card.forward(100)
        card.pendown()
    card.penup()
    card.goto(-200, -50)
    card.pendown()
    for i in range(4):
        card.begin_fill()
        for j in range(4):
            card.forward(100)
            card.left(90)
        card.end_fill()
        card.penup()
        card.forward(100)
        card.pendown()
    card.penup()

def reveal_card(index):
    x = -200 + (index % 4) * 100 + 40
    y = 50 - (index // 4) * 100 - 20
    pen.penup()
    pen.goto(x, y + 50)
    pen.pendown()
    pen.write(numbers[index], font=("Arial", 24, "normal"))

def hide_cards():
    for index in click_positions[-2:]:
        if visited[index] == False:
            continue
        x = -200 + (index % 4) * 100
        y = 50 - (index // 4) * 100
        card.penup()
        card.goto(x, y)
        card.pendown()
        card.begin_fill()
        for _ in range(4):
            card.forward(100)
            card.left(90)
        card.end_fill()
    click_positions[-2:] = []

sc = turtle.Screen()
sc.bgcolor("sky blue")
sc.setup(500, 500)

card = turtle.Turtle()
card.speed(0)
card.hideturtle()
card.penup()
card.goto(-200, 50)
card.pendown()
draw_cards()

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

sc.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
