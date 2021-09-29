from turtle import Turtle

FONT=("Calibri", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed(0)
        self.hideturtle()
        self.setheading(90)
        self.penup()
        
        self.l_score=0
        self.r_score=0
        self.update_score_board()
    
    def update_score_board(self):
        self.goto(0,-280)
        for i in range(1,31):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
    
        self.clear()
        self.goto(-100,250)
        self.write(self.l_score, align="center",font= FONT)
        
        self.goto(50,250)
        self.write(self.r_score,align="center",font=FONT)

        self.goto(0,-280)
        for i in range(1,31):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
    
    def l_point(self):
        self.l_score += 1
        self.update_score_board()
    
    def r_point(self):
        self.r_score += 1
        self.update_score_board()
           
    
