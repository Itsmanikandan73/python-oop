class SmartDevice:
    # class variable (shared by all devices)
    ecosystem = "SmartHome"

    # The Constructor (__init__)
    # 'self' must always be the first parameter in instance methods.
    # we can use default arguments (like price = 0) to mimic constructor overloading!
    def __init__(self, name, brand, price=0):
        self.name = name
        self.brand = brand
        self.price = price
        self.is_on = False  # You can set default states without passing them as arguments

    # An instance method
    def toggele_power(self):
        # 'self' allows us to access and change this specific object's data
        self.is_on = not self.is_on
        state = "ON" if self.is_on else "OFF"
        print(f"{self.name} is now {state}.")

    def display_info(self):
        # Note how we must use 'self' to access variables inside the class
        print(f"Device: {self.name} | Brand: {self.brand} | Price: ${self.price}")

# Creating an object passing all arguments
device1 = SmartDevice("Echo Dot", "Amazon", 49)
device2 = SmartDevice("Alexa", "Amazon", 75)

# calling methods on the objects
print("---- Device 1 ----")
device1.display_info()
device1.toggele_power()

print("\n--- Device 2 ----")
device2.display_info()
device2.toggele_power()

print("\n --- Understanding 'self' ----")
# Behind the scenes, when you call device1.toggle_power(), it converts SmartDevice.toggle_power(device1)
# That is why 'self' is required in the method definition!
print(f"Memory address of device1: {hex(id(device1))}")                