import time
from ..Page_object.class_file import OrangeHRM
from ..Page_object.locator import *
from ..Page_object.data_file import *

import pytest

@pytest.mark.usefixtures('get_driver')

class Test_Orange_website:

    def test_login_functionality(self):
        self.Orange = OrangeHRM(self.driver)
        self.Orange.lanuch_url(url)
        self.Orange.enter_user_name(user_name)
        self.Orange.enter_password(Password)
        self.Orange.click_login()
        time.sleep(10)
