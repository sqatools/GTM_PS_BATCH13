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

    # Add New Employee
    def click_Employee_menu(self):
        self.click_element(Employee_Menu)

    def click_Add_Employee_sub_menu(self):
        self.click_element(Add_Employee_Submenu)

    def select_branch(self, drop_down_branch):
        self.select_dropdown_by_visible_text(Drop_Down_Branch, drop_down_branch)

    #def enter_Employee_ID(self, employee_id):
     #   self.enter_text(Employee_id, employee_id)

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