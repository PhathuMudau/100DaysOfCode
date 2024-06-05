import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.shape("turtle")
# tim.color("teal")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# for n in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# no = 3
#
# while no < 11:
#     r = random.randint(1, 255)
#     g = random.randint(1, 255)
#     b = random.randint(1, 255)
#     tup = (r, g, b)
#     colormode(255)
#     for n in range(no):
#         tim.pencolor(tup)
#         angle = 360/no
#         tim.forward(100)
#         tim.right(angle)
#     no += 1


# angles = [0, 90, 180, 270]
# colours = ["blue", "red", "orange", "coral", "teal", "purple", "cornsilk", "aquamarine", "gold", "salmon"]
# tim.pensize(10)
# tim.speed("fastest")
#
# for _ in range(500):
#     tim.color(random.choice(colours))
#     tim.forward(25)
#     tim.setheading(random.choice(angles))

def colours():
    """Return a random RGB tuple"""
    turtle.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour_choice = (r, g, b)
    return colour_choice


number = 0

while number <= 360:
    heading = number
    tim.setheading(heading)
    tim.speed("fastest")
    tim.color(colours())
    tim.circle(100)

    number += 2







screen = Screen()
screen.exitonclick()