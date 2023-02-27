from turtle import Turtle

FONT = ("Courier", 30, "normal")
ALIGNMENT = "center"
MSG = "GAME OVER :("


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0, -270)

    def crash(self):
        self.write(MSG, align=ALIGNMENT, font=FONT)