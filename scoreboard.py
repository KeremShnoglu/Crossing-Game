from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.SCORE=0
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.write(f"Score = {self.SCORE}", False, align='left', font=FONT)
    def score_increase(self):
        self.SCORE+=1
        self.clear()
        self.write(f"Score = {self.SCORE}", False, align='left', font=FONT)