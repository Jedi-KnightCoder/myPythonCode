import turtle
import pandas
from lil_turtle import Moving_Turtle

from number_correct import Correct

screen = turtle.Screen()  # creates screen object
# screen.title("U.S States Game")  # creates screen title
image = "blank_states_img.gif"  # associates gif file to image variable
screen.addshape(image)  # adds a new image type

turtle.shape(image)  # sets the turtle shape to the image file
data = pandas.read_csv("50_states.csv")  # reads the csv file and converts to dataframe
# state_dict = data.to_dict()
all_states = data["state"].to_list()
numerator = 1
title = "Guess the State"
continue_on = True
while len(all_states) > 0:
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()
    if answer_state == "Exit":
        all_states = pandas.DataFrame(all_states)
        all_states.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        chosen_row = data[data.state == answer_state]
        x_cord = int(chosen_row.x)
        y_cord = int(chosen_row.y)
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(x_cord, y_cord)
        new_turtle.write(arg=answer_state)
        all_states.remove(answer_state)
        title = f"{numerator} / 50"
        numerator += 1
        if len(all_states) == 0:
            print("You Won!!")










# numerator = 1
# baby_turtle = Moving_Turtle()
# title = "Guess the State"
# new_title = Correct()
#
# new_list = []
# continue_on = True
# while continue_on:
#     answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()
#     for list_ in state_dict['state']:
#         if answer_state == state_dict['state'][list_] and answer_state not in new_list:
#             new_list.append(answer_state)
#             chosen_row = data[data.state == answer_state]  # choose the row for the entered state
#             selected_state = chosen_row.state
#             x_cord = int(chosen_row.x)
#             y_cord = int(chosen_row.y)
#             # baby_turtle = turtle.Turtle()
#             baby_turtle.goto(x_cord, y_cord)
#             baby_turtle.write(arg=answer_state)
#             title = f"{numerator} / 50"
#             # title = new_title.update_score()
#             # baby_turtle.update_score()
#
#             # data.drop(data[data['state'] == answer_state], axis=1)
#
#             numerator += 1

screen.exitonclick()  # exits the screen when clicked on

# for new_dict in len(state_dict):

# if chosen_row =="Empty DataFrame":
#     print("not good")

# print(state_dict['state'])

# if answer_state in state_dict[answer_state]:
#     print("matching state")
# else:
#     print("not in the table")
# print(data[data['state'] == answer_state])
# state_dict = data.to_dict(orient='tight')['data']
# print(state_dict)
# # print(data[data['state'] == answer_state])
