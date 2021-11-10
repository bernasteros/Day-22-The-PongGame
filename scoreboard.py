from turtle import Turtle

STYLE = ('Courier', 35, 'bold')


class Score(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.hideturtle()
        self.sety(width/4)
        self.setx(height/2 - 20)
        self.color("white")
        self.penup()
        self.count = 0
        self.write(str(self.count), font=STYLE, align='center')

    def count_up(self):
        self.count += 1
        self.clear()
        self.write(str(self.count), font=STYLE, align='center')