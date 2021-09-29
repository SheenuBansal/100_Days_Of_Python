from turtle import Turtle

MOVE_DISTANCE=20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.shape("turtle")
        self.penup()
        self.goto(0,-245)  
        self.setheading(90)
        self.color("green")  

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.reset()
        self.create_player()
        