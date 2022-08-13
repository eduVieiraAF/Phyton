
# * copyfile() = copies the content of a file
# * copy() = copyfile() + permission mode + directory or destination
# * copy2() = copy + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('test.txt', 'text_copy.txt') # source, destination/create file's name
