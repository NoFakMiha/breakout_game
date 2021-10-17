import tkinter as tk
from turtle import Screen
from blocks import Blocks, BLOCK_WIDTH
from player import  PLayer

Blocks()
user = PLayer()

screen = Screen()
screen.listen()
screen.onkeypress(user.player_move_right, "Right")
screen.onkeypress(user.player_move_left, "Left")





screen.exitonclick()
