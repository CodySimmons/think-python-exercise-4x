import turtle
import math

print("4.1")


def square(t):
    for i in range(4):
        t.right(90)
        t.forward(100)


bob = turtle.Turtle()
circle_draw = turtle.Turtle()
circle_draw.color("Blue")
square(bob)


print('4.2')


def square(t, length):
    for i in range(4):
        t.right(90)
        t.forward(length)


square(bob, 300)
square(bob, 25)


print('4.3')


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, length, n):
    """
    Draws n line segments with the given length and
    angle (in degrees) between them. t is a turtle.
    """
    angle = 360/n
    polyline(t, n, length, angle)


polygon(bob, 100, 7)


print("4.5")


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


arc(bob, 45, 90)


print("4.4")


def circle(t, r):
    arc(t, r, 360)


circle(circle_draw, 100)
