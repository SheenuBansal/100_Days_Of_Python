from turtle import Turtle
import random

colors=["red","orange","yellow","blue","violet","brown","green"]
MOVE_DISTANCE=20

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars=[]
        self.car_speed=MOVE_DISTANCE

    def generate_car(self):   
        new_car = Turtle(shape="square")
        new_car.color(random.choice(colors))
        new_car.shapesize(stretch_len=2,stretch_wid=1)
        new_car.penup()
        pos_y=random.randint(-200,200)
        new_car.goto(300,pos_y)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
             car.backward(self.car_speed)

    def level_up_speed(self):
        self.car_speed+= MOVE_DISTANCE
        
