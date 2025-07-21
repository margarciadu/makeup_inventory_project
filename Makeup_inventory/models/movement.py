# === Movement Log ===

# Class to represent product movements: entry, output, or expiration
class MovementRecord:
    def __init__(self, product_id, movement_type, quantity, date):
        self.product_id = product_id      # Product ID
        self.type = movement_type         # Type: 'entry', 'output', or 'expired'
        self.quantity = quantity          # Quantity of the movement
        self.date = date                  # Date and time of the movement

    def __str__(self):
        # String representation of a movement record
        # date.strftime converts the stored date into a readable text format with the desired structure.
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | ID: {self.product_id} | {self.type.upper()} | Quantity: {self.quantity}"