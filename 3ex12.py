import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")
tess.stamp()
for i in range(12):
    tess.pendown()
    tess.forward(100)
    tess.stamp()
    tess.penup()
    tess.backward(100)
    tess.left(30)
    