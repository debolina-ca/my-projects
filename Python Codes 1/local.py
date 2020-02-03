from datetime import date, datetime
import os, os.path
import math
from random import randint

t = datetime.today().minute
t = math.sqrt(t) + 15                # Take the square root of ..the current minute + 15
t = round(t)
randnum = randint(10000, 50000)
date = datetime.today()
date = date.strftime("%m_%d_%y")
dir_name = date + "_" + str(randnum)
print(dir_name)
print(os.getcwd())
os.chdir('parent_dir')
print(os.getcwd())
os.mkdir('name')
print(os.listdir())

if "parent_dir" not in os.getcwd():
    if os.path.exists("./parent_dir"):
        print("Changing working dir to parent_dir")
        os.chdir("parent_dir")
    else:
        os.mkdir(os.getcwd() + "./parent_dir")
        print("Changing working dir to parent_dir")
        os.chdir("parent_dir")
else:
    while "parent_dir" not in os.getcwd()[-11:]:
        os.chdir("..")
        print("moved up", os.getcwd())

# print the current working directory (should be "parent_dir")
print("The current working directory is:", os.getcwd())