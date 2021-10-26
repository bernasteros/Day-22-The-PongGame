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

    def segments(self):
        for segment in range(PADDLE_LENGTH):
            new_square = Turtle()
            new_square.color(COLOR)
            new_square.shape(SHAPE)
            new_square.penup()
            new_square.sety(0 - 20 * segment)
