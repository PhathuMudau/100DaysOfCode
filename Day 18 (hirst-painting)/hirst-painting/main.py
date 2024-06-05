from turtle import Turtle, Screen
import random

# import colorgram
#
# colours = colorgram.extract('image.jpg', 30)
#
# extract = []
#
# for n in range(3, 26):
#     colour_extract = colours[n]
#     rgb = colour_extract.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     colour = (r, g, b)
#     extract.append(colour)
#
# print(extract)
# print(len(extract))
import turtle

colour_list = [
    (23, 16, 94), (232, 43, 6), (153, 14, 30), (41, 181, 158), (127, 253, 206), (237, 71, 166),
    (209, 179, 208), (246, 218, 21), (40, 133, 242), (244, 247, 253), (246, 218, 5), (207, 148, 178),
    (126, 155, 204), (106, 189, 174), (224, 134, 117), (81, 87, 136), (150, 64, 75), (209, 87, 66),
    (49, 44, 100), (244, 168, 154), (175, 184, 222), (111, 9, 23), (179, 30, 10)
]


turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.hideturtle()
start_x = -250
start_y = -250
tim.goto(start_x, start_y)

for _ in range(10):
    for n in range(10):
        tim.color(random.choice(colour_list))
        tim.dot(20)
        tim.forward(50)

    start_y += 50
    tim.goto(start_x, start_y)




screen = Screen()
screen.exitonclick()