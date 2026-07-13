# Parent class 1
class NetworkNode:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        print(f"[NetworkNode Init] Setting IP to {self.ip_address}")

    def ping(self):
        print(f"Pinging Network node at {self.ip_address}....")

# Parent class 2
class StorageUnit:
    def __init__(self, capacity):
        self.capacity = capacity
        print(f"[StorageUnit Init] Allocating {self.capacity} of storage")

    def read_data(self):
        print(f"Reading data chunks from storage blocks....")

# Child Class inheritance from BOTH  parents
# Order matters: NetworkNOde is checked BEFORE StorageUnit
class NetworkAttachedStorage(NetworkNode, StorageUnit):
    
    def __init__(self, ip_address, capacity, server_name):
        # To initialize multiple parents safely in python without breaking MRO,
        # we call the construction explicitly using the class names.
        NetworkNode.__init__(self, ip_address)
        StorageUnit.__init__(self, capacity)

        self.server_name = server_name
        print(f"[NAS Init] Server '{self.server_name}' is fully online")

print("---- 1. Initializing NAS (Multiple Parents) ----\n")
nas_drive = NetworkAttachedStorage("192.268.1.49", "8 TB", "OwlStorage")

print("\n----- 2. Accessing Inherited Methods ----")
# Available from NetworkNode parent
nas_drive.ping()

# Available from StorageUnit parent 
nas_drive.read_data()

print("\n ----3. Checking Method Resolution Order (MRO)")
# The .__mro__ attribute (or help) function shows the exact search route python takes.
print("MRO Search Order:")
for position, cls in enumerate(NetworkAttachedStorage.__mro__, start=1):
    print(f"{position}. {cls.__name__}")

position = NetworkAttachedStorage.__mro__
print(position)