import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        rand_x = random.randint(-250, 250)
        rand_y = random.randint(-250, 250)
        self.goto(rand_x, rand_y)





