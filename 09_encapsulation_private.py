class BankAccount:
    
    def __init__(self, owner, initial_balance):
        self.owner = owner      # Public attribute
        self._account_type = "Savings" # Protected attribute (one underscore)
        self.__balance = initial_balance  # Protected attribute (two underscore)

    # Public method to securely access private data
    def get_balance(self):
        return self.__balance

    # Public method to securely modify private data with verification rules
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

# ----- Execution -----
account = BankAccount("x86owl", 1000)

print("\n---- 1. Accessing Public and Protected Data ----")
print(f"Account Owner: {account.owner}")
print(f"Account Type: {account._account_type}") # it will, work but not use this in real app

print("\n---- 2. Attempting to access Private Data ----")
# This will throw an attributeError! python hides  __balance from direct view.
try:
    print(account.__balance)
except AttributeError as e:
    print(f"Error caught successfully: {e}")

print(f"\n---- 3. Modifying Data the Right way ----")
# we use the public methods instead of changing variables directly
account.deposit(250)
print(f"Verified Balance via getter method: ${account.get_balance()}")

print("\n--- 4. Demystifying Name Mangling ---")
# Behind the scenes, python renames '__balance' to '_ClassName__variable'.
# You *can* bypass security if you explicitly call the mangled name (useful for debugging)
print(f"Bypassed Access (Mangled Name): ${account._BankAccount__balance}")
