

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"
    
    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.pages})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title == other.title and
                self.author == other.author)
    
    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages > other.pages

    def __le__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages <= other.pages

    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages + other.pages

    def __contains__(self, item):
        if not isinstance(item, Book):
            return NotImplemented
        return self.title in item.title or self.author in item.author

    def __getitem__ (self, item):
        if hasattr(self, item):
            return getattr(self, item)
        else: 
            return f"Book has no attribute {item}"
        
book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1178)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book3 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)

for book in [book1, book2, book3]:
    print(book)
    print(book == book2) 
    print(book < book1)
    print(book > book2)
    print(book >= book2)
    print(book + book2)
    print("The" in book)
    print(book["title"])
    print(book["author"])
    print(book["pages"])
    print(book["audio"])