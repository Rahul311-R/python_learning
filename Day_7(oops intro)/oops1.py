class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display(self):
        print(self.title)
        print(self.author)

a = input("Enter the title:")
b = input("Enter the author:")
car = Book(a,b)
car.display()