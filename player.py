from turtle import Turtle

SPEED = 10
STARTING_Y = -200
TARGET = 280
PLAYER_COLOR = "green"
PLAYER_SHAPE = "turtle"


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color(PLAYER_COLOR)
        self.shape(PLAYER_SHAPE)
        self.penup()
        self.left(90)
        self.goto(0, STARTING_Y)

    def move(self):
        self.forward(10)