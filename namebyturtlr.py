import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("SHAKIB")

# Create and set up the turtle
t = turtle.Turtle()
t.speed(5)
t.pensize(5)
t.color("blue")

# Function to move without drawing
def move_without_drawing(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Draw S
move_without_drawing(-200, 50)
t.setheading(0)
t.circle(25, 180)
t.circle(-25, 180)

# Draw H
move_without_drawing(-150, 0)
t.setheading(90)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(30)
t.left(90)
t.forward(50)
t.backward(100)

# Draw A
move_without_drawing(-80, 0)
t.setheading(70)
t.forward(110)
t.right(140)
t.forward(110)
t.backward(55)
t.right(110)
t.forward(38)

# Draw K
move_without_drawing(-20, 0)
t.setheading(90)
t.forward(100)
t.backward(50)
t.right(45)
t.forward(70)
t.backward(70)
t.right(90)
t.forward(70)

# Draw I
move_without_drawing(40, 0)
t.setheading(90)
t.forward(100)

# Draw B
move_without_drawing(80, 0)
t.setheading(90)
t.forward(100)
t.right(90)
t.circle(-25, 180)
t.right(180)
t.circle(-25, 180)

# Hide turtle and keep window open
t.hideturtle()
screen.mainloop()