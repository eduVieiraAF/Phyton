import requests

api_key = "c6a3e0fc5ba340738eee3fab1615b8a2"

recipe_id = 123456

endpoint = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}"

response = requests.get(endpoint)

data = response.json()

ingredients = data['extendedIngredients']
cooking_time = data['readyInMinutes']
title = data['title']
picture = data['image']

print("Title:", title)
print("Cooking Time:", cooking_time)
print("Ingredients:", ingredients)
print("Picture:", picture)
