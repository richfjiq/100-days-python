import turtle as t

timmy = t.Turtle()

for _ in range(15):
    timmy.pen(fillcolor="black", pencolor="black", pensize=1)
    timmy.forward(10)
    timmy.pen(fillcolor="black", pencolor="white", pensize=1)
    timmy.forward(10)

screen = t.Screen()
screen.exitonclick()
