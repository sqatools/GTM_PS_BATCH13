from selenium.webdriver.common.by import By

class LoginPage:

    username = (By.ID, "username")
    password = (By.ID, "password")
    submit = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.submit).click()