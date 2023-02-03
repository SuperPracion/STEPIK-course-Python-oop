class Vector:
    def __init__(self, *args):
        self.values = [*sorted(filter(lambda x: isinstance(x, int), args))]

    def __str__(self):
        if self.values:
            return f'Вектор({", ".join(map(str, self.values))})'
        else:
            return 'Пустой вектор'


v1 = Vector(3, 2, 1, 4, 5, 9, 10)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"