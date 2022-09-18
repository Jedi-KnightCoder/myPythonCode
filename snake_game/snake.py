from turtle import Turtle

x_position = [(0, 0), (-20, 0), (-40, 0)]  # position the constants at the top
# so they can be used by all the functions

move_distance = 20  # the distance you want to move the snake.
# If u move anything past 20 the snake breaks up

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):  # this function creates the snake
        for position in x_position:
            self.add_segment(position)

    def add_segment(self, position): #adds a new segment to snake when it eats the food
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def reset(self): #deletes all snake segments
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # function below adds the new object to the end of the snake by calling
    # the add_segment function using the [-1] list slicing notation
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):  # move the snake across the screen
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)






