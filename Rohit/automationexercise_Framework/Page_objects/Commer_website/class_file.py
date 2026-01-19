from selenium import webdriver
from selenium.webdriver.common.by import By
from ...Page_objects.Commer_website.locator_file import *
from ...base.selenium_base import Selenium_base
from selenium.webdriver.support.select import Select


class CommerWebsite(Selenium_base):
    def __init__(self, driver):
        print(Selenium_base.__init__)
        super().__init__(driver)

    def launch_url(self, url):
        self.driver.get(url)

    def enter_User_Name(self,use_name):
        self.enter_text(User_Name,use_name)

    def enter_User_Email_address(self,use_email):
        self.enter_text(User_Email_address,use_email)

    def click_signup_button(self):
        self.click_element(User_Signup_btn)

    # Enter Account Information:
    #def click_select_MR(self):
     #   self.click_element(select_MR)
    def click_select_MR(self):
        select_MR = (By.ID, "id_gender1")
        self.click_element(select_MR)

    def enter_password(self,password):
        self.enter_text(Password,password)

    def select_date(self, date_text):
        date_element = self.driver.find_element(By.XPATH, "//select[@data-qa='days']")  # replace with your actual locator
        select = Select(date_element)
        select.select_by_visible_text(date_text)

    def select_month(self,month_text):
        month_element = self.driver.find_element(By.XPATH,"//select[@data-qa='months']")
        select = Select(month_element)
        select.select_by_visible_text(month_text)

    def select_year(self,year_text):
        year_element = self.driver.find_element(By.XPATH, "//select[@data-qa='years']")
        select = Select(year_element)
        select.select_by_visible_text(year_text)

    def click_specail_offer_checkbox(self):
        self.driver.find_element(*specail_offer_checkbox).click()

    def enter_First_Name(self,first_name):
        self.enter_text(First_Name,first_name)

    def enter_Last_Name(self,last_name):
        self.enter_text(Last_Name,last_name)

    def enter_company_name(self,company_name):
        self.enter_text(Company,company_name)

    def enter_address(self,address):
        self.enter_text(Address,address)

    def select_country(self,country_text):
        country_element = self.driver.find_element(By.XPATH, "//input[@data-qa='country']")
        select = Select(country_element)
        select.select_by_visible_text(country_text)

    def enter_state(self,state):
        self.enter_text(State,state)

    def enter_city(self, city):
        self.enter_text(City,city)

    def enter_zipocde(self, zip):
        self.enter_text(Zipcode,zip)

    def enter_mobile(self, mobile):
        self.enter_text(Mobile_number,mobile)

    def click_Create_Account_button(self):
        self.click_element(Create_Account_btn)

    def click_continue_button(self):
        self.click_element(continue_btn)

    def click_logout_button(self):
        self.click_element(Logout_btn)

    # Login to your account
    def enter_Login_email_address(self,email_Add):
        self.enter_text(Login_Email_address,email_Add)

    def enter_Login_Password(self,password):
        self.enter_text(Login_Password,password)

    def click_login_button(self):
        self.click_element(Login_button)

    #Categary
    def click_Men(self):
        self.click_element(Men)

    def click_Tshirt(self):
        self.click_element(Tshirt)

    def click_view_product(self):
        self.click_element(view_product)

    def enter_quantity(self,quantity):
        self.enter_text(Quantity,quantity)

    def click_Add_card_btn(self):
        self.click_element(Add_card_button)

    def click_view_cart_btn(self):
        self.click_element(view_cart_button)

    def click_Proceed_to_checkout_button(self):
        self.click_element(Proceed_to_checkout_btn)

    def enter_Comment_box(self, comment):
        self.enter_text(comment_box,comment)

    def click_Place_order_button(self):
        self.click_element(Place_order_btn)

    def enter_name_on_Card(self, card_name):
        self.enter_text(Name_on_card, card_name)

    def  enter_card_number(self,card_no):
        self.enter_text(card_number,card_no)

    def  enter_CVC(self, cvc):
        self.enter_text(CVC,cvc)

    def enter_Exp_month(self, exp_month):
        self.enter_text(Exp_month,exp_month)

    def  enter_Exp_year(self, exp_year):
        self.enter_text(Exp_year,exp_year)

    def click_pay_confirm_button(self):
        self.click_element(Pay_confirm_btn)

    def click_download_Invoice(self):
        self.click_element(Download_Invoice)

    def click_order_continue_btn(self):
        self.click_element(order_continue)

    #Women
    def click_Polo(self):
        self.click_element(Polo)

    def click_Women(self):
        self.click_element(Women)

    def click_Saree(self):
        self.click_element(Saree)

    def click_Saree_view_product(self):
        self.click_element(Saree_view_product)

    def click_saree_Add_cart(self):
        self.click_element(saree_Add_cart)

    def click_saree_view_cart(self):
        self.click_element(saree_view_cart)

    def  click_saree_proceed_check_out(self):
        self.click_element(saree_proceed_check_out)

    def enter_saree_comment_box(self, comt_box):
        self.enter_text(saree_comment_box, comt_box)

    def click_Saree_Place_order_button(self):
        self.click_element(Saree_Place_order_btn)

    def enter_saree_Name_on_card(self,name_card):
        self.enter_text(saree_Name_on_card, name_card)

    def enter_saree_card_number(self,saree_card_no):
        self.enter_text(saree_card_number,saree_card_no)

    def enter_saree_CVV(self,saree_cvv):
        self.enter_text(saree_CVV,saree_cvv)

    def enter_Saree_Exp_Month(self,saree_exp_month):
        self.enter_text(Saree_Exp_Month,saree_exp_month)

    def enter_Saree_Exp_Year(self,saree_exp_year):
        self.enter_text(Saree_Exp_Year,saree_exp_year)

    def click_Saree_Pay_Confirm_btn(self):
        self.click_element(Saree_Pay_Confirm_btn)

    def click_Saree_Download_Invoice(self):
        self.click_element(Saree_Download_Invoice)

    def click_Saree_Continue(self):
        self.click_element(Saree_Continue)

    # KIDS
    def click_kids(self):
        self.click_element(Kids)

    def click_tops_shirts(self):
        self.click_element(Tops_Shirts)

    def click_to_product(self):
        self.click_element(click_product)

    def click_btn_Add_to_cart(self):
        self.click_element(btn_Add_to_cart)

    def click_view_Cart(self):
        self.click_element(click_view_to_Cart)

    def click_Proceed_to_checkout(self):
        self.click_element(click_Proceed_to_checkout)

    def enter_kid_comments(self,kid_comt):
        self.enter_text(kid_comments,kid_comt)

    def click_Place_order_btn(self):
        self.click_element(kids_Place_order)

    def enter_kids_name_of_Card(self,card_name):
        self.enter_text(Kids_name_of_Card, card_name)

    def enter_kids_card_no(self,card_no):
        self.enter_text(kids_card_no,card_no)

    def enter_kids_cvc(self,kid_cvc):
        self.enter_text(kids_cvc,kid_cvc)

    def enter_kids_Exp_month(self,exp_month):
        self.enter_text(kids_Exp_month,exp_month)

    def enter_kids_Exp_year(self,exp_yrs):
        self.enter_text(kids_Exp_Year,exp_yrs)

    def click_kids_Pay_Confirm_btn(self):
        self.click_element(kids_Pay_Confirm_btn)

    def click_kids_downlaod_invoice(self):
        self.click_element(kids_downlaod_invoice)

    def click_kids_continue_btn(self):
        self.click_element(kids_continue_btn)

























