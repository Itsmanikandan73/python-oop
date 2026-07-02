class Animal:   #parent class

    def __init__(self, name):
        self.name = name
        self.is_alive = True    #boolean

    def eat():
        print(f"{self.name} is eating")

    def sleep():
        print(f"{self.name} is sleeping")

    def __str__(self):
        return f"{self.name}\n {self.is_alive}\n"

class Dog(Animal): # child class
    pass 

class Cat(Animal):
    pass

dog1 = Dog("chembban")
print(dog1)
dog1.eat()
