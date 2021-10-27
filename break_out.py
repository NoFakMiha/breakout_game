import tkinter as tk
from turtle import Screen
from blocks import Blocks
from player import  PLayer
from ball import  Ball


blocks=Blocks()
blocks.making_block(-240,240)
user = PLayer()


screen = Screen()
screen.tracer()
screen.bgcolor("#222831")
screen.setup(width=600, height=500)

screen.listen()


ball = Ball()


screen.onkeypress(user.player_move_right, "Right")
screen.onkeypress(user.player_move_left, "Left")



game =True

x = ball.ball_location_x()
y = ball.ball_location_x()


change_direction_x = 0
change_direction_y = 1
while game == True:


    ball.ball_moving(x,y)
    x += change_direction_x
    y +=change_direction_y



    if blocks.hit(ball.postion()) == True:
        change_direction_y = -1


    elif user.hit_user(ball.postion()) == 0:
        change_direction_x = -1
        change_direction_y = 1

    elif user.hit_user(ball.postion()) == 1:
        change_direction_x = 0
        change_direction_y = 1

    elif user.hit_user(ball.postion()) == 2:
        change_direction_x = +1
        change_direction_y = 1

    elif ball.ball_location_x() == 290:
        change_direction_x = -1

    elif ball.ball_location_x() == -290:
        change_direction_x = +1






screen.exitonclick()
