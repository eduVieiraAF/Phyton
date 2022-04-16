import os
import shutil

path = 'text2_copy.txt'

try:
    os.remove(path) # ! Does not remove folder/directories
    os.rmdir # * to remove directories which doesn't contain files
    shutil.rmtree(path) # ! removes folder and all files within it
    
except FileNotFoundError:
    print("File not founs")

except PermissionError:
    print("You cannot delete folder")

except OSError:
    print("You cannot delete folder that contain files")
    
else:
    print (path, "delete succefully.")