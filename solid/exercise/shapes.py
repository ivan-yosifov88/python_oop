from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, side, side_height):
        self.side = side
        self.side_height = side_height

    def get_area(self):
        return self.side * self.side_height / 2


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def total_area(self):
        result = 0
        for shape in self.shapes:
            result += shape.get_area()
        return result




shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)


