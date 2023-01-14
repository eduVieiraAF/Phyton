import requests

# Define your API key
api_key = "c6a3e0fc5ba340738eee3fab1615b8a2"

# Set the URL for the API endpoint
endpoint = "https://api.spoonacular.com/recipes/findByIngredients"

# Set the parameters for the API call
params = {
    "apiKey": api_key,
    "ingredients": "sausage",
}

response = requests.get(endpoint, params=params)

print(response.status_code)

# print(response.text)

if response.status_code == 200:
    response_dict = response.json()

    # print(response_dict)

    print(response_dict[0]["id"])
    print(response_dict[0]["image"])
    print(response_dict[0]["title"])
    print(response_dict[0]["usedIngredients"])
