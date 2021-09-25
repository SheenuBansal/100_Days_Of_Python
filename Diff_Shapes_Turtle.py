# # --------------------- CHALLENGE 3 -----------------------------
# --------------------DRAW VARIOUS SHAPES WITH RANDOM COLORS --------------------------

from turtle import Turtle, Screen, colormode
import random

my_screen=Screen()
kimmy=Turtle()

def chose_color():
    my_screen.colormode(255)
    first_color=random.randint(1,255)
    second_color=random.randint(1,255)
    third_color=random.randint(1,255)
    kimmy.pencolor(first_color,second_color,third_color)


def diff_shapes(i):
    chose_color()
    angle=int(360/i)
    for _ in range(i):
        kimmy.forward(100)
        kimmy.right(angle)


for i in range(3,11):
    diff_shapes(i)

my_screen.exitonclick()

