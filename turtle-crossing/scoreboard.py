from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 250)
        self.upgrade_score()

    def upgrade_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up_score(self):
        self.level += 1
        self.upgrade_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
