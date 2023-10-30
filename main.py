from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


def setup_screen():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    return screen


def play_game():
    screen = setup_screen()
    right_paddle = Paddle(x_pos=350, y_pos=0)
    left_paddle = Paddle(x_pos=-350, y_pos=0)
    ball = Ball()

    screen.listen()
    screen.onkeypress(fun=right_paddle.up, key="Up")
    screen.onkeypress(fun=right_paddle.down, key="Down")
    screen.onkeypress(fun=left_paddle.up, key="w")
    screen.onkeypress(fun=left_paddle.down, key="s")

    playing = True
    while playing:
        time.sleep(0.1)
        screen.update()
        ball.move()

    screen.exitonclick()


play_game()
