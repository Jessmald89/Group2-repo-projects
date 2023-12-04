import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture(scope="module")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

# Each test gets a fresh page instance

def test_remove_fruit_from_cart(context):
    page = context.new_page()
    page.goto('http://127.0.0.1:5000')

    # Add an item (e.g., Banana) to the cart
    page.select_option('select[name="add_operation"]', label='Banana')
    page.click('input[name="add_submit"]')

    # Remove the item from the cart
    page.select_option('select[name="remove_operation"]', label='Banana')
    page.click('input[name="remove_submit"]')

    # Check if the cart is empty after removing Banana
    cart_items = page.query_selector_all('.right-box p[name="item_display"]')
    assert not any('Banana' in item.text_content() for item in cart_items), "Banana should not be in the cart after removal"

def test_add_fruit_to_cart(context):
    page = context.new_page()
    page.goto('http://127.0.0.1:5000')

    # Select an item and add it to the cart
    page.select_option('select[name="add_operation"]', label='Banana')
    page.click('input[name="add_submit"]')

    # Check if the item has been added to the cart
    cart_content = page.inner_text('[name="item_display"]') 
    assert 'Banana' in cart_content, "Banana should be in the cart"

def test_check_quantity(context):
    page = context.new_page()
    page.goto('http://127.0.0.1:5000')

    # Add two bananas to the cart
    page.select_option('select[name="add_operation"]', label='Banana')
    page.click('input[name="add_submit"]')

    # Get the quantity of bananas in the cart
    cart_content = page.inner_text('.right-box p')  
    banana_quantity = cart_content.count('Banana')  

    # Assert that the quantity of bananas is 1
    assert banana_quantity == 1, "Expected 1 Bananas in the cart"

def test_validate_page_title(context):
    page = context.new_page()
    page.goto('http://127.0.0.1:5000')

    # Get the title of the webpage
    title = page.title()

    # Define the expected title
    expected_title = "Fruit Stand"  

    # Assert that the fetched title matches the expected title
    assert title == expected_title, f"Expected title: {expected_title}, Actual title: {title}"

def test_select_dropdown_option(context):
    page = context.new_page()
    page.goto('http://127.0.0.1:5000')

    # Define the selector for the dropdown element
    dropdown_selector = 'select[name="add_operation"]'  
    option_to_select = 'Banana' 

    page.select_option(dropdown_selector, label=option_to_select)

def test_receipt_page(context):
    page = context.new_page()
    page.goto('http://127.0.0.1:5000')  

    # Add Banana to cart
    page.select_option('select[name="add_operation"]', label='Banana')
    page.click('input[name="add_submit"]')

    # Enter name as 'John'
    page.fill('input[name="user_name"]', 'John')
    page.click('input[name="name_submit"]')

    # Click on 'Checkout'
    page.click('input[name="see_cart"]')

    # Click on 'Purchase'
    page.click('input[name="purchase_submit"]')

    # Check if 'Banana' appears on the receipt page
    page.wait_for_selector('h1.banner:has-text("Receipt")')
    
    # Check if 'Banana' appears in the item list on the receipt
    banana_displayed = page.inner_text('p[name="item_display"]:has-text("Banana")')
    assert 'Banana' in banana_displayed, "'Banana' not found on the receipt page"
    
    # Close the page
    page.close()
