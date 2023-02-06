class PowerTwo:
    def __init__(self, n):
        self.pos = -1
        self.end_pow = n

    def __next__(self):
        if self.end_pow <= self.pos:
            raise StopIteration

        self.pos += 1
        return pow(2, self.pos)

    def __iter__(self):
        return self

numbers = PowerTwo(2)

iterator = iter(numbers)

print(next(iterator))  # печатает 1
print(next(iterator))  # печатает 2
print(next(iterator))  # печатает 4
print(next(iterator))  # исключение StopIteration