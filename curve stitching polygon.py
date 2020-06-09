
import turtle
import time


def curve(length, steps, angle, xcor, ycor, posAngle, color, backcolor):  # Curve Stitching Method
    pAngle = posAngle
    # Otherwise it starts at -45 degrees

    turtle.penup()
    turtle.speed(0)

    turtle.seth(pAngle)
    turtle.goto(xcor, ycor)
    turtle.left(angle/2)
    turtle.pendown()
    turtle.pencolor(backcolor)

    turtle.forward(length)

    x2 = turtle.xcor()
    y2 = turtle.ycor()

    turtle.back(length)
    turtle.right(angle)
    turtle.forward(length)

    x1 = turtle.xcor()
    y1 = turtle.ycor()
    times = length // steps

    for stepNum in range(times, length, times):

        turtle.penup()

        turtle.seth(pAngle)
        turtle.right(angle / 2)

        turtle.goto(x1, y1)
        turtle.bk(stepNum)
        Point1 = turtle.pos()

        turtle.goto(x2, y2)
        turtle.left(angle)

        turtle.bk(length - stepNum)
        turtle.pencolor(color)

        turtle.pendown()
        turtle.goto(Point1)

    time.sleep(0)


# User Input
circRad = 200
numSides = int(input("Enter the number of sides of the polygon: "))
steps = int(input("Enter the number of steps(subdivisions): "))
color = input("Enter the color of the curve: ")
backcolor = input("Enter the color of the sides: ")

# Speed of program
turtle.speed(0)



turtle.penup()
turtle.goto(0, -circRad)

turtle.setheading(90)

# Creates arrays for position, x-coordinate, y-coordiate, and orientation
pos = []
x = []
y = []
head = []

# Defines variables angles, cAngle, point1, x1, and y1
angle = 360 / numSides
cAngle = round((180 * (numSides - 2))/numSides)
point1 = turtle.position()
x1 = turtle.xcor()
y1 = turtle.ycor()

# Adds x1,y1, point 1, and 90 degrees to empty lists
x.append(x1)
y.append(y1)
pos.append(point1)
head.append(90)

turtle.forward(circRad)
turtle.setheading(270)


# Finds the points and saves their orientation, position, and x and y coordinate
for p in range(1, numSides, 1):

    turtle.right(angle)
    turtle.forward(circRad)

    # Saves point data in local variables
    point = turtle.pos()
    xv = turtle.xcor()
    yv = turtle.ycor()
    h = turtle.heading()

    h = 180 + h
    # Faces opposite direction as point orientation

    # Saves local variables to lists
    pos.append(point)
    x.append(round(xv))
    y.append(round(yv))
    head.append(round(h))

    turtle.bk(circRad)

turtle.forward(circRad)

# Connects the points
for c in range(1, numSides + 1, 1):
    turtle.goto(pos[c - 1])

# Goes to point 2
turtle.goto(pos[0])
turtle.goto(pos[1])

# Records data from point 2
x2 = turtle.xcor()
y2 = turtle.ycor()

# Inputs point 2 data to the distance formula and rounds
length = (((x2 - x1)**2) + ((y2-y1)**2))**(1/2)
length = round(length)

# Inputs the information into the curve stitching method for each angle
for q in range(0, numSides, 1):
    curve(length, steps, cAngle, x[q], y[q], head[q], color, backcolor)

# Final image
turtle.hideturtle()
time.sleep(12)



