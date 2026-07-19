"""
Test Case

Verify L1 resolves customer issue without escalation
"""

import pytest

from ..pages.login_page import LoginPage
from ..pages.dashboard_page import DashboardPage
from ..pages.ticket_page import TicketPage

from ..agents.planner_agent import PlannerAgent


class TestL1Flow:

    @pytest.mark.smoke
    def test_l1_support_flow(self, driver):

        login = LoginPage(driver)

        dashboard = DashboardPage(driver)

        ticket = TicketPage(driver)

        planner = PlannerAgent()

        login.open_application("https://telecom-demo.com")

        login.login("admin", "admin123")

        assert login.is_login_successful()

        dashboard.search_customer("1001")

        dashboard.open_ticket_module()

        ticket.create_new_ticket(

            "TV Channel Issue",

            "TV channels not loading"

        )

        response = planner.process_ticket({

            "ticket_id": 101,

            "customer_id": 1001,

            "issue": "TV Channel Issue",

            "area": "Pune"

        })

        assert response["status"] == "Resolved"

        assert response["assigned"] == "L1"