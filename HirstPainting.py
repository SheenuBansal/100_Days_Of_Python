# Using Colorgram to extract various colors from some image

# import colorgram

# colors=colorgram.extract("E:\\100_days_of_Python\\HirstPainting_Project\\damien_hirst_dot_painting.jpg",20)

# required_colors=[]
# for i in range(len(colors)):
#     required_colors.append(tuple(colors[i].rgb))

# print(required_colors)

###### You can remove white from this color list, by checking colors on w3schools platform. ######
######The more closer u are to 255, its probably white ######

# color_list=[(244, 240, 232), (245, 235, 239), (229, 238, 244), (237, 244, 241), (199, 157, 115), (45, 110, 147), (134, 171, 190), (226, 207, 114), (134, 83, 67), (150, 64, 84), (197, 142, 153), (188, 88, 104), (188, 99, 84), (150, 178, 165), (172, 153, 61), (69, 114, 93), (37, 49, 67), (224, 172, 181), (58, 47, 40), (223, 178, 170)]

from turtle import Turtle, Screen, colormode
import random

my_screen=Screen()


def chose_color():
    my_screen.colormode(255)
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    lilly.pencolor(r,g,b)

lilly=Turtle()
lilly.speed(0)

lilly.setheading(225)
lilly.penup()
lilly.hideturtle()
lilly.forward(300)
lilly.setheading(0)


for i in range(1,101):
    chose_color()    
    lilly.dot(15)
    lilly.forward(50)

    if i % 10 == 0 :
        lilly.setheading(90)
        lilly.forward(50)
        lilly.setheading(180)
        lilly.forward(500)
        lilly.setheading(0)

my_screen.exitonclick()














