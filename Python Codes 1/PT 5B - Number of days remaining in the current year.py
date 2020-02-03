# Practice Task 5B - Write a program to compute the number of days remaining in the current year
from datetime import datetime, timedelta
date1 = datetime.today()
date2 = datetime(year = 2020, month = 1, day = 1)
delta1 = date2 - date1
print(delta1.days, "days remaining in the current year")
