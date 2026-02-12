import turtle
from turtle import Turtle
class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()
