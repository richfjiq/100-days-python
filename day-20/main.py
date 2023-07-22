from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

all_turtles = []

for _ in range(0, 3):
    piece = Turtle()
    piece.shape("square")
    piece.color("white")
    piece.setpos(_ * -20, 0)
    all_turtles.append(piece)


screen.exitonclick()
