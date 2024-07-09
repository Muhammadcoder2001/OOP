''''''

class Book:
    def __init__(self, name, page_count, price):
        self.name = name
        self.page_count = page_count
        self.price = price

    def add_pages(self, pages):
        self.page_count += pages

    def adjust_price(self):
        if self.page_count > 100:
            self.price /= 2

    def display_info(self):
        return f"Name: {self.name}, Page Count: {self.page_count}, Price: ${self.price:.2f}"

books = []
for i in range(5):
    name = input(f"{i+1}-kitobning nomini kiriting: ")
    page_count = int(input(f"{i+1}-kitobning sahifalar sonini kiriting: "))
    price = float(input(f"{i+1}-kitobning narxini kiriting: "))
    books.append(Book(name, page_count, price))

for book in books:
    book.add_pages(10)
    book.adjust_price()

for book in books:
    print(book.display_info())
