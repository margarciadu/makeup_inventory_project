from services.stock import Stock
from services.json_manager import load_inventory_from_json
from menu_interface.menu import show_menu

if __name__ == "__main__":
    stock = Stock()
    load_inventory_from_json("inventory_json/inventario.json", stock)
    show_menu(stock)