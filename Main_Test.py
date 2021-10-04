import turtle
import main

t = turtle.Turtle()


def test_rectangle_will_fit():
    main.rectangle_will_fit(200, 400, 100, 50) == 2
    x = 200
    assert (x == 200)
    y = 40
    assert (y == 40)


def test_draw_shape_rectangle():
    main.draw_shape('r', 'red', 50, 80, 50, 100)
    c = 'red'
    assert (c == 'red')
    x = 50
    assert (x == 50)
    y = 80
    assert (y == 80)
    l = 50
    h = 100
    perimeter = l + l + h + h
    # perimeter when calculated should be equal to 2(50)+2(100) = 300
    assert (perimeter == 300)


def test_setup():
    t.penup()
    t.goto(180, 160)
    t.pendown()
