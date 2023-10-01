import turtle
import random

alpha = turtle.Turtle()
my_screen = turtle.Screen()
turtle.colormode(255)
alpha.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_tuple = (r, g, b)
    return random_tuple


def making_spirograph(angle):
    for i in range(int(360 / angle)):
        alpha.color(random_color())
        alpha.circle(100)
        alpha.left(angle)


making_spirograph(7)

my_screen.exitonclick()
