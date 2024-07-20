import turtle
from random import randint, shuffle
from time import sleep

WIDTH = 600
HIGHT = 500
COLORS = ["red", "black", "blue", "orange", "pink", "purple", "green", "brown", "yellow", "cyan"]

def get_number_of_racers() -> int:
    while True:
        number_of_racers = input("Enter the number of racers (2 - 10): ")
        try:
            number_of_racers = int(number_of_racers)
            if 2 <= number_of_racers <= 10:
                return number_of_racers
            else:
                print("Invalid number! Please enter a valid racers number!")
        except ValueError:
            print("Invalid input!")

def race(colors) -> int:
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = randint(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y > HIGHT // 2 - 30:
                return colors[turtles.index(racer)]

def create_turtles(colors) -> list:
    turtles = []
    x_axis = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setposition(-x_axis // 2 + (i + 1) * 40 - (len(colors) * 15), -HIGHT // 2 + 20)
        turtles.append(racer)
    
    return turtles

def init_turtle():
    sc = turtle.Screen()
    sc.setup(WIDTH, HIGHT)
    sc.title("Turtles Race")

racers = get_number_of_racers()
init_turtle()

shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner in this race is: {winner}! Congratulations 🎉.")
sleep(3)
