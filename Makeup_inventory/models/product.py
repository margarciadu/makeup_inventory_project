# === Product Classes ===

# Base class for all products
class Product:
    def __init__(self, name, id, price, brand):
        self.name = name              # Product name
        self.id = id                  # Unique product ID
        self.price = price            # Product price
        self.brand = brand            # Product brand
    def __str__(self):
        # String representation of a product
        return f"[{self.id}] {self.name} | ${self.price:.2f} | {self.brand}"