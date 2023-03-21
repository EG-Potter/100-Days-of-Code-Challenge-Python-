from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Generates Snake
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Snake Game & Movement
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.25)

    # Snake Moves
    snake.move()


print(len(snake.segments))

# Exits Game
screen.exitonclick()

