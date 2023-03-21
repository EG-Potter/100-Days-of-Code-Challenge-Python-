from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        # Generates Scoreboard.
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Scoreboard:  {self.score}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    # Updates Scoreboard.
    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Scoreboard:  {self.score}", False, align=ALIGNMENT, font=FONT)

    # Game Over.
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
