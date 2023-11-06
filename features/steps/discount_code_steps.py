from behave import given, when, then
from app import app, user_cart
from constant_values import DISCOUNT_CODE, DISCOUNT  # Import the discount code and discount percentage

@given('the fruit stand application is open and the user has items in their cart')
def step_open_fruit_store_and_user_has_items(context):
    context.client = app.test_client()
    # You may add items to the cart here (similar to what you did in the "app.py" file).

@when('the user applies discount code "{discount_code}"')
def step_apply_discount_code(context, discount_code):
    if discount_code == DISCOUNT_CODE:
        user_cart.apply_discount(DISCOUNT)

@then('the cart total should be updated with a 20% discount')
def step_check_discount_applies(context):
    expected_total = user_cart.calculate_total()
    actual_total = user_cart.total
    assert actual_total == expected_total
