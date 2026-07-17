# Component class 1
class CPU:
    def __init__(self, model, speed_ghz):
        self.model = model
        self.speed_ghz = speed_ghz

    def process_data(self):
        return f"CPU ({self.model}) is executing threads at {self.speed_ghz} GHz."

# Component class 2
class Storage:
    def __init__(self, capacity_gb, drive_type):
        self.capacity_gb = capacity_gb
        self.drive_type = drive_type

    def read_write(self):
        return f"Storage ({self.capacity_gb}GB {self.drive_type})"

# The main class that COMPOSE both components
class Workstation:
    def __init__(self, name, cpu_obj, storage_obj):
        self.name = name
        
        # We are passing actual object of other classes into out attributes!
        self.cpu = cpu_obj
        self.storage = storage_obj

    def run_benchmark(self):
        print(f"--- Runnign Diagnostics for Workstation: {self.name} ----")
        # Delegate the work to the respective internal components
        print(self.cpu.process_data())
        print(self.storage.read_write())

# 1. First, create the standalone componets
my_cpu = CPU("Intel i9-14900k", 5.8)
my_storage = Storage(2048, "NVMe SSD")

# 2. Build the workstation by passing the objects inside
# Workstation HAS A CPU, and HAS A storage unit.
desktop = Workstation("Owl-Rig-01", my_cpu, my_storage)

# 3. Trigger the system
desktop.run_benchmark()