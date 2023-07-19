import turtle as t

timmy = t.Turtle()


def shape_color(sides):
    if sides == 3:
        return timmy.color("gold1")
    elif sides == 4:
        return timmy.color("DodgerBlue")
    elif sides == 5:
        return timmy.color("gray30")
    elif sides == 6:
        return timmy.color("green4")
    elif sides == 7:
        return timmy.color("hotpink")
    elif sides == 8:
        return timmy.color("OrangeRed")
    elif sides == 9:
        return timmy.color("red")
    elif sides == 10:
        return timmy.color("DarkOrchid4")


def draw_shapes(sides):
    shape_side = sides
    n = shape_side - 2
    deg = (n * 180) / shape_side

    shape_color(sides)

    for _ in range(shape_side):
        timmy.forward(100)
        timmy.right(180 - deg)

    print("After for loop")


def multiple_shapes():
    base = 3
    while base < 11:
        draw_shapes(base)
        base += 1
    timmy.forward(100)


multiple_shapes()

screen = t.Screen()
screen.exitonclick()
