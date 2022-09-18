from turtle import Turtle, Screen


class Correct(Turtle):

    def __init__(self):
        # super().__init__()
        self.numerator = 1
        self.denominator = 50
        # self.numerator = 1
        # self.shape("turtle")
        screen = Screen()
        screen.title(f"{self.numerator}/{self.denominator}")
        self.update_score()

    def update_score(self):
        self.numerator += 1







