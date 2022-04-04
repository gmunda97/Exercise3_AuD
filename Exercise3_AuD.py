#!/usr/bin/env python3

# Question 1

def count_vowels(text):
    count = 0
    vowels = set("aeiouAEIOU")
    if type(text) == str:
        for letter in text:
            if letter in vowels:
                count = count + 1
        return count
    else:
        return 42


text = "Jack is learning python"
count_vowels(text)

# Question 2

def hamming(text1, text2):
    count = 0
    if len(text1) == len(text2):
        for letter in range(len(text1)):
            if text1[letter] != text2[letter]:
                count = count + 1
        return count
    else:
        return 0

text1 = "cat"
text2 = "map"

hamming(text1, text2)

# Question 3

class Vehicle:
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Doors: {2}".format(self.color, self.fuel_type, self.doors)

class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Passengers: {2}".format(self.color, self.fuel_type, self.passengers)


v1 = Vehicle("red", "gasoline")
c1 = Car("blue", "diesel", 4)
b1 = Bus("black", "diesel", 50)

print(c1.__str__())
print(b1.__str__())

# Question 4

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return "{0}, {1}". format(self.name, self.author)

b1 = Book("Lord of the Rings", "Tolkien")

print(b1)

# Question 5

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return "{0},{1}".format(self.name, self.author)


class BookShelf:
    def __init__(self, books):
        self.books = books

    def add_book_list(self, book_list):
        for i in book_list:
            if isinstance(i, Book):
                self.books.append(i)

    def books_by_author(self, author):
        book_names = []
        for i in self.books:
            if str(i.author) == author:
                book_names.append(str(i.name))
        return (book_names)

    def get_books(self):
        gb = []
        for i in self.books:
            gb.append(str(i.name))
        return(gb)

    def clear_shelf(self):
        self.books.clear()


bs1 = BookShelf([Book("Lord of the Rings", "Tolkien"), Book("Alone Together", "Turkle")])

b_list = [Book("STAND", "Phelps"), Book("A Promised Land", "Obama"), Book("Python", "Turing"), ("NN", "Me"), (123, 456)]
bs1.add_book_list(b_list)

for i in bs1.books:
    print("{0}, {1}".format(i.name, i.author))

print(bs1.books_by_author("Obama"))
print(bs1.books_by_author("Turkle"))
print(bs1.get_books())
bs1.clear_shelf()
