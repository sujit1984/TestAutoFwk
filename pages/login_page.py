from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.password_popup = (By.CLASS_NAME, "some-popup-class")  # Update with actual locator
        self.ok_button = (By.CLASS_NAME, "some-ok-button-class")  # Update with actual locator

    def open_login_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        self.close_password_popup()

    def close_password_popup(self):
        try:
            popup = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.password_popup)
            )
            if popup.is_displayed():
                self.driver.find_element(*self.ok_button).click()
                print("Password change popup detected and closed.")
        except (NoSuchElementException, TimeoutException):
            print("No password change popup found, proceeding normally.")
