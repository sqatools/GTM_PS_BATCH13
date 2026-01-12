from selenium import webdriver
from selenium.webdriver.common.by import By
from ...Page_objects.Commer_website.locator_file import *
from ...base.selenium_base import Selenium_base


class CommerWebsite(Selenium_base):
    def __init__(self, driver):
        print(Selenium_base.__init__)
        super().__init__(driver)

    def launch_url(self, url):
        self.driver.get(url)

    def enter_User_Name(self,use_name):
        self.enter_text(User_Name,use_name)

    def enter_User_Email_address(self,use_email):
        self.enter_text(User_Email_address,use_email)

    def click_signup_button(self):
        self.click_element(User_Signup_btn)
