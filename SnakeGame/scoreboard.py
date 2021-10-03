from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Arial", 13, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = 0
        with open("high_score_data.txt", mode="r") as data:
            self.highest_score = int(data.read())
         
        self.penup()
        self.hideturtle()
        self.goto(0,275)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.total_score} \t Highest Score: {self.highest_score}",align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.total_score += 1
        self.update_scoreboard()

    # If you want to end Game. Proceed like below...
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"GAME OVER !! ",align=ALIGNMENT, font=FONT)

    def reset_game(self):

        if self.total_score > self.highest_score :
            self.highest_score = self.total_score
            with open("high_score_data.txt",mode="w") as data:
                data.write(str(f"{self.highest_score}"))

        self.total_score=0
        self.clear()
        self.update_scoreboard()