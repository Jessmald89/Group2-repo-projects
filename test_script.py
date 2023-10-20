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
    Test that expected title matches the actual title of the page.
    """
    browser.get('http://localhost:5000')  # Access the app
    expected_title = 'Fruit Stand'  # Specify expected title
    actual_title = browser.title  # Get actual title

    assert expected_title == actual_title, "Expected title does not match actual title"


def test_select_add(browser):
    """
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


def test_input(browser):
    browser.get('http://localhost:5000')  # Access the app
    test_disc_code = 'DISCOUNT20'

    discount = browser.find_element(By.NAME, 'discount_code')

    discount.clear()

    discount.send_keys(test_disc_code)
    discount.send_keys(Keys.RETURN)