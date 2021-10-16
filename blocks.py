import turtle
# Blocks settings
SHAPE = "square"
BLOCK_WIDTH = 1
SIZE_LENGTH = 8
START_X = -240
START_Y = 240

class Blocks():
    def __init__(self):

        self.block = turtle.Turtle(SHAPE)
        self.block.hideturtle()
        self.block.speed(10)
        self.block.penup()
        self.block.goto(START_X,START_Y)

        self.block.showturtle()

        self.block.shapesize(stretch_wid=BLOCK_WIDTH, stretch_len=SIZE_LENGTH)
