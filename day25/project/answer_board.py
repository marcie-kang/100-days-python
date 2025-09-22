from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Answerboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0

    def update_answer(self, answer, x, y):
        self.goto(x, y)
        self.score += 1
        self.write(answer, align="left", font=FONT)
