from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.shape("turtle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        #self.continue_on = True
        self.x_move = 10
        self.y_move = 10
        self.new_speed = 0.1
        #self.speed(1)

        # self.move_the_ball()

    def move_the_ball(self):
        x_position = self.xcor() + self.x_move
        y_position = self.ycor() + self.y_move
        self.goto(x=x_position, y=y_position)

    def bounce_y(self):
        self.y_move *= -1
        # this only changes the y coordinate so that the ball
        # bounces off the top or bottom of the screen and the
        # ball continues to travel on the x axis

    def bounce_x(self):
        self.x_move *= -1
        self.new_speed *= .1
        # self.speed(self.new_speed)
        # if self.new_speed > 10:
        #     self.new_speed = 0


    def reset_position(self):
        # resets the ball to coordinates (0,0) and then moves
        # the ball into the opponents court on the left paddle
        self.hideturtle()
        self.goto(x=0, y=0)
        self.new_speed = .1
        self.bounce_x()
        self.showturtle()


