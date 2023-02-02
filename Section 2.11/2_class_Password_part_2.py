from string import ascii_letters


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if '@' not in value:
            raise ValueError("Логин должен содержать один символ '@'")
        elif '.' not in value[value.index('@'):]:
            raise ValueError("Логин должен содержать символ '.'")

        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if 4 > len(value) > 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if not Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')

        self.__password = value

    @staticmethod
    def is_include_digit(value):
        return any(s.isdigit() for s in value)

    @staticmethod
    def is_include_all_register(value):
        return all([any(s.isupper() for s in value),
                    any(s.islower() for s in value)])

    @staticmethod
    def is_include_only_latin(value):
        return all(s in ascii_letters or s.isdigit() for s in value)

    @staticmethod
    def check_password_dictionary(value):
        with open('easy_passwords.txt', mode='rt', encoding='utf-8') as file:
            return not value in file.read()


r1 = Registration('qwerty@rambler.ru', 'QwrRt124')  # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# теперь пытаемся запись плохие пароли
#r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
#r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
#r1.password = 43  # raise TypeError("Пароль должен быть строкой")
