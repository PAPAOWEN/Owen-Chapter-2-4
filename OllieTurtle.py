import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
ollie=turtle.Turtle()
ollie.shape("turtle")
ollie.color("blue")
ollie.stamp()
for i in range(12):
    ollie.penup()
    ollie.forward(100)
    ollie.pendown()
    ollie.forward(10)
    ollie.penup()
    ollie.forward(10)
    ollie.stamp()
    ollie.backward(120)
    ollie.left(30)
    ollie.penup()


