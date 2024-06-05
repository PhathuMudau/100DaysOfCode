from turtle import Turtle

PADDLE_MOVEMENT = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + PADDLE_MOVEMENT
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - PADDLE_MOVEMENT
        self.goto(self.xcor(), new_y)

