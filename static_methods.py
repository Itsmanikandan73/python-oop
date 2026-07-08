class Invoice:
    tax_rate = 0.18 # 18% of GST (class variable)

    def __init__(self, item, price):
        self.item = item
        self.price = price

    # 1. Instance method: Needs "self" to access specific iteam data
    def generate_bill(self):
        # Using the static method helper inside the class
        total = Invoice.calculate_total(self.price, Invoice.tax_rate)
        print(f"Iteam: {self.item} | Base: ${self.price} | Total (inc. tax): ${total:.2f}")

    # 2. Static Method: No self, no cls. It's an isolated utility helper
    # It just takes raw parameters does math, and returns a value
    @staticmethod
    def calculate_total(base_price, tax):
        return base_price + (base_price * tax)

    # 3. Another static method example Validation check
    @staticmethod
    def is_valid_price(price):
        return price > 0

print("\n---- 1. Using a Static Method directly without an object ----")
# Beacuse static methods don't relly on instance data, you can call item
# directly using the class name. Perfect for quick validation or calculations.
is_valid = Invoice.is_valid_price(-50)
print(f"Is -50 a valid price? {is_valid}")

print(f"\n---- 2. Creating an object and using the helper inside ---")
#Standard instace generation
bill1 = Invoice("Mechanical keyboard", 120)
bill2 = Invoice("Ultrawide monitor", 350)

bill1.generate_bill()
bill2.generate_bill()

