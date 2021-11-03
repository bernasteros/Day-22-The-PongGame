from turtle import Turtle
from time import sleep

# Overall Properties
MOVE_DISTANCE = 20
COLOR = "white"
SHAPE = "circle"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

# Todo: Reset ball if landed a goal
    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()
