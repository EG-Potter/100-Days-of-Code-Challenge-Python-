import colorgram
from data import colors
import turtle as t

# colors = colorgram.extract('image.jpeg', 20)
#
# rgb_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_list.append(rgb_tuple)
#
# print(rgb_list)

# Dots 20 in size, 50 spaces between

import random
t.colormode(255)

dot_machine = t
dot_machine.penup()
dot_machine.hideturtle()

x = -200
y = -200

dot_machine.goto(x, y)

for i in range(10):
    for z in range(10):
        dot_machine.dot(20, random.choice(colors))
        dot_machine.forward(50)
    y += 50
    dot_machine.goto(x, y)

window = t.Screen()
window.exitonclick()
