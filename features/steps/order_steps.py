from behave import given, when, then
from pages.product_page import ProductPage

@given("I am logged in to SauceDemo")
def login(context):
    context.execute_steps('''
        given I am on the SauceDemo login page
        when I enter valid credentials
    ''')

@when("I add a product to the cart")
def add_product(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.add_product_to_cart()

@when("I proceed to checkout")
def checkout(context):
    context.product_page.proceed_to_checkout()

@then("I should see the order confirmation message")
def verify_order(context):
    assert "checkout-step-one.html" in context.driver.current_url
    context.driver.quit()
