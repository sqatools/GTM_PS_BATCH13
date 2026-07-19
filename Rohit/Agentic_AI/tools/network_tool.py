"""
Network Tool

Responsible for:
1. Router Status
2. Signal Strength
3. Packet Loss
4. Area Outage
"""

import random


class NetworkTool:

    def router_status(self, router):

        routers = {

            "RTR001": "ONLINE",

            "RTR002": "OFFLINE",

            "RTR003": "ONLINE"

        }

        return routers.get(router, "UNKNOWN")

    def signal_strength(self, area=None):

        if area == "Mumbai":
            return 25

        return random.randint(20, 100)

    def packet_loss(self):

        return random.randint(0, 15)

    def check_area_outage(self, area):

        outage = {

            "Pune": False,

            "Mumbai": True,

            "Nashik": False

        }

        return outage.get(area, False)