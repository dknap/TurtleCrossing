from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
import random
from car import Car
from end_game import GameOver

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
screen.onkey(player.move, KEY)

for car in range(0, 700):        # generate cars
    new_car = Car()
    car_x = random.randint(300, 50000)
    car_y = random.randint(-200, 220)
    new_car.goto(car_x, car_y)
    cars.append(new_car)

end_game = GameOver()

# game flow loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # car behaviour
    for car in cars:
        car.drive(CAR_SPEED)
    if player.ycor() > TARGET_Y:
        # go to next level and reset turtle's position to default
        player.goto(RESET_POSITION)
        level.update_level()
        CAR_SPEED *= 1.3
        for car in cars:
            car.drive(CAR_SPEED)

    # detect collides with a car
    for car in cars:
        if player.distance(car.position()) < 25:
            game_is_on = False
            end_game.crash()

    screen.update()

screen.exitonclick()