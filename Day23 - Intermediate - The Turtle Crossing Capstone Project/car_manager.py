import turtle
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed=10
    def generate_car(self):
        random_choice = random.randint(1, 3)
        if random_choice == 1:
            new_car=Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed+=7


