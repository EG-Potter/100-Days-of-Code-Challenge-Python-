from turtle import Turtle
# Tuples for starting positions of Snake.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Generates the Snake.
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Adds a new segment to the snake.
    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    # Extends size of snake.
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Moves all Snake Segments in Coordination.
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # Direction Upward.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Direction Downward.
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Direction Left.
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Direction Right.
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
