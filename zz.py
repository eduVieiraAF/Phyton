import requests

url = "https://api.exchangeratesapi.io/latest?base=USD&symbols=BRL"

response = requests.get(url)

# Parse the response JSON to extract the exchange rate
rate = response.json()

print("The current exchange rate for the US dollar is:", rate)
