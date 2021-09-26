from turtle import Turtle, Screen
from snake import Snake
import time

my_screen=Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.title("Welcome To The Snake Game!!!")
my_screen.tracer(0)

snake=Snake()

my_screen.listen()
my_screen.onkey(fun=snake.snake_up, key="Up")
my_screen.onkey(fun=snake.snake_down, key="Down")
my_screen.onkey(fun=snake.snake_left, key="Left")
my_screen.onkey(fun=snake.snake_right, key="Right")

is_game_on=True
while is_game_on:
    my_screen.update()
    time.sleep(0.5)
    snake.move()

my_screen.exitonclick()