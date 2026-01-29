from turtle import Turtle,Screen
timmy=Turtle()
screen=Screen()
# #Todo 1: make a square
#  # for i in range(4):
#  #     timmy.forward(100)
#  #     timmy.right(90)
#  # screen.exitonclick()
#  #Todo 2: make  a dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#Todo 3: make shapes
side=3
while side<=10:
    for i in range(side):
        timmy.right(360/side)
        timmy.forward(100)
    side+=1

screen.exitonclick()