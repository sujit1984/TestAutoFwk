from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from pages.login_page import LoginPage
import time

@given('I am on SauceDemo login page')
def open_login_page(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.implicitly_wait(5)

    context.login_page = LoginPage(context.driver)
    context.login_page.open_login_page()

@when("I enter valid credentials")
def enter_credentials(context):
    context.login_page.login("standard_user", "secret_sauce")
    time.sleep(4)  # Wait for potential pop-up

# @when("I click Ok on the pop-up")
# def click_Ok(context):
#     try:
#         alert = context.driver.switch_to.alert  # Switch to alert
#         print(alert.text)  # Print the pop-up message
#         alert.accept()  # Click OK (Use alert.dismiss() to cancel)
#     except:
#         print("No JavaScript alert found.")

@then("I should be redirected to the products page")
def check_redirection(context):
    assert "inventory.html" in context.driver.current_url, "Login failed, not redirected"
    context.driver.quit()
