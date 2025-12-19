from ...base.seleium_base import SeleniumBase
from ...Page_objects.banking_website.banking_website_locator import *
from selenium import webdriver

class Banking_Website(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

     #Customer Register
    def launch_banking_website(self, url):
        self.driver.get(url)

    def click_customer_Register(self):
        self.click_element(Customer_Register)

    def enter_First_name(self,first_name):
        self.enter_text(First_Name, first_name)

    def enter_Last_name(self,last_name):
        self.enter_text(Last_Name, last_name)

    def enter_Address(self,address):
        self.enter_text(Address, address)

    def enter_City(self,city):
        self.enter_text(City, city)

    def enter_State(self, state):
        self.enter_text(State, state)

    def enter_Zip_Code(self, zip_code):
        self.enter_text(Zip_Code, zip_code)

    def enter_Phone(self, phone):
        self.enter_text(Phone, phone)

    def enter_SSN(self, ssn):
        self.enter_text(SSN, ssn)

    def enter_Username(self, username):
        self.enter_text(Username, username)

    def enter_Password(self, password):
        self.enter_text(Password, password)

    def enter_Confirm_Password(self, confirm_password):
        self.enter_text(Confirm, confirm_password)

    def click_Register_button(self):
        self.click_element(Register_btn)

    def click_Logout_button(self):
        self.click_element(Logout_btn)

    #Customer_login
    def enter_customer_username(self,cust_username):
        self.enter_text(CUSTOMER_LOGIN_USERNAME, cust_username)

    def enter_customer_login_password(self,cust_password):
        self.enter_text(CUSTOMER_LOGIN_PASSWORD, cust_password)

    def click_customer_login_button(self):
        self.click_element(LOGIN_BUTTON)

    def click_logout_button(self):
        self.click_element(LOGOUT_BUTTON)

    #customer_forgot_login
    def click_forgot_login_button(self):
        self.click_element(forgot_login_btn)

    def enter_forgot_login_firstname(self,forgot_firstname):
        self.enter_text(forgot_login_FirstName, forgot_firstname)

    def enter_forgot_login_lastname(self,forgot_lastname):
        self.enter_text(forgot_login_LastName, forgot_lastname)

    def enter_forgot_login_address(self,forgot_login_address):
        self.enter_text(forgot_login_Address, forgot_login_address)

    def enter_forgot_login_city(self,forgot_login_city):
        self.enter_text(forgot_login_City, forgot_login_city)

    def enter_forgot_login_state(self,forgot_login_state):
        self.enter_text(forgot_login_State, forgot_login_state)

    def enter_forgot_login_zip_code(self,forgot_zip_code):
        self.enter_text(forgot_login_Zip_Code, forgot_zip_code)

    def enter_forgot_login_ssn(self,forgot_login_ssn):
        self.enter_text(forgot_login_SSN, forgot_login_ssn)

    def click_find_my_info(self):
        self.click_element(find_my_login_info_btn)

    # Open_New_Account
    def click_open_new_account_tab(self):
        self.click_element(Open_New_Account)

    def select_account_type(self,account_type):
        self.select_dropdown_value(ACCOUNT_TYPE_DROPDOWN, account_type)

    def select_from_account(self,fr_account):
        self.select_dropdown_value(FROM_ACCOUNT_DROPDOWN,fr_account)

    def click_open_new_account_button(self):
        self.click_element(Open_New_Account_btn)











