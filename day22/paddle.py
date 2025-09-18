from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, start_position):
        super().__init__()
        self.shape("square")
        self.setposition(start_position)
        self.color("white")
        self.shapesize(5, 1)
        self.penup()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
