import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("black")
turtle.speed(0)
turtle_colors = ["red","blue","purple","yellow","orange"]

for i in range(10):
    turtle_instance.color(turtle_colors[i % 5])
    turtle_instance.circle(5 * i)
    turtle_instance.circle(-5 * i)





turtle.mainloop()

