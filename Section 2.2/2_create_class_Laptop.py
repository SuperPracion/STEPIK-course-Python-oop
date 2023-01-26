class Laptop:
    def __init__(self, brand=None, model=None, price=None):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'


hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name) # выводит "hp 15-bw0xx"