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

       # Add New Employee
    def test_Add_Employee_functionality(self):
        self.bank = Banking_website(self.driver)
        self.bank.click_Employee_menu()
        self.bank.click_Add_Employee_sub_menu()
        self.bank.select_branch("Yewatmal Branch, 4106")
        time.sleep(3)
        self.bank.enter_Employee_ID(Employee_ID)
        self.bank.enter_employee_first_name(Employee_FirstName)
        self.bank.enter_employee_last_name(Employee_LastName)
        self.bank.enter_Employee_email(Employee_Email)
        self.bank.enter_Employee_phone(Employee_Phone)
        self.bank.enter_Employee_position(Employee_Position)
        self.bank.select_Employee_hire_date(Employee_HireDate)
        self.bank.enter_Employee_password(Employee_Password)
        time.sleep(3)
        self.bank.click_add_employee_button()
        time.sleep(5)
        self.bank.verify_Employee_Add_sucess_alert("New Employee added successfully..!")
        DBUtils.insert_employee(EMPLOYEE_DB_DATA)


    # Delete Employees
    def test_delete_employee_details_functionality(self):
        self.bank = Banking_website(self.driver)
        self.bank.click_Employee_menu()
        self.bank.click_delete_employee()
        self.bank.select_delete_employee_drop_down(Delete_Employee_from_drop_down)
        time.sleep(5)
        self.bank.click_view_button()
        self.bank.click_on_delete_employee_Details_btn()
        time.sleep(3)
        self.bank.verify_make_sure_to_delete_employee_alert("Are you sure you want to delete this employee?")
        time.sleep(3)
        self.bank.verify_employee_delete_successfully_alert(" Employee deleted successfully..!")
        DBUtils.delete_employee_by_id(5516)
        DBUtils.update_employee(5519, UPDATE_EMPLOYEE_DATA)

