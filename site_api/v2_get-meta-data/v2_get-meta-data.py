"""
Получить метаданные локации
"""

import requests
import os
from dotenv import load_dotenv
import json


load_dotenv()

url = "https://hotels4.p.rapidapi.com/"
endpoints = "v2/get-meta-data"
headers = {
    "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
    "X-RapidAPI-Host": os.getenv("RAPIDAPI_HOST")
}

response = requests.get(url=url+endpoints, headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    with open("v2_get-meta-data.txt", "w") as file:
        json.dump(data, file, indent=4)
else:
    print("Error")
    print(response.text)
