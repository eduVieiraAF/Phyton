message = input("> ")
words = message.split(" ")
emojis = {
    ":)": "😀",
    ":(": "😕",
    ":|": "😑",
    ":p": "😋"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "  # if I don't have a key, use that word as default value

print(output)
