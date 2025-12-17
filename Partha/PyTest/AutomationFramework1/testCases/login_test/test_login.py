import time

import pytest
from ...pageObjects.login_page.login_page_class import LoginPage
from ...pageObjects.login_page.login_page_data import json_file_path, jsn_data
from ...Utilities.util_tools import Util

@pytest.mark.usefixtures("get_driver")
class TestLogin:

    @pytest.fixture(scope= "function", autouse=True)
    def setup_method(self):
        self.lp = LoginPage(self.driver)
        self.util = Util()
        self.json_data = self.util.read_json_data(json_file_path)
        self.lp.launch_login_page(self.json_data["login_url"])

    def test_verify_login_page(self):
        self.lp.enter_username(self.json_data["username"])
        time.sleep(3)
        self.lp.enter_password(self.json_data["password"])
        time.sleep(3)
        self.lp.click_login_button()
        time.sleep(3)

    @pytest.mark.parametrize("user, passwd", jsn_data["users_list"])
    def test_login_parametrization(self, user, passwd):
        self.lp.launch_login_page(self.json_data["login_url"])
        self.lp.enter_username(user)
        time.sleep(1)
        self.lp.enter_password(passwd)
        time.sleep(1)
        self.lp.click_login_button()