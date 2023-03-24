"""
Получить предложения недвижимости
"""

import requests
import os
from dotenv import load_dotenv
import json


load_dotenv()

url = "https://hotels4.p.rapidapi.com/"
endpoints = "properties/v2/get-offers"
payload = {
    "propertyId": "9209612",
    "currency": None,  # можно подставить "USD"
    "eapid": None,  # можно подставить 1
    "locale": None,  # можно подставить "en-US"
    "siteId": None,  # можно подставить 300000001
    "checkInDate": {
        "day": 6,
        "month": 10,
        "year": 2022
    },
    "checkOutDate": {
        "day": 9,
        "month": 10,
        "year": 2022
    },
    "destination": {
        "coordinates": {},
        "regionId": "6054439"
    },
    "rooms": [
        {
            "adults": 2,
            "children": [{"age": 5}, {"age": 7}]
        },
        {
            "adults": 2,
            "children": []
        }
    ]
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
    "X-RapidAPI-Host": os.getenv("RAPIDAPI_HOST")
}

response = requests.post(url=url + endpoints, json=payload, headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    with open("properties_v2_get-offers.txt", "w") as file:
        json.dump(data, file, indent=4)
else:
    print("Error")
    print(response.text)
