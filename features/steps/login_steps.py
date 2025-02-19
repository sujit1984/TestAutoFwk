from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import time


@given("I am on the SauceDemo login page")
def open_login_page(context):
    try:
        # Ensure WebDriver is installed and starts correctly
        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service)

        # Open the login page
        context.driver.get("https://www.saucedemo.com/")
        context.driver.implicitly_wait(5)

        # Verify the page has loaded correctly
        assert "Swag Labs" in context.driver.title, "Login page did not load correctly"

        context.login_page = LoginPage(context.driver)

    except Exception as e:
        print(f"Error: {e}")
        raise AssertionError("Failed to open SauceDemo login page")


@when("I enter valid credentials")
def enter_credentials(context):
    try:
        context.login_page.login("standard_user", "secret_sauce")
        time.sleep(2)  # Allow some time for page transition
    except Exception as e:
        print(f"Error: {e}")
        raise AssertionError("Failed to enter credentials")


@then("I should be redirected to the products page")
def check_redirection(context):
    try:
        assert "inventory.html" in context.driver.current_url, "Login failed, not redirected"
        context.driver.quit()
    except Exception as e:
        print(f"Error: {e}")
        raise AssertionError("Login assertion failed")
