from turtle import Turtle


class Pad(Turtle):
    def __init__(self, position):
        self.position = (380 * position, 0)
        super().__init__()
        self.shape("square")
        self.pu()
        self.resizemode("user")
        self.shapesize(1, 5)
        self.color(1, 1, 1)
        self.setpos(self.position)
        self.seth(90)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)
