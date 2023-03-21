from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

# Generates User Paddle.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Generates Ball.
game_ball = Ball()

# Generates Scoreboard.
scoreboard = Scoreboard()

# User Controls for Paddle.
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Starts Ping Pong Game.
game_is_on = True

while game_is_on:
    if game_is_on:
        time.sleep(game_ball.move_speed)
        screen.update()
        game_ball.game_on()

        # Detects Out of Bound (Left).
        if game_ball.xcor() == 380:
            game_ball.reset()
            scoreboard.l_point()

        # Detects Out of Bound (Right).
        elif game_ball.xcor() == -380:
            game_ball.reset()
            scoreboard.r_point()

        # Detects Collision with boundary.
        elif game_ball.ycor() == 280 or game_ball.ycor() == -280:
            game_ball.bounce_y()

        # Detects Collision with Paddles.
        elif game_ball.distance(r_paddle) < 45 and game_ball.xcor() > 320:
            game_ball.bounce_x()

        elif game_ball.distance(l_paddle) < 45 and game_ball.xcor() < -320:
            game_ball.bounce_x()



# Exits Game.
screen.exitonclick()
