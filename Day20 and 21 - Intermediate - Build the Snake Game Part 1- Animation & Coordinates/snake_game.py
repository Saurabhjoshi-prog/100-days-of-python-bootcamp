from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameover import Gameover
import time
scoreboard=Scoreboard()
food=Food()
screen=Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600,height=600)
segments=[]
screen.tracer(0)
snake=Snake()
screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")
screen.update()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        print("nom nom nom")
        scoreboard.clea_screen()
        scoreboard.increase_score()
        food.refresh()
    #Detect collusion with the wall
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        GG = Gameover()
        game_is_on=False

screen.exitonclick()