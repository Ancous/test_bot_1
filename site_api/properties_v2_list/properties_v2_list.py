"""
Список свойств с параметрами и фильтрами
"""

import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

url = "https://hotels4.p.rapidapi.com/"
endpoints = "properties/v2/list"
payload = {
    "currency": None,
    "eapid": None,
    "locale": None,
    "siteId": None,
    "destination": {
        "coordinates": None,
        "regionId": "6054439"  # required
    },
    "checkInDate": {           # required
        "day": 10,             # required
        "month": 10,           # required
        "year": 2022           # required
    },
    "checkOutDate": {          # required
        "day": 15,             # required
        "month": 10,           # required
        "year": 2022           # required
    },
    "rooms": [                 # required
        {
            "adults": 2,       # required
            "children": []     # required
        }
    ],
    "resultsStartingIndex": None,
    "resultsSize": None,
    "sort": None,
    "filters": {
        "hotelName": None,
        "price": {
            "min": None,
            "max": None
        },
        "guestRating": None,
        "accessibility": None,
        "travelerType": None,
        "mealPlan": None,
        "poi": None,
        "regionId": None,
        "lodging": None,
        "amenities": None,
        "star": None,
        "paymentType": None,
        "bedroomFilter": None,
        "availableFilter": None,
    }
}
headers = {
    "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
    "X-RapidAPI-Host": os.getenv("RAPIDAPI_HOST")
}

response = requests.post(url=url + endpoints, json=payload, headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    with open("properties_v2_list.txt", "w") as file:
        json.dump(data, file, indent=4)
else:
    print("Error")
    print(response.text)
