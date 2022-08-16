from turtle import Turtle

ALIGN = "center"
LEFT_ALIGN = "left"
RIGHT_ALIGN = "right"
FONT = ('Courier', 65, 'normal')
GAME_OVA = ('Arial', 30, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_one_score = 0
        self.player_two_score = 0
        # self.score_keeper = f"Score: {self.current_score}"
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.player_one_score}", move=False, align=ALIGN, font=FONT, )

        self.goto(100, 200)
        self.write(arg=f"{self.player_two_score}", move=False, align=ALIGN, font=FONT, )

    # def update_scoreboard_2(self):
    #     self.write(arg=f"{self.player_two_score}", move=False, align=ALIGN, font=FONT)

    def increase_player1_score(self):  # player 1 is the left paddle
        self.player_one_score += 1
        self.update_scoreboard()

    def increase_player2_score(self):  # player 2 is the left paddle
        self.player_two_score += 1
        self.update_scoreboard()
