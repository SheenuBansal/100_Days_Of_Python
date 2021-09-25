from turtle import Turtle, Screen
import random

lilly=Turtle()
my_screen=Screen()
lilly.speed(0)
direction=0

def chose_color():
    my_screen.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    lilly.pencolor(r,g,b)

while direction<=360:
    chose_color()
    direction=direction+5
    lilly.setheading(direction)
    lilly.circle(100)


my_screen.exitonclick()

