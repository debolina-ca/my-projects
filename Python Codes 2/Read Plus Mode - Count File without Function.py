# Read Plus Mode - r+ - Create a Counting File that has one line "Count is: x" and Print out the changed value
# Overwrite with new count at the x location (x is an integer)

# Create a file with initial count of 0
count_file = open("count_file.txt", "w+")
count_file.write("Count is: 0")
count_file.seek(0)
print(count_file.readline().strip)
count_file.close()

# Print out before and after count value for only 1 time
count_file = open("count_file.txt", "r+")
count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)
count = int(count_line[10:]) + 1        # get the integer character after the colon and space, cast and increment

# Write the incremented value to the file - overwrite before value
count_file.seek(10)
count_file.write(str(count))
count_file.seek(0)
print("\nAFTER\n" + count_file.readline().strip())
count_file.close()
