"""
Login Page

Functions:
1. Login
2. Verify Login
3. Logout
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    username = (By.ID, "username")

    password = (By.ID, "password")

    login_button = (By.ID, "loginBtn")

    dashboard_text = (By.XPATH, "//h1[text()='Dashboard']")

    logout_button = (By.ID, "logoutBtn")

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    def open_application(self, url):

        self.driver.get(url)

    def login(self, username, password):

        self.wait.until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(username)

        self.driver.find_element(
            *self.password
        ).send_keys(password)

        self.driver.find_element(
            *self.login_button
        ).click()

    def is_login_successful(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.dashboard_text
            )
        ).is_displayed()

    def logout(self):

        self.driver.find_element(
            *self.logout_button
        ).click()