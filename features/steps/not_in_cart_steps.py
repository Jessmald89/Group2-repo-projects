# Import Behave and necessary modules
from behave import given, when, then
from app import app
from cart import Cart
from food import Food

# Define a "given" step - the fruit stand application is open, and the user has items in the cart
@given("the fruit stand application is open and the user has items in the cart")
def step_items_in_cart(context):
    # Create a test client for the application
    context.app = app.test_client()
    
    # Create a user cart and add two Food items (Banana and Apple) to it
    context.user_cart = Cart()
    context.user_cart.add(Food("Banana", 2.00))
    context.user_cart.add(Food("Apple", 3.00))

# Define a "when" step - the user attempts to remove an incorrect item from the cart
@when("the user attempts to remove an incorrect item from the cart")
def step_attempt_remove_incorrect_item(context):
    # Simulate a user's attempt to remove an item (Orange) from the cart using a POST request
    context.response = context.app.post("/", data={"form2_submit": "Remove", "remove_operation": "Orange"})

# Define a "then" step - check if the cart contents should remain the same
@then("the cart contents should remain the same")
def step_check_cart_unchanged(context):
    # Verify that the cart's contents remain the same (i.e., no items were removed)
    assert len(context.user_cart.item_names) == 2
    # Verify that the response status code is 200 (indicating a successful request)
    assert context.response.status_code == 200
    # Verify that a message indicating "Item not found in the cart!" is present in the response data
    assert b"Item not found in the cart!" in context.response.data
