import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def shrinkingSqare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

shrinkingSqare(150)
shrinkingSqare(130)
shrinkingSqare(110)
shrinkingSqare(90)
shrinkingSqare(70)
shrinkingSqare(50)
shrinkingSqare(30)
shrinkingSqare(10)


turtle.done()
