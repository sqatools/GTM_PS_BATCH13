import pytest
from ...Page_objects.Open_HRM_website.Open_HRM_Class import Open_HRM_Login
from ...Page_objects.Open_HRM_website.Open_HRM_data import *

@pytest.mark.usefixtures("get_driver")

class Test_Open_HRM:
    def test_Open_login(self):
        self.ol=Open_HRM_Login()
        self.ol.launch_open_HRM_website(url=website_url)
        self.ol.login_to_open_HRM_website()
