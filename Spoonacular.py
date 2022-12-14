import requests

# Define your API key
api_key = "c6a3e0fc5ba340738eee3fab1615b8a2"

# Set the URL for the API endpoint
endpoint = "https://api.spoonacular.com/recipes/findByIngredients"

# Set the parameters for the API call
params = {
    "apiKey": api_key,
    "ingredients": "prawn, honey, chilli",
    #"number": 5,
    #"ranking": 2
}

# Make the API call and get the response
response = requests.get(endpoint, params=params)

# Print the response status code to make sure the call was successful
print(response.status_code)

# Print the response body to see the results of the call
print(response.text)

if response.status_code == 200:
    # Convert the response to a Python dictionary
    response_dict = response.json()

    # Print the dictionary to see the structure of the response
    print(response_dict)

    # Access individual elements of the response
    print(response_dict[0]["id"])
    print(response_dict[0]["image"])
    print(response_dict[0]["title"])
    print(response_dict[0]["usedIngredients"])
