from datetime import datetime
from models.movement import MovementRecord 

# === Inventory Management ===

# Main class to manage products and inventory
class Stock:
    def __init__(self):
        self.products = {}     # Dictionary of products (ID -> Product) 
        self.inventory = {}    # Inventory count (ID -> Quantity) 
        self.history = []      # List of movement records

    def add_product(self, product):
        # Adds a product data if it doesn't already exist
        if product.id not in self.products:
            self.products[product.id] = product
            self.inventory[product.id] = 0 # It registers the product with an initial amount of 0
            print("Product added")
        else:
            print("Product already exists")

    def register_entry(self, product_id, amount):
        # Registers incoming stock of already existing product data
        if product_id in self.products:
            self.inventory[product_id] += amount
            record = MovementRecord(product_id, "entry", amount, datetime.now()) #record is a single movement represented as an object
            self.history.append(record) # record is now added to the inventory's history
            print("Entry registered")
        else:
            print("Product not found")

    def register_output(self, product_id, amount):
        # Registers outgoing stock
        product = self.products.get(product_id)
        if product and not getattr(product, 'expired', False) and self.inventory.get(product_id, 0) >= amount:
            self.inventory[product_id] -= amount
            record = MovementRecord(product_id, "output", amount, datetime.now()) #record is a single movement represented as an object
            self.history.append(record) # record is now added to the inventory's history
            print("Output registered")
        else:
            print("Insufficient stock or product not found or expired")

    def show_inventory(self):
         # Displays current inventory even product with 0 amount in stock
        print("\n=== CURRENT INVENTORY ===")
        for pid, product in self.products.items():
            quantity = self.inventory.get(pid, 0) # if no entries have been registered, it shows the product´s quantity as 0
            status = "EXPIRED" if getattr(product, 'expired', False) else ""
            print(f"{product} | Quantity: {quantity} {status}")
        print()

    def show_history(self):
          # Displays full movement history
        print("\n=== MOVEMENT HISTORY ===")
        for record in self.history:
            print(record)

    def find_product(self, product_id):
        # Returns a product by its ID
        return self.products.get(product_id, "Product not found")

    def check_expirations(self):
        # Removes expired makeup products from inventory
        for pid, product in self.products.items():
            if hasattr(product, 'expiration_date') and not getattr(product, 'expired', False):
                if product.expiration_date < datetime.now().date():
                    product.expired = True
                    self.history.append(MovementRecord(pid, "expired", 0, datetime.now()))
                    print(f"Product {pid} marked as expired")
