import requests
import json

def post_request():
    url = "https://api.restful-api.dev/objects"

    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Core i9",
            "Hard disk size": "1 TB"
        }
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, json=payload)

    print(response.text)

post_request()