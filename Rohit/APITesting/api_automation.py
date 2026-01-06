import requests
from pprint import pprint
import json

def get_all_objects():
    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    pprint(response.json())
    print(response.status_code)
    print(response.text)


#get_all_objects()

def get_specific_objects():
    url = "https://api.restful-api.dev/objects?id=3&id=5&id=10"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    pprint(response.json())
    print(response.text)
    print(response.status_code)

#get_specific_objects()

def create_objects():
    url = "https://api.restful-api.dev/objects"    #ff8081819782e69e019b4929eac65cb0

    payload = json.dumps({
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    pprint(response.json())
    print(response.text)
    print(response.status_code)

#create_objects()

def update_existing_object(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
        "name": "Apple MacBook 20",
        "data": {
            "year": 2029,
            "price": 8900.99,
            "CPU model": "Intel Core i12",
            "Hard disk size": "8 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    pprint(response.json())
    print(response.text)
    print(response.status_code)

#update_existing_object("ff8081819782e69e019b687b0edb0c22")

def partial_update_object(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
        "name": "Apple MacBook Pro 26"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    pprint(response.json())
    print(response.text)
    print(response.status_code)

#partial_update_object("ff8081819782e69e019b687b0edb0c22")


def delete_object(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    pprint(response.json())
    print(response.text)
    print(response.status_code)

delete_object("ff8081819782e69e019b687b0edb0c22")