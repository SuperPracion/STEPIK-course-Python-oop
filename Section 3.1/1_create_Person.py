class Person:
    def __init__(self, name, surname, gender='male'):
        if gender not in ('male', 'female'):
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            gender = 'male'

        self.gender = gender
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{"Гражданин" if self.gender == "male" else "Гражданка"} {self.surname} {self.name}'

p1 = Person('Chuck', 'Norris')
print(p1) # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2) # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3) # печатает "Гражданин Кеноби Оби-Ван"