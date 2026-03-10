# Login Page Object Model
# Contains selectors and methods for login page interactions
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "username")
    password = (By.ID, "password")
    submit = (By.ID, "Login")

    def open_url(self):
        self.driver.get("https://ctcorphyd.com/EBanking_build1/admin.php")

    def enter_username(self, user):
        self.driver.find_element(*self.username).send_keys(user)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.Login).click()