from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
# 4. Create the ball and make it move
ball = Ball()
# 8. Keep score
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # 5. Detect collision with wall and bounce
    ball.collision_wall()
    # 6. Detect collision with paddle
    if (
        ball.distance(paddle_right) < 50
        and ball.xcor() > 320
        or ball.distance(paddle_left) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()
    # 7. Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
