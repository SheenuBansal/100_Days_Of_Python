from turtle import Turtle

ALIGNMENT="center"
POSITION = (-250,240)
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(POSITION)
        self.hideturtle()
        self.level_number=1
        self.update_scoreboard()      

    def increase_score(self):
        self.level_number+=1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level : {self.level_number}",align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.write(arg=f"Game Over !! ",align=ALIGNMENT, font=FONT)
        