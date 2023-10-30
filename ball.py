from turtle import Turtle

TOP_HEIGHT = 280
BOTTOM_HEIGHT = -280
RIGHT_WIDTH = 380
LEFT_WIDTH = -380
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
        self.goto(x=0, y=0)

    def move(self):
        if self.ycor() > TOP_HEIGHT or self.ycor() < BOTTOM_HEIGHT:
            self.bounce()
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        if RIGHT_WIDTH > self.xcor() > LEFT_WIDTH:
            self.goto(x=new_x, y=new_y)

    def bounce(self):
        self.y_move *= -1
