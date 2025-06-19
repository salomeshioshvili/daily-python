from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-40, 240)
        self.write(f"{self.score_l}", align="center", font=("Courier", 48, "normal"))
        self.goto(60, 240)
        self.write(f"{self.score_r}", align="center", font=("Courier", 48, "normal"))

    def increase_score_r(self):
        self.score_r += 1
        self.update_scoreboard()

    def increase_score_l(self):
        self.score_l += 1
        self.update_scoreboard()