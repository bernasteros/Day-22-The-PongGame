from turtle import Turtle

# Overall Properties
MOVE_DISTANCE = 20
COLOR = "white"
SHAPE = "square"
PADDLE_LENGTH = 4

# Steering
UP = 90
DOWN = 270

class Paddle:
    def __init__(self):
        self.paddle = []
        self.segments()
        self.head = self.paddle[0]

    def segments(self):
        for segment in range(PADDLE_LENGTH):
            new_square = Turtle()
            new_square.setheading(UP)
            new_square.color(COLOR)
            new_square.shape(SHAPE)
            new_square.penup()
            new_square.sety(0 - 20 * segment)
            self.paddle.append(new_square)

    def move(self):
        for tile_num in range(len(self.paddle) - 1, 0, -1):
            new_x = self.paddle[tile_num - 1].xcor()
            new_y = self.paddle[tile_num - 1].ycor()
            self.paddle[tile_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)