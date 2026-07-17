from dataclasses import dataclass, field

# Using the decorator tells python to auto-generate:
# __init__(), __repr__(), and __eq__() automatically
@dataclass
class ServerConfig:
    host: str 
    port: int 
    active: bool = True  # Default value

    # Advanced: if you want a default list or dict, you must use field(default_factory=...)
    # This prevents all instances from accidentally sharing the same list in memory.
    allowed_ips: list[str] = field(default_factory=lambda: ["127.0.0.1"])


# 1. Initialization
# We didn't have to write an __init__ method, but it work perfectly!
config_a = ServerConfig("192.168.1.100", 8080)
config_b = ServerConfig("192.168.1.100", 8080)
config_c = ServerConfig("10.0.0.1", 443, active=False, allowed_ips=["10.0.0.5","10.0.0.6"])


print("----1. Auto-Generated __repr__ ----")
# Dataclasses print beatifully by default without writing custom formatting code
print(config_a)
print(config_c)

print("\n----2. Auto-Generated __eq__ (Equality check) ----")
# Normally, config_a == config_b would return False beacuse they are in different memeory addresses.
# But dataclasses automatically compare their actual field values!
print(f"Is config A equal to Config B? {config_a == config_b}")
print(f"Is config A equal to Config C? {config_a == config_c}")

print("\n--- 3. Modifying fields ----")
# You can update values just like standared class attributes
config_a.port = 9000
print(f"Updated Port for config A: {config_a.port}")
