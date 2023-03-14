class Countdown:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        self.nums = iter(range(self.value, -1, -1))
        return self.nums

    def __next__(self):
        return next(self.nums)


count = Countdown(2)

assert hasattr(count, '__next__') is True
assert hasattr(count, '__iter__') is True

iterator = iter(count)
assert next(iterator) == 2
assert next(iterator) == 1
assert next(iterator) == 0
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('Элементы итератора Countdown(7)')
for i in Countdown(7):
    print(i)

print('-' * 10)
print('Элементы итератора Countdown(10)')
for i in Countdown(10):
    print(i)