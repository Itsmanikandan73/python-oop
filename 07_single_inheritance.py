# 1. THE PARENT CLASS (superclass)
class Device:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def power_on(self):
        print(f"The {self.brand} device is powering up...")

    # 2. THE CHILD CLASS (Subclass)
    # Smartphone inherits everything from Device
class SmartPhone(Device):
    def __init__(self, brand, price, os_name, storage):
        # super().__init__() automatically calls the parent's constructor 
        # It passes 'brand' and 'price' to the Device class to handle
        super().__init__(brand, price)

        # Now we handle the unique attributes specific ONLY to a SmartPhone
        self.os_name = os_name
        self.storage = storage

    # Unique method only available to SmartPhone instance 
    def make_call(self, contact):
        print(f"Dialing {contact} on my {self.brand} phone running {self.os_name}...")

# ---- Excution ----
print("\n---- 1. Testing parent Class ----")
# A generic device only has acess to brand , price and power_on()
generic_tech = Device("GenericBrand", 35)
generic_tech.power_on()

print("\n--- 2. Testing child class (Inheritance) ---")
# creating a smartphone requires parent arguments (Lenovo, 300) AND child arguments (Android, 128GB)
my_phone = SmartPhone("Lenovo", 300,"Android", "128 GB")

# Look at this! my_phone can use power_on() even though we didn't write it inside SmartPhone!
my_phone.power_on()

# It can also use its own unique methods
my_phone.make_call("x86owl")

print("\n---- 3. Verifying Relationships ----")
# Python built-ins to check class structures
print(f"Is my_phone an instance of SmartPhone? {isinstance(my_phone, SmartPhone)}")
print(f"Is my_phone an instance of Device? {isinstance(my_phone, Device)}")
print(f"Is my_phone an subclass of Device? {isinstance(SmartPhone, Device)}")