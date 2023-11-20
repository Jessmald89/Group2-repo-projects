import unittest
import requests

class TestFruitStandAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000'  # Base URL for API

    def test_add_to_cart(self):
        # Test adding a fruit to the cart
        endpoint = f"{self.base_url}/"  # Define endpoint for adding to cart
        payload = {"add_operation": "Banana"}  # Define payload with operation and fruit
        response = requests.post(endpoint, data=payload)  # Send POST request to add Banana to cart
        self.assertEqual(response.status_code, 200)  # Assert response status code is 200 (success)

    def test_remove_from_cart(self):
        # Test removing a fruit from the cart
        endpoint = f"{self.base_url}/"  # Define endpoint for removing from cart
        payload = {"remove_operation": "Apple"}  # Define payload with operation and fruit
        response = requests.post(endpoint, data=payload)  # Send POST request to remove Apple from cart
        self.assertEqual(response.status_code, 200)  # Assert response status code is 200 (success)

    def test_completing_purchase(self):
        # Test completing the purchase in the cart
        endpoint = f"{self.base_url}/cart"  # Define endpoint for completing purchase
        response = requests.post(endpoint, data={})  # Send POST request to complete purchase
        self.assertEqual(response.status_code, 200)  # Assert response status code is 200 (success)

    def test_cart_sorting_by_price(self):
        # Test sorting the cart by price (High-to-Low)
        endpoint = f"{self.base_url}/cart"  # Define endpoint for sorting cart
        params = {"sort_submit": "High-to-Low"}  # Define sorting parameter
        response = requests.post(endpoint, data=params)  # Send POST request to sort cart by price
        self.assertEqual(response.status_code, 200)  # Assert response status code is 200 (success)

if __name__ == '__main__':
    unittest.main()
