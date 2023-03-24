"""
Получить подробную информацию об объекте
"""

import requests
import os
from dotenv import load_dotenv
import json


load_dotenv()

url = "https://hotels4.p.rapidapi.com/"
endpoints = "properties/v2/detail"
payload = {
    "propertyId": "9209612",  # required
    "currency": None,  # можно подставить "USD"
    "eapid": None,  # можно подставить 1
    "locale": None,  # можно подставить "en_US"
    "siteId": None,  # можно подставить 300000001
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
    "X-RapidAPI-Host": os.getenv("RAPIDAPI_HOST")
}

response = requests.post(url=url + endpoints, json=payload, headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    with open("properties_v2_detail.txt", "w") as file:
        json.dump(data, file, indent=4)
else:
    print("Error")
    print(response.text)
