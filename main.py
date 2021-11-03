from time import sleep
from paddle import Paddle
from turtle import Screen
from ball import Ball

WIDTH = 1000
HEIGHT = 600
STARTING_POSITION = WIDTH/2 - 40

# Establish a Basic-Screen
screen = Screen()
players = []
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

# Create two Paddle and make it steerable

p1 = Paddle(x_position=STARTING_POSITION * -1)
p2 = Paddle(x_position=STARTING_POSITION)
ball = Ball()

screen.listen()
screen.onkey(p1.up, "w")
screen.onkey(p1.down, "s")
screen.onkey(p2.up, "Up")
screen.onkey(p2.down, "Down")

game_is_on = True
while game_is_on:

    p1.move()
    p2.move()
    ball.move()

    if ball.ycor() > HEIGHT/2 - 20 or ball.ycor() < HEIGHT/2 * -1 + 20:
        ball.bounce_y()

    if ball.distance(p2.head) < 50 and ball.xcor() > STARTING_POSITION - 20 \
            or ball.distance(p1.head) < 50 and ball.xcor() < STARTING_POSITION - 20 * -1:
        ball.bounce_x()

    # Todo: Manage Paddle-Missing event (Reset?)
    # Todo: Count the goals and display them

    screen.update()
    sleep(0.1)




screen.exitonclick()