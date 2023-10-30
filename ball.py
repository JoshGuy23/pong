from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x=0, y=0)

    def move(self):
        if self.xcor() < 380 and self.ycor() < 280:
            self.goto(x=self.xcor() + 10, y=self.ycor() + 10)
