import time

import  pytest

from ..conftest import get_driver
from ...Page_objects.website.website_page import WebsitePage
from ...Page_objects.website.data_file import *

@pytest.mark.usefixtures("get_driver")
class TestWebsite:
    def test_website_verify(self):
        self.wp = WebsitePage(self.driver)
        self.wp.launch_website(url=website_url)
        self.wp.enter_Name(name=Name)
        self.wp.enter_Email(email=Email)
        self.wp.Select_male_radio()
        self.wp.enter_Mobile(mobile=Mobile)
        self.wp.enter_date_of_birth(DOB)
        self.wp.enter_Subjects(subj=Subjects)
        self.wp.select_Hobbies_Sport_checkbox()
        self.wp.upload_file(file_path=r"D:\test_data\text_file.txt")
        self.wp.enter_current_Address(address=Current_Address)
        time.sleep(5)
        self.wp.enter_state(State)
        time.sleep(5)
        self.wp.enter_city(City)
        time.sleep(5)
        self.wp.enter_login_btn()
        time.sleep(10)

