import turtle as t
import random
        #mmodule


colours = [
    "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
    "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
]

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_list = (r, g, b)
    # color_list = tuple(color_list)
    return color_list

spiro = t.Turtle()
spiro.shape("turtle")
# spiro.circle(50)
# spiro.setheading(10)
a = 10
spiro.speed(0)
for draw in range(75):
    spiro.color(random_color())
    spiro.setheading(a)
    spiro.circle(100)
    a += 5

screen = t.Screen()
screen.exitonclick()


