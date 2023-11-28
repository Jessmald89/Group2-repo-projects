import unittest
from app import app
from cart import Cart
from food import Food

class TestCart(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.cart = Cart()

    def test_empty_cart(self):
        # Check if the cart is empty initially
        self.assertEqual(self.cart.items, [])

    def test_add_item(self):
        # Add a banana to the cart
        banana = Food("Banana", 2.50)
        self.cart.add(banana)
        self.assertEqual(self.cart.items, [banana])

    def test_remove_item(self):
        # Add a banana to the cart, then remove it
        banana = Food("Banana", 2.50)
        self.cart.add(banana)
        self.cart.remove(banana)
        self.assertEqual(self.cart.items, [])

    def test_check_quantity(self):
        # Add two bananas to the cart and check the quantity
        banana = Food("Banana", 2.50)
        self.cart.add(banana)
        self.cart.add(banana)

        # Iterate through the cart items and count the number of bananas
        banana_quantity = 0
        for item in self.cart.items:
            if item.name == "Banana":
                banana_quantity += 1

        # Assert that the quantity of bananas is 2
        self.assertEqual(banana_quantity, 2)

    def test_sort_items(self):
        # Add a banana, an apple, and an orange to the cart, then sort items by price in descending order
        banana = Food("Banana", 2.50)
        apple = Food("Apple", 1.99)
        orange = Food("Orange", 3.99)
        self.cart.add(banana)
        self.cart.add(apple)
        self.cart.add(orange)
        self.cart.sort("desc")
        item_list = self.cart.items
        self.assertEqual(item_list, [orange, banana, apple])
    
    def test_empty_inventory(self):
        # Check if the inventory of each fruit becomes empty after adding and removing items
        banana = Food("Banana", 2.50)
        apple = Food("Apple", 1.99)
        orange = Food("Orange", 3.99)

        # Add 5 of each fruit to the cart
        for _ in range(5):
            self.cart.add(banana)
            self.cart.add(apple)
            self.cart.add(orange)

        # Check if the inventory of each fruit is empty after removing all items
        self.assertEqual(self.cart.quantity, {'Banana': 0, 'Apple': 0, 'Orange': 0})