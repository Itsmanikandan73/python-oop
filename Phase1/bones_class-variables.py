class Students:
    
    class_year = 2024 # This is an class variable
    num_of_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Students.num_of_students += 1

    def __str__(self):
        return f" Name: {self.name}\n Age: {self.age}\n year: {Students.class_year}\n num_of_students: {self.num_of_students}"

student1 = Students("anamika", 22)
student2 = Students("jenny", 25)
student3 = Students("alwin", 23)

print(student1)
print("\n")
print(student2)
print("\n")
print(student3)