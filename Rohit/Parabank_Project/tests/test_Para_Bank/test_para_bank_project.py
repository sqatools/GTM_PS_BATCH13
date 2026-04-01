import time

import pytest
from ...Base.Selenium_Base import Selenium_Base
from ...Page_object.Para_bank.Para_locator_File import *
from ...Page_object.Para_bank.Para_data_file import *
from ...Page_object.Para_bank.Para_class_File import Para_bank

@pytest.mark.usefixtures("get_driver")

class Test_Para_Bank_Website:

      def test_Registration_functionality(self):
          self.Para_bank = Para_bank(self.driver)
          self.Para_bank.launch_Para_bank_url()
          self.Para_bank.click_on_Register_Button()
          self.Para_bank.enter_First_name(FirstName)
          self.Para_bank.enter_Last_name(LastName)
          self.Para_bank.enter_Address(address)
          self.Para_bank.enter_City(city)
          self.Para_bank.enter_State(state)
          self.Para_bank.enter_Zip_code(zipcode)
          self.Para_bank.enter_Phone(phone)
          self.Para_bank.enter_SSN(ssn)
          self.Para_bank.enter_Username(username)
          self.Para_bank.enter_Password(password)
          self.Para_bank.enter_Confirm(Confirm)
          self.Para_bank.click_Register_button()


      def test_customer_login_functionality(self):
          self.Para_bank = Para_bank(self.driver)
          self.Para_bank.enter_loginUser_name(User_name)
          self.Para_bank.enter_loginPassword(Password)
          self.Para_bank.click_Login_button()
          time.sleep(10)