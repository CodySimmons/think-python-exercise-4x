import turtle


print("4.1")


def square(t):
    for i in range(4):
        t.right(90)
        t.forward(100)


bob = turtle.Turtle()
square(bob)


print('4.2')


def square(t, length):
    for i in range(4):
        t.right(90)
        t.forward(length)


square(bob, 300)
square(bob, 25)


print('4.3')


def polygon(t, length, n):
    for i in range(n):
        t.right(360.0/n)
        t.forward(length)


polygon(bob, 100, 7)


print("4.4")


def circle(t, radius):
    polygon(t, radius, 360)


circle(bob, 2)


# skipping 4.5 because nah.
