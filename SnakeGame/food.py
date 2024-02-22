from turtle import Turtle
import random
class Food(Turtle): #Inherit turtle class

    def __init__(self):
        super().__init__() #Initialize from Turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed("fastest")

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)