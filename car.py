from turtle import Turtle
import random

COLORS = ["black", "red", "blue", "pink", "purple"]
SHAPE = "square"


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color = self.color(COLORS[0], COLORS[random.randint(0, len(COLORS) - 1)])
        self.penup()
        self.goto(0, 0)
        self.shapesize(stretch_wid=1, stretch_len=2)
        print(self.color)