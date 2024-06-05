from turtle import Turtle
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-50, 220)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(50, 220)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
