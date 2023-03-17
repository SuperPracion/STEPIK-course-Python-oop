from abc import abstractmethod


class Employee:
    @abstractmethod
    def calculate_salary(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class SalariedEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary