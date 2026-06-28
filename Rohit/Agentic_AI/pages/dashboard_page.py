"""
Dashboard Page

Functions:
1. Search Customer
2. View Network Status
3. Open Ticket Module
4. View Dashboard Metrics
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    search_box = (By.ID, "customerSearch")

    search_button = (By.ID, "searchBtn")

    customer_name = (By.ID, "customerName")

    network_status = (By.ID, "networkStatus")

    ticket_menu = (By.ID, "ticketMenu")

    outage_count = (By.ID, "outageCount")

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    def search_customer(self, customer_id):

        self.wait.until(
            EC.visibility_of_element_located(
                self.search_box
            )
        ).clear()

        self.driver.find_element(
            *self.search_box
        ).send_keys(customer_id)

        self.driver.find_element(
            *self.search_button
        ).click()

    def get_customer_name(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.customer_name
            )
        ).text

    def get_network_status(self):

        return self.driver.find_element(
            *self.network_status
        ).text

    def open_ticket_module(self):

        self.driver.find_element(
            *self.ticket_menu
        ).click()

    def get_outage_count(self):

        return self.driver.find_element(
            *self.outage_count
        ).text