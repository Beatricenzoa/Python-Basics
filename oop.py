#object-oriented programming
# properties + functions

class Book:
    def __init__(self,title,author,isbn,price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
    def print_details(self):
        print("title:",self.title)
        print("Author:",self.author)
        print("ISBN:",self.isbn)
        print("price:",self.price)
        print("----------------")
    def apply_discount(self,discount):
        self.price = self.price * (1 - discount/100)
        print("New price is ",self.price)

b1 = Book("The River and the Source","Margaret Ogola","ISBN-10", 1500)
b2 = Book("Shreds of Tenderness","John Ruganda", "ISBN-15", 2000)

b1.print_details()
b1.apply_discount(10)
b1.print_details()
print(b2.title)