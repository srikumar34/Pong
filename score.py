from turtle import Turtle


class ScoreBoard(Turtle):
    """This is score board"""

    def __init__(self, where):
        super().__init__()
        self.color(0.3, 0.3, 1)
        self.pu()
        self.hideturtle()
        self.score = 0
        self.setposition(0, 280)
        self.where = where
        if where == -1:
            self.write(arg="Score: " + str(self.score) + "\t\t\t", move=False, align="right", font=("Times New Roman", 15, "normal"))
        else:
            self.write(arg="\t\t" + "Score: " + str(self.score), move=False, align="left", font=("Times New Roman", 15, "normal"))

    def add(self):
        self.score += 1
        self.clear()
        if self.where == -1:
            self.write(arg="Score: " + str(self.score) + "\t\t\t", move=False, align="right", font=("Times New Roman", 15, "normal"))
        else:
            self.write(arg="\t\t" + "Score: " + str(self.score), move=False, align="left", font=("Times New Roman", 15, "normal"))

    def game_over(self):
        self.home()
        self.clear()
        self.write("Game Over! Final Score: " + str(self.score), False, "center", ("Times New Roman", 20, "normal"))
