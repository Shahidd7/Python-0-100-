#Blueprint
class Book:
    def __init__(self, title, author):
                self.title = title
                self.author = author
                self.is_available = True
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
#construction
library = []
users = []
while True:
    
    print("--- Library System ---")
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Register a User")
    print("4. Lend a book")
    print("5. Quit")
    choice = int(input("Which option you want to select(1-5)"))
    if(choice == 1):
        title = input("Enter the title of the book:")
        author = input("Enter the author of the book:")
        new_book = Book(title, author)
        library.append(new_book)
    elif(choice == 2):
        for book in library:
            print(f" Title:{book.title} | Author:{book.author}  | Available:{book.is_available}")
        else:
             print("No books added")
    elif(choice == 3):
        name=input("Enter the Users name:")
        new_user = User(name)
        users.append(new_user)
        print(f"{name} added successfully")
    elif(choice == 4):
        user_name=input("what is your name")
        book_title=input("Enter which book you want to lend:")
        
        found_user=None
        for u in users:
             if(u.name == user_name):
                found_user = u
                break
        else:
             print("user not found") 

        found_book=None
        for b in library:
             if(b.title == book_title):
                  found_book = b
                  break
        else:
             print("user not found")  

        if found_user and found_book:
             if found_book.is_available:
                  found_book.is_available = False
                  found_user.borrowed_books.append(found_book)
                  print(f"{found_book.title} lent to {found_user.name} successfully")
             else:
                  print("Sorry ! book is alrready borrowed")
        else:
             print('user or book not found')          


         
    else:
        break
