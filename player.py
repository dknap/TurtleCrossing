from turtle import Turtle

SPEED = 10
STARTING_POSITION = (0, -270)
PLAYER_COLOR = "green"
PLAYER_SHAPE = "turtle"


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color(PLAYER_COLOR)
        self.shape(PLAYER_SHAPE)
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(SPEED)