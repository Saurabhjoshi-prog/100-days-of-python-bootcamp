import random
import turtle
from turtle import Turtle,Screen
timmy=Turtle()
screen=Screen()
# #Todo 1: make a square
  # for i in range(4):
#  #     timmy.forward(100)
#  #     timmy.right(90)
#  # screen.exitonclick()
#  #Todo 2: make  a dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# #Todo 3: make shapes and each shape with different colours
# colors=["crimson","coral","orange red","chocolate","brown","aquamarine","medium aquamarine"]
# side=3
# while side<=10:
#     timmy.color(random.choice(colors))
#     for i in range(side):
#         timmy.right(360/side)
#         timmy.forward(100)
#     side+=1

# #Todo: Turtle Challenge 4 - Generate a Random Walk
# timmy.shape("turtle")
# p=1
# s=1
# movement=[90,180,270,0]
# colors=["crimson","coral","orange red","chocolate","brown","aquamarine","medium aquamarine"]
# for i in range (0,200):
#     a=random.choice(movement)
#     timmy.color(random.choice(colors))
#     timmy.forward(30)
#     timmy.setheading(a)
#     timmy.pensize(p)
#     timmy.speed(s)
#
#     p+=0.20
#     s+=1

# #Todo:Python Tuples and How to Generate Random RGB Colours
# screen.colormode(255)
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     color=(r,g,b)
#     return color
# timmy.shape("turtle")
# p=1
# s=1
# movement=[90,180,270,0]
# for i in range (0,200):
#     a=random.choice(movement)
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(a)
#     timmy.pensize(p)
#     timmy.speed(s)
#
#     p+=0.20
#     s+=1
#Todo:Turtle Challenge 5 - Draw a Spirograph
screen.colormode(255)
def random_color():
     r=random.randint(0,255)
     g=random.randint(0,255)
     b=random.randint(0,255)
     color=(r,g,b)
     return color
timmy.shape("turtle")
timmy.speed(0)
def make_spirograph(size):
    for i in range (int(360//size)):
        timmy.color(random_color())
        timmy.circle(-100)
        current_heading=timmy.heading()
        timmy.setheading(current_heading+size)
make_spirograph(7)
screen.exitonclick()