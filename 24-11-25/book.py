class Book:
    def __init__(self, id, name, author ):
        self.id = id
        self.name = name
        self.author = author
        print("Hello!!! Welcome to the Book Counter")
    def display(self):
        print("Book Title" , self.name, "with ID", self.id, "Author Name " , self.author)

s = Book("B005", "ABC", "Nihal")

s.display()
