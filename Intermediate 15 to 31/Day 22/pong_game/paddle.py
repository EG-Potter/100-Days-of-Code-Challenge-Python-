from turtle import Turtle


class Paddle(Turtle):
    # Generates a Paddle.
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.color("white")
        self.penup()

    # Direction Upward.
    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    # Direction Downward.
    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
