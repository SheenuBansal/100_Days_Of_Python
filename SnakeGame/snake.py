from turtle import Turtle

# Starting Positions of all three turtles(which combine to form snake)
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """ Creating a Snake of length 3 squares"""      
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def move(self):
        """ Making a snake move"""

        # Direction of Tail of Snake
        # eg we have turtle of 3 length, 3 will move to 2, 2 will move to 1 position and 1 will go in new direction, so will count separately.
        for segment_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[segment_num-1].xcor()
            new_y = self.segments[segment_num-1].ycor()
            self.segments[segment_num].goto(new_x,new_y)
        
        # Direction of Head of Snake
        self.head.forward(MOVE_DISTANCE)

    def snake_up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)

    def snake_left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)

    def snake_right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)


        