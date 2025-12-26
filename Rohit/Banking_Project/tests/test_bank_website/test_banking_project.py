import time

import pytest
from ...Page_objects.Banking_website.banking_class import Banking_website
from ...Page_objects.Banking_website.banking_locator import *
from ...Page_objects.Banking_website.banking_datafile import *
from ...utilities.db_utils import DBUtils

@pytest.mark.usefixtures("get_driver")

class Test_Banking_Website:

    # Admin Login
    def test_Admin_login_functionality(self):
        self.bank = Banking_website(self.driver)
        self.bank.launch_banking_url(url=website_url)
        self.bank.click_Admin_menu()
        self.bank.enter_Admin_Username(Admin_username)
        self.bank.enter_Admin_Password(Admin_Password)
        self.bank.click_Admin_Login()
        time.sleep(10)

    # Add Branches
    def test_Add_Branch_functionality(self):
        self.bank = Banking_website(self.driver)
        self.bank.click_Branch_tab()
        self.bank.click_Add_Branch_sub_menu()
        self.bank.enter_Branch_id(Branch_id)
        self.bank.enter_Branch_Name(Branch_Name)
        self.bank.enter_Branch_Address(Branch_Address)
        self.bank.enter_Branch_city(Branch_City)
        self.bank.enter_Branch_state(Branch_State)
        self.bank.enter_Branch_zipcode(Branch_Zipcode)
        self.bank.enter_Branch_phone(Branch_Phone)
        time.sleep(3)
        self.bank.click_Add_Branch_button()
        time.sleep(5)
        self.bank.verify_sucess_alert("Branch added successfully !!")
        DBUtils.insert_branch(ADD_BRANCH_DATA)
