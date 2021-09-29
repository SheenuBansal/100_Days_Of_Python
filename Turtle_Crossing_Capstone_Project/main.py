from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from carmanager import CarManager
import time

my_screen = Screen()
my_screen.screensize(canvwidth=600, canvheight=600)
my_screen.title("Turtle Crossing Game !!")
my_screen.tracer(0)

scoreboard=Scoreboard()
player=Player()
carmanager=CarManager()

my_screen.listen()
my_screen.onkey(fun=player.move_up, key="Up")

is_game_on= True
counter=0
while is_game_on :
    my_screen.update()
    time.sleep(0.1)
    counter+=1
    
    # Cotrolling the number of cars generated.
    if counter % 6 == 0:
        carmanager.generate_car()
        carmanager.move_cars()

    # Checking when the player has crossed finished line.  
    if player.ycor()>240 :
        player.reset_player()
        carmanager.level_up_speed()
        scoreboard.increase_score()

    # Detecting the collision of player with cars.
    for car in carmanager.cars :
        if car.distance(player) <= 20 :
            scoreboard.game_over()                
            is_game_on = False

my_screen.exitonclick()