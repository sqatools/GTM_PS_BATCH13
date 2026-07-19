"""
Network Agent

Check outage
Check OLT
Check ONU
Check Router
"""


class NetworkAgent:

    def check_network(self, ticket):

        area = ticket["area"]

        outage = {

            "Pune": "UP",

            "Mumbai": "DOWN",

            "Nashik": "UP"

        }

        if outage.get(area) == "DOWN":

            return {

                "status": "DOWN",

                "reason": "Area Outage"

            }

        return {

            "status": "UP"

        }