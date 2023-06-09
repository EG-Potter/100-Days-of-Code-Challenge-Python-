from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Generate Screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Generates Scoreboard.
scoreboard = Scoreboard()

# Generates Snake & Food.
snake = Snake()
food = Food()

# User Controls on Snake.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Snake Game & Movement.
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.25)

    # Snake Moves.
    snake.move()

    # Detect Collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_scoreboard()

    # Detect Collision with Wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect Collision with Tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
# Exits Game
screen.exitonclick()

