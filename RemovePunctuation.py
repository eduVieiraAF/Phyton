punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

message = "Hello, World! Welcome - and have fun..."

no_punct = ""

for char in message:
    if char not in punct:
        no_punct = no_punct + char

print(no_punct)
