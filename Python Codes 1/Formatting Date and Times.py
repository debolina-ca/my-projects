# Formatting Dates and Times

# [ ] Write a program that displays the time: (17:39:10) as:
# 1) 05:39:10 PM
# 2) 17:39:10
from datetime import time
t = time(hour = 17, minute = 39, second = 10)
formatted_string = t.strftime("%I:%M:%S %p")
print(formatted_string)
formatted_string = t.strftime("%H:%M:%S")
print(formatted_string)

# [ ] Write a program that displays the date: (October 23rd 2018) as:
# 1) Oct 23, 2018
# 2) 10/23/18
# 3) 23/October/2018
# 4) Tuesday October 23
from datetime import date
dt = date(2018, 10, 23)
formatted_string = dt.strftime("%b %d, %Y")
print(formatted_string)
formatted_string = dt.strftime("%m/%d/%y")
print(formatted_string)
formatted_string = dt.strftime("%d/%B/%Y")
print(formatted_string)
formatted_string = dt.strftime("%A %B %d")
print(formatted_string)