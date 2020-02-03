# Platform Identification
import sys
print(sys.platform)

# Directory Operations
import os
print('Working Directory Start: ', os.getcwd())

os.chdir('..')
print('Working Directory Change: ', os.getcwd())

os.chdir('Python Fundamentals')
print('Working Directory Change: ', os.getcwd())

# os.listdir()
print(os.listdir())
