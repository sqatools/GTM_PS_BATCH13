# pip install requests
import requests

def get_all_objects():
    url = "https://api.restful-api.dev/objects"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.status_code)
    print(response.text)

#get_all_objects()

def get_specific_objects():
    url = "https://api.restful-api.dev/objects?id=3&id=5&id=10"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.json())
    print(response.status_code)

#get_specific_objects()
def create_object():
    import requests
    import json

    url = "https://api.restful-api.dev/objects"

    payload = json.dumps({
        "name": "Apple MacBook Pro 160",
        "data": {
            "year": 2025,
            "price": 1849.99,
            "CPU model": "Intel Core i10",
            "Hard disk size": "4 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    #print(response.text)
    print(response.json())
    print(response.status_code)

#create_object()
# ff8081819782e69e019b48df1a085c82


def update_existing_object(id):
    import requests
    import json
    from pprint import pprint

    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
        "name": "Apple MacBook Pro 200",
        "data": {
            "year": 2030,
            "price": 1849.99,
            "CPU model": "Intel Core i10",
            "Hard disk size": "5 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    pprint(response.json())
    print(response.status_code)

#update_existing_object("ff8081819782e69e019b48df1a085c82")


def patch_existing_object(id):
    import requests
    import json

    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
        "name": "Apple MacBook Pro 300"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.json())



#patch_existing_object("ff8081819782e69e019b48df1a085c82")

def delete_object(id):
    import requests
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = ""
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.json())


delete_object("ff8081819782e69e019b48df1a085c82")





