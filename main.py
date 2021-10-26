from time import sleep
from paddle import Paddle
from turtle import Screen

WIDTH = 1000
HEIGHT = 600
STARTING_POSITION = WIDTH/2 - 20

# Establish a Basic-Screen
screen = Screen()
players = []
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

# Todo: Create a Paddle and make it steerable

p1 = Paddle(x_position=STARTING_POSITION)
p2 = Paddle(x_position=STARTING_POSITION * -1)

game_is_on = True

while game_is_on:
    p1.move()
    p2.move()
    screen.update()
    sleep(0.1)


# Todo: Establish a 2nd Paddle for 2nd Player

# Todo: Create a ball and make it move

# Todo: Establish Ball-Move and Collision Model

# Todo: Establish Ball-Paddle Collision Model

# Todo: Manage Paddle-Missing event (Reset?)

# Todo: Count the goals and display them

screen.exitonclick()