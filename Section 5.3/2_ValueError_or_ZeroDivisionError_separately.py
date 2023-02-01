class Divisor:
    __slots__ = ('__a', '__b')

    def __init__(self, value_a=0, value_b=0):
        self.__a = value_a
        self.__b = value_b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def division(self):
        return self.__a / self.__b

try:
    divisor = Divisor(int(input()), int(input()))
    print(f'Результат деления {divisor.a} на {divisor.b}: {divisor.division}')
except ValueError:
    print('Введите целое число')
except ZeroDivisionError:
    print('Делитель не должен быть равен нулю')