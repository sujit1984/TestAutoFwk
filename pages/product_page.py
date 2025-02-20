from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_add_button = (By.CLASS_NAME, "btn_inventory")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")

    def add_product_to_cart(self):
        self.driver.find_element(*self.product_add_button).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.cart_button).click()
        self.driver.find_element(*self.checkout_button).click()
