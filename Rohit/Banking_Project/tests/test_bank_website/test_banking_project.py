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

    # view Branch
    def test_view_branch_details_functionality(self):
        self.bank = Banking_website(self.driver)
        self.bank.click_Branch_tab()
        self.bank.click_view_branch_submenu_button()
        time.sleep(5)

    # delete Branch
    def test_delete_branch_functionality(self):
        self.bank = Banking_website(self.driver)
        self.bank.click_Branch_tab()
        self.bank.click_delete_branch_submenu_button()
        self.bank.click_delete_branch()
        self.bank.verify_deleted_branch_Successfully_alert("Branch Details Deleted Successfully..!")
        time.sleep(5)

    # update Branch
    def test_update_branch_functionality(self):
        self.bank = Banking_website(self.driver)
        self.bank.click_Branch_tab()
        self.bank.click_update_Branch_submenu_button()
        self.bank.click_update_branch_btn()
        self.bank.enter_update_Branch_Name(update_Branch_Name)
        self.bank.enter_update_Branch_Address(update_Branch_Address)
        self.bank.enter_update_Branch_City(update_Branch_City)
        self.bank.enter_update_Branch_state(update_Branch_State)
        self.bank.enter_update_Branch_Zipcode(update_Branch_Zipcode)
        self.bank.enter_update_Branch_phone(update_Branch_Phone)
        self.bank.click_update_Branch_update_button()
        time.sleep(3)
        self.bank.verify_branch_details_updated_alert("Branch Details Updated Successfully..!")
        time.sleep(5)

       # Add New Employee
    def test_Add_Employee_functionality(self):
        self.bank = Banking_website(self.driver)
        time.sleep(3)
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

    def test_view_employee_details_functionality(self):
        self.bank = Banking_website(self.driver)
        time.sleep(3)
        self.bank.click_Employee_menu()
        self.bank.click_view_employee_submenu_button()
        self.bank.select_view_employee_branch(view_employee_select_branch)
        self.bank.click_view_employee_view_button()
        time.sleep(5)


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
        DBUtils.delete_employee_by_id(5593)
        DBUtils.update_employee(5594, UPDATE_EMPLOYEE_DATA)

     # update Employee
    def test_update_Employee_Branch_functionality(self):
        self.bank = Banking_website(self.driver)
        self.bank.click_Employee_menu()
        self.bank.click_Update_employee_btn()
        self.bank.select_update_branch(update_employee_branch)
        self.bank.click_update_employee_view_btn()
        self.bank.click_update_btn()
        self.bank.enter_update_employee_first_name(update_employee_FirstName)
        self.bank.enter_update_employee_last_name(update_employee_LastName)
        self.bank.enter_update_Employee_email(update_employee_Email)
        self.bank.enter_update_Employee_phone(update_employee_Phone)
        self.bank.enter_update_Employee_Position(update_employee_Position)
        self.bank.select_update_Employee_hire_date(update_employee_Hire_date)
        time.sleep(5)
        self.bank.click_update_Employee_Update_btn()
        self.bank.verify_Updated_Employee_successfully_alert("Updated Employee details successfully..!")
        time.sleep(5)

    # Account type
    def test_Account_types_functionality(self):
        self.bank = Banking_website(self.driver)
        self.bank.click_Account_type_tab()
        self.bank.click_Add_Account_type_submenu()
        self.bank.enter_Account_type(Account_type)
        self.bank.click_Account_type_Add_btn()
        time.sleep(5)
        self.bank.verify_Account_type_successfully_alert("Account Type added successfully !!")
        time.sleep(5)
   




        





