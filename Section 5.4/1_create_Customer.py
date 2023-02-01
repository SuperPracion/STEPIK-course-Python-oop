class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    @staticmethod
    def check_type(value):
        if not isinstance(value, (int, float)):
            raise TypeError('Банк работает только с числами')

    def withdraw(self, value_for_off):
        self.check_type(value_for_off)

        if self.balance < value_for_off:
            raise ValueError('Сумма списания превышает баланс')

        self.balance -= value_for_off

    def deposit(self, value_for_add):
        self.check_type(value_for_add)
        self.balance += value_for_add


bob = Customer('Bob Odenkirk')
#bob.deposit('hello') # TypeError: Банк работает только с числами
bob.deposit(200)
print(bob.balance)  # 200
#bob.withdraw(300)  # ValueError: Сумма списания превышает баланс
bob.withdraw(150)
print(bob.balance)  # 50