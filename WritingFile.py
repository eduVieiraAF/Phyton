
text = "A simple way to write files\n using Python.\n"

with open('test2.txt','w') as file:
    file.write(text)
    
text = "New text with append."

with open('test2.txt','a') as file:
    file.write(text)