from ...base.Naukriselenium import NaukriSelenium
from ...Page_objects.naukri_flow.naukri_locator import *
from ...Page_objects.naukri_flow.naukri_datafile import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Automation(NaukriSelenium):
    def __init__(self,driver):
        super().__init__(driver)

    def launch_naukri_url(self):
        self.driver.get(Naukri_Url)

    def click_naulkri_login(self):
        self.click_element(Login_btn)

    def enter_naukri_username(self,nkusername):
        self.enter_text(Naukri_User_name,nkusername)

    def enter_naukri_password(self,nkpassword):
        self.enter_text(Naukri_Password,nkpassword)

    def click_naukri_loginbtn(self):
        self.click_element(Naukri_login_btn)


    def click_on_serach_button(self):
        self.click_element(click_srch_btn)

    def enter_keyword(self,keyword):
        self.enter_text(Enter_Keyword,keyword)

    def click_select_experience(self):
        self.click_element(click_Select_experience)

    def select_years_from_drop_down(self, select_years_dp, value):
        self.get_element(select_years_dp).click()

        option_xpath = f"//*[contains(@title,'{value}')]"

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()

    def enter_location(self,location):
        self.enter_text(Enter_location,location)

    def click_serach_btn(self):
        self.click_element(Click_Serach_btn)