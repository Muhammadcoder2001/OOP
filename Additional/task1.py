class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def diplay_info(self):
        print(f"Kitob nomi: {self.title} , Muallifi: {self.author}, yaratilgan yili: {self.year}")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def display_info(self):
        print(f"User: {self.name} user id: {self.user_id}")

        
class library:
    def __init__(self):
        self.books = []
        self.users = []
        self.borrow_books = []
        self.return_books = []
       

    def add_book(self, book:Book):
        self.books.append(book)
        return f"Kitob qo'shildi: {book.title} {book.author} {book.year}"

    def add_user(self, user: User): 
        self.users.append(user)
        return f"Yangi user qo'shildi: {user.name} {user.user_id}" 

    def borrow_book(self, borrow_book: Book):
        self.borrow_books.append(borrow_book)
        return f"Olib ketilgan kitob {borrow_book.title} {borrow_book.author} {borrow_book.year}" 

    def back_books(self, user:User):
        self.return_books.append(user)
        return f"Kitob qaytargan foydalanuvchi {user.name} {user.user_id}"



book1 =  Book('Python Programming', 'John Doe', 1997)
book2 = Book('Learning C++', 'Jane Smith', 2000)
user1 = User("Anvar", "12qwerty21")
user2 = User("Sarvar", "23456tefsv")

print(library().add_book(book1))
print(library().borrow_book(book2))
print(library().add_user(user1))
print(library().back_books(user2))



