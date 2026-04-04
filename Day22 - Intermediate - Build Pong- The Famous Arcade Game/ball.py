from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.x_move=10
        self.y_move=10
        self.movespeed=0.1

    def move(self,):
        self.penup()
        newxcor=(self.xcor()+self.x_move)
        newycor=(self.ycor()+self.y_move)
        self.goto(newxcor,newycor)
    def y_bounce(self):
        self.y_move=self.y_move*-1
    def x_bounce(self):
        self.x_move=self.x_move*-1
        self.movespeed=self.movespeed*0.9
    def reset_ball(self):
        self.movespeed=0.1
        self.goto(0,0)
        self.x_bounce()

