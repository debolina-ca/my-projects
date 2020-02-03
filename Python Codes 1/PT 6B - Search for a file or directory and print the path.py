# Practice Task 6B: Path operations

# [ ] Write a program that prompts the user for a file or directory name
# if it exists in the current working directory, it prints whether it is a file or directory
import os, os.path
print(os.getcwd())
os.chdir('parent_dir')
print(os.getcwd())

name = input("Enter the name of a file or a directory: ")
abs_path = os.path.abspath(name)
if os.path.exists(abs_path):
    print("Path Exists")
    # Test to see if it is a file or a directory
    if os.path.isfile(abs_path):
        print("It's a file")
    elif os.path.isdir(abs_path):
        print("It's a dir")
    print(abs_path)
else:
    print("Path doesn't exist")
