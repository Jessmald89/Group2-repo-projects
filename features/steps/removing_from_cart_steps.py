from behave import given, when, then
from cart import Cart
from food import Food

@given('the user has items in the cart')
def step_user_has_items_in_cart(context):
    context.store = Cart()
    context.fruit = Food('Banana', 2.00)  
    context.store.add(context.fruit)

@when('the user removes an object from the cart')
def step_user_removes_object_from_cart(context):
    context.store.remove(context.fruit)

@then('the object will be removed from the cart')
def step_check_object_removed_from_cart(context):
    assert context.fruit not in context.store.item_names
