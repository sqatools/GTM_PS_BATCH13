"""
CRM Tool

Responsible for:
1. Get Customer Details
2. Get Active Plan
3. Get Installation Status
4. Get Previous Tickets
"""

class CRMTool:

    def __init__(self):

        self.customers = {

            1001: {

                "name": "Rahul",

                "router": "RTR001",

                "plan": "Fiber 200 Mbps",

                "installation": "Completed"

            },

            1002: {

                "name": "Rohit",

                "router": "RTR002",

                "plan": "Fiber 100 Mbps",

                "installation": "Pending"

            }

        }

    def get_customer(self, customer_id):

        return self.customers.get(

            customer_id,

            {

                "status": "Customer Not Found"

            }

        )

    def get_active_plan(self, customer_id):

        customer = self.get_customer(customer_id)

        return customer.get("plan")

    def get_installation_status(self, customer_id):

        customer = self.get_customer(customer_id)

        return customer.get("installation")