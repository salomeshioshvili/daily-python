# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst_painting.png', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

import turtle as t
from turtle import Screen
import random

sali = t.Turtle()
sali.shape("turtle")
sali.speed("fast")

sali.hideturtle()

t.colormode(255)
color_list = [(232, 241, 239), (229, 235, 242), (239, 232, 238), (122, 95, 41), (71, 31, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 171), (151, 92, 115), (35, 90, 26), (7, 154, 72), (205, 63, 91), (221, 178, 218), (168, 129, 77), (1, 64, 147), (3, 79, 29), (4, 220, 218), (80, 135, 179), (132, 158, 177), (81, 110, 136), (116, 187, 164), (11, 215, 222), (117, 19, 37), (131, 224, 209), (230, 173, 165), (243, 205, 7)]

sali.penup()
sali.goto(-225, -225)
sali.setheading(0)

for i in range(10):
    for j in range(10):
        sali.dot(20, random.choice(color_list))
        sali.penup()
        sali.forward(50)
    sali.teleport(-225, (sali.ycor() + 50))

screen = Screen()
screen.exitonclick()