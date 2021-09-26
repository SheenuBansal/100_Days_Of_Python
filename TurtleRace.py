from turtle import Turtle, Screen, mode
import random

my_screen=Screen()
my_screen.setup(width=700,height=600)

is_race_on=False
colors=["violet","blue","green","yellow","orange","red"]
user_bet= my_screen.textinput(title="Guess who will win", prompt="Type color of turtle from VIBGYOR, you bet on: ")

finishing_line=Turtle()
finishing_line.hideturtle()
finishing_line.penup()
finishing_line.goto(x=320,y=-280)
finishing_line.setheading(90)
finishing_line.pendown()
finishing_line.forward(560)
finishing_line.color("black")

all_turtles=[]
x=-320
y=-200


for i in range(6):
    new_turtle =Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    y=y+50
    new_turtle.goto(x,y)
    all_turtles.append(new_turtle)

if user_bet :
    is_race_on=True

while is_race_on:

    for participant in all_turtles:

        if participant.xcor()> 320 :
            is_race_on=False
            winner=participant.pencolor()

            if user_bet==winner:
                print(f"You won!!! You guessed right. The winner was {winner} turtle.")
            else:
                print(f"You lost. It was not {user_bet} turtle. The winner was {winner} turtle.")
                
        participant.forward(random.randint(0,10))

my_screen.exitonclick()
    


