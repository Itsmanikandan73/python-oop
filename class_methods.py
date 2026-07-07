class Member:
    # class variable
    community = "python India"

    def __init__(self, username, role):
        self.username = username
        self.role = role

    def display(self):
        print(f"User: {self.username} | Role: {self.role} | Community: {Member.community}")

    # 1. A standard class method to modify a class variable
    @classmethod
    def update_community(cls, new_name):
        # 'cls' refers to the Member class itself, just like 'self' refers to the instance
        cls.community = new_name

    # 2. An alternative constructor class method
    # Useful when data comes in differnt format (like a hyphenated string)
    @classmethod
    def from_string(cls, data_string):
        # Splits "x86owl-Admin" into ["x86owl", "Adimin"]
        username,role = data_string.split("-")

        # cls(...) is exactly like running Member (username, role)
        return cls(username, role)

# -------- Excution --------
# standard initialization
user1 = Member("alice_dev", "Developer")

# Alternative initialization using our class method
# This parser the string and returns a brand new Member object automatically!
user2 = Member.from_string("x86owl-Admin")

print("---- Initial State ----")
user1.display()
user2.display()

print("\n------ Modifying class variable via class method -----")
# we call class methods directly on the class, not the instance
Member.update_community("FOSS India")

# Both instace reflect the update because 'cla.community' changed it globally
user1.display()
user2.display()