from turtle import Turtle
import random

CARS = []
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.CAR = [[280, self.ycor()]]
        self.create_car()
        self.add_car()
        self.move_car()
        self.remove()

    def create_car(self):
        if len(self.CAR) < 1:
            self.add_car()

        car = Turtle(shape="square")
        car.color(random.choice(COLORS))
        car.penup()
        random_y = random.randint(-240, 240)
        car.goto(280, random_y)
        self.CAR.append(car)
        self.add_car()

    def add_car(self):
        car = Turtle(shape="square")
        car.color(random.choice(COLORS))
        car.penup()
        self.CAR.append(car)
        random_y = random.randint(-240, 240)
        car.goto(280, random_y)
        if len(self.CAR) > 0:
            car.goto(300, random_y)
        # if len(CARS) < 100:
        #     if random.randrange(0, 10) == (1 or 3 or 5 or 7):
        #         car.penup()
        #         CARS.append(car)
        #         random_y = random.randint(-240, 240)
        #         car.goto(280, random_y)

    def move_car(self):
        for car in car.CARS:
            car.backward(STARTING_MOVE_DISTANCE)

    def remove(self):
        for car in CARS:
            if car.xcor() < -330:
                car.color("white")
                CARS.remove(car)

