import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    car_manager.move_cars()
    if player.border_check():
        player.staring_position()
        car_manager.speed_up()
        scoreboard.increase_score()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    time.sleep(0.1)
    screen.update()

screen.exitonclick()