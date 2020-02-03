# Read Plus Mode - r+ - Create a Counting File that has one line "Count is: x" and Print out the Counted Values Multiple Times
# Overwrite with new count at the x location (x is an integer)

# Create a file with initial count of 0
count_file = open("count_file.txt", "w+")
count_file.write("Count is: 0")
count_file.seek(0)
print(count_file.readline().strip)
count_file.close()

# Function Code: Increment - Count or inc_count() that reads file and updates the count


def inc_count(cnt_file):
    cnt_file.seek(0, 0)
    cnt_line = cnt_file.readline().strip()
    cnt = int(cnt_line[10:]) + 1                     # get the integer character after the colon and space, cast and increment
    cnt_file.seek(10, 0)
    cnt_file.write(str(cnt))
    return cnt


# Call Function to Read Write and Count Multiple Times

# Print out before count value for first time
count_file = open("count_file.txt", "r+")
count_file.seek(0)
count_line = count_file.readline().strip()
print("\n BEFORE\n" + count_line)

# Call Function inc_count() to increase count 5 times
for i in range(0, 5):
    count = inc_count(count_file)
    count_file.seek(0)
    print("\n AFTER inc_count() call", i+1, "\n" + count_file.readline().strip())

count_file.close()