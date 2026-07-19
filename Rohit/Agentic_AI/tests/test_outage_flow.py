"""
Verify Area Outage

AI should bypass L1

Directly assign L2
"""

import pytest

from ..agents.planner_agent import PlannerAgent


class TestOutageFlow:

    @pytest.mark.regression
    def test_area_outage(self):

        planner = PlannerAgent()

        response = planner.process_ticket({

            "ticket_id": 104,

            "customer_id": 1001,

            "issue": "Internet Down",

            "area": "Mumbai"

        })

        assert response["status"] == "Escalated"

        assert response["assigned"] == "Field Engineer"