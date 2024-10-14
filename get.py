
#* .get()

random_words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "orange", "peach", "pear", "strawberry", "watermelon"]
word_counts = {}

# word_counts["hey"] #! error

for word in random_words:
    word_counts[word] = word_counts.get(word, 0) + 1 
    

print(word_counts)