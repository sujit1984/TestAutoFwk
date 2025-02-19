from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

@given("I am on the SauceDemo login page")
def open_login_page(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(5)
    context.login_page = LoginPage(context.driver)
    context.login_page.open_login_page()

@when("I enter valid credentials")
def enter_credentials(context):
    context.login_page.login("standard_user", "secret_sauce")

@then("I should be redirected to the products page")
def check_redirection(context):
    assert "inventory.html" in context.driver.current_url
    context.driver.quit()
