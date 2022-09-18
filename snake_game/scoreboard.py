from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')
GAME_OVA = ('Arial', 30, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        # super().__init__()
        super(Scoreboard, self).__init__()
        self.current_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        # self.score_keeper = f"Score: {self.current_score}"
        # self.turtle = Turtle()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 260)
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self): #updates the scoreboard
        self.clear()
        self.write(arg=f"Score: {self.current_score}   High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self): #increases the score
        self.current_score += 1
        self.clear()
        self.update_scoreboard()

    #commented out the game over function to reset the scoreboard to figure
    #out whether the current score is greater than the high score of the game.

    # def game_over(self):
    #     # self.clear()
    #     self.goto(x=0, y=0)
    #     self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=GAME_OVA)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.current_score = 0
        self.update_scoreboard()





