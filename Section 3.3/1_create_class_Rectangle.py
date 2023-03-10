class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __str__(self):
        return f'Rectangle({self.width}x{self.height})'
