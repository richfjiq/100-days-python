import turtle as t
import random

# import colorgram

# colors = colorgram.extract("spots.jpg", 25)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

color_list = [
    (199, 175, 117),
    (124, 36, 24),
    (210, 221, 213),
    (168, 106, 57),
    (186, 158, 53),
    (6, 57, 83),
    (109, 67, 85),
    (113, 161, 175),
    (22, 122, 174),
    (64, 153, 138),
    (39, 36, 36),
    (76, 40, 48),
    (9, 67, 47),
    (90, 141, 53),
    (181, 96, 79),
    (132, 40, 42),
    (210, 200, 151),
    (141, 171, 155),
    (179, 201, 186),
    (172, 153, 159),
    (212, 183, 177),
    (176, 198, 203),
]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()


def draw_dots(y, times, mid):
    tim.setpos((-mid, y))
    for _ in range(times):
        tim.dot(20, random.choice(color_list))
        if _ == times - 1:
            break
        tim.forward(50)


def draw_picture(size):
    middle = (size / 2) * 50
    y = -1 * middle
    while y < 50 * size - middle:
        draw_dots(y, size, middle)
        y += 50


draw_picture(10)


screen = t.Screen()
screen.exitonclick()
