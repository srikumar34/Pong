from turtle import Turtle
from random import randint


class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.color(1, 1, 1)
        self.resizemode("user")
        self.shapesize(0.75, 0.75)
        self.degrees(360)  # decides how many degrees in circle, default 360; for rad use .radians()
        self.speed(0)
        self.setheading(randint(-36, 36))
        self.motion = 0

    def start(self):
        self.motion = 5

    def move(self):
        self.forward(self.motion)

    def bounce_x(self):
        self.seth(180 - self.heading())
        self.motion += 0.1

    def bounce_y(self):
        self.seth(360 - self.heading())

    def reposition(self, a):
        self.motion = 0
        self.home()
        head = randint(-36, 36)
        head = head + 180 * a
        self.setheading(head)
