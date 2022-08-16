from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.hideturtle()
        self.your_level = 1
        self.goto(x=-150, y=250)
        self.scoreboard_update()

    def scoreboard_update(self):
        self.clear()
        self.write(arg=f"Level:{self.your_level}", move=False, align="right",
                   font=FONT)

    def increase_score(self):
        self.your_level += 1
        self.scoreboard_update()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER", align="center", font=FONT)

    # def current_score(self):
    # self.clear()
    # self.goto(x=-150, y=250)
    # self.write(arg=f"Level:{self.your_level}", move=False, align="right",
    #            font=FONT)
