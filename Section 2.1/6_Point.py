class Point:
    def set_coordinates(self, x_value, y_value):
        self.x = x_value
        self.y = y_value

    def get_distance(self, some_point):
        if not isinstance(some_point, Point):
            print('Передана не точка')
        else:
            return ((self.x - some_point.x) ** 2 + (self.y - some_point.y) ** 2) ** 0.5


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)  # вернёт 5.0
p1.get_distance(10)  # Распечатает "Передана не точка"
