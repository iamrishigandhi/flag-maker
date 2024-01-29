import turtle
from turtle import *

# Screen for Output
screen = turtle.Screen()
screen.setup(width=850, height=450)

# Defining a turtle Instance
t = turtle.Turtle()
t.speed(0)

# initially penup()
t.penup()
t.goto(-425, 250)
t.pendown()

# Red Rectangle
t.color("red")
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.end_fill()
t.left(90)
t.forward(200)

turtle.done()