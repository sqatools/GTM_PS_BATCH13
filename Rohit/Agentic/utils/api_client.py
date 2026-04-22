import requests

HEADERS = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Content-Type": "application/json"
}

def post(url, payload):
    return requests.post(url, json=payload, headers=HEADERS, timeout=5)