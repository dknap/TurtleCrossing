from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
import random
from car import Car

RESET_POSITION = (0, -270)
TARGET_Y = 250
KEY = "space"
cars = []
CAR_SPEED = 10

# screen setting
screen = Screen()
screen.title("Turtle Crossing Project")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()           # create new player
screen.listen()

level = Scoreboard()        # count level and increase difficulty


for car in range(0, 500):        # generate cars
    new_car = Car()
    car_x = random.randint(300, 30000)
    car_y = random.randint(-200, 220)
    new_car.goto(car_x, car_y)
    cars.append(new_car)

game_is_on = True
while game_is_on:                   # game flow loop
    time.sleep(0.1)
    for car in cars:
        car.drive(CAR_SPEED)
    screen.onkey(player.move, KEY)
    if player.ycor() > TARGET_Y:
        for car in cars:
            car.drive(CAR_SPEED)
        player.goto(RESET_POSITION)
        level.update_level()                # go to next level and reset turtle's position to default
        CAR_SPEED *= 1.3

    screen.update()

screen.exitonclick()