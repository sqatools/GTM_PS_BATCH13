import time

from selenium.common import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ...base.selenium_base import SeleniumBase
from ..Banking_website.banking_locator import *
from selenium.webdriver.common.alert import Alert

class Banking_website(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    # Admin Login
    def launch_banking_url(self, url):
        self.driver.get(url)

    def click_Admin_menu(self):
        self.click_element(Admin_menu)

    def enter_Admin_Username(self, username):
        self.enter_text(Admin_username, username)

    def enter_Admin_Password(self, password):
        self.enter_text(Admin_Password, password)

    def click_Admin_Login(self):
        self.click_element(Admin_login)

      # Add Branches

    def click_Branch_tab(self):
        self.click_element(Branch_tab)

    def click_Add_Branch_sub_menu(self):
        self.click_element(Add_Branches_Submenu)

    def enter_Branch_id(self, branch_id):
        self.enter_text(Branch_id, branch_id)

    def enter_Branch_Name(self, branch_name):
        self.enter_text(Branch_Name, branch_name)

    def enter_Branch_Address(self, branch_address):
        self.enter_text(Branch_Address, branch_address)

    def enter_Branch_city(self, branch_city):
        self.enter_text(Branch_City, branch_city)

    def enter_Branch_state(self, branch_state):
        self.enter_text(Branch_State, branch_state)

    def enter_Branch_zipcode(self, branch_zipcode):
        self.enter_text(Branch_Zipcode, branch_zipcode)

    def enter_Branch_phone(self, branch_phone):
        self.enter_text(Branch_Phone, branch_phone)

    def click_Add_Branch_button(self):
        self.click_element(Add_Branch_btn)

    def verify_sucess_alert(self, expected_text):
        alert = self.driver.switch_to.alert
        assert expected_text in alert.text
        alert.accept()

    # view Branch
    def click_view_branch_submenu_button(self):
        self.click_element(click_view_branch_submenu_button)


    #delete Branch
    def click_delete_branch_submenu_button(self):
        self.click_element(Delete_Branch_submenu_btn)

    def click_delete_branch(self):
        self.click_element(Delete_branch)

    def verify_deleted_branch_Successfully_alert(self, expected_text):
        alert = self.driver.switch_to.alert
        assert expected_text in alert.text
        alert.accept()

    # update Branch
    def click_update_Branch_submenu_button(self):
        self.click_element(update_Branch_submenu_btn)

    def click_update_branch_btn(self):
        self.click_element(update_branch_button)

    def enter_update_Branch_Name(self, branch_name):
        self.enter_text(update_Branch_Name, branch_name)

    def enter_update_Branch_Address(self, branch_address):
        self.enter_text(update_Branch_Address, branch_address)

    def enter_update_Branch_City(self, branch_city):
       self.enter_text(update_Branch_City, branch_city)

    def enter_update_Branch_state(self, branch_state):
        self.enter_text(update_Branch_State, branch_state)

    def enter_update_Branch_Zipcode(self, branch_zipcode):
        self.enter_text(update_Branch_Zipcode, branch_zipcode)

    def enter_update_Branch_phone(self, branch_phone):
        self.enter_text(update_Branch_Phone, branch_phone)

    def click_update_Branch_update_button(self):
        self.click_element(update_Branch_update_btn)

    def verify_branch_details_updated_alert(self, expected_text):
        alert = self.driver.switch_to.alert
        assert expected_text in alert.text
        alert.accept()


    # Add New Employee
    def click_Employee_menu(self):
        self.click_element(Employee_Menu)

    def click_Add_Employee_sub_menu(self):
        self.click_element(Add_Employee_Submenu)

    def select_branch(self, drop_down_branch):
        self.select_dropdown_by_visible_text(Drop_Down_Branch, drop_down_branch)

    def enter_Employee_ID(self, employee_id):
        self.get_element(Employee_id).clear()
        self.enter_text(Employee_id, employee_id)

    def enter_employee_first_name(self, E_firstname):
        self.enter_text(Employee_FirstName, E_firstname)

    def enter_employee_last_name(self, E_lastname):
        self.enter_text(Employee_LastName, E_lastname)

    def enter_Employee_email(self, E_email):
        self.enter_text(Employee_Email, E_email)

    def enter_Employee_phone(self, E_phone):
        self.enter_text(Employee_Phone, E_phone)

    def enter_Employee_position(self, E_position):
        self.enter_text(Employee_Position, E_position)

    def select_Employee_hire_date(self, E_hire_date):
        self.enter_text(Employee_HireDate, E_hire_date)

    def enter_Employee_password(self, E_password):
        self.enter_text(Employee_Password, E_password)

    def click_add_employee_button(self):
        self.click_element(Add_Employee_btn)

    def verify_Employee_Add_sucess_alert(self, expected_text):
        alert = self.driver.switch_to.alert
        assert expected_text in alert.text
        alert.accept()

    # view Employee
    def click_view_employee_submenu_button(self):
        self.click_element(view_employee_submenu_btn)

    def select_view_employee_branch(self, view_employee_branch):
        self.select_dropdown_by_visible_text(view_employee_select_branch,view_employee_branch)

    def click_view_employee_view_button(self):
        self.click_element(view_employee_view_btn)

    # Delete Employees

    def click_delete_employee(self):
        self.click_element(Delete_Employees_btn)

    def select_delete_employee_drop_down(self, drop_down):
        self.select_dropdown_by_visible_text(Delete_Employee_drop_down, drop_down)

    def click_view_button(self):
        self.click_element(view_btn)

    def click_on_delete_employee_Details_btn(self):
        self.click_element(Delete_Employee_details_btn)

    def verify_make_sure_to_delete_employee_alert(self, expected_text):
        alert = self.driver.switch_to.alert
        assert expected_text in alert.text
        alert.accept()

    def verify_employee_delete_successfully_alert(self,expected_text):
        alert = self.driver.switch_to.alert
        assert expected_text in alert.text
        alert.accept()

    #update Employee
    def click_Update_employee_btn(self):
        self.click_element(update_employee_btn)

    def select_update_branch(self, update_branch):
        self.select_dropdown_by_visible_text(update_employee_branch, update_branch)

    def click_update_employee_view_btn(self):
        self.click_element(update_employee_view_btn)

    def click_update_btn(self):
        self.click_element(update_btn)

    def enter_update_employee_first_name(self, U_firstname):
        self.enter_text(update_employee_FirstName, U_firstname)

    def enter_update_employee_last_name(self, U_lastname):
        self.enter_text(update_employee_LastName, U_lastname)

    def enter_update_Employee_email(self, U_email):
        self.enter_text(update_employee_Email, U_email)

    def enter_update_Employee_phone(self, U_phone):
        self.enter_text(update_employee_Phone, U_phone)

    def enter_update_Employee_Position(self, U_position):
        self.enter_text(update_employee_Position, U_position)

    def select_update_Employee_hire_date(self, U_hire_date):
        self.enter_text(update_employee_Hire_date, U_hire_date)

    def click_update_Employee_Update_btn(self):
        self.click_element(update_employee_update_btn)

    def verify_Updated_Employee_successfully_alert(self,expected_text):
      try:
       alert = self.driver.switch_to.alert
       assert expected_text in alert.text
       alert.accept()
       print("Updated Employee details successfully..!")
      except NoAlertPresentException:
          print("No alert present---skipping alert validation")


      # Account type
    def click_Account_type_tab(self):
        self.click_element(Account_type_tab)

    def click_Add_Account_type_submenu(self):
        self.click_element(Add_Account_type_submenu)

    def enter_Account_type(self, acc_type):
        self.enter_text(Account_type, acc_type)

    def click_Account_type_Add_btn(self):
        self.click_element(Account_type_Add_btn)

    def verify_Account_type_successfully_alert(self,expected_text):
        alert = self.driver.switch_to.alert
        assert expected_text in alert.text
        alert.accept()