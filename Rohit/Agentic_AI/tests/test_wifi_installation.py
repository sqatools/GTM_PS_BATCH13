"""
Verify WiFi Installation Request

AI should assign
nearest field engineer
"""

import pytest

from ..agents.planner_agent import PlannerAgent


class TestWifiInstallation:

    @pytest.mark.sanity
    def test_wifi_installation(self):

        planner = PlannerAgent()

        response = planner.process_ticket({

            "ticket_id": 103,

            "customer_id": 1002,

            "issue": "WiFi Installation",

            "area": "Nashik"

        })

        assert response["status"] == "Assigned"

        assert response["work_order"]["engineer"] is not None

        assert response["work_order"]["eta"] == "2 Hours"