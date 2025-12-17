import time

import pytest
from ...page_objects.login_page.login_page_class import LoginPage
from ...page_objects.login_page.login_page_data import json_file_path, jsn_data
from ...utilities.utils_tools import Util

@pytest.mark.usefixtures("get_driver_with_headless")
class TestLoginPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.lp = LoginPage(self.driver)
        self.util = Util()
        self.json_data = self.util.read_json_data(json_file_path)
        self.lp.launch_login_page(self.json_data["login_url"])


    def test_verify_login_functionality(self):
        self.lp.enter_username(self.json_data['username'])
        time.sleep(3)
        self.lp.enter_password(self.json_data['password'])
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
        self.driver.save_screenshot("login_page.png")

