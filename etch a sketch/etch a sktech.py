from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")

def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def turn_left():
    tim.left(50)


def turn_right():
    tim.right(50)


def go_up():
    tim.setheading(90)

def clear_screen():
    tim.reset()


screen.listen()

# def all_functions(a)

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="Up", fun=go_up)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
