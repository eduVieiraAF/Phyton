
import pprint
import json

with open("crypto.json", "r", encoding="utf-8") as f:
    file = json.load(f)

pprint(file)