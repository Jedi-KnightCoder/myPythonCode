from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.turtle_list = []
        self.random_color = random.randint(0, 5)
        self.create_cars()
        self.new_speed = 10

    def create_cars(self):  # generates a random color for the cars and
        # moves the turtle to the given y position

        for index in range(len(COLORS)):
            self.color(COLORS[self.random_color])
            random_y = random.randrange(250, -250, -STARTING_MOVE_DISTANCE)
            self.goto(x=320, y=random_y)

    def move_cars_faster(self):
        self.new_speed += 50

        #another way to write the code is to disable inheritance and create
        #cars in the function listed below.
        # new_car = Turtle("shape")
        # new_car.penup()
        # new_car.color(random.choice(COLORS))
        # new_car.shapesize(stretch_wid=1, stretch_len=2)
        # new_car.setheading(180)
        # random_y = random.randrange(250, -250, -STARTING_MOVE_DISTANCE)
        # list = []
        # new_car.goto(x=320, y=random_y)
        # list.append(new_car)




