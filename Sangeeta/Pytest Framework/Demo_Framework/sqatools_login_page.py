import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from basepage import Base_Page
from sqatools_locator import *

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

class SqaBookingPage(Base_Page):
    def __init__(self, driver):
        super.__init__(driver)

    def launch_website(self, url):
        self.get_driver(url)

    def enter_from_city(self, from_city):
        self.enter_text(from_city_field, from_city)

    def enter_destination_city(self, to_city):
        self.enter_text(dest_city_field, to_city)

    def enter_billing_name(self, bill_name):
        self.enter_text(billing_name_field, bill_name)

