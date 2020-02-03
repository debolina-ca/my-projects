# Rename a Directory
import os
print(os.getcwd())
os.mkdir('new_child')
print('Created new_child dir')
print(os.listdir())
os.rename('new_child', 'old_child')
print('Renamed new_child as old_child')
print(os.listdir())
