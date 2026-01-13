from selenium import webdriver
from selenium.webdriver.common.by import By
from ...Page_objects.Commer_website.locator_file import *
from ...base.selenium_base import Selenium_base
from selenium.webdriver.support.select import Select


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

    # Enter Account Information:
    def click_select_MR(self):
        self.click_element(select_MR)

    def enter_password(self,password):
        self.enter_text(Password,password)

    def select_date(self, date_text):
        date_element = self.driver.find_element(By.XPATH, "//select[@data-qa='days']")  # replace with your actual locator
        select = Select(date_element)
        select.select_by_visible_text(date_text)

    def select_month(self,month_text):
        month_element = self.driver.find_element(By.XPATH,"//select[@data-qa='months']")
        select = Select(month_element)
        select.select_by_visible_text(month_text)

    def select_year(self,year_text):
        year_element = self.driver.find_element(By.XPATH, "//select[@data-qa='years']")
        select = Select(year_element)
        select.select_by_visible_text(year_text)

    def click_specail_offer_checkbox(self):
        self.driver.find_element(*specail_offer_checkbox).click()

    def enter_First_Name(self,first_name):
        self.enter_text(First_Name,first_name)

    def enter_Last_Name(self,last_name):
        self.enter_text(Last_Name,last_name)

    def enter_company_name(self,company_name):
        self.enter_text(Company,company_name)

    def enter_address(self,address):
        self.enter_text(Address,address)

    def select_country(self,country_text):
        country_element = self.driver.find_element(By.XPATH, "//input[@data-qa='country']")
        select = Select(country_element)
        select.select_by_visible_text(country_text)

    def enter_state(self,state):
        self.enter_text(State,state)

    def enter_city(self, city):
        self.enter_text(City,city)

    def enter_zipocde(self, zip):
        self.enter_text(Zipcode,zip)

    def enter_mobile(self, mobile):
        self.enter_text(Mobile_number,mobile)

    def click_Create_Account_button(self):
        self.click_element(Create_Account_btn)

    def click_continue_button(self):
        self.click_element(continue_btn)
