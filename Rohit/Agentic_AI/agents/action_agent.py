from pages.login_page import LoginPage

class ActionAgent:

    def __init__(self, driver):
        self.page = LoginPage(driver)

    def execute(self, step):

        if step == "open_login_page":
            self.page.open()

        elif step == "enter_username":
            self.page.enter_username("student")

        elif step == "enter_password":
            self.page.enter_password("Password123")

        elif step == "click_login":
            self.page.click_login()