# Practice Task 6A: File System - Directory operations

# [ ] Complete the following program to:
# 1) navigate to `parent_dir` directory (if not already in it)
# 2) create a new directory called `practice_1`
# 3) change the working directory to `practice_1`
# 4) display the current working directory to verify you are in the correct location
# 5) create a new directory called `practice_2`
# 6) verify that `practice_2` was created by listing the content of the current directory
# 7) rename `practice_2` as `sub_practice_2`
# 8) verify the name was successful changed by listing the content of the current directory
# 9) remove `sub_practice_2`
# 10) change working directory to the parent directory using `..`
# 11) remove `practice_1`
# 12) verify your current working directory and display its content

import os, os.path
# 1) navigate to `parent_dir` directory (if not already in it)
print(os.getcwd())
os.chdir('parent_dir')
print("Current working directory:", os.getcwd())

# 2) create a new directory called `practice_1`
os.mkdir('practice_1')

# 3) change the working directory to `practice_1`
os.chdir('practice_1')

# 4) display the current working directory to verify you are in the correct location
print(os.getcwd())

# 5) create a new directory called `practice_2`
os.mkdir('practice_2')

# 6) verify that `practice_2` was created by listing the content of the current directory
print("listing the content of the current directory to verify practice_2 is created", os.listdir())

# 7) rename `practice_2` as `sub_practice_2`
os.rename('practice_2', 'sub_practice_2')

# 8) verify the name was successful changed by listing the content of the current directory
print("listing the content of the current directory to verify name was successfully changed", os.listdir())

# 9) remove `sub_practice_2`
os.rmdir('sub_practice_2')

# 10) change working directory to the parent directory using `..`
os.chdir('..')

print(os.getcwd())

# 11) remove `practice_1`
os.rmdir('practice_1')

# 12) verify your current working directory and display its content
print(os.listdir())
