from ...base.seleium_base import SeleniumBase
from ...Page_objects.banking_website.banking_website_locator import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Banking_Website(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

     #Customer Register
    def launch_banking_website(self, url):
        self.driver.get(url)

    def click_customer_Register(self):
        self.click_element(RegistrationLoc.Customer_Register)

    def enter_First_name(self, first_name):
       self.enter_text(RegistrationLoc.field_First_Name, first_name)

    # def enter_First_name(self, locator, value):
    #     element = self.driver.find_element(*locator)
    #     element.clear()
    #     element.send_keys(value)

    #def enter_Last_name(self,last_name):
     #   self.enter_text(RegistrationLoc.Last_Name_field, last_name)

    def enter_Last_name(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    #def enter_Address(self,address):
     #   self.enter_text(RegistrationLoc.Address_field, address)

    def enter_Address(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    #def enter_City(self,city):
     #   self.enter_text(RegistrationLoc.City_field, city)
    def enter_City(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    #def enter_State(self, state):
     #   self.enter_text(RegistrationLoc.State_field, state)
    def enter_State(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    #def enter_Zip_Code(self, zip_code):
     #   self.enter_text(RegistrationLoc.Zip_Code_field, zip_code)
    def enter_Zip_Code(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    #def enter_Phone(self, phone):
    #    self.enter_text(RegistrationLoc.Phone_field, phone)
    def enter_Phone(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    #def enter_SSN(self, ssn):
    #    self.enter_text(RegistrationLoc.SSN_field, ssn)
    def enter_SSN(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    #def enter_Username(self, username):
    #    self.enter_text(RegistrationLoc.Username_field, username)
    def enter_Username(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    #def enter_Password(self, password):
    #    self.enter_text(RegistrationLoc.Password_field, password)
    def enter_Password(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    #def enter_Confirm_Password(self, confirm_password):
    #    self.enter_text(RegistrationLoc.Confirm_field, confirm_password)
    def enter_Confirm_Password(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def click_Register_button(self):
        self.click_element(RegistrationLoc.Register_btn)

    def click_Logout_button(self):
        self.click_element(RegistrationLoc.Logout_btn)

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
        self.click_element(Open_New_Account.open_New_Account)

    def select_account_type(self,account_type):
        self.select_dropdown_by_visible_text(Open_New_Account.ACCOUNT_TYPE_DROPDOWN, account_type)

    def select_from_account(self,fr_account):
        self.select_dropdown_by_visible_text(Open_New_Account.FROM_ACCOUNT_DROPDOWN,fr_account)


    def click_open_new_account_button(self):
        self.click_element(Open_New_Account.Open_New_Account_btn)

    #Accounts overview
    def Click_Account_Overview_menu(self):
        self.click_element(Account_Overview.account_overview)

    #Funds Transfer
    def click_Fund_Transfer_menu(self):
        self.click_element(Funds_Transfer.transfer_fund)

    def enter_amount(self,locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def select_Funds_From_account(self,Fr_account):
        self.select_dropdown_by_visible_text(Funds_Transfer.From_account, Fr_account)

    def select_Funds_to_account(self,to_account):
        self.select_dropdown_by_visible_text(Funds_Transfer.To_account, to_account)

    def click_transfer_button(self):
        self.click_element(Funds_Transfer.Transfer_btn)


    #Bill Payment Service
    def click_bill_payment_menu(self):
        self.click_element(Bill_Payment_menu)

    def enter_Payee_Name(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_Bill_Address(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_Bill_City(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_Bill_State(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_Bill_Zip_Code(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_Bill_Phone(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_Bill_Account(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_Bill_Verify_Account(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_Bill_Amount(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_Bill_From_account(self,locator, value):
        element = self.driver.find_element(*locator)
        Select(element).select_by_value(value)

    def click_bill_send_payement(self):
        self.click_element(Bill_send_payement)

#Find Transactions
    def click_find_tranasaction_menu(self):
        self.click_element(find_transaction_menu)

    def select_transaction_account(self, locator, value):
        element = self.driver.find_element(*locator)
        element.send_keys(value)

    def enter_find_by_date(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def click_find_date_transaction_button(self):
        self.click_element(find_date_btn)

    def enter_from_transaction_date(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_to_transaction_date(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def click_find_transaction_findbybtn(self):
        self.click_element(Find_date_Range_btn)

    def enter_find_by_amount(self, locator, value):
        element = self.driver.find_element(*locator)
        element.send_keys(value)

    def click_findbyamount_btn(self):
        self.click_element(Find_to_Amount_trans_btn)

    # Update Contact Info
    def click_update_Contact_Info_menu(self):
        self.click_element(Update_Contact_Info_menu)

    def enter_update_first_name(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_update_last_name(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_update_profile_address(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_update_profile_City(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_update_profile_State(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_update_profile_zip_code(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_update_profile_Phone(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def click_update_profile_button(self):
        self.click_element(update_profile_button)

    #Request_Loan
    def click_request_loan_menu(self):
        self.click_element(Request_Loan_Menu)

    def enter_requestloan_loan_amount(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_requestloan_down_payment(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_requestloan_from_account(self, locator, value):
        element = self.driver.find_element(*locator)
        element.send_keys(value)

    def click_requestloan_apply_now_btn(self):
        self.click_element(Requestloan_Apply_Now_btn)

    # Customer Care
    def click_Customer_Care_menu(self):
        self.click_element(customer_care_menu)

    def enter_customer_care_name(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_Customer_Care_Email(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_Customer_Care_Phone(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def enter_Customer_Care_Message(self, locator, value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def click_Send_to_Customer_Care_btn(self):
        self.click_element(Send_to_Customer_Care_btn)

    # ParaSoft Demo Website
    def click_paraSoft_demo_website_menu(self):
        self.click_element(ParaSoft_Website_menu)

    #home_Page
    def click_home_page_menu(self):
        self.click_element(Home_Page_Menu)

    # ParaBank Is Now Re-Opened
    def click_paraBank_Is_Re_open(self):
        self.click_element(ParaBank_menu)

    # New! Online Bill Pay
    def click_new_online_bill_pay(self):
        self.click_element(New_Online_bill_Pay)

    # New! Online Account Transfers
    def click_new_online_account_transfer(self):
        self.click_element(New_online_account_transfer)