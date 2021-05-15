from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.x = random.randint(-400, 400)
        self.y = random.randint(-250, 250)
        self.goto(self.x, self.y)
        self.sped = STARTING_MOVE_DISTANCE

    def move(self):
        self.x -= self.sped
        self.goto(self.x, self.y)

    def check(self, left=-320):
        return self.x < left

    def respawn(self):
        self.x = 400
        self.y = random.randint(-250, 250)
        self.goto(self.x, self.y)

    def speed_up(self):
        self.sped += MOVE_INCREMENT


class CarManager:
    def __init__(self):
        self.cars = []
        self.spawn_cars()

    def spawn_cars(self):
        for _ in range(20):
            self.cars.append(Car())

    def move_cars(self):
        for car in self.cars:
            car.move()
            if car.check():
                car.respawn()

    def speed_up(self):
        for car in self.cars:
            car.speed_up()
