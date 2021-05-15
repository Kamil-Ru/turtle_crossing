import random
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def border_check(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    def staring_position(self):
        self.goto(STARTING_POSITION)






