class Date:
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year
        self.__date = None
        self.__usa_date = None

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        self.__day = day
        self.__date = None
        self.__usa_date = None

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        self.__month = month
        self.__date = None
        self.__usa_date = None

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year
        self.__date = None
        self.__usa_date = None

    @property
    def date(self):
        if self.__date is None:
            self.__date = f'{self.__day}/{self.month}/{self.__year}'
        return self.__date

    @property
    def usa_date(self):
        if self.__usa_date is None:
            self.__usa_date = f'{self.__month}-{self.__day}-{self.__year}'
        return self.__usa_date


d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date)  # 05/10/2001
print(d1.usa_date)  # 10-05-2001
print(d2.date)  # 15/03/0999
print(d2.usa_date)  # 03-15-0999
