# Index operator [] gives access to a sequence's element (str, list, tuples)

str_input = input("Enter a sentence: ")
print()

if(str_input[0].islower()):
    str_input = str_input.capitalize()
    print((str(str_input)) + "! You didn't start a sentence with a capital " +
     (str(str_input[0]) + "."))
else:
    print("Exactly, always start a sentence with a Capital letter.")

# Creating substrings

print()
chars = str_input[0:2].upper() #starting index at ZERO until (:) the 2 second character
print(str(chars) + " are the first 2 letters")

print()
chars2 = str_input[2:].lower() #starting index at the 2nd character until last
print("Ops, dropped the first 2 letters - " + str(chars2))

print()
chars3 = str_input[-1].upper() #accessing last index
print(str(chars3) + " is the last letter of your sentence.")