from turtle import Screen
import time

# screen setting
screen = Screen()
screen.title("Turtle Crossing Project")
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()