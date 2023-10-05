import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_flask_app(browser):
    browser.get('http://localhost:5000')
    assert 'Welcome to My Flask App' in browser.page_source

if __name__ == '__main__':
    pytest.main()