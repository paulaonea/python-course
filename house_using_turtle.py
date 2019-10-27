# Draw a house using turtle module

import turtle


def rectangle(length, width):
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)


def position(x, y):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()


def window(x, y):
    position(x, y)
    turtle.seth(90)
    rectangle(6, 75)
    position(x + 8, y + 6)
    turtle.seth(90)
    rectangle(60, 60)
    position(x + 8, y + 36)
    turtle.seth(0)
    turtle.forward(60)
    position(x + 38, y + 6)
    turtle.seth(90)
    turtle.forward(60)
    position(x + 68, y + 66)
    turtle.circle(30, 180)


def door(x, y):
    position(x, y)
    turtle.seth(90)
    rectangle(120, 60)
    position(x + 6, y + 6)
    turtle.seth(90)
    rectangle(52, 48)
    position(x + 6, y + 61)
    turtle.seth(90)
    rectangle(52, 48)
    position(x + 60, y + 120)
    turtle.circle(30, 180)
    position(x + 28, y + 120)
    turtle.seth(135)
    turtle.forward(28)
    position(x + 30, y + 120)
    turtle.seth(90)
    turtle.forward(30)
    position(x + 32, y + 120)
    turtle.seth(45)
    turtle.forward(28)


turtle.speed("fastest")

for x, y in [(-180, -300), (-180, -120), (-180, 60)]:
    position(x, y)
    turtle.seth(90)
    rectangle(8, 360)

for x, y in [(-174, -292), (-174, - 112), (174, -292), (174, -112)]:
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.seth(90)
    turtle.forward(172)

window(-146, -80)
window(-37, -80)
window(72, -80)
window(-146, -240)
window(72, -240)
door(-37, -288)

turtle.done()
