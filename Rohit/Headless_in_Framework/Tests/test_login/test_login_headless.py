import time

import pytest

from ...Page_objects.login_page_class import login_Page
from ...Utilities.utils_tools import Utils
from ...Page_objects.login_data import json_file_path,jsn_data

@pytest.mark.usefixtures("get_driver_with_headless")
class Test_login:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.lp =login_Page(self.driver)
        self.utils = Utils()
        self.json_data = self.utils.read_json_data(json_file_path)
        self.lp.launch_login_page(self.json_data["login_url"])

    def test_veify_login(self):
        self.lp.user_name(self.json_data["Username"])
        self.lp.user_password(self.json_data["Password"])
        time.sleep(3)
        self.lp.click_submit()
        self.lp.click_contact_tab()
        time.sleep(3)
        self.lp.enter_First_name(self.json_data["First_name"])
        self.lp.enter_Last_name(self.json_data["Last_name"])
        self.lp.enter_email(self.json_data["Email"])
        time.sleep(3)
        self.lp.enter_message(self.json_data["Message"])
        time.sleep(3)
        self.lp.click_contact_Submit()
        time.sleep(3)

# python -m pytest -v --browser_name=chrome --headless=False  .\Tests\test_login\
# python -m pytest -v --browser_name=chrome --headless=True  .\Tests\test_login\