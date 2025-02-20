from behave import given, when, then
from pages.product_page import ProductPage

@given("I am logged in to SauceDemo")
def login(context):
    context.execute_steps('''
        Given I am on SauceDemo login page
        When I enter valid credentials
    ''')

@when("I add product to the cart")
def add_product(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.add_product_to_cart()

@when("I proceed to checkout")
def checkout(context):
    context.product_page.proceed_to_checkout()

@then("I should see the order confirmation page")
def verify_order(context):
    assert "checkout-step-one.html" in context.driver.current_url, "Order page not reached"
    context.driver.quit()
