class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213


print(getattr(Book, 'writer'))
print(getattr(Book, 'name'))
