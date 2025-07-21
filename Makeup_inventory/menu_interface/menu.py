from datetime import datetime

from models.makeup import Makeup
from models.perfume import Perfume
from services.json_manager import save_inventory_to_json

# === User Interface ===

def show_menu(stock):
    while True:
        print("\n=== INVENTORY MENU ===")
        print("1. Show inventory")
        print("2. Register stock entry")
        print("3. Register stock output")
        print("4. Find product by ID")
        print("5. Show movement history")
        print("6. Check expired products")
        print("7. Save inventory to JSON")
        print("8. Add product manually")
        print("9. Delete product by ID")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            stock.show_inventory()
        elif choice == "2":
            try:
                pid = int(input("Product ID: "))
                qty = int(input("Quantity to add: "))
                stock.register_entry(pid, qty)
            except ValueError:
                print("Invalid input")
        elif choice == "3":
            try:
                pid = int(input("Product ID: "))
                qty = int(input("Quantity to remove: "))
                stock.register_output(pid, qty)
            except ValueError:
                print("Invalid input")
        elif choice == "4":
            try:
                pid = int(input("Product ID: "))
                product = stock.find_product(pid)
                print(product)
            except ValueError:
                print("Invalid ID")
        elif choice == "5":
            stock.show_history()
        elif choice == "6":
            stock.check_expirations()
        elif choice == "7":
            save_inventory_to_json("data/inventario.json", stock)
        elif choice == "8":
            try:
                tipo = input("Type of product (makeup/perfume): ").strip().lower()
                name = input("Name: ")
                pid = int(input("Product ID: "))
                price = float(input("Price: "))
                brand = input("Brand: ")
                if tipo == "makeup":
                    color = input("Color: ")
                    size = float(input("Size in ml: "))
                    expiration_str = input("Expiration date (YYYY-MM-DD): ")
                    expiration_date = datetime.strptime(expiration_str, "%Y-%m-%d").date()
                    product = Makeup(name, pid, price, brand, color, size, expiration_date)
                elif tipo == "perfume":
                    scent = input("Scent: ")
                    volume = float(input("Volume in ml: "))
                    product = Perfume(name, pid, price, brand, scent, volume)
                else:
                    print("Unknown product type")
                    continue
                stock.add_product(product)
            except Exception as error:
                print("Error:", error)
        elif choice == "9":
            try:
                pid = int(input("Product ID to delete: "))
                if pid in stock.products:
                    del stock.products[pid]
                    del stock.inventory[pid]
                    print(f"Product {pid} deleted.")
                else:
                    print("Product not found.")
            except ValueError:
                print("Invalid input")
        elif choice == "0":
            print("Exiting the system")
            break
        else:
            print("Invalid option")
