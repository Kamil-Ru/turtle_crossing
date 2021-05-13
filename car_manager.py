from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(random.choice(COLORS))
        self.penup()

        self.x = 300
        self.y = random.randint(-250, 250)
        self.goto(self.x, self.y)

    def car_move(self):
        self.x -= STARTING_MOVE_DISTANCE
        self.goto(self.x, self.y)


