from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Welcome To The Snake Game!!!")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard=Scoreboard()
boundary_wall=[-285,285]

my_screen.listen()
my_screen.onkey(fun=snake.snake_up, key="Up")
my_screen.onkey(fun=snake.snake_down, key="Down")
my_screen.onkey(fun=snake.snake_left, key="Left")
my_screen.onkey(fun=snake.snake_right, key="Right")

is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.15)
    snake.move()

    # Detect collission with food
    if snake.head.distance(food)<12 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or \
        snake.head.ycor() > 288 or snake.head.ycor() < -285 : 

        is_game_on = False
        scoreboard.game_over()

    # Detect collision with own tail
    for segment in snake.segments[1:] :
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

            

        
my_screen.exitonclick()
