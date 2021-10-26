from turtle import Turtle
from main import HEIGHT

STYLE = ('Courier', 30, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.sety(HEIGHT/2 - 20)
        self.color("white")
        self.penup()
        self.count = 0
        self.write(str(self.count), font=STYLE, align='center')

    def count_up(self):
        self.count += 1
        self.clear()
        self.write("Score:" + str(self.count), font=STYLE, align='center')