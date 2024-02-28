import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#728FCE")
drawing_board.title("Python Turtle")
turtle_instance = turtle.Turtle()

#square
'''
turtle_instance.forward(100)
turtle_instance_2 = turtle.Turtle()
turtle_instance_2.left(90)
turtle_instance_2.forward(100)
turtle.done()
'''

#circle
'''
for i in range(5):
    turtle_instance.forward(100)
    turtle_instance.right(144)
'''

#polygon
num_sides = int(input("Kenar giriniz:"))
angle=360.0 / (num_sides)
side_lenght = 100

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_lenght)


turtle.done()