class Library:
    no_of_books = 0
    books = []

    def __init__(this, no_of_books):
        this.no_of_books = no_of_books
        this.books = []

    def add_book(this, name):
        this.name = name
        this.books.append(this.name)
        this.no_of_books = len(this.books)

    def print_books(this):
        for name in this.books:
            print(name)

a = Library(0)
a.add_book("The secret of nagas")
a.add_book("The Alchemist")

print("Books in the library:")
a.print_books()
print("Total books:", a.no_of_books)
        