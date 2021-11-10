from time import sleep
from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Score

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
p1_score = Score(width=WIDTH, height=HEIGHT)
p2 = Paddle(x_position=STARTING_POSITION)
p2_score = Score(width=WIDTH, height=HEIGHT*-1)
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
            or ball.distance(p1.head) < 50 and ball.xcor() < (STARTING_POSITION) * -1 + 20:
        ball.bounce_x()

    # Reset R Paddle miss
    if ball.xcor() > STARTING_POSITION + 20:
        ball.reset_ball()
        p2_score.count_up()

    # Reset L Paddle miss
    if ball.xcor() < (STARTING_POSITION + 20) *-1:
        ball.reset_ball()
        p1_score.count_up()
    # Todo: Count the goals and display them


    screen.update()
    sleep(0.1)

screen.exitonclick()