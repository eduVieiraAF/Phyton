import os

folder_path = ""
file_list = os.listdir(folder_path)

for file in file_list:
    if file.endswith("*.txt"):
        os.remove(os.path.join(folder_path, file))

print("DONE!")
