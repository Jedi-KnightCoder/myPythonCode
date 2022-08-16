from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, a):
        super().__init__()
        self.shape("square")
        self.color("white")
        #self.hideturtle()
        self.penup()
        self.speed(0)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(a)

        # self.paddle_right = Turtle(shape="square")
        # self.paddle_left = Turtle(shape="square")
        # self.paddle_right = Paddle((350, 0))
        # self.paddle_left = Paddle((-350, 0))

        # self.right_paddle(a)
        # self.left_paddle(a)
        # self.color("white")
        # self.setheading(90)

    # def many_paddles(self, x, y):
    #     for _ in range(2):
    #         self.paddle_right.color("white")
    #         self.paddle_right.hideturtle()
    #         self.paddle_right.penup()
    #         self.paddle_right.speed(0)
    #         self.paddle_right.shapesize(stretch_len=1, stretch_wid=5, outline=0)
    #     self.paddle_right.goto(self.a)
    #     self.paddle_left.goto(self.b)

    # def right_paddle(self, a):  # draws the right paddle
    #     # self.paddle_right = shape ="square"
    #     # self.paddle_right.color("white")
    #     # self.paddle_right.hideturtle()
    #     # self.paddle_right.penup()
    #     # self.paddle_right.speed(0)
    #     # self.paddle_right.shapesize(stretch_len=1, stretch_wid=5, outline=0)
    #     self.paddle_right.goto(a)
    #     # self.paddle_right.goto(x=350, y=0)
    #     self.paddle_right.showturtle()
    #
    # def left_paddle(self, a):  # creates the paddle
    #     # paddle_left = Turtle(shape="square")
    #     self.paddle_left.color("white")
    #     self.paddle_left.hideturtle()
    #     self.paddle_left.penup()
    #     # paddle_left.resizemode(rmode="user")
    #     self.paddle_left.shapesize(stretch_len=1, stretch_wid=5, outline=0)
    #     self.paddle_left.goto(a)
    #     # self.paddle_left.goto(x=-350, y=0)
    #     # print(self.paddle.xcor())
    #     self.paddle_left.showturtle()



        # def right_paddle(self):  # creates the paddle
        #     paddle_right = Turtle(shape="square")
        #     paddle_right.color("white")
        #     paddle_right.hideturtle()
        #     paddle_right.penup()
        #     # paddle_right.resizemode(rmode="user")
        #     paddle_right.shapesize(stretch_len=1, stretch_wid=5, outline=0)
        #     paddle_right.goto(x=350, y=0)
        #     paddle_right.showturtle()
