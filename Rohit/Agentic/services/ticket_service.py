import requests
import uuid

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

HEADERS = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Content-Type": "application/json"
}

def create_ticket(service_type: str) -> dict:
    payload = {
        "title": f"{service_type} Issue",
        "body": "Customer raised request",
        "userId": 1
    }

    try:
        response = requests.post(
            BASE_URL,
            json=payload,
            headers=HEADERS,
            timeout=5
        )

        if response.status_code == 201:
            data = response.json()
            return {
                "ticket_id": data.get("id", str(uuid.uuid4())),
                "service": service_type,
                "status": "Ticket Created Successfully"
            }
        else:
            return {
                "ticket_id": str(uuid.uuid4()),
                "service": service_type,
                "status": "Ticket API Failed"
            }


    except Exception as e:  # ✅ catch all exceptions

        return {

            "ticket_id": str(uuid.uuid4()),

            "service": service_type,

            "status": f"Error: {str(e)}"

        }