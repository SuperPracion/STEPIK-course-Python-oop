class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


attrs = input().split()

for attr in attrs:
    print(f'{attr}-{"YES" if hasattr(Person, attr) else "NO"}')
