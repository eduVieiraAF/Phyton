
import os

source = "C:\\Users\\edu_v\\Python\\file.txt"
destination = "C:\\Users\\edu_v\\IdeaProjects\\Kotlin Programming\\file_moved.txt" # can rename file

try:
    
    if os.path.exists(destination):
        
        print("File already exists within folder")
    
    else:
        
        os.replace(source, destination)
        print("File was successfully moved from:\n" + source + "to: " + destination)
            
except FileNotFoundError:
    
    print("File not found")
    
# * we can move directories using the code above too, too
