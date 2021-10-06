import math
import turtle

t = turtle.Turtle()

xmax = 200
xmin = -xmax
ymax = 200
ymin = -ymax


def grid():
    t.penup()
    t.goto(-200, 200)
    t.pendown()
    for i in range(4):
        t.forward(400)
        t.right(90)


def setup(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def rectangle_will_fit(x, y, l, h):
    setup(x, y)
    if x + l > xmax or x < xmin:
        print("The shape does not fit horizontally")
    if y + h > ymax or y < ymin:
        print("The shape does not fit vertically")


def circle_will_fit(x, y, l):
    setup(x, y)
    if x + l > xmax or x < xmin:
        print("The shape does not fit horizontally")
    if y + h > ymax or y < ymin:
        print("The shape does not fit vertically")


def triangle_will_fit(x, y, l, h):
    setup(x, y)
    if x + l > xmax or x < xmin:
        print("The shape does not fit horizontally")
    if y + h > ymax or y < ymin:
        print("The shape does not fit vertically")


def draw_shape(shape, c, x, y, l, h=0):
    if shape == 'r':
        perimeter = 2 * (l + h)
        setup(x, y)
        t.fillcolor(c)
        t.begin_fill()
        for i in range(2):
            t.forward(l)
            t.left(90)
            t.forward(h)
            t.left(90)
        t.end_fill()

    elif shape == 'c':
        perimeter = 2 * math.pi * l
        setup(x, y)
        t.fillcolor(c)
        t.begin_fill()
        t.circle(l)
        t.end_fill()

    elif shape == 't':
        perimeter = 3 * l
        setup(x, y)
        t.fillcolor(c)
        t.begin_fill()
        for i in range(3):
            t.forward(l)
            t.left(120)

    return perimeter


def main():
    grid()


main()

perimeter1 = draw_shape('r', 'red', 50, 80, 50, 100)
perimeter2 = draw_shape('c', 'blue', -120, 0, 50)
perimeter3 = draw_shape('t', 'pink', -5, -100, 120)

print(perimeter1, '\n', perimeter2, '\n', perimeter3, '\n')
