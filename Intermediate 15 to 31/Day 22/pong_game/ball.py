from turtle import Turtle
import random


# Generates Ball.
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    # Generates Ball & Movement.
    def game_on(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    # Resets Ball & Movement.
    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.y = random.choice([-10, 10])
        self.move_speed = 0.1

    # Changes Y value according to bounce.
    def bounce_y(self):
        self.y *= -1
        self.move_speed *= 0.9

    # Changes X value according to bounce.
    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9



