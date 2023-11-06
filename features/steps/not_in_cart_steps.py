# Import Behave and necessary modules
from behave import given, when, then
from app import app
from cart import Cart
from food import Food

@given("the fruit stand application is open and the user has items in the cart")
def step_items_in_cart(context):
    context.app = app.test_client()
    context.user_cart = Cart()
    context.user_cart.add(Food("Banana", 2.00))
    context.user_cart.add(Food("Apple", 3.00))

@when("the user attempts to remove an incorrect item from the cart")
def step_attempt_remove_incorrect_item(context):
    context.response = context.app.post("/", data={"form2_submit": "Remove", "remove_operation": "Orange"})

@then("the cart contents should remain the same")
def step_check_cart_unchanged(context):
    # Verify that the cart's contents remain the same (i.e., no items were removed)
    assert len(context.user_cart.item_names) == 2
    assert context.response.status_code == 200
    assert b"Item not found in the cart!" in context.response.data
