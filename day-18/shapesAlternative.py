import turtle as t
import random

tim = t.Turtle()

colors = [
    "gold1",
    "DodgerBlue",
    "gray30",
    "green4",
    "hotpink",
    "OrangeRed",
    "red",
    "DarkOrchid4",
]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
