from turtle import Turtle,Screen
from snake import Snake
import time
screen=Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600,height=600)
segments=[]
screen.tracer(0)
snake=Snake()
screen.update()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()