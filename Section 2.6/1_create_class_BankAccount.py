class BankAccount:
    def __init__(self, acc_num, balance):
        self._account_number = acc_num
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        self._balance = value