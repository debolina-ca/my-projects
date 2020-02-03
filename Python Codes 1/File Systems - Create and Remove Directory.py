# Create and Remove Directory
import os
print(os.getcwd())
# Create a new directory
os.mkdir('new_dir')
print("Created new child directory")

# Remove directory
os.rmdir('new_dir')
print("removed new directory")
print(os.listdir())

