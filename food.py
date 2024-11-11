from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        ranx = random.randint(-280, 280)
        rany = random.randint(-280, 280)
        self.goto(ranx, rany)




