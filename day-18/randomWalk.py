import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

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

direction = [0, 90, 180, 270]
tim.width(15)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def random_walk(steps):
    for _ in range(steps):
        tim.color(random_color())
        tim.forward(50)
        tim.setheading(random.choice(direction))

    # total_steps = 0

    # while total_steps <= steps:
    #     tim.color(random.choice(colors))
    #     tim.forward(50)
    #     tim.setheading(random.choice(direction))
    #     total_steps += 1


random_walk(200)

screen = t.Screen()
screen.exitonclick()
