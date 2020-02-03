#  Module 1 Final Coding Activity: Directory creator

# [ ] The following program is designed to generate a number of directories.
# The directory names follow the pattern (MM_DD_YY_randnum), where:
#     - MM_DD_YY: is today's date as month/day/year
#     - randnum: is a random integer between 10000 and 50000
# For example, if today is May 12th, 2016, then the following would be valid names: 05_12_16_11050 or 05_12_16_15001
#
# For this task, you should complete the functions:
# 1) `directory_count()`
# 2) `name_generator()`
# 3) `directory_creator(name)`
# 4) `create()`
# HINT: You should import all necessary modules

from datetime import datetime
import os, os.path
import math
from random import randint


def directory_count():
    # Calculate the number of directories to be generated
    t = datetime.today().minute          # Get the current minute using appropriate functionality from `datetime`
    t = math.sqrt(t) + 15                # Take the square root of ..the current minute + 15
    t = round(t)                         # Round the square root to an integer
    dir_count = t
    return dir_count


def name_generator():
    randnum = randint(10000, 50000)      # randnum: is a random integer between 10000 and 50000
    date = datetime.today()              # MM_DD_YY: is today's date as month/day/year
    date = date.strftime("%m_%d_%y")
    dir_name = date + "_" + str(randnum)     # The directory names follow the pattern (MM_DD_YY_randnum)
    return dir_name


def directory_creator(name):
    # Create a single directory called `name` in the current working director
    os.mkdir(name)


def create():
    x = directory_count()                              # Use `directory_count` to calculate the number of directories
    for count in range(x):
        name1 = name_generator()                       # `name_generator`
        directory_creator(name1)                       # use `directory_creator'


# Change working directory to `parent_dir` or `create`
if "parent_dir" not in os.getcwd():
    if os.path.exists("./parent_dir"):
        print("Changing working dir to parent_dir")
        os.chdir("parent_dir")
    else:
        os.mkdir(os.getcwd() + "./parent_dir")
        print("Changing working dir to parent_dir")
        os.chdir("parent_dir")
else:                                                # so the code can run multiple times
    while "parent_dir" not in os.getcwd()[-11:]:     # while directory not ending with 'parent_dir' move up the path ..\
        os.chdir("..")                                # move up in dir to find 'parent_dir'
        print("moved up", os.getcwd())

print("The current working directory is:", os.getcwd())          # print the current working directory (should be "parent_dir")
if os.path.exists(os.getcwd() + "./randoms_directory") != True:
    os.mkdir("randoms_directory")                                # check for randoms_directory if not present, create new
print("Changing working dir to randoms_directory")
os.chdir("randoms_directory")
print("The current working directory is:", os.getcwd())

create()                                               # Generate the necessary directories inside "randoms_directory"

print("Current directory content:", os.listdir())      # list the content of the current directory
