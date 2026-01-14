
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT =180


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.pu()
        new_snake.goto(position)
        self.segment.append(new_snake)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]


    def extend_snake(self):
        self.add_segment(self.segment[-1].position())
        pass

    def move(self):
        for snak_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[snak_num - 1].xcor()
            new_y = self.segment[snak_num - 1].ycor()
            self.segment[snak_num].goto(new_x, new_y)

        self.head.forward(DISTANCE)
        # self.segment[0].left(90)
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

