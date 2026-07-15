class Developer:
    
    def __init__(self, alias, handle, language):
        self.alias = alias
        self.handle = handle
        self.language = language

    # 1. __repr__ is for DEVELOPERS
    # It should be unambiguous and if possible, look like the code used to create the object.
    # It is used when debugging, looking at objects in a list, or in an interactive terminal.
    def __repr__(self):
        return f"Developer(alias='{self.alias}',handle='{self.handle}', language='{self.language}')"

    # 2. __str__ is for END-USERS
    # It should be clean, readable, and user friendly
    # It triggers automatically when you print() or str().
    def __str__(self):
        return f"User: {self.alias} (@{self.handle}) | Core Tech: {self.language}"

    
# creating a instance
dev = Developer("x86owl","owl_code", "Python")

print("\n----1. Using print() (Triggers __str__) ----")
print(dev)

print("\n---- 2. Inspecting via a List (Triggers __repr__) ----")
# if you put the object inside a list, python prints the  list container using __repr__
# so developers can see the exact state of the objects inside.
dev_team = [dev] # Intance assinging to the List
print(dev_team)

print("\n--- 3. Forcing either method explicitly ---")
# you can manually call them using built-in function
print("Explicit str() : ", str(dev))
print("Explicit repr(): ", repr(dev))