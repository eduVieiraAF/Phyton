from key import API_KEY
import requests
import json

link = 'https://api.openai.com/v1/chat/completions'
headers = {"Authorization": f"Bearer { API_KEY }", "Content-Type": "application/json"}
id_model = "gpt-3.5-turbo"
body_message = {
    "model": id_model,
    "messages": [
        {" role": "user", "content": "I'm using your API in a Python script. Any tips for me?" }]
}

body_message = json.dumps(body_message)

req = requests.post(link, headers=headers, data=body_message)
res = req.json()
# GPTReply = res["choices"][0]["message"]["content"]

print(res)
