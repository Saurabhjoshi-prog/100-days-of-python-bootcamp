from turtle import Turtle ,Screen
timmy=Turtle()
screen=Screen()
def move_forwards():
    return timmy.forward(10)
screen.listen()
screen.onkey(key="space",fun=move_forwards)
screen.exitonclick()