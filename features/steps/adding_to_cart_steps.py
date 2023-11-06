# Import necessary modules
from behave import given, when, then
from cart import Cart
from food import Food

# Define a "given" step - the fruit stand application is available
@given('the fruit stand application is available')
def step_open_fruit_store(context):
    # Create a Cart object to represent the user's shopping cart
    context.store = Cart()

# Define a "when" step - the user adds an object to the cart
@when('the user adds an object to the cart')
def step_user_adds_object_to_cart(context):
    # Create a Food object (e.g., a Banana) with a price of $2.00
    context.fruit = Food('Banana', 2.00)
    # Add the Food object to the user's shopping cart
    context.store.add(context.fruit)

# Define a "then" step - check if the object is added to the cart
@then('the object should be added to the cart')
def step_check_object_added_to_cart(context):
    # Assert that the Food object (context.fruit) is in the list of item names in the cart
    assert context.fruit in context.store.item_names
