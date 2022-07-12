import colorgram
import turtle as t
import random

t.colormode(255)  # t.colormode(255) allows you
# to choose colors based on numbers

art = t.Turtle()
art.speed("fastest")
art.hideturtle()
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)  # extracts colors from the image.jpg

for color in colors:  # chooses red, green, blue from the image.jpg pic
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# list below is new color list that was generated from the for loop listed above
new_color_list = [(202, 164, 110), (149, 75, 50),
                  (222, 201, 136), (53, 93, 123), (170, 154, 41),
                  (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
                  (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
                  (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
                  (107, 127, 153), (176, 192, 208), (168, 99, 102)]

art.penup()
continue_on = True
a = 1
art.setheading(225)
art.forward(300)
art.setheading(0)


def start_again():
    art.penup()
    art.left(90)
    art.forward(50)
    art.right(90)
    art.setheading(0)
    art.back(500)


while continue_on:
    if a == 10:
        continue_on = False
    for painting in range(10):
        art.dot(20, random.choice(new_color_list))
        art.penup()
        art.forward(50)
        art.pendown()
    a += 1
    print(a)
    start_again()

screen = t.Screen()
screen.exitonclick()

# art.penup()
# art.setposition(0, y_position)
# y_position += 40
# dot()

#
# def dot():
#     for painting in range(10):
#         art.dot(20, random.choice(new_color_list))
#         art.penup()
#         art.forward(50)
#         art.pendown()
#     dot()
#     # art.penup()
#     # art.setposition(0, y_position)
#     # y_position += 40
#
#
# dot()

# def change_coordinates(y_position):
#     new_position = y_position + 40
#     art.penup()
#     art.setposition(0, y_position)
