from product import Product
from product_manager import ProductManager

manager = ProductManager()

# Dodavanje proizvoda
manager.add_product(Product("Laptop", 1000, 5))
manager.add_product(Product("Telefon", 500, 10))

# Prikaz proizvoda i ukupne vrednosti
manager.display_products()
print(f"Total Inventory Value: {manager.total_inventory_value()}")
