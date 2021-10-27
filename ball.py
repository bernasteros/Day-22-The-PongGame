from turtle import Turtle

# Overall Properties
MOVE_DISTANCE = 20
COLOR = "white"
SHAPE = "circle"

class Ball:
    def __init__(self):
        self.ball = []
        self.initiate_ball()

    def initiate_ball(self):
        new_ball = Turtle()
        new_ball.color(COLOR)
        new_ball.shape(SHAPE)
        new_ball.penup()
        self.ball.append(new_ball)

# Todo: Make the ball move
# Todo: Make the ball move on random angles
    def move_ball(self):
        pass

# Todo: Change direction if hit by a paddle
    def change_direction(self):
        pass

# Todo: Reset ball if landed a goal
    def reset_ball(self):
        pass

