"""
Verify Internet Down issue
is automatically escalated to L2
"""

import pytest

from ..agents.planner_agent import PlannerAgent


class TestL2Flow:

    @pytest.mark.regression
    def test_l2_support_flow(self):

        planner = PlannerAgent()

        response = planner.process_ticket({

            "ticket_id": 102,

            "customer_id": 1002,

            "issue": "Internet Down",

            "area": "Mumbai"

        })

        assert response["status"] == "Escalated"

        assert response["assigned"] == "Field Engineer"