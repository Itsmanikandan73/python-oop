# 1. Base parent class
class Compiler:
    def __init__(self, name):
        self.name = name

    def compile_code(self):
        # Defualt behaviour (to be overridden by children )
        print("Compiling code generically...\n")

# 2. Chile class 1. -Overridding the parent method
class GCC(Compiler):
    def compile_code(self):
        print(f"[{self.name}]: Translating c++ source into an x86 binary optimized for Linux.\n")

# 3. Child class 2 - Overridding the parent method with different logic
class CPython(Compiler):
    def compile_code(self):
        print(f"[{self.name}] Parsing python source into bytcode and running it on the VM.\n")

# Creating a list of different Compiler objects, Python allows mixed types in lists effortlessly!
toolchain = [
    GCC("g++ 13.2"),
    CPython("CPython 3.12"),
    GCC("MinGW")
]

print("\n ---- Polymorphism in Action ----\n")
# We loop through the list and call the exact same method name '.compile_code()', python dynamically checks the object type and runs the correct version!
for tool in toolchain:
    tool.compile_code()

print("\n--- Polymorphism via Functions ---\n")
# You can also pass different objects into a single global fuction
def excute_compilation(compiler_obj):
    compiler_obj.compile_code()

special_compiler = CPython("PyPy")
excute_compilation(special_compiler)
