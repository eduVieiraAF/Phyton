
# * copyfile() = copies the content of a file
# * copy() = copyfile() + permission mode + directory or destination
# * copy2() = copy + copies metadata (file's creation and modificaition times)

import shutil

shutil.copyfile('test2.txt', 'text2_copy.txt') # source, destination/create file's name
