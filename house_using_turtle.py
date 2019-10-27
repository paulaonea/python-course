# Draw a house using turtle module

import turtle


def position(x, y):  #move turtle to the given (x, y) position
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()


def rectangle(x, y, length, width, size, direction):
    turtle.pensize(size)
    turtle.seth(direction)
    position(x, y)
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)


def line(x, y, length, size, direction):
    turtle.pensize(size)
    turtle.seth(direction)
    position(x, y)
    turtle.forward(length)


def circle(x, y, radius, angle, size):
    turtle.pensize(size)
    position(x, y)
    turtle.circle(radius, angle)


def window(x, y):
    rectangle(x, y, 6, 75, thick_pen, 90)
    rectangle(x + 8, y + 6, 60, 60, thick_pen, 90)
    line(x + 8, y + 36, 60, thin_pen, 0)
    line(x + 38, y + 6, 60, thin_pen, 90)
    circle(x + 68, y + 66, 30, 180, thick_pen)


def door(x, y):
    rectangle(x, y, 120, 60, thick_pen, 90)
    rectangle(x + 6, y + 5, 52, 48, thick_pen, 90)
    rectangle(x + 6, y + 62, 52, 48, thick_pen, 90)
    circle(x + 60, y + 120, 30, 180, thick_pen)
    line(x + 28, y + 120, 28, thin_pen, 135)
    line(x + 30, y + 120, 30, thin_pen, 90)
    line(x + 32, y + 120, 28, thin_pen, 45)


def roof(x, y):
    turtle.pensize(thick_pen)
    position(x, y)
    turtle.seth(80)
    turtle.forward(85)
    turtle.right(80)
    turtle.forward(317)
    turtle.right(80)
    turtle.forward(85)
    position(x + 6, y + 32)
    for i in range(4):
        turtle.circle(21,152)
        turtle.seth(284)
        turtle.circle(22, 152)
        turtle.seth(284)
    position(x + 12, y + 64)
    for i in range(8):
        turtle.circle(21,152)
        turtle.seth(284)


def flowers(x, y):
    rectangle(x, y, 12, 115, thick_pen, 90)
    position(x + 109, y + 12)
    turtle.seth(90)
    for i in range(6):
        turtle.forward(5)
        turtle.circle(8.5, 180)
        turtle.forward(5)
        turtle.seth(90)


def stairs(x, y):
    for i in range(3):
        rectangle(x - i * 5, y - i * 5, 5, 68 + 2 * i * 5, thin_pen, 90)


turtle.speed("fastest")

thick_pen = 3
thin_pen = 2

turtle.pensize(thick_pen)
position(-180, -300)
turtle.seth(90)
turtle.forward(8)
turtle.right(90)
turtle.forward(145)
turtle.penup()
turtle.setx(35)
turtle.pendown()
turtle.forward(144)
turtle.right(90)
turtle.forward(8)
turtle.right(90)
turtle.forward(135)
turtle.penup()
turtle.setx(-44)
turtle.pendown()
turtle.forward(135)


for x, y in [(-180, -120), (-180, 60)]:
    rectangle(x, y, 8, 360, thick_pen, 90)

for x, y in [(-174, -292), (-174, - 112), (174, -292), (174, -112)]:
    line(x, y, 172, thick_pen, 90)

for x, y in [(-146, -80), (-37, -80), (72, -80), (-146, -240), (72, -240)]:
    window(x, y)

door(-29, -286)
roof(-174, 68)
flowers(-166, -292)
flowers(52, -292)
stairs(-34, -293)
position(1000,1000)


turtle.done()
