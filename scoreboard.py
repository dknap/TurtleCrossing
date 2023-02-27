from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "right"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(250, 250)
        self.level = 1
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def update_level(self):             # update and print current level
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)