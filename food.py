from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__("square")
        self.pen(pendown=False, pencolor="", fillcolor="red", pensize=20)
        self.refresh()

    def refresh(self):
        random_xcor = random.randint(-250, 250)
        random_ycor = random.randint(-250, 250)
        self.goto(random_xcor, random_ycor)
