from product import Product
from product_manager import ProductManager

manager = ProductManager()

# Dodavanje proizvoda
manager.add_product(Product("Laptop", 1000, 5))
manager.add_product(Product("Telefon", 500, 10))

# Prikaz proizvoda i ukupne vrednosti
manager.display_products()
print(f"Total Inventory Value: {manager.total_inventory_value()}")
from cart import Cart

cart = Cart()
cart.add_to_cart(Product("Laptop", 1000, 2))
cart.add_to_cart(Product("Telefon", 500, 1))

cart.display_cart()
print(f"Total Cart Value: {cart.calculate_total()}")
