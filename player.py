from turtle import  Turtle

PLAYER_WIDTH = 1
PLAYER_LENGTH = 3
PLAYER_SHAPE= "square"

start_x = 0
start_y = -230

PLAYER_BLOCKS = {
    0: [],
    1: [],
    2: [],
}

class PLayer():
    def __init__(self):
        start_x = -60
        start_y = -230
        for i in range(len(PLAYER_BLOCKS)):
            self.player = Turtle()
            self.player.color("white")
            self.player.penup()
            self.player.hideturtle()
            self.player.speed(10)
            self.player.goto(start_x, start_y)
            self.player.showturtle()
            self.player.shape(PLAYER_SHAPE)
            self.player.shapesize(stretch_wid=PLAYER_WIDTH, stretch_len=PLAYER_LENGTH)
            start_x +=60
            PLAYER_BLOCKS[i] = self.player


    def player_move_right(self):
        for i in range(len(PLAYER_BLOCKS)):
            location = PLAYER_BLOCKS[i].xcor()
            location += 30
            PLAYER_BLOCKS[i].goto(location, start_y)

    def player_move_left(self):
        for i in range(len(PLAYER_BLOCKS)):
            location = PLAYER_BLOCKS[i].xcor()
            location -= 30
            PLAYER_BLOCKS[i].goto(location, start_y)

    def hit_user(self, ball_position):
        for i in range(len(PLAYER_BLOCKS)):
            if PLAYER_BLOCKS[i].distance(ball_position) < 40:
                return i
