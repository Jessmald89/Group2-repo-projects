import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_title_validation(browser):
    """
    Test Case ID: 0001
    Test that expected title matches the actual title of the page.
    """
    browser.get('http://localhost:5000')  # Access the app
    expected_title = 'Fruit Stand'  # Specify expected title
    actual_title = browser.title  # Get actual title

    assert expected_title == actual_title, "Expected title does not match actual title"

def test_total_calculation_with_discount(browser):
    """
    Test Case ID: 0002
    Tests the total calculation with a discount applied.
    """
    browser.get('http://localhost:5000')  # Access the app

    # Select and add a Banana to the cart
    select = Select(browser.find_element(By.NAME, 'add_operation'))
    select.select_by_visible_text('Banana')

    # Click "Add to Cart" button
    add_to_cart = browser.find_element(By.NAME, 'form1_submit')
    add_to_cart.click()

    # Enter a valid discount code (e.g., 'DISCOUNT20')
    discount = browser.find_element(By.NAME, 'discount_code')
    discount.clear()
    discount.send_keys('DISCOUNT20')
    discount.send_keys(Keys.RETURN)

    # Verify that the total is correctly calculated (after applying the discount)
    total_text = browser.find_element(By.XPATH, '//p[contains(text(), "Total: $")]').text
    assert total_text.startswith('Total: $1.6')  


def test_select_add(browser):
    """
    Test Case ID: 0003, 0004
    Test that items are successfully selected and added to cart.
    """
    browser.get('http://localhost:5000')  # Access the app

    # Select Banana from dropdown menu
    select = Select(browser.find_element(By.NAME, 'add_operation'))
    select.select_by_visible_text('Banana')

    # Click "Add to Cart" button
    browser.find_element(By.NAME, 'form1_submit').click()

    # Handle StaleElementReferenceException and re-locate dropdown element
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    dropdown = WebDriverWait(browser, 10, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.NAME, 'add_operation')))

    # Test that selected option matches expected option
    select = Select(dropdown)
    selected_option = select.first_selected_option
    assert selected_option.text == "Banana"

    # Test that item has been added to cart
    cart = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'item_display')))
    assert "Banana" in cart.text, "Item not added to cart."

def test_remove_item(browser):
    """
    Test Case ID: 0005
    Test that items are successfully removed from cart
    """

    # Access the app
    browser.get('http://localhost:5000')

    # Select a valid item to add to the cart (e.g., 'Banana')
    select = Select(browser.find_element(By.NAME, 'add_operation'))
    select.select_by_visible_text('Banana')

    # Click "Add to Cart" button
    add_to_cart = browser.find_element(By.NAME, 'form1_submit')
    add_to_cart.click()

    # Select the same item to remove (e.g., 'Banana')
    select = Select(browser.find_element(By.NAME, 'remove_operation'))
    select.select_by_visible_text('Banana')

    # Click "Remove from Cart" button
    remove_from_cart = browser.find_element(By.NAME, 'form2_submit')
    remove_from_cart.click()

    # Ensure the item has been removed from the cart
    cart = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'item_display')))
    assert "Banana" in cart.text, "Item not removed from cart."

def test_invalid_item_removal(browser):
    """
    Test Case ID: 0006
    Test that attempts to remove an item not in cart are properly handled.
    """
    # Access the app
    browser.get('http://localhost:5000')

    # Select a valid item to add to the cart (e.g., 'Banana')
    select = Select(browser.find_element(By.NAME, 'add_operation'))
    select.select_by_visible_text('Banana')

    # Click "Add to Cart" button
    add_to_cart = browser.find_element(By.NAME, 'form1_submit')
    add_to_cart.click()

    # Wait for the 'Remove from Cart' button to be clickable
    remove_from_cart = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.NAME, 'form2_submit'))
    )

    # Attempt to remove an invalid item (e.g., 'Orange')
    select = Select(browser.find_element(By.NAME, 'remove_operation'))
    select.select_by_visible_text('Orange')

    # Click "Remove from Cart" button
    remove_from_cart.click()

    # Ensure the item has been removed from the cart
    cart = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'item_display'))
    )
    assert "Orange" not in cart.text, "Attempted to remove item not in cart"


def test_input(browser):
    """
    Test Case ID: 0007, 0008
    Test the input of a discount code and submission
    """

    browser.get('http://localhost:5000')  # Access the app
    test_disc_code = 'DISCOUNT20'

    discount = browser.find_element(By.NAME, 'discount_code')

    discount.clear()

    discount.send_keys(test_disc_code)
    discount.send_keys(Keys.RETURN)

def test_clear_cart(browser):
    """
    Test Case ID: 0009
    Test that cart is cleared when clicking "Purchase"
    """

    # Access the app
    browser.get('http://localhost:5000')

    # Select a valid item to add to the cart (e.g., 'Banana')
    select = Select(browser.find_element(By.NAME, 'add_operation'))
    select.select_by_visible_text('Banana')

    # Click "Add to Cart" button
    add_to_cart = browser.find_element(By.NAME, 'form1_submit')
    add_to_cart.click()

    # Click "Purchase Items in Cart" button
    purchase_items = browser.find_element(By.NAME, 'form3_submit')
    purchase_items.click()

    # Ensure the cart has been cleared
    cart = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'item_display')))
    assert "Banana" not in cart.text, "Cart not cleared after purchase."

