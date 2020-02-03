# Task 4: append
task4_file = open('task4_file.txt', 'w+')
task4_file.write("Line1\nLine2\nLine3\n")
task4_file.close()
task4_file = open('task4_file.txt', 'a+')
for item in range(5):
    task4_file.write("append #" + str(item)+"\n")
    task4_file.seek(0, 0)          # In append mode the file should only write to the end of the file regardless of setting seek() location
task4_file.seek(0, 0)
print(task4_file.read())
