import time
import pytest

from Rohit.mockbank_framework.base.selenium_base import SeleniumBase
from Rohit.mockbank_framework.Page.locator_file import *
from Rohit.mockbank_framework.Page.class_file import MockBankPage
from Rohit.mockbank_framework.Page.data_file import *

@pytest.mark.usefixtures("get_driver")

class Test_MockBank:

    def test_login_functionality(self):
        self.MC = MockBankPage(self.driver)
        self.MC.launch_url(Web_URL)
        self.MC.click_signup()
        time.sleep(5)

