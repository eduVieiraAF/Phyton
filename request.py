import requests
import json

url = "https://investing-cryptocurrency-markets.p.rapidapi.com/coins/list"


headers = {
'X-RapidAPI-Key': "5375f1194amshb057f0fe5663137p14cc2bjsna7ae5ec520d1",
'X-RapidAPI-Host': "investing-cryptocurrency-markets.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

data = response.json()

list = data["data"][0]

crypto = list["screen_data"]["crypto_data"]

btc = crypto[0]

print(btc["name"])
print(btc["inst_price_usd"])
print(btc["logo_url"])