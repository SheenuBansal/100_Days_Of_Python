from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Arial", 13, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,275)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.total_score}",align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.total_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER !! ",align=ALIGNMENT, font=FONT)