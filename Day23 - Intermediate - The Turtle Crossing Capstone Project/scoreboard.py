from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-270,250)
        self.write(f"Score: {self.level}", align="left", font=FONT)
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.level}", align="left",font=FONT)
    def increase_score(self):
        self.level+=1
        self.update_score()
    def game_over(self):
        self.goto(0,-36)
        self.write(f"GAME OVER", align="center", font=("Courier", 50, "normal"))



