import turtle

myPen = turtle.Turtle()
myPen.color("blue")


def drawPolygon(numberOfsides, startingPoint):
    exteriorAngle = 360 / numberOfsides
    length = 600 / numberOfsides
    myPen.penup()
    myPen.goto(-50, startingPoint)
    myPen.pendown()

    for i in range(0, numberOfsides):
        myPen.forward(length)
        myPen.left(exteriorAngle)


drawPolygon(3, 300)
drawPolygon(4, 100)
drawPolygon(6, -100)
drawPolygon(8, -350)

turtle.done
