from turtle import  Turtle

PLAYER_WIDTH = 1
PLAYER_LENGTH = 10
PLAYER_SHAPE= "square"
start_x= 0
start_y=-230

class PLayer():
    def __init__(self):


        self.player = Turtle()
        self.player.color("white")
        self.player.penup()
        self.player.hideturtle()
        self.player.speed(10)
        self.player.goto(start_x, start_y)
        self.player.showturtle()
        self.player.shape(PLAYER_SHAPE)
        self.player.shapesize(stretch_wid=PLAYER_WIDTH, stretch_len=PLAYER_LENGTH)

    def player_move_right(self):
        location = self.player.xcor()
        location += 20
        self.player.goto(location, start_y)

    def player_move_left(self):
        location = self.player.xcor()
        location -= 20
        self.player.goto(location, start_y)
