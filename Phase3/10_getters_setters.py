class Cpu:
    def __init__(self, model, cores):
        self.model = model
        # we assign the property setter directly here to trigger the validation check.
        self.cores = cores

    # 1. THE GETTER
    # Turing a method into a read-only property attribute
    @property
    def cores(self):
        # we store the actual value inside a  private/procted variable
        return self._cores

    # 2. THE SETTER
    # This monitors any attempt to change or set the 'cores' value
    @cores.setter
    def cores(self, value):
        if not isinstance(value, int) or value <= 0:
            # prevent bad data from entring your object
            raise ValueError("Core count must be a positive integer!")

        self._cores = value
        print(f"[Success] Cores set to {value}")

# ----- Execution -----

# This triggers the setter during initialization
processor = Cpu("Ryzen 9", 16)

print("\n ---- 1. Reading values via the Getter ----")
# Notice WE DO NOT use parentheses like processor.cores()
# The @property decoretor lets us read it like a normal attributes!
print(f"Processor: {processor.model} | Cores: {processor.cores}")

print("\n ---- 2. Updating values via the Setter -----")
# Modifying the value like a variable. This automatically runs the setter logic.
processor.cores = 24
print(f"Updated Core Count: {processor.cores}")

print("\n ---- 3. Testing Validation Checks ----")
# Let's try to pass bad data (like a string or negative number)
try:
    processor.cores = -4
except ValueError as error:
    print(f"Validation Blocked Input: {error}")