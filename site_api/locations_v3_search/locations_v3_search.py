"""
Поиск связанных местоположений и предложений
"""

import requests
import os
from dotenv import load_dotenv
import json


load_dotenv()

url = "https://hotels4.p.rapidapi.com/"
endpoints = "locations/v3/search"
querystring = {
    "q": "new york",  # required
    "locale": None,
    "langid": None,
    "siteid": None
}
headers = {
    "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
    "X-RapidAPI-Host": os.getenv("RAPIDAPI_HOST")
}

response = requests.get(url=url+endpoints, params=querystring, headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    with open("locations_v3_search.txt", "w") as file:
        json.dump(data, file, indent=4)
else:
    print("Error")
    print(response.text)
