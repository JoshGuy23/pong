from turtle import Screen
from paddle import Paddle


def setup_screen():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    return screen


def start():
    screen = setup_screen()
    right_paddle = Paddle(x_pos=350, y_pos=0)

    screen.listen()
    screen.onkey(fun=right_paddle.up, key="Up")
    screen.onkey(fun=right_paddle.down, key="Down")

    playing = True
    while playing:
        screen.update()

    screen.exitonclick()


start()
