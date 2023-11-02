from behave import given, when, then
from cart import Cart
from food import Food

@given('the fruit stand application is available')
def step_open_fruit_store(context):
    context.store = Cart()

@when('the user adds an object to the cart')
def step_user_adds_object_to_cart(context):
    context.fruit = Food('Banana', 2.00)  
    context.store.add(context.fruit)

@then('the object should be added to the cart')
def step_check_object_added_to_cart(context):
    assert context.fruit in context.store.item_names
