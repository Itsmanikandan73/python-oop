class FleetDrone:
    # 1. CLASS VARIABLE
    # Shared by all instance. If the fleet status changes, every drone updates
    fleet_status = "ACTIVE"
    drone_count = 0 # To keep track of the all the objects created

    def __init__(self, drone_id, battery_level):
        # 2. INSTANCE VARIABLES
        # Unique to each specific drone object.
        self.drone_id = drone_id
        self.battery_level = battery_level

        # Increment the total drone count every time a new object is initialized
        FleetDrone.drone_count += 1

    def report(self):
        # Notice we can access both types of variables inside an instance method
        print(f"Drone [{self.drone_id}] | Battery: {self.battery_level} | Fleet Status: {self.fleet_status}")

print(f"Initial Total Drones: {FleetDrone.drone_count}")

# Creating two unique drone instances
drone_a = FleetDrone("Alpha-1", 92)
drone_b = FleetDrone("Beta-2", 45)

print("\n--- Individual Drone Status ---")
drone_a.report()
drone_b.report() 
print(f"Total Drones Deployed: {FleetDrone.drone_count}")

print("\n --- Modifying an Instance Variable ---")
# Changing drone_a's battery doesn't touch drone_b
drone_a.battery_level = 85
print(f"Drone A Battery: {drone_a.battery_level}%")
print(f"Drone B Battery: {drone_b.battery_level}%")

print("\n ---Modifying the class Variable ---")
# If the command center orders a RECALL, we change it at the clas level
FleetDrone.fleet_status = "RECALL"

# Both drones automatically reflect this change 
drone_a.report()
drone_b.report()

    