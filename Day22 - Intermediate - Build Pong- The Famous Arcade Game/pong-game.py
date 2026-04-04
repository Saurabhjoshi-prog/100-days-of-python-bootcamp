from turtle import Turtle,Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time
ball=Ball()
scoreboard=Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)
right_paddle=Paddle(350)
left_paddle=Paddle(-350)
screen.listen()
right_paddle.go_up()
screen.onkey(right_paddle.go_up,"Up")
screen.listen()
screen.onkey(right_paddle.go_down,"Down")
screen.listen()
screen.onkey(left_paddle.go_up,"w")
screen.listen()
screen.onkey(left_paddle.go_down,"s")
game_is_on=True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    #collision with the wall
    if ball.ycor()>270 or ball.ycor()<-270:
        ball.y_bounce()
    #collision with the paddle
    if ball.xcor()>324 and ball.distance(right_paddle)<50 or ball.xcor()<-324 and ball.distance(left_paddle)<50:
        ball.x_bounce()
    #left misses
    if ball.xcor()<-380:
        ball.reset_ball()
        scoreboard.left_miss()

    #right misses
    elif ball.xcor()>380:
        ball.reset_ball()
        scoreboard.right_miss()


screen.exitonclick()