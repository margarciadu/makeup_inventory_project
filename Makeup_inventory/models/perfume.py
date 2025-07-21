from .product import Product

# Subclass for perfume products
class Perfume(Product):
    def __init__(self, name, id, price, brand, scent, volume):
        super().__init__(name, id, price, brand)
        self.scent = scent            # Perfume scent
        self.volume = volume          # Volume in ml

    # String representation of a perfume product
    def __str__(self):
        return (f"[{self.id}] {self.name} | Perfume | ${self.price:.2f} | {self.brand} | "
                f"Scent: {self.scent} | {self.volume}ml")