import turtle as t #this imports MODULE named turtle as an alias named t
import random
tim = t.Turtle() #the variable tim = t(module).Turtle()class


########### Challenge 4 - Random Walk ########
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

def pace():
    for walk in range(100):
        tim.forward(20)
        tim.setheading(random.choice([0, 90, 180, 270]))
        tim.width(10)
        # tim.width(random.randint(1, 15))
        #tim.color(random.choice(colours))
        tim.color(random_color())


pace()
my_tuple = (1, 2, 6, 3)
print(my_tuple)

screen = t.Screen()
screen.exitonclick()

