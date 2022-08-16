import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
player = Player()
your_score = Scoreboard()
turtle_list = []

screen.onkeypress(fun=player.go_up, key="Up")  # moves the turtle up

game_is_on = True
# new_timer = .1
counter = 6
for_ward = 20
while game_is_on:
    time.sleep(.1)
    screen.update()
    if counter == 6:
        cars = CarManager()
        turtle_list.append(cars)
        for num in range(len(turtle_list)):
            turtle_list[num].forward(for_ward)  # move variable called from the player class

            if player.distance(turtle_list[num].pos()) < 25:  # detects if there is a collision between the turtle and
                # the car  or player.ycor() in turtle_list
                game_is_on = False
                your_score.game_over()

            # if turtle goes past the y-cord of 280 the turtle resets back
            # to the starting position of x=0 and y = 280
            # increases the for_ward variable by 50 to make the cars move faster
            # when starting position function is called and the if condition is met self.move increases by  5
            if player.is_at_finish_line():
                player.go_to_start()
                for_ward += 5
                your_score.increase_score()

    counter -= 1
    if counter == 0:
        counter = 6

screen.exitonclick()
