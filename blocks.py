import turtle
import random
from turtle import Screen
# Blocks settings
SHAPE = "square"
BLOCK_WIDTH = 1
SIZE_LENGTH = 8
COLOR = "#393E46", "#00ADB5", "#EEEEEE", "#F9ED69"
start_x = -240
start_y = 240

class Blocks():
    def __init__(self):
        start_x = -240
        start_y = 240

        for i in range(14):
            self.block = turtle.Turtle(SHAPE)
            self.block.penup()
            self.block.hideturtle()
            self.block.fillcolor(random.choice(COLOR))
            self.block.speed(10)
            self.block.goto(start_x,start_y)
            self.block.showturtle()
            self.block.shapesize(stretch_wid=BLOCK_WIDTH, stretch_len=SIZE_LENGTH)
            start_x = start_x + 150
            if i == 4 or i == 8:
                start_x = -240
                start_y -= 20
        self.screen = Screen()
        self.screen.bgcolor("#222831")
        self.screen.setup(width=500, height=500)
