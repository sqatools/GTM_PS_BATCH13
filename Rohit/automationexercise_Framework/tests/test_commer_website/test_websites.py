import time

import pytest
from ...Page_objects.Commer_website.locator_file import *
from ...Page_objects.Commer_website.data_file import *
from ...Page_objects.Commer_website.class_file import CommerWebsite



@pytest.mark.usefixtures("get_driver_with_headless")
class Test_Commer_Website:

    def test_Signup_functionality(self):
        self.comm = CommerWebsite(self.driver)
        self.comm.launch_url(url="https://automationexercise.com/login")
        self.comm.enter_User_Name(User_Name)
        self.comm.enter_User_Email_address(User_Email_address)
        self.comm.click_signup_button()
        self.comm.click_select_MR()
        self.comm.enter_password(Password)
        self.comm.select_date(Date)
        self.comm.select_month(Month)
        self.comm.select_year(Year)
        self.comm.click_specail_offer_checkbox()
        self.comm.enter_First_Name(First_Name)
        self.comm.enter_Last_Name(Last_Name)
        self.comm.enter_company_name(Company)
        self.comm.enter_address(Address)
        # self.comm.select_country(Country)
        self.comm.enter_state(State)
        self.comm.enter_city(City)
        self.comm.enter_zipocde(Zipcode)
        self.comm.enter_mobile(Mobile_number)
        self.comm.click_Create_Account_button()
        self.comm.click_continue_button()
        self.comm.click_logout_button()


    def test_login_functionality(self):
        self.comm = CommerWebsite(self.driver)
        self.comm.enter_Login_email_address(Login_Email_address)
        self.comm.enter_Login_Password(Login_Password)
        self.comm.click_login_button()


    def test_category_functionality(self):
        self.comm=CommerWebsite(self.driver)
        self.comm.click_Men()
        self.comm.click_Tshirt()
        self.comm.click_view_product()
        #self.comm.enter_quantity(Quantity)
        self.comm.click_Add_card_btn()
        self.comm.click_view_cart_btn()
        self.comm.click_Proceed_to_checkout_button()
        self.comm.enter_Comment_box(comment_box)
        self.comm.click_Place_order_button()
        self.comm.enter_name_on_Card(Name_on_card)
        self.comm.enter_card_number(card_number)
        self.comm.enter_CVC(CVC)
        self.comm.enter_Exp_month(Exp_month)
        self.comm.enter_Exp_year(Exp_year)
        self.comm.click_pay_confirm_button()
        self.comm.click_download_Invoice()
        self.comm.click_order_continue_btn()


    def test_women_functionality(self):
        self.comm = CommerWebsite(self.driver)
        self.comm.click_Polo()
        self.comm.click_Women()
        self.comm.click_Saree()
        self.comm.click_Saree_view_product()
        self.comm.click_saree_Add_cart()
        self.comm.click_saree_view_cart()
        self.comm.click_saree_proceed_check_out()
        self.comm.enter_saree_comment_box(saree_comment_box)
        self.comm.click_Saree_Place_order_button()
        self.comm.enter_saree_Name_on_card(saree_Name_on_card)
        self.comm.enter_saree_card_number(saree_card_number)
        self.comm.enter_saree_CVV(saree_CVV)
        self.comm.enter_Saree_Exp_Month(Saree_Exp_Month)
        self.comm.enter_Saree_Exp_Year(Saree_Exp_Year)
        self.comm.click_Saree_Pay_Confirm_btn()
        self.comm.click_Saree_Download_Invoice()
        self.comm.click_Saree_Continue()


    def test_Kids_functionality(self):
        self.comm = CommerWebsite(self.driver)
        self.comm.click_kids()
        self.comm.click_tops_shirts()
        self.comm.click_to_product()
        self.comm.click_btn_Add_to_cart()
        self.comm.click_view_Cart()
        self.comm.click_Proceed_to_checkout()
        self.comm.enter_kid_comments(kids_comments)
        self.comm.click_Place_order_btn()
        self.comm.enter_kids_name_of_Card(Kid_name_of_Card)
        self.comm.enter_kids_card_no(kid_card_no)
        self.comm.enter_kids_cvc(kid_cvc)
        self.comm.enter_kids_Exp_month(kids_Exp_months)
        self.comm.enter_kids_Exp_year(kids_Exp_Years)
        self.comm.click_kids_Pay_Confirm_btn()
        self.comm.click_kids_downlaod_invoice()
        self.comm.click_kids_continue_btn()

