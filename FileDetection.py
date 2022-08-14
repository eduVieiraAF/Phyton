import os

path = "C:\\edu_v\\Documents\\eduVieiraAF.png"

if os.path.exists(path):
    print("Location found")
    
    if os.path.isfile(path):
        print("File found")
    
    elif os.path.isdir(path):
        print("This is a directory")
    
    else:
        print("Not found")

else:
    print("Location not found")