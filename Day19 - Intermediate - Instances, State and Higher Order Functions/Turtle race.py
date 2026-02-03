from turtle import Screen,Turtle
import random
screen = Screen()
screen.setup(width=500,height=400)
a=screen.textinput(title="Make a bet on a Color",prompt="red,green,yellow,blue,purple,indigo")
t_color=["red","green","yellow","blue","purple","orange","indigo"]
y_index=[180,-180,-120,120,60,-60,0]
all_turtles=[]
race_is_on=False
for turtle_index in range(0,7):
    timmy=Turtle("turtle")
    timmy.penup()
    timmy.color(t_color[turtle_index])
    timmy.goto(-230, y_index[turtle_index])
    all_turtles.append(timmy)
if a in t_color:
    race_is_on=True
screen.update()
while race_is_on:
    for turtle_index in all_turtles:
        turtle_index.forward(random.randint(1, 10))
        if turtle_index.xcor()>230:
            winner=turtle_index
            race_is_on=False
            if winner == a.lower():
                print("Congratulations! You win!")
            else:
                print("Sorry, you lose!")
screen.exitonclick()
