print()

word1 = "Race"
word2 = "Care"

word1 = word1.lower()
word2 = word2.lower()

# Check if strings' length are the same
if (len(word1) == len(word2)):
    
    # sort strings
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    
    #check if char sequence is the same
    if (sorted_word1 == sorted_word2):
        
        print(word1.capitalize() + " and " + word2 + " are an anagram.")
    
    else:
        
        print(word1.capitalize() + " and " + word2 + " are NOT an anagram.")
        
# if strings's lenght are not the same, they're not an anagram
else:
    
    print(word1.capitalize() + " and " + word2 + " are NOT anagram.")
    
print()