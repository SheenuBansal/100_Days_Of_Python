from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        # actual size of circle is 20*20, now it wud be 10*10
        self.shapesize(stretch_len=0.2, stretch_wid=0.2)
        self.color("yellow")
        self.speed(0)
        self.refresh()

    def refresh(self):

        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)

    