from turtle import Screen
from paddles import Paddle
from moving_ball import Ball
from scoreboard import Scoreboard
import time

# ping_pong_paddles = Paddle()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Ping Pong")
screen.tracer()
ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Scoreboard()
screen.listen()


# tennis_line = Goal()
# tennis_line.draw_divider()

def right_up():  # function that moves right paddle up with onclick.
    new_y = r_paddle.ycor() + 20
    r_paddle.goto(x=r_paddle.xcor(), y=new_y)

    # r_paddle.sety(r_paddle.ycor() + 20)  # this is the code I wrote


def right_down():  # function that moves right paddle down with onclick.
    r_paddle.sety(r_paddle.ycor() - 20)


def left_up():  # function that moves left paddle up with onclick.
    l_paddle.sety(l_paddle.ycor() + 20)


def left_down():  # function that moves left paddle down with onclick.
    l_paddle.sety(l_paddle.ycor() - 20)


# used onkeypress so I could just hold the key down and the paddle move
# instead of using onkeyclick
screen.onkeypress(fun=right_up, key="Up")  # moves right paddle up
screen.onkeypress(fun=right_down, key="Down")  # moves right paddle down
screen.onkeypress(fun=left_up, key="w")  # moves left paddle up
screen.onkeypress(fun=left_down, key="a")  # moves left paddle down

new_speed = 0
game_is_on = True
while game_is_on:
    time.sleep(ball.new_speed)
    # new_sleep -= 0.1
    # ball.speed(1)

    screen.update()
    ball.move_the_ball()

    # if statement that  detects a collision with the top
    # and bottom of the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # this determines if a collision occurs with the either paddle
    # movement between paddles occur on the x axis
    if ball.distance(r_paddle.pos()) < 50 and ball.xcor() > 320 or ball.distance(
            l_paddle.pos()) < 50 and ball.xcor() < - 320:
        ball.bounce_x()
    # ball.speed(new_speed)

    # resets the ball to the beginning and goes to the other opponent
    # this occurs when right paddle misses
    # right paddle is player two. if right paddle misses increase the score for player one.
    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_player1_score()

    # if left paddle misses increase the score for the right paddle which is player 2
    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_player2_score()

screen.exitonclick()
