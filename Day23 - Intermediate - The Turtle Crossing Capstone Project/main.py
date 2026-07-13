import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.go_up,"Up")

car_manager = CarManager()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move()

    #Detect the collusion
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            scoreboard.game_over()

            game_is_on = False
    if player.is_finished_line():
        scoreboard.increase_score()
        car_manager.increase_speed()
        player.go_back()




screen.exitonclick()





