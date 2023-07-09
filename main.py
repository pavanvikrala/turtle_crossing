import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    # Detect collision with a car
    for vehicle in car.all_cars:
        if vehicle.distance(player) < 25:
            game_is_on = False
            score.game_over()

    # Detect Successful crossing
    if player.finish_line():
        player.goto_start()
        car.level_up()
        score.increase_level()

screen.exitonclick()
