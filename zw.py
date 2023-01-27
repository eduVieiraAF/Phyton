import requests


url = "https://footapi7.p.rapidapi.com/api/search/ronaldo"

headers = {
	"X-RapidAPI-Key": "d4c44073eamsh4e207011b1db247p18fcaajsne2c47b61d3fe",
	"X-RapidAPI-Host": "footapi7.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

data = response.json()

list = data["results"]

for i in range(0,len(list)):

    print(f"{ i + 1 } → The winner in the game { list[i] ['score']}  and the total goals are {list[i] ['type']}")