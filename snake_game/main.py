from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

#controls the turtle
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    #detect collision with food.
    if snake.head.distance(food) < 15:
        #score.current_score += 1
        food.refresh()
        score.increase_score()
        snake.extend()
        # with open("my_file.txt", mode="w") as file:
        #     file.write(f"{score.high_score}")


    #detect collision with wall.
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset()

        # game_is_on = False commented out code so that game can reset
        # score.game_over()


    #Detect collion with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.reset()
            snake.reset()
            # game_is_on = False commented out code so that game can reset
            # score.game_over()


    #if head collides with any segment in the tail: trigger GAME OVER


# x_position = [(0, 0), (-20, 0), (-40, 0)]
# segments = []

#loop creates the snake
# for position in x_position:
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.penup()
#     new_turtle.goto(position)
#     segments.append(new_turtle)


#makes segment 2 move to segment 1 and segment 1 moves to position 0
    # for seg_num in range(len(segments)-1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(x=new_x, y=new_y)
    # segments[0].forward(20)

    # def test_up():
    #     segments[0].setheading(90)
    # screen.onkey(fun=test_up(), key="w")
    # segments[0].left(90)
    # segments[0].forward(40)
    # game_is_on = False

screen.exitonclick()