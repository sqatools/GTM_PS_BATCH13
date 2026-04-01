from ...Base.Selenium_Base import *
from ...Page_object.Para_bank.Para_data_file import *
from ...Page_object.Para_bank.Para_locator_File import *


class Para_bank(Selenium_Base):
    def __init__(self,driver):
        super().__init__(driver)

    #Register
    def launch_Para_bank_url(self):
        self.driver.get(Para_bank_url)

    def click_on_Register_Button(self):
        self.click_element(Register_menu)

    def enter_First_name(self,first_name):
        self.enter_text(First_Name, first_name)

    def enter_Last_name(self,last_name):
        self.enter_text(Last_Name, last_name)

    def enter_Address(self,address):
        self.enter_text(Address, address)

    def enter_City(self,city):
        self.enter_text(City, city)

    def enter_State(self,state):
        self.enter_text(State, state)

    def enter_Zip_code(self,zip_code):
        self.enter_text(Zip_code, zip_code)

    def enter_Phone(self,phone):
        self.enter_text(Phone, phone)

    def enter_SSN(self,ssn):
        self.enter_text(SSN, ssn)

    def enter_Username(self,username):
        self.enter_text(Username, username)

    def enter_Password(self,password):
        self.enter_text(Password, password)

    def enter_Confirm(self,confirm):
        self.enter_text(Confirm, confirm)

    def click_Register_button(self):
        self.click_element(Register_btn)

    # Customer Login
    def enter_loginUser_name(self,loginuser_name):
        self.enter_text(User_name, loginuser_name)

    def enter_loginPassword(self,loginpassword):
        self.enter_text(password, loginpassword)

    def click_Login_button(self):
        self.click_element(Login_btn)

