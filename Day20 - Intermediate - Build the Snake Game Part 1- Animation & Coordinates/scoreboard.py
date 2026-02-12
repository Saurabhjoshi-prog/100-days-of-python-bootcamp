from turtle import Turtle,Screen
s=Screen()
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.a=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"ScoreBoard {self.a}", align="center", font=("Courier", 12, "normal"))
    def increase_score(self):
        self.a += 1
        self.write(f"ScoreBoard {self.a}", align="center", font=("Courier", 12, "normal"))
    def clea_screen(self):
        self.clear()

