from collections import defaultdict

words = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# def default_factory():
#     return 20

# word_count = defaultdict(default_factory)
word_count = defaultdict(int)

for word in words:
    word_count[word] += 1

print(dict(word_count))