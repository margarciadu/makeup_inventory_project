import json
from datetime import datetime
from models.makeup import Makeup
from models.perfume import Perfume

# === Bulk Load from JSON ===

# Loads product data from a JSON file into inventory
def load_inventory_from_json(filepath, stock): # The def keyword must go at the beginning of the line (without indentation) when you are defining a top-level function (outside of another function or class).
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        product_type = item.get("Type of Product", "").lower()
        name = item.get("Name")
        pid = int(item.get("Product ID"))
        raw_price = item.get("Price")
        if isinstance(raw_price, str):
            raw_price = raw_price.replace("$", "").replace(",", ".").strip()
        price = float(raw_price)
        brand = item.get("Brand")
        quantity = int(item.get("Quantity", 0))

        # Create makeup product
        if product_type == "makeup":
            color = item.get("Color")
            raw_size = item.get("Size", "").lower().replace("ml", "").replace("g", "").strip()
            size = float(raw_size.replace(",", "."))
            expiration_str = item.get("Expiration date")
            expiration_date = datetime.strptime(expiration_str, "%Y-%m-%d").date()
            product = Makeup(name, pid, price, brand, color, size, expiration_date)
            
        # Create perfume product
        elif product_type == "perfume":
            scent = item.get("Scent")
            raw_volume = item.get("Size", "").lower().replace("ml", "").strip()
            volume = float(raw_volume.replace(",", "."))
            product = Perfume(name, pid, price, brand, scent, volume)

        else:
            continue #Skip unknown product types

        # Add product and register initial stock
        stock.add_product(product)
        stock.register_entry(pid, quantity)

# === Save Inventory to JSON ===


# Saves current inventory to a JSON file
def save_inventory_to_json(filepath, stock):
    data = []
    for pid, product in stock.products.items():
        item = {
            "Product ID": product.id,
            "Name": product.name,
            "Price": product.price,
            "Brand": product.brand,
            "Quantity": stock.inventory[pid]
        }
        # Add extra fields depending on product type
        if isinstance(product, Makeup):
            item.update({
                "Type of Product": "Makeup",
                "Color": product.color,
                "Size": f"{product.size}ml",
                "Expiration date": product.expiration_date.strftime("%Y-%m-%d")
            })
        elif isinstance(product, Perfume):
            item.update({
                "Type of Product": "Perfume",
                "Scent": product.scent,
                "Size": f"{product.volume}ml"
            })
        data.append(item)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Inventory saved successfully.")