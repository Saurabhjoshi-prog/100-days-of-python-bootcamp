
import random
from turtle import Screen,Turtle
# import colorgram

# colors=colorgram.extract("das.jpg",30)
# rgb_list=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_list.append(new_color)

list_hi_kehde=[(108, 110, 127), (209, 155, 94), (139, 141, 151), (188, 61, 29), (226, 213, 107), (235, 217, 225), (207, 148, 176), (102, 110, 172), (177, 157, 45), (225, 233, 227), (37, 40, 20), (29, 27, 68), (193, 20, 8), (31, 46, 29), (225, 168, 197), (45, 46, 103), (212, 86, 59), (126, 90, 99), (237, 172, 159), (89, 100, 91), (205, 82, 108), (182, 184, 214), (155, 164, 156), (179, 16, 22), (45, 27, 46), (71, 71, 41), (52, 71, 53), (222, 204, 29)]
timmy=Turtle()
screen=Screen()
screen.colormode(255)
timmy.shape("turtle")
timmy.pensize(20)
k=0
for i in range(10):
    timmy.goto(0, k)

    for j in range(10):
        timmy.pendown()
        timmy.color(random.choice(list_hi_kehde))
        timmy.forward(1)
        timmy.penup()
        timmy.forward(50)
    k += 50




screen.exitonclick()