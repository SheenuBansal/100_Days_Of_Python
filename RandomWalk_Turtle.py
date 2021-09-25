from turtle import Turtle, Screen,colormode
import random

lilly=Turtle()
my_screen=Screen()
lilly.speed(10)

def chose_color():
    my_screen.colormode(255)
    first_color=random.randint(0,255)
    second_color=random.randint(0,255)
    third_color=random.randint(0,255)
    lilly.pencolor(first_color,second_color,third_color)


def turtles_direction():
    direction=[0,90,180,270]
    return random.choice(direction)

for _ in range(200):
    chose_color()
    lilly.pensize(10)
    lilly.left(turtles_direction())
    lilly.forward(30)
    
my_screen.exitonclick()