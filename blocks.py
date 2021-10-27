import turtle
import random
from turtle import Screen
import time
# Blocks settings
SHAPE = "square"
BLOCK_WIDTH = 1
SIZE_LENGTH = 6
COLOR = "#393E46", "#00ADB5", "#EEEEEE", "#F9ED69"
start_x = -240
start_y = 240
coordinates_blocs = {}
turtles = []




class Blocks():
    def __init__(self):
        start_x = -240
        start_y = 240

        self.screen = Screen()

    def making_block(self, start_x, start_y):
        start_x = -240
        start_y = 240
        for i in range(15):
            self.block = turtle.Turtle(SHAPE)
            turtles.append(self.block)
            self.block.penup()
            self.block.hideturtle()
            self.block.fillcolor(random.choice(COLOR))
            self.block.speed(10)
            self.block.goto(start_x,start_y)
            self.block.showturtle()
            self.block.shapesize(stretch_wid=BLOCK_WIDTH, stretch_len=SIZE_LENGTH)
            start_x = start_x + 120
            if i == 4 or i == 9:
                start_x = -240
                start_y -= 20
            coordinates_blocs[i] = start_x ,start_y


    def block_hit(self, ball_x, ball_y):
            for i in coordinates_blocs:
                if coordinates_blocs[i][0]-170 < ball_x <=coordinates_blocs[i][0] and coordinates_blocs[i][1]-5 <=ball_y <=coordinates_blocs[i][1]-5:
                    return True, i
                    # print(f"Ball just hit block nr.: {i}")
                    # print(f" Block nr. {i}, x = {coordinates_blocs[i][0]}, y = {coordinates_blocs[i][1]},ball x = {ball_x} ball y = {ball_y}")


    def delete_block(self, number):
        turtles[number].goto(700,900)


    def hit(self, ball_positon):
        for i in range(len(turtles)):
            if turtles[i].distance(ball_positon) < 40:
                self.delete_block(i)
                return True




