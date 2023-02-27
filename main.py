from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard

RESET_POSITION = (0, -200)
TARGET_Y = 200

# screen setting
screen = Screen()
screen.title("Turtle Crossing Project")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()           # create new player
screen.listen()

level = Scoreboard()        # count level and increase difficulty

game_is_on = True
while game_is_on:                   # game flow loop
    time.sleep(0.1)
    screen.onkey(player.move, "space")
    if player.ycor() > TARGET_Y:
        player.goto(RESET_POSITION)
        level.update_level()                # go to next level and reset turtle's position to default
    screen.update()

screen.exitonclick()