from ..services.ticket_service import create_ticket
from ..services.network_service import check_outage, restart_network

def take_action(decision: str) -> dict:

    # ✅ Step 1: Always create ticket
    ticket = create_ticket("Customer Issue")

    # ✅ Step 2: Update ticket based on decision
    if decision == "CHECK_AVAILABILITY":
        ticket["status"] = "Technician Assigned"

    elif decision == "CHECK_OUTAGE":
        if check_outage():
            network_result = restart_network()
            ticket["status"] = network_result["status"]
        else:
            ticket["status"] = "No outage found"

    else:
        ticket["status"] = "Escalated to human"

    # ✅ Step 3: Always return ticket (IMPORTANT)
    return ticket