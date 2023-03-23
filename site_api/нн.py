import requests


url = "https://binance43.p.rapidapi.com/ticker/24hr"

headers = {
    "X-RapidAPI-Key": "ff7772a042msh6a228b87e989065p14aa2cjsn57d1c0ebb4e4",
    "X-RapidAPI-Host": "binance43.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
