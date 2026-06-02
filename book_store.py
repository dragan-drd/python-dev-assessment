class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        return 2026 - self.publication_year

    def get_summary(self):
        return f"-------------------------\nTitle: {self.publication_year}\n-------------------------\nAuthor: {self.author}\n-------------------------\nYear published: {self.publication_year}\n-------------------------\nISBN: {self.isbn}\n-------------------------\n"


harry_potter = Book(
    "Harry Potter and the Philosopher's Stone",
    "J. K. Rowling",
    "978-0-7475-3269-9",
    1997,
)
alchemist = Book(
    "The Alchemist",
    "Paulo Coelho",
    "0-06-250217-4",
    1988
)
man_called_ove = Book(
    "A Man Called Ove",
    "Fredrik Backman",
    "9781476738024",
    2014
)

print(f"Title - {harry_potter.title}")
print(f"Author - {harry_potter.author}")
print(f"Age - {harry_potter.get_age()}")
print(harry_potter.get_summary())
print("\n")
print(f"Title - {alchemist.title}")
print(f"Author - {alchemist.author}")
print(f"Age - {alchemist.get_age()}")
print(alchemist.get_summary())
print("\n")
print(f"Title - {man_called_ove.title}")
print(f"Author - {man_called_ove.author}")
print(f"Age - {man_called_ove.get_age()}")
print(man_called_ove.get_summary())
