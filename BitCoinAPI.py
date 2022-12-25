import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    coin = data["chartName"]
    currency = data["bpi"]["USD"]["code"]
    price = data["bpi"]["USD"]["rate"]
    lastestRate = data["time"]["updated"]
    # print(price)
    print(f"The current price of {coin} at {lastestRate} is {currency} ${price}")
    print(data["disclaimer"])
    # print(lastestRate)

else:
    print(response.status_code)