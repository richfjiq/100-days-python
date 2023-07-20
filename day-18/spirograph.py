import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_circle(deg):
    tim.circle(100)
    tim.setheading(deg)


def draw_spirograph(gap):
    degrees = 0
    while degrees <= 360:
        tim.color(random_color())
        draw_circle(degrees)
        degrees += gap


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
