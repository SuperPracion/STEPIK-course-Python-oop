class Addition:
    def __call__(self, *args, **kwargs):
        print(f'Сумма переданных значений = {sum(num for num in args if isinstance(num, (int, float)))}')


add = Addition()

add(10, 20) # печатает "Сумма переданных значений = 30"
add(1, 2, 3.4) # печатает "Сумма переданных значений = 6.4"
add(1, 2, 'hello', [1, 2], 3) # печатает "Сумма переданных значений = 6"