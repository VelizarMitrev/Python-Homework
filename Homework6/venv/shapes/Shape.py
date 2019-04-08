import turtle

class Shape(turtle.Turtle):
    color = "black"
    speed_of_drawing = 1000
    size = 100
    def __init__(self, size=100):
        self.size = size


class Triangle(Shape):
    def __init__(self, size=100):
        self.size = size

    def draw_shape(self):
        turtle.color(self.color)
        turtle.speed(self.speed_of_drawing)
        turtle.forward(self.size / 2)
        turtle.left(120)
        for i in range(0,2):
            turtle.forward(self.size)
            turtle.left(120)
        turtle.forward(self.size / 2)


class Circle(Shape):
    def __init__(self, size=100):
        self.size = size

    def draw_shape(self):
        turtle.color(self.color)
        turtle.speed(self.speed_of_drawing)
        turtle.circle(self.size)


class Square(Shape):
    def __init__(self, size=100):
        self.size = size

    def draw_shape(self):
        turtle.color(self.color)
        turtle.speed(self.speed_of_drawing)
        turtle.forward(self.size / 2)
        turtle.left(90)
        for i in range(0,3):
            turtle.forward(self.size)
            turtle.left(90)
        turtle.forward(self.size / 2)


class Pentagon(Shape):
    def __init__(self, size=100):
        self.size = size

    def draw_shape(self):
        turtle.color(self.color)
        turtle.speed(self.speed_of_drawing)
        turtle.forward(self.size / 2)
        turtle.left(60)
        for i in range(0, 5):
            turtle.forward(self.size)
            turtle.left(60)
        turtle.forward(self.size / 2)


class Star(Shape):
    def __init__(self, size=100):
        self.size = size

    def draw_shape(self):
        turtle.color(self.color)
        turtle.speed(self.speed_of_drawing)
        for i in range(0, 5):
            turtle.left(144)
            turtle.forward(self.size)

