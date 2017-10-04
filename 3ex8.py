import turtle
wn = turtle.Screen()
alex=turtle.Turtle()
for a in (160, -43, 270, -97, -43, 200, -940, 17, -86):
    alex.left(a)
    alex.forward(100)
    print("heading=",sum(160, -43, 270, -97, -43, 200, -940, 17, -86))
  