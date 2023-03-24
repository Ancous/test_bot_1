"""
Система отелей объединяется с Expedia.
Эта конечная точка помогает преобразовать старый идентификатор отеля
(встроенный в общую ссылку, например: «ho133528» на сайте hotels.com/ho133528/) в новый (423818).
"""

import requests
import os
from dotenv import load_dotenv
import json


load_dotenv()

url = "https://hotels4.p.rapidapi.com/"
endpoints = "properties/v2/resolve-url"
querystring = {
    "id": "ho546370",   # required
    "locale": None,  # можно вставить "en_US"
    "langid": None,  # можно вставить 1033
    "siteid": None,  # можно вставить 300000001
}
headers = {
    "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
    "X-RapidAPI-Host": os.getenv("RAPIDAPI_HOST")
}

response = requests.get(url=url + endpoints, params=querystring, headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    with open("properties_v2_resolve-url.txt", "w") as file:
        json.dump(data, file, indent=4)
else:
    print("Error")
    print(response.text)
