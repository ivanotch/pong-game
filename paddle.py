from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(position)

    def up(self):
        self.setpos(self.xcor(), self.ycor() + 20)

    def down(self):
        self.setpos(self.xcor(), self.ycor() - 20)
