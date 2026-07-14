class SoftwareProject:
    def __init__(self, name, lines_of_code):
        self.name = name
        self.lines_of_code = lines_of_code

    # 1. Overloading the '+' operator (__add__)
    # Define what happens when you do: project1 + project2
    def __add__(self, other):
        if isinstance(other, SoftwareProject):
            # we combine the names and sum up the lines of code to return a NEW project 
            combined_name = f"{self.name} & {other.lines_of_code} Integration"
            combined_log = self.lines_of_code + other.lines_of_code
            return SoftwareProject(combined_name, combined_log)
        raise TypeError("You can only add a SoftwareProject to another Softwareproject")

    # 2. Overloading the '==' operator (__eg__)
    # Define what happens when you check: project1 == project2 
    def __eq__(self, other):
        if isinstance(other, SoftwareProject):
            return self.lines_of_code == other.lines_of_code
        return False

    # 3. Overloading the '>' operator (__gt___ for "greater than")
    def __gt__(self, other):
        if isinstance(other, SoftwareProject):
            return self.lines_of_code > other.lines_of_code
        raise TypeError("Comparison must be between two SoftwareProject")

    def __repr__(self):
        return f"Project('{self.name}', LOC: {self.lines_of_code})"


# creating three project instances
frontend = SoftwareProject("React Frontend", 12000)
backend = SoftwareProject("Python API", 15000)
legacy_system = SoftwareProject("Legacy COBOL", 15000)

print("---- 1. Using Overloading Operations ----")
# checking equality (==) using __eq__
print(f"Is backed equal in the size to legacy? {backend == legacy_system}")
print(f"Is frontend bigger than backend? {frontend > backend}")

print("\n---- 2. Performing Addition (+)  ---")
# Merging frontend and backend using __add__
merged_system = frontend + backend
print(f"Result of addition: {merged_system}")