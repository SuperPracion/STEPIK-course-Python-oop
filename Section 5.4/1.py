class Employee:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)

emp = Employee('Mathew')
print(emp.name)
emp.display()