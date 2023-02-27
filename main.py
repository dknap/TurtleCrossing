from turtle import Screen
import time
from player import Player

# screen setting
screen = Screen()
screen.title("Turtle Crossing Project")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()  # create new player
screen.listen()

game_is_on = True
while game_is_on:                   # game flow loop
    time.sleep(0.1)
    screen.onkey(player.move, "space")
    screen.update()

screen.exitonclick()