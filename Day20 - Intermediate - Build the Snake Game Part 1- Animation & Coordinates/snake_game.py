from turtle import Turtle,Screen
import time
screen=Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600,height=600)
segments=[]
screen.tracer(0)
for i in range(3):
    timmy=Turtle()
    timmy.color("white")
    timmy.shape("circle")
    timmy.penup()
    timmy.goto(i*-20, 0)
    segments.append(timmy)
screen.update()
game_is_on=True
while game_is_on:
    screen.update()

    for i in range(len(segments)-1,0,-1):
        newx=segments[i-1].xcor()
        newy=segments[i-1].ycor()
        segments[i].goto(newx,newy)
    segments[0].forward(20)
    segments[0].right(90)
    time.sleep(0.1)

screen.exitonclick()