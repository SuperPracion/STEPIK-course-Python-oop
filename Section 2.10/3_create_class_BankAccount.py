class BankAccount:
    bank_name = 'Tinkoff Bank'
    address = 'Москва, ул. 2-я Хуторская, д. 38А'

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def create_account(cls, name, deposit):
        return BankAccount(name, deposit)


    @classmethod
    def bank_info(cls):
        return f'{cls.bank_name} is located in {cls.address}'