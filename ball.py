import turtle
from turtle import Screen

BALL_SHAPE = "circle"



class Ball:
    def __init__(self):
        self.ball = turtle.Turtle(BALL_SHAPE)
        self.ball.penup()

        self.screen = Screen()

    def ball_moving(self, x,y):
        self.ball.goto(x,y)

    def ball_location_x(self):
        return self.ball.xcor()

    def ball_location_y(self):
        return self.ball.ycor()

    def postion(self):
        return self.ball.pos()