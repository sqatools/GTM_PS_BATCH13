# Login Test Cases
# Test suite for login functionality
from automation.pages.login_page import LoginPage


def test_login(driver):

    lp = LoginPage(driver)

    lp.open_url()

    lp.enter_username("admin")

    lp.enter_password("admin")

    lp.click_login()

    assert "Logged In Successfully" in driver.page_source