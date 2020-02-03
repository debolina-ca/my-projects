# Path Operations - Check if Absolute Path, If File or Path, If file exists
import os
os.chdir('parent_dir')
print("Current working directory", os.getcwd())
abs_path = os.path.abspath('child1_dir/leaf1.txt')
print("Absolute path to leaf1.txt is: ", abs_path)
# Test if the path exists
if os.path.exists(abs_path):
    print("Path Exists")
    # Test to see if it is a file or a directory
    if os.path.isfile(abs_path):
        print("It's a file")
    elif os.path.isdir(abs_path):
        print("It's a dir")
else:
    print("Path doesn't exist")
