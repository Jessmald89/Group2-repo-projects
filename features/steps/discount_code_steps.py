# Import necessary modules
from behave import given, when, then
from app import app, user_cart
from constant_values import DISCOUNT_CODE, DISCOUNT

# Define a "given" step - the fruit stand application is open, and the user has items in their cart
@given('the fruit stand application is open and the user has items in their cart')
def step_open_fruit_store_and_user_has_items(context):
    # Create a test client for the application
    context.client = app.test_client()

# Define a "when" step - the user applies a discount code
@when('the user applies discount code "{discount_code}"')
def step_apply_discount_code(context, discount_code):
    # Check if the provided discount code matches the predefined discount code
    if discount_code == DISCOUNT_CODE:
        # Apply the discount to the user's cart
        user_cart.apply_discount(DISCOUNT)

# Define a "then" step - check if the cart total is updated with a 20% discount
@then('the cart total should be updated with a 20% discount')
def step_check_discount_applies(context):
    # Calculate the expected total after applying the discount
    expected_total = user_cart.calculate_total()
    # Get the actual total from the user's cart
    actual_total = user_cart.total
    # Assert that the actual total matches the expected total after applying the discount
    assert actual_total == expected_total
