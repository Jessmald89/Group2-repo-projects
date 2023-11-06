# Import Behave and necessary modules
from behave import given, when, then
from cart import Cart
from food import Food

# Define a "given" step - the user has items in the cart
@given('the user has items in the cart')
def step_user_has_items_in_cart(context):
    # Create a Cart object to represent the user's shopping cart
    context.store = Cart()
    
    # Create a Food object (e.g., a Banana) with a price of $2.00
    context.fruit = Food('Banana', 2.00)
    
    # Add the Food object to the user's shopping cart
    context.store.add(context.fruit)

# Define a "when" step - the user removes an object from the cart
@when('the user removes an object from the cart')
def step_user_removes_object_from_cart(context):
    # Remove the Food object from the user's shopping cart
    context.store.remove(context.fruit)

# Define a "then" step - check if the object will be removed from the cart
@then('the object will be removed from the cart')
def step_check_object_removed_from_cart(context):
    # Assert that the Food object (context.fruit) is not in the list of item names in the cart
    assert context.fruit not in context.store.item_names
