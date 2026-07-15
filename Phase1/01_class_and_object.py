class person:
    
    def __init__(self, Name, Age, Place, fav_OS):
        self.Name = Name
        self.Age = Age
        self.Place = Place
        self.fav_OS = fav_OS

    def __repr__(self):     # we can use __str__ or __repr__ it is the cleanest way
        # Returning all the attributes formatted one line by one.
        return f" Name: {self.Name}\n Age: {self.Age}\n Place: {self.Place}\n Os: {self.fav_OS}\n"

class laptop:
        def __init__(self, brand, ram, storage):
            self.brand = brand
            self.ram = ram
            self.storage = storage

        def print_all(self): # The lazy way of doing it.
            #vars(self) returns a dictionary of all attributes
            print(vars(self))

from dataclasses import dataclass  # The modern way
@dataclass
class Book:
    titile: str 
    author: str 
    year  : int 
    price : int 

print("\n")
book = Book("The Atomic Habit", "Jaymes Clear", 1998 ,250)
print(book)

print("\n")
first_one = person("x86owl", 24, "kerala", "Linux")

print(first_one)
other = laptop("lenovo", "20 GB", "1 TB")
other.print_all()







