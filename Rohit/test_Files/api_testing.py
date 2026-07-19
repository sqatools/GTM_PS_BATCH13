import requests
import json
""""
def test_get():
    url = "https://api.restful-api.dev/objects/7"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200


def test_post():
    url = "https://api.restful-api.dev/objects"
    payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
    }

    response = requests.post(url,json=payload)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200


def test_put():
    url = "https://api.restful-api.dev/objects/7"
    payload = {
        "name": "Apple MacBook Pro 22",
        "data": {
            "year": 2026,
            "price": 777.90,
            "CPU model": "Intel Core i11",
            "Hard disk size": "2 TB",
            "color": "Golden"
        }
    }
    response = requests.put(url, json=payload)
    print(response.status_code)
    print(response.json())


def test_get():
    url = "https://api.restful-api.dev/objects/7"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200


def test_post():
    url = "https://api.restful-api.dev/objects"
    payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
    }

    response = requests.post(url,json=payload)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200

items = ["apples", "bananas", "cherries"]
item_rate = [200, 30, 370]

items_with_rate = []

for i in range(len(items)):
    items_with_rate.append((items[i],item_rate[i]))
print(items_with_rate)
"""
def test_get():
    url = "https://api.restful-api.dev/objects/7"
    response = requests.get("https://api.restful-api.dev/objects/7")
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200

def test_post():
    url = "https://api.restful-api.dev/collections/{collectionName}/objects"
    payload = {
        "name" : "Apple MacBook Pro 16",
                 "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }

    }

    response = requests.post (url,json=payload)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200