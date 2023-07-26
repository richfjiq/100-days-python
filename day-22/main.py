from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# 1. Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# 2. Create and move a paddle
# 3. Create another paddle
paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

# 4. Create the ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score

screen.exitonclick()
