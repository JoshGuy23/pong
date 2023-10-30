from turtle import Turtle

MOVE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = MOVE
        self.y_move = MOVE

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.set_ball()

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def set_ball(self):
        self.goto(x=0, y=0)
