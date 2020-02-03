# [ ] Write a program to print the absolute path of all directories in "parent_dir"
# HINTS:
# 1) Verify you are inside "parent_dir" using os.getcwd()
# 2) Use os.listdir() to get a list of files and directories in "parent_dir"
# 3) Iterate over the elements of the list and print the absolute paths of all the directories
import os
print(os.getcwd())
x_list = os.listdir()
print(x_list)
for item in x_list:
    abs_path = os.path.abspath(item)
    print(abs_path)