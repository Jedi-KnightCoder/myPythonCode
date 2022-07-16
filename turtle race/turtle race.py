from turtle import Turtle, Screen
########TURTLE RACE#################
import random
is_race_on = False
new_turtle = Turtle(shape="turtle")
new_turtle.speed("fastest")
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter"
                                              "a Color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_positions = [-100, -70, -40, -10, 20, 50]
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won the bet! {winning_color} is the winner")
            else:
                print(print(f"You lost the bet! {winning_color} is the winner"))

        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
        # screen.onclick()








screen.exitonclick()
