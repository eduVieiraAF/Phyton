import json
import requests


def tell_joke():
    jokes = []

    for i in range(0, 5):
        joke = get_joke()
        jokes.append(joke)

    for joke in jokes:
        print(joke.setup)
        print(joke.punchline)
        print("")


class Joke:
    def __init__(self, id, type, setup, punchline):
        self.id = id
        self.type = type
        self.setup = setup
        self.punchline = punchline


def get_joke():
    endpoint = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(endpoint)

    joke_dict = json.loads(response.text)

    joke = Joke(joke_dict['id'], joke_dict['type'], joke_dict['setup'], joke_dict['punchline'])

    return joke


tell_joke()
