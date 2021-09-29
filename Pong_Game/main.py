from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

import time

my_screen=Screen()
my_screen.setup(width=800,height=600)
my_screen.bgcolor("black")
my_screen.title("Let's play Pong Game !! ")
my_screen.tracer(0)

left_paddle=Paddle((-350, 0))
right_paddle=Paddle((350, 0))

ball=Ball()
scoreboard=Scoreboard()

my_screen.listen()
my_screen.onkey(fun=right_paddle.move_up,key="Up")
my_screen.onkey(fun=right_paddle.move_down,key="Down")


my_screen.onkey(fun=left_paddle.move_up,key="w")
my_screen.onkey(fun=left_paddle.move_down,key="s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor()>280 or ball.ycor() < -280 :
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(right_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle misses 
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle misses 
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

my_screen.exitonclick()
