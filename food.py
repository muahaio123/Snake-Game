from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()  # create food class that inherit everything from turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # half the length and width of the default circle (20 -> 10)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))
