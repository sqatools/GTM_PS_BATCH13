import time

import pytest
from ...Page_objects.banking_website.banking_website_class import Banking_Website
from ...Page_objects.banking_website.banking_data_file import *
from ...Page_objects.banking_website.banking_website_locator import *


@pytest.mark.usefixtures("get_driver")
class TestBankingWebsite:
      #Customer_Register
      def test_Customer_Register_functionality(self):
          self.bw = Banking_Website(self.driver)
          self.bw.launch_banking_website(url=website_url)
          self.bw.enter_First_name(First_Name)
          self.bw.enter_Last_name(Last_Name)
          self.bw.enter_Address(Address)
          self.bw.enter_City(City)
          self.bw.enter_State(State)
          self.bw.enter_Zip_Code(Zip_Code)
          self.bw.enter_Phone(Phone)
          self.bw.enter_SSN(SSN)
          time.sleep(3)
          self.bw.enter_Username(Username)
          self.bw.enter_Password(Password)
          self.bw.enter_Confirm_Password(Confirm)
          self.bw.click_Registration_button()
          time.sleep(5)
          self.bw.click_Logout_button()
          time.sleep(5)

      #customer_login
      def test_customer_login_functionality(self):
          self.bw = Banking_Website(self.driver)
          self.bw.launch_banking_website(url=website_url)
          self.bw.enter_customer_username(Customer_login_Username)
          time.sleep(3)
          self.bw.enter_customer_login_password(Customer_login_Password)
          self.bw.click_customer_login_button()
          time.sleep(5)
          self.bw.click_logout_button()
          time.sleep(5)

      #Customer_forgot_login
      def test_customer_forgot_login_functionality(self):
          self.bw = Banking_Website(self.driver)
          self.bw.launch_banking_website(url=website_url)
          self.bw.click_forgot_login_button()
          self.bw.enter_forgot_login_firstname(forgot_login_FirstName)
          self.bw.enter_forgot_login_lastname(forgot_login_LastName)
          self.bw.enter_forgot_login_address(forgot_login_Address)
          self.bw.enter_forgot_login_city(forgot_login_City)
          self.bw.enter_forgot_login_state(forgot_login_State)
          time.sleep(3)
          self.bw.enter_forgot_login_zip_code(forgot_login_Zip_Code)
          self.bw.enter_forgot_login_ssn(forgot_login_SSN)
          time.sleep(3)
          self.bw.click_find_my_info()
          time.sleep(3)

      #Open_New_Account
      def test_Open_New_Account_functionality(self):
       self.bw = Banking_Website(self.driver)
       self.bw.launch_banking_website(url=website_url)
       self.bw.enter_customer_username(Customer_login_Username)
       self.bw.enter_customer_login_password(Customer_login_Password)
       self.bw.click_customer_login_button()
       time.sleep(3)
       self.bw.click_open_new_account_tab()
       self.bw.select_account_type(Account_type)
       self.bw.select_from_account(from_account)
       time.sleep(3)
       self.bw.click_open_new_account_button()
       time.sleep(3)
