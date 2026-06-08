#!/usr/bin/env python3
import turtle
import time
import random

WIDTH, HEIGHT = 800,800
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'cyan','pink', 'purple']
screen = turtle.Screen()
screen.title('Turtle Racing')
screen.setup(WIDTH,HEIGHT)
MIN_RACER = 2
MAX_RACER = 10

def init_turtle():
    screen = turtle.Screen()
    screen.title('Turtle Racing')
    screen.setup(WIDTH,HEIGHT)

def get_number_of_racers():
    racer = 0
    while True:
        racer = input("Enter the number of racers (2-10): ")
        if racer.isdigit():
            racer = int(racer)
            if MIN_RACER <= racer <= MAX_RACER:
                break
            else:
                print(f"Ther number of racer should be between ({MIN_RACER} - {MAX_RACER})")
        else:
            print(f"Input not a numeric... Try Again!")
    return racer

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2+20 )
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)  
            racer.forward(distance)
            
            x,y   = racer.pos()
            if y >= HEIGHT //2 - 10:
                return colors[turtles.index(racer)]
                
    

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(winner)
time.sleep(5)

