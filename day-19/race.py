from turtle import Turtle, Screen, colormode
import random

colormode(255)
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_position = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []


for index in range(0, 7):
    runner = Turtle()
    runner.shape("turtle")
    runner.color(colors[index])
    runner.penup()
    runner.goto(-230, y_position[index])
    all_turtles.append(runner)


def race_app():
    winner = ""

    if user_bet:
        should_continue = True

    while should_continue:
        for index in range(0, 7):
            runner = all_turtles[index]
            if runner.xcor() >= 230:
                winner = colors[index]
                should_continue = False
            runner.forward(random.randint(1, 10))

    if winner == user_bet.lower():
        print(f"You've won :).")

    print(f"You've lost :( The winner is the turtle color: {winner}")


race_app()
