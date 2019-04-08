import turtle
from shapes.Shape import *

background_colors = ["red", "green", "blue", "white", "yellow", "purple"]

wn = turtle.Screen()
wn.bgcolor("black")

square = Square(0)
square.speed_of_drawing = 100000
turtle.hideturtle()
turtle.sety(-200)

color_numerical_value = 0

for i in range(0, 100):
    if color_numerical_value == len(background_colors):
        color_numerical_value = 0
    square.size = i * 3 + 250
    square.color = background_colors[color_numerical_value]
    color_numerical_value += 1
    square.draw_shape()

square.draw_shape()

wn.mainloop()

