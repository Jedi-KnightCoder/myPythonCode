from turtle import Turtle


class Goal(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.pencolor("white")
        self.pensize(5)
        self.speed("fastest")
        self.goto(x=0, y=-300)
        self.setheading(90)

    def draw_divider(self):
        for x in range(31):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)


