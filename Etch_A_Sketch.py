from turtle import Turtle, Screen, mode
import random

lilly=Turtle()
my_screen=Screen()

lilly.speed(0)

def chose_color():
    my_screen.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    lilly.pencolor(r,g,b)
    
def move_forward():
    chose_color()
    lilly.forward(30)

def move_backward():
    chose_color()
    lilly.backward(30)

def move_left():
    chose_color()
    new_heading=lilly.heading()+10
    lilly.setheading(new_heading)

def move_right():
    chose_color()
    new_heading=lilly.heading()-10
    lilly.setheading(new_heading)

def draw_circle():
    chose_color()
    lilly.circle(5)

def clear():
    lilly.clear()
    lilly.penup()
    lilly.home()
    lilly.pendown()


my_screen.listen()
my_screen.onkey(move_forward,key="w")
my_screen.onkey(move_backward,key="s")
my_screen.onkey(move_left,key="d")
my_screen.onkey(move_right,key="a")
my_screen.onkey(draw_circle,key="r")
my_screen.onkey(clear,key="c")

my_screen.exitonclick()