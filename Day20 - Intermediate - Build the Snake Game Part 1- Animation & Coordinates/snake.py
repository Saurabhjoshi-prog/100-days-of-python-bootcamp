from turtle import Turtle
MOVE_DISTANCE=20
class Snake:
    def __init__(self):
        self.segments=[]
        self.createsnake()
    def createsnake(self):
        for i in range(3):
            timmy = Turtle()
            timmy.color("white")
            timmy.shape("circle")
            timmy.penup()
            timmy.goto(i * -20, 0)
            self.segments.append(timmy)
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[i - 1].xcor()
            newy = self.segments[i - 1].ycor()
            self.segments[i].goto(newx, newy)
        self.segments[0].forward(MOVE_DISTANCE)




