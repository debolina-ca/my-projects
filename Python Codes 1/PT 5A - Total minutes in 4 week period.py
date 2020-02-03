# Practice Task 5A: timedelta: Total minutes in 4 week period
# Write a program to find out how many minutes are in a 4-week period
# Hint: Use a timedelta object and the total_seconds() method

from datetime import datetime, timedelta
from math import trunc
date1 = datetime(day = 1, month = 7, year = 2019)
date2 = datetime(day = 29, month = 7, year = 2019)
delta1 = date2 - date1
tot_secs = delta1.total_seconds()
tot_mins = tot_secs/60
print("There are", trunc(tot_mins), "minutes in a 4-week period")