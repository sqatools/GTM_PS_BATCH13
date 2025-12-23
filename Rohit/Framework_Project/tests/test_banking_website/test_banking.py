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
        self.bw.enter_First_name(first_name="Rohit")
        self.bw.enter_Last_name(RegistrationLoc.Last_Name_field,"More")
        self.bw.enter_Address(RegistrationLoc.Address_field,"490B,Mohan Apartment, Shaniwar Peth, Satara")
        self.bw.enter_City(RegistrationLoc.City_field,"Karad")
        self.bw.enter_State(RegistrationLoc.State_field,"Maharastra")
        self.bw.enter_Zip_Code(RegistrationLoc.Zip_Code_field,"411039")
        self.bw.enter_Phone(RegistrationLoc.Phone_field,"8900345678")
        self.bw.enter_SSN(RegistrationLoc.SSN_field,"654890763")
        time.sleep(3)
        self.bw.enter_Username(RegistrationLoc.Username_field,"Mahesh91")
        self.bw.enter_Password(RegistrationLoc.Password_field,"Karad@123")
        self.bw.enter_Confirm_Password(RegistrationLoc.Confirm_field,"Karad@123")
        self.bw.click_Registration_button(RegistrationLoc.Register_btn)
        time.sleep(1)
        self.bw.click_Logout_button()
        time.sleep(1)

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

       # Open_New_Account
    def test_Open_New_Account_functionality(self):
        self.bw = Banking_Website(self.driver)
        self.bw.launch_banking_website(url=website_url)
        self.bw.enter_customer_username(Customer_login_Username)
        self.bw.enter_customer_login_password(Customer_login_Password)
        self.bw.click_customer_login_button()
        time.sleep(3)
        self.bw.click_open_new_account_tab()
        self.bw.select_account_type("SAVINGS")
        # self.bw.select_from_account(Open_New_Account.FROM_ACCOUNT_DROPDOWN)
        time.sleep(3)
        self.bw.click_open_new_account_button()
        time.sleep(3)


    #Account_Overview
    def test_Account_Overview(self):
            self.bw = Banking_Website(self.driver)
            self.bw.Click_Account_Overview_menu()
            time.sleep(5)

    #Funds Transfer
    def test_Funds_Transfer_functionality(self):
           self.bw = Banking_Website(self.driver)
           self.bw.click_Fund_Transfer_menu()
           time.sleep(3)
           self.bw.enter_amount(Funds_Transfer.Amount,"100")
           time.sleep(3)
           self.bw.select_Funds_From_account("19005")
           time.sleep(3)
           self.bw.select_Funds_to_account("19671")
           time.sleep(3)
           self.bw.click_transfer_button()
           time.sleep(3)

           #Bill Payment Service
    def test_Bill_Payement_Service_functionality(self):
           self.bw = Banking_Website(self.driver)
           self.bw.click_bill_payment_menu()
           self.bw.enter_Payee_Name(Payee_Name,"Rohit Chavan")
           self.bw.enter_Bill_Address(Bill_Address,"45A Shaniwar Peth")
           self.bw.enter_Bill_City(Bill_City,"Karad")
           self.bw.enter_Bill_State(Bill_State,"Maharastra")
           self.bw.enter_Bill_Zip_Code(Bill_Zip_Code,"415110")
           self.bw.enter_Bill_Phone(Bill_Phone,"9087543212")
           self.bw.enter_Bill_Account(Bill_Account,"19005")
           self.bw.enter_Bill_Verify_Account(Verify_Account,"19005")
           self.bw.enter_Bill_Amount(Bill_Amount,"50")
           time.sleep(5)
           self.bw.enter_Bill_From_account(Bill_From_account,"19671")
           time.sleep(3)
           self.bw.click_bill_send_payement()
           time.sleep(3)


           # Find Transactions
    def test_find_transaction_functioanlity(self):
           self.bw = Banking_Website(self.driver)
           self.bw.click_find_tranasaction_menu()
           self.bw.select_transaction_account(Select_an_account,"19005")
           time.sleep(3)
           self.bw.enter_find_by_date(Find_by_Date,"12-20-2025")
           time.sleep(3)
           self.bw.click_find_date_transaction_button()
           time.sleep(5)
           self.bw.click_find_tranasaction_menu()
           time.sleep(3)
           self.bw.enter_from_transaction_date(Find_by_from_Date_Range,"12-20-2025")
           self.bw.enter_to_transaction_date(Find_by_to_Date_Range,"12-23-2025")
           time.sleep(3)
           self.bw.click_find_transaction_findbybtn()
           time.sleep(3)
           self.bw.click_find_tranasaction_menu()
           time.sleep(3)
           self.bw.enter_find_by_amount(Find_by_Amount,"100")
           time.sleep(3)
           self.bw.click_findbyamount_btn()
           time.sleep(5)


           # Update Contact Info
    def test_update_contact_info_functioanlity(self):
           self.bw = Banking_Website(self.driver)
           self.bw.click_update_Contact_Info_menu()
           self.bw.enter_update_first_name(update_First_Name,"Rahul")
           self.bw.enter_update_last_name(update_profile_Last_Name,"Chavan")
           self.bw.enter_update_profile_address(update_profile_Address,"Near Alankar sangam")
           self.bw.enter_update_profile_City(update_profile_City,"Mumbai")
           self.bw.enter_update_profile_State(update_profile_State,"Maharastra")
           self.bw.enter_update_profile_zip_code(update_profile_zip_code,"411028")
           self.bw.enter_update_profile_Phone(update_profile_Phone,"8190378002")
           time.sleep(5)
           self.bw.click_update_profile_button()
           time.sleep(5)

           # Request_Loan
    def test_Request_Loan_functioanlity(self):
           self.bw = Banking_Website(self.driver)
           self.bw.click_request_loan_menu()
           self.bw.enter_requestloan_loan_amount(Requestloan_Loan_Amount,"1000")
           self.bw.enter_requestloan_down_payment(Requestloan_Down_Payment,"200")
           self.bw.enter_requestloan_from_account(Requestloan_From_account,"19005")
           self.bw.click_requestloan_apply_now_btn()

           # Customer Care
    def test_customer_Care_functionality(self):
           self.bw = Banking_Website(self.driver)
           self.bw.click_Customer_Care_menu()
           self.bw.enter_customer_care_name(Customer_Care_Name,"Mohan Singh")
           self.bw.enter_Customer_Care_Email(Customer_Care_Email,"dheerajchavan@gmail.com")
           self.bw.enter_Customer_Care_Phone(Customer_Care_Phone,"6534890765")
           time.sleep(5)
           self.bw.enter_Customer_Care_Message(Customer_Care_Message,"Learning Python scripting mailing message")
           self.bw.click_Send_to_Customer_Care_btn()
           time.sleep(5)

           # ParaSoft Demo Website
    def test_Parasoft_Demo_website(self):
           self.bw =Banking_Website(self.driver)
           self.bw.click_paraSoft_demo_website_menu()
           time.sleep(5)

           #Home_Page
    def test_Home_Page_functionality(self):
         self.bw = Banking_Website(self.driver)
         self.bw.click_home_page_menu()
         time.sleep(5)

         # ParaBank Is Now Re-Opened
    def test_ParaBank_Is_Re_open_functionality(self):
           self.bw = Banking_Website(self.driver)
           self.bw.click_paraBank_Is_Re_open()
           time.sleep(5)
           self.driver.back()
           time.sleep(5)

           # New! Online Bill Pay
    def test_New_Online_Bill_Pay_Functionality(self):
           self.bw = Banking_Website(self.driver)
           self.bw.click_new_online_bill_pay()
           time.sleep(5)
           self.driver.back()
           time.sleep(5)

           # New! Online Account Transfers
    def test_online_Account_Transfer_Functionality(self):
           self.bw = Banking_Website(self.driver)
           self.bw.click_new_online_account_transfer()
           time.sleep(5)
           self.driver.back()
           self.driver.forward()
           time.sleep(3)
           self.driver.back()
           time.sleep(5)