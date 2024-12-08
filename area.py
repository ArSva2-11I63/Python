class Polygon:
    def __init__(self, *dimensions):
        self.dimensions = dimensions

    def area(self):
        pass

class Rectangle(Polygon):
    def area(self):
        length, width = self.dimensions
        return length * width

class Square(Polygon):
    def area(self):
        side, = self.dimensions
        return side ** 2

class Triangle(Polygon):
    def area(self):
        base, height = self.dimensions
        return 0.5 * base * height

class Trapezium(Polygon):
    def area(self):
        base1, base2, height = self.dimensions
        return 0.5 * (base1 + base2) * height

def calculate_area(polygon):
    return polygon.area()

if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Square(4),
        Triangle(6, 8),
        Trapezium(5, 10, 6)
    ]

    for shape in shapes:
        print(f"The area of {shape.__class__.__name__} is: {shape.area()}")
