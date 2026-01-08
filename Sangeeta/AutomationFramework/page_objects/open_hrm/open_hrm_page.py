from ...basepg.selenium_base import SeleniumBase
from ...page_objects.open_hrm.open_hrm_page_locator import *

class LoginPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(self, driver)

    def launch_url(self):
