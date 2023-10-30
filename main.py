from turtle import Screen


def setup_screen():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    return screen


def start():
    screen = setup_screen()
    screen.exitonclick()


start()
