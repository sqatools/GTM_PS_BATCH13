"""
Ticket Page

Functions:
1. Create Ticket
2. Assign L1
3. Escalate to L2
4. Assign Field Engineer
5. Close Ticket
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TicketPage:

    issue_dropdown = (By.ID, "issueType")

    description = (By.ID, "description")

    create_ticket = (By.ID, "createTicket")

    ticket_number = (By.ID, "ticketId")

    assign_l1 = (By.ID, "assignL1")

    assign_l2 = (By.ID, "assignL2")

    assign_engineer = (By.ID, "assignEngineer")

    close_ticket = (By.ID, "closeTicket")

    ticket_status = (By.ID, "ticketStatus")

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    def create_new_ticket(self, issue, details):

        self.wait.until(
            EC.visibility_of_element_located(
                self.issue_dropdown
            )
        ).send_keys(issue)

        self.driver.find_element(
            *self.description
        ).send_keys(details)

        self.driver.find_element(
            *self.create_ticket
        ).click()

    def get_ticket_id(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.ticket_number
            )
        ).text

    def assign_to_l1(self):

        self.driver.find_element(
            *self.assign_l1
        ).click()

    def assign_to_l2(self):

        self.driver.find_element(
            *self.assign_l2
        ).click()

    def assign_field_engineer(self):

        self.driver.find_element(
            *self.assign_engineer
        ).click()

    def close_current_ticket(self):

        self.driver.find_element(
            *self.close_ticket
        ).click()

    def get_ticket_status(self):

        return self.driver.find_element(
            *self.ticket_status
        ).text