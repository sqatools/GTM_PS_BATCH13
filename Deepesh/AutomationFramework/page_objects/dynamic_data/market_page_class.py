from selenium.webdriver.common.by import By
from ...base.selenium_base import SeleniumBase

class MarketPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_nse_website(self, url):
        self.driver.get(url)

    def get_market_turnover_value(self, row_num=1):
        table_row = (By.XPATH, f"//div[@class='market_turnover']//table/tbody/tr[{row_num}]/td")
        table_row_elements = self.get_elements_list(table_row)
        data_list = [col.text for col in table_row_elements]
        return data_list



