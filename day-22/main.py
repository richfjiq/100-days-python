from turtle import Turtle, Screen
from paddle import Paddle

# 1. Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# 2. Create and move a paddle
paddle_left = Paddle((-350, 0))
# 3. Create another paddle
paddle_right = Paddle((350, 0))

screen.listen()
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

# 4. Create the ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score

screen.exitonclick()
