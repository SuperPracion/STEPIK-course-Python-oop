class Person:
    def __init__(self, name, last, age):
        self.first_name = name
        self.last_name = last
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        return self.age >= 18


p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult()) # выводит "True"