from .product import Product

# Subclass for makeup products
class Makeup(Product):
    def __init__(self, name, id, price, brand, color, size, expiration_date):
        super().__init__(name, id, price, brand)
        self.color = color                      # Makeup color
        self.size = size                        # Size in ml
        self.expiration_date = expiration_date  # Expiration date
        self.expired = False

 # String representation of a makeup product
    def __str__(self):
        return (f"[{self.id}] {self.name} | Makeup | ${self.price:.2f} | {self.brand} | "
                f"{self.color} | {self.size}ml | Expiration Date: {self.expiration_date}")