print()

word1 = input("Enter a word: ").lower()
word2 = input("Enter another word: ").lower()

# Check if strings' length are the same
if len(word1) == len(word2):
    # sort strings
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    # check if char sequence is the same
    if sorted_word1 == sorted_word2:
        print(word1.capitalize() + " and " + word2 + " are an anagram.")
    else:
        print(word1.capitalize() + " and " + word2 + " are NOT an anagram.")

# if strings' length are not the same, they're not an anagram
else:
    print(word1.capitalize() + " and " + word2 + " are NOT an anagram.")
