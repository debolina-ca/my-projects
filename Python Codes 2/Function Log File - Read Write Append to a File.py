# Read Write Append to a File
# Location: C:\Users\N\PycharmProjects\Python Fundamentals
# Instead of .txt, .doc or .xls file can be also created in the same way

# Create a local log file
log_file = open('log-file.txt', 'w')
# log_file = open('log-file.doc', 'w')
# log_file = open('log-file.xls', 'w')

log_file.close()

# Enter data input for log file from user using a function
log_file = open('log_file.txt', 'a+')
# log_file = open('log_file.doc', 'a+')
# log_file = open('log_file.xls', 'a+')


def logger(log):
    log_entry = input("enter log item (press enter to quit): ")
    count = 0
    while log_entry:
        count += 1
        log.write(str(count) + ": " + log_entry + "\n")
        log_entry = input("enter log item (press enter to quit): ")
    return count


num_logs = logger(log_file)

# Seek pointer to beginning of file and print everything in the file
log_file.seek(0)
log_text = log_file.read()
print("\n Number of logs entered: ", num_logs, "\n")
print(log_text)
log_file.close()
