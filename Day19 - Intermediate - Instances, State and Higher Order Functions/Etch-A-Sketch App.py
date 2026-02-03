from turtle import Turtle,Screen
mouse=Turtle()
screen=Screen()
screen.listen()
def move_forwards():
    return mouse.forward(10)
def move_back():
    return mouse.back(10)
def turn_left():
    return mouse.left(10)
def turn_right():
    return mouse.right(10)
def clear():
    return screen.resetscreen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_back)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="q",fun=clear)
screen.exitonclick()