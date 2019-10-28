# Draw a house using turtle module

import turtle


def position(x, y):  # move turtle to the given (x, y) position
    turtle.penup()
    turtle.setposition(x, y)
    turtle.fill(False)
    turtle.pendown()


def rectangle(x, y, length, width, size, direction, fill=False, pen_colour="black", fill_colour="white"):
    turtle.pensize(size)
    turtle.color(pen_colour, fill_colour)
    turtle.seth(direction)
    position(x, y)
    turtle.fill(fill)
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
    turtle.fill(False)


def line(x, y, length, size, direction, pen_colour="black"):
    turtle.pensize(size)
    turtle.color(pen_colour)
    turtle.seth(direction)
    position(x, y)
    turtle.forward(length)


def circle(x, y, radius, angle, size, pen_colour="black", fill_colour="white"):
    turtle.pensize(size)
    turtle.color(pen_colour, fill_colour)
    position(x, y)
    turtle.circle(radius, angle)


def window(x, y):
    rectangle(x + 8, y + 6, 60, 60, thick_pen, 90, True, "#720000", "#c8f0ff")
    rectangle(x, y, 6, 75, thick_pen, 90, True, "#3f0000", "#3f0000")
    line(x + 8, y + 36, 60, thin_pen, 0, "#720000")
    line(x + 38, y + 6, 60, thin_pen, 90, "#720000")
    circle(x + 68, y + 66, 30, 180, thick_pen, "#720000")


def door(x, y):
    rectangle(x, y, 120, 60, thick_pen, 90, True, "#3f0000", "#660000")
    rectangle(x + 6, y + 5, 52, 48, thick_pen, 90, True, "#3f0000", "#660000")
    rectangle(x + 6, y + 62, 52, 22, thick_pen, 90, True, "#3f0000", "#c8f0ff")
    rectangle(x + 32, y + 62, 52, 22, thick_pen, 90, True, "#3f0000", "#c8f0ff")
    circle(x + 60, y + 120, 30, 180, thick_pen, "#3f0000")
    line(x + 28, y + 120, 28, thin_pen, 135, "#3f0000")
    line(x + 30, y + 120, 30, thin_pen, 90, "#3f0000")
    line(x + 32, y + 120, 28, thin_pen, 45, "#3f0000")


def roof(x, y, fill, pen_colour="black", fill_color="white"):
    turtle.pensize(thick_pen)
    position(x, y)
    turtle.color(pen_colour, fill_color)
    turtle.fill(fill)
    turtle.seth(80)
    turtle.forward(85)
    turtle.right(80)
    turtle.forward(330)
    turtle.right(80)
    turtle.forward(85)
    turtle.right(100)
    turtle.forward(360)
    turtle.right(260)
    position(x + 6, y + 32)
    for i in range(4):
        turtle.circle(23,152)
        turtle.seth(284)
        turtle.circle(22, 152)
        turtle.seth(284)
    position(x + 11, y + 64)
    for i in range(8):
        turtle.circle(21.5,152)
        turtle.seth(284)


def flowers(x, y):
    position(x + 109, y + 12)
    turtle.seth(90)
    turtle.color("#8b0000", "#DC143C")
    turtle.fill(True)
    turtle.pensize(thin_pen)
    for i in range(6):
        turtle.forward(5)
        turtle.circle(8.5, 180)
        turtle.forward(5)
        turtle.seth(90)
    turtle.right(90)
    turtle.forward(100)
    turtle.fill(False)
    rectangle(x, y, 12, 115, thin_pen, 90, True, "#003d00", "#006500")
    turtle.fill(False)



def stairs(x, y, fill, pen_color, fill_color):
    for i in range(3):
        rectangle(x - i * 5, y - i * 5, 5, 68 + 2 * i * 5, thin_pen, 90, fill, pen_color, fill_color)


turtle.speed("fastest")

thick_pen = 3
thin_pen = 2


# walls
for x, y in [(-180, -300), (-180, -120)]:
    rectangle(x, y, 8, 360, thick_pen, 90, True, "#e2914d", "#e9ac79")

for x, y in [(-174, -292), (-174, - 112)]:
    rectangle(x, y, 172, 348, thick_pen, 90, True, "#e2914d", "#f4d5bb")

for x, y in [(-180, 60)]:
    rectangle(x, y, 8, 360, thick_pen, 90, True, "#3f0000", "#720000")

# roof
roof(-180, 70, True, "#3f0000", "#720000")

# stairs
stairs(-34, -293, True, "#4e5a65", "#718191")

# door
door(-30, -287)

# windows
for x, y in [(-146, -80), (-37, -80), (72, -80), (-146, -240), (72, -240)]:
    window(x, y)

# flowers
flowers(-166, -290)
flowers(52, -290)

position(1000,1000)

turtle.done()