from turtle import Turtle,Screen
MOVE_DISTANCE=20
screen = Screen()
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
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)




