from behave import given, when, then
from cart import Cart
from food import Food

# Given step: the user has items in the cart
@given('items found in cart')
def step_items_in_cart(context):
    context.user_cart = Cart()  # Create a Cart instance for the user
    context.fruit = Food('Banana', 2.00)  # Create a Food instance (Banana) to add to the cart
    context.user_cart.add(context.fruit)  # Add the Banana to the cart

# When step: the user clicks the 'Purchase' button
@when('the user clicks the "Purchase" button')
def step_user_clicks_purchase_button(context):
    context.user_cart.purchase()  # Simulate the user clicking the 'Purchase' button

# Then step: the cart should be empty after the purchase
@then('the cart should be empty after the purchase')
def step_check_cart_empty(context):
    assert len(context.user_cart.item_names) == 0  # Check if the cart is empty after the purchase
    assert context.user_cart.subtotal == 0.0  # Check if the subtotal is reset to 0
    assert context.user_cart.discount == 0.0  # Check if the discount is reset to 0
    assert context.user_cart.discount_applied is False  # Check if the discount_applied flag is reset
    assert context.user_cart.purchase_message == "Thank you for purchasing!"  # Check the purchase message
